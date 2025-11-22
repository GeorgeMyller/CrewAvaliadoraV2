#!/usr/bin/env python3
"""Streamlit app para executar a análise de repositórios usando CrewAvaliadora

Uso:
    uv run streamlit run src/streamlit_app.py
ou
    streamlit run src/streamlit_app.py
"""
from __future__ import annotations

import sys
import tempfile
import shutil
import os
from pathlib import Path
import time
import streamlit as st

# Garante que o pacote local esteja no path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.analyze_repo import clone_repository, generate_base_report, run_crewai_analysis, get_git_diff


def list_outputs_for_project(outputs_dir: Path) -> list[Path]:
    if not outputs_dir.exists():
        return []
    return sorted([p for p in outputs_dir.iterdir() if p.is_file()], key=lambda p: p.stat().st_mtime, reverse=True)


def app():
    st.set_page_config(page_title="CrewAvaliadora — Analyzer", layout="wide")
    st.title("CrewAvaliadora — Análise de Repositório")

    st.markdown("Insira a URL do repositório Git (ex: https://github.com/user/repo) e clique em **Analyze**.")

    col1, col2 = st.columns([3, 1])
    with col1:
        repo_url = st.text_input("Repository URL")
    with col2:
        analyze_mode = st.selectbox("Modo de Análise", ["Completa", "Incremental (Diff)"])

    base_ref = None
    head_ref = None
    if analyze_mode == "Incremental (Diff)":
        c1, c2 = st.columns(2)
        with c1:
            base_ref = st.text_input("Base Ref (ex: main, commit hash)", value="main")
        with c2:
            head_ref = st.text_input("Head Ref (ex: develop, feature-branch)", value="HEAD")

    analyze_btn = st.button("Analyze")

    if analyze_btn:
        if not repo_url or not repo_url.startswith("http"):
            st.error("Informe uma URL válida do repositório (começando com http/https).")
            return

        project_name = repo_url.rstrip("/").split("/")[-1].replace('.git', '')
        outputs_dir = ROOT / "outputs" / project_name
        outputs_dir.mkdir(parents=True, exist_ok=True)

        status = st.empty()
        prog = st.progress(0)
        logs = st.empty()

        temp_dir = None
        try:
            status.info("Preparando diretório temporário...")
            temp_dir = tempfile.mkdtemp(prefix=f"crew_analysis_{project_name}_")
            prog.progress(5)

            status.info("Clonando repositório...")
            with st.spinner("Clonando repositório (pode demorar)..."):
                # Se for incremental, precisamos de histórico completo ou suficiente
                depth = 0 if analyze_mode == "Incremental (Diff)" else 1
                ok = clone_repository(repo_url, temp_dir, depth=depth)
            prog.progress(20)
            if not ok:
                st.error("Falha ao clonar o repositório. Verifique a URL e tente novamente.")
                return

            diff_content = None
            if analyze_mode == "Incremental (Diff)" and base_ref and head_ref:
                status.info(f"Obtendo diff entre {base_ref} e {head_ref}...")
                diff_content = get_git_diff(temp_dir, base_ref, head_ref)
                if not diff_content:
                    st.warning("Não foi possível obter o diff ou ele está vazio. Prosseguindo com análise completa.")
                else:
                    st.info(f"Diff obtido: {len(diff_content)} caracteres.")
                    with st.expander("Ver Diff"):
                        st.code(diff_content[:2000] + ("..." if len(diff_content) > 2000 else ""))

            status.info("Gerando relatório base (quick report)...")
            base_report_path = outputs_dir / "relatorio_codebase_inicial.md"
            with st.spinner("Gerando relatório base..."):
                ok = generate_base_report(temp_dir, str(base_report_path))
            prog.progress(60)
            if not ok:
                st.error("Falha ao gerar o relatório base.")
                return

            status.info("Executando análise CrewAI (isso pode levar alguns minutos)...")
            with st.spinner("Executando análise CrewAI..."):
                ok = run_crewai_analysis(str(base_report_path), str(outputs_dir), project_name, temp_dir, diff_content)
            prog.progress(95)
            if not ok:
                st.error("Falha na análise CrewAI. Verifique os logs do servidor para mais detalhes.")
                return

            prog.progress(100)
            status.success("Análise concluída com sucesso!")

            # Lista e exibe o relatório final mais recente
            files = list_outputs_for_project(outputs_dir)
            if files:
                st.subheader("Outputs gerados")
                for f in files:
                    st.write(f"- {f.name} — {round(f.stat().st_size/1024,1)} KB")

                # Tenta encontrar o relatorio final padrão
                final_candidates = [f for f in files if f.name.startswith(f"relatorio_final_{project_name}")]
                final_report = final_candidates[0] if final_candidates else files[0]

                st.subheader("Relatório final (preview)")
                try:
                    text = final_report.read_text(encoding="utf-8")
                    st.markdown(text)
                except Exception as e:
                    st.error(f"Não foi possível ler o relatório: {e}")
            else:
                st.warning("Nenhum arquivo de output encontrado.")

        except Exception as e:
            st.exception(e)
        finally:
            if temp_dir and os.path.exists(temp_dir):
                try:
                    shutil.rmtree(temp_dir)
                except Exception:
                    pass


if __name__ == "__main__":
    app()