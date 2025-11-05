#!/usr/bin/env python3
"""
🎯 Script Unificado de Análise de Repositório
==============================================

Fluxo completo:
1. Clona repositório
2. Gera relatório base
3. Executa análise CrewAI
4. Organiza outputs na pasta outputs/
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def clone_repository(repo_url: str, target_dir: str) -> bool:
    """Clone repositório do GitHub"""
    try:
        logger.info(f"📥 Clonando repositório: {repo_url}")
        result = subprocess.run(
            ['git', 'clone', '--depth', '1', repo_url, target_dir],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            logger.info("✅ Repositório clonado com sucesso")
            return True
        else:
            logger.error(f"❌ Erro ao clonar: {result.stderr}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Erro: {e}")
        return False


def generate_base_report(repo_path: str, output_file: str) -> bool:
    """Gera relatório base da codebase"""
    try:
        logger.info("📊 Gerando relatório base...")
        
        # Usa quick report (mais rápido)
        quick_report_path = Path(__file__).parent / "quick_report.py"
        if not quick_report_path.exists():
            logger.error(f"❌ Script não encontrado: {quick_report_path}")
            return False
        
        # Executa gerador rápido
        result = subprocess.run(
            [sys.executable, str(quick_report_path), repo_path, output_file],
            capture_output=True,
            text=True,
            timeout=60  # Apenas 60 segundos
        )
        
        if result.returncode != 0:
            logger.error(f"❌ Erro ao gerar relatório: {result.stderr}")
            logger.error(f"stdout: {result.stdout}")
            return False
        
        # Verifica que arquivo foi criado
        if os.path.exists(output_file):
            size = os.path.getsize(output_file)
            logger.info(f"✅ Relatório base gerado: {output_file} ({size:,} bytes)")
            return True
        else:
            logger.error("❌ Relatório não foi gerado")
            return False
            
    except Exception as e:
        logger.error(f"❌ Erro: {e}")
        return False


def run_crewai_analysis(base_report: str, output_dir: str, project_name: str) -> bool:
    """Executa análise CrewAI"""
    try:
        logger.info("🚀 Iniciando análise CrewAI...")
        
        # Importa e executa crew
        sys.path.insert(0, str(Path(__file__).parent.parent))
        from src.crew_avaliadora import CodebaseAnalysisCrewV2
        
        # Lê relatório base
        with open(base_report, 'r', encoding='utf-8') as f:
            codebase_report = f.read()
        
        # Prepara output
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"relatorio_final_{project_name}_{timestamp}.md")
        
        # Executa análise
        crew = CodebaseAnalysisCrewV2()
        result = crew.analyze_codebase(codebase_report, output_file)
        
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            logger.info(f"✅ Análise completa: {output_file} ({file_size:,} bytes)")
            return True
        else:
            logger.error("❌ Relatório final não foi gerado")
            return False
            
    except Exception as e:
        logger.error(f"❌ Erro na análise: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print("Uso: python analyze_repo.py <repo_url>")
        print("Exemplo: python analyze_repo.py https://github.com/user/repo")
        sys.exit(1)
    
    repo_url = sys.argv[1]
    
    # Extrai nome do projeto
    project_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
    
    print("="*70)
    print("🎯 Análise Completa de Repositório")
    print("="*70)
    print(f"📦 Projeto: {project_name}")
    print(f"🔗 URL: {repo_url}")
    print("="*70)
    print()
    
    # Prepara diretórios
    base_dir = Path(__file__).parent.parent
    outputs_dir = base_dir / "outputs" / project_name
    outputs_dir.mkdir(parents=True, exist_ok=True)
    
    temp_dir = None
    try:
        # 1. Clone repositório
        temp_dir = tempfile.mkdtemp(prefix=f"crew_analysis_{project_name}_")
        if not clone_repository(repo_url, temp_dir):
            logger.error("❌ Falha ao clonar repositório")
            sys.exit(1)
        
        print()
        
        # 2. Gera relatório base
        base_report = outputs_dir / "relatorio_codebase_inicial.md"
        if not generate_base_report(temp_dir, str(base_report)):
            logger.error("❌ Falha ao gerar relatório base")
            sys.exit(1)
        
        print()
        
        # 3. Executa análise CrewAI
        if not run_crewai_analysis(str(base_report), str(outputs_dir), project_name):
            logger.error("❌ Falha na análise CrewAI")
            sys.exit(1)
        
        print()
        print("="*70)
        print("✅ ANÁLISE COMPLETA!")
        print("="*70)
        print(f"📁 Outputs salvos em: {outputs_dir}")
        print()
        
        # Lista arquivos gerados
        for f in outputs_dir.iterdir():
            if f.is_file():
                size = f.stat().st_size
                print(f"  📄 {f.name} ({size:,} bytes)")
        print()
        
    except KeyboardInterrupt:
        print("\n⚠️ Análise interrompida pelo usuário")
        sys.exit(130)
    except Exception as e:
        logger.error(f"❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Limpa diretório temporário
        if temp_dir and os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
                logger.info("🧹 Diretório temporário limpo")
            except Exception as e:
                logger.warning(f"⚠️ Erro ao limpar temp: {e}")


if __name__ == "__main__":
    main()
