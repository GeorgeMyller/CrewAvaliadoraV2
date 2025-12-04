#!/usr/bin/env python3
"""Streamlit app para executar a análise de repositórios usando CrewAvaliadora

Uso:
    uv run streamlit run src/streamlit_app.py
ou
    streamlit run src/streamlit_app.py
"""

from __future__ import annotations

import io
import mimetypes
import os
import shutil
import sys
import tempfile
import time
import zipfile
from pathlib import Path

import streamlit as st

# Garante que o pacote local esteja no path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.analyze_repo import (  # noqa: E402
    clone_repository,
    generate_base_report,
    get_git_diff,
    run_crewai_analysis,
)


def list_outputs_for_project(outputs_dir: Path) -> list[Path]:
    if not outputs_dir.exists():
        return []
    return sorted(
        [p for p in outputs_dir.iterdir() if p.is_file()],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )


def app():
    st.set_page_config(
        page_title="CrewAvaliadora — AI Code Analyzer",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS for better UI
    st.markdown(
        """
        <style>
        .main {
            padding-top: 2rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #FF4B4B;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #FF2B2B;
            color: white;
        }
        .report-container {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/robot-2.png", width=80)
        st.title("CrewAvaliadora")
        st.markdown("---")
        st.markdown("### ⚙️ Configurações")
        st.info("Versão: 2.0.0 (Beta)")

        st.markdown("### 📝 Sobre")
        st.markdown(
            "Este sistema utiliza **Agentes de IA** (CrewAI + Gemini) para analisar repositórios de código, "
            "gerando relatórios detalhados sobre arquitetura, qualidade, segurança e produto."
        )
        st.markdown("---")
        st.caption("Desenvolvido por George Myller")

    # Main Header
    col_title, col_logo = st.columns([4, 1])
    with col_title:
        st.title("🚀 Análise de Repositório com IA")
        st.markdown("#### Gere insights profundos sobre seu código em minutos.")

    st.markdown("---")

    # Input Section
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            repo_url = st.text_input(
                "🔗 URL do Repositório Git", placeholder="https://github.com/usuario/repo"
            )
        with col2:
            analyze_mode = st.selectbox("🛠️ Modo de Análise", ["Completa", "Incremental (Diff)"])

        base_ref = None
        head_ref = None
        if analyze_mode == "Incremental (Diff)":
            st.info(
                "ℹ️ O modo incremental compara duas referências git para focar a análise apenas nas mudanças."
            )
            c1, c2 = st.columns(2)
            with c1:
                base_ref = st.text_input(
                    "Base Ref (ex: main)", value="main", help="Branch ou commit de origem"
                )
            with c2:
                head_ref = st.text_input(
                    "Head Ref (ex: feature/x)",
                    value="HEAD",
                    help="Branch ou commit com as alterações",
                )

        analyze_btn = st.button("🚀 Iniciar Análise", type="primary")

    if analyze_btn:
        if not repo_url or not repo_url.startswith("http"):
            st.error("❌ Informe uma URL válida do repositório (começando com http/https).")
            return

        # Security Check
        from src.security.guardrails import InputGuard

        guard = InputGuard()

        is_valid, error = guard.validate_prompt(repo_url)
        if not is_valid:
            st.error(f"⛔ Erro de Segurança: {error}")
            return

        if analyze_mode == "Incremental (Diff)":
            if base_ref:
                is_valid, error = guard.validate_prompt(base_ref)
                if not is_valid:
                    st.error(f"⛔ Erro de Segurança (Base Ref): {error}")
                    return
            if head_ref:
                is_valid, error = guard.validate_prompt(head_ref)
                if not is_valid:
                    st.error(f"⛔ Erro de Segurança (Head Ref): {error}")
                    return

        project_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
        outputs_dir = ROOT / "outputs" / project_name
        outputs_dir.mkdir(parents=True, exist_ok=True)

        # Status Container
        status_container = st.status("🔄 Processando análise...", expanded=True)

        temp_dir = None
        diff_content = None

        try:
            status_container.write("📂 Preparando ambiente temporário...")
            temp_dir = tempfile.mkdtemp(prefix=f"crew_analysis_{project_name}_")

            status_container.write("⬇️ Clonando repositório...")
            # Se for incremental, precisamos de histórico completo ou suficiente
            depth = 0 if analyze_mode == "Incremental (Diff)" else 1
            ok = clone_repository(repo_url, temp_dir, depth=depth)

            if not ok:
                status_container.update(label="❌ Falha na clonagem!", state="error")
                st.error("Falha ao clonar o repositório. Verifique a URL e tente novamente.")
                return

            if analyze_mode == "Incremental (Diff)" and base_ref and head_ref:
                status_container.write(f"🔍 Extraindo diff entre `{base_ref}` e `{head_ref}`...")
                diff_content = get_git_diff(temp_dir, base_ref, head_ref)
                if not diff_content:
                    st.warning(
                        "⚠️ Não foi possível obter o diff ou ele está vazio. Prosseguindo com análise completa."
                    )
                else:
                    status_container.write(f"✅ Diff obtido: {len(diff_content)} caracteres.")

            status_container.write("📊 Gerando relatório base (estatísticas)...")
            base_report_path = outputs_dir / "relatorio_codebase_inicial.md"
            ok = generate_base_report(temp_dir, str(base_report_path))

            if not ok:
                status_container.update(label="❌ Falha no relatório base!", state="error")
                st.error("Falha ao gerar o relatório base.")
                return

            status_container.write(
                "🤖 Executando Agentes de IA (CrewAI)... Isso pode levar alguns minutos."
            )
            ok = run_crewai_analysis(
                str(base_report_path), str(outputs_dir), project_name, temp_dir, diff_content
            )

            if not ok:
                status_container.update(label="❌ Falha na análise da IA!", state="error")
                st.error(
                    "Falha na análise CrewAI. Verifique os logs do servidor para mais detalhes."
                )
                return

            status_container.update(
                label="✅ Análise concluída com sucesso!", state="complete", expanded=False
            )


            # Results Section
            st.divider()
            st.subheader(f"📊 Resultados: {project_name}")

            files = list_outputs_for_project(outputs_dir)

            if files:
                # Tabs for better organization
                tab1, tab2, tab3 = st.tabs(
                    ["📄 Relatório Final", "📂 Arquivos & Downloads", "🔍 Diff Analisado"]
                )

                # Tab 1: Report Preview
                with tab1:
                    # Tenta encontrar o relatorio final padrão
                    final_candidates = [
                        f for f in files if f.name.startswith(f"relatorio_final_{project_name}")
                    ]
                    final_report = final_candidates[0] if final_candidates else files[0]

                    try:
                        text = final_report.read_text(encoding="utf-8")
                        st.markdown(text)
                    except Exception as e:
                        st.error(f"Não foi possível ler o relatório: {e}")

                # Tab 2: Downloads
                with tab2:
                    st.info("Baixe os relatórios gerados individualmente ou em pacote.")

                    # Opção: baixar todos os outputs em um ZIP
                    if len(files) > 1:
                        try:
                            zip_buffer = io.BytesIO()
                            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
                                for f in files:
                                    zf.write(str(f), arcname=f.name)
                            zip_buffer.seek(0)
                            st.download_button(
                                "📦 Baixar Todos (ZIP)",
                                zip_buffer.getvalue(),
                                file_name=f"{project_name}_outputs.zip",
                                mime="application/zip",
                                type="primary",
                            )
                        except Exception:
                            st.warning("Não foi possível criar o arquivo ZIP para download.")

                    st.markdown("---")

                    for f in files:
                        c1, c2, c3 = st.columns([0.1, 0.7, 0.2])
                        with c1:
                            st.write("📄")
                        with c2:
                            st.write(f"**{f.name}**")
                            st.caption(
                                f"{round(f.stat().st_size / 1024, 1)} KB • {time.ctime(f.stat().st_mtime)}"
                            )
                        with c3:
                            try:
                                with f.open("rb") as fh:
                                    data = fh.read()
                                mime = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
                                st.download_button(
                                    "⬇️ Baixar", data, file_name=f.name, mime=mime, key=f.name
                                )
                            except Exception:
                                st.error("Erro")
                        st.divider()

                # Tab 3: Diff View
                with tab3:
                    if diff_content:
                        st.code(diff_content, language="diff")
                    else:
                        st.info(
                            "Nenhum diff foi utilizado nesta análise (Modo Completo ou Diff vazio)."
                        )

            else:
                st.warning("Nenhum arquivo de output encontrado.")

        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
            st.exception(e)
        finally:
            if temp_dir and os.path.exists(temp_dir):
                try:
                    shutil.rmtree(temp_dir)
                except Exception as e:
                    print(f"Erro ao limpar diretório temporário: {e}")


if __name__ == "__main__":
    app()
