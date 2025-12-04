#!/usr/bin/env python3
"""
✅ CREW HEALTH CHECK - Verificação Completa do Sistema
=====================================================

Script que verifica se toda a infraestrutura CrewAI está funcionando corretamente.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import importlib.util


def print_header(title):
    """🎯 Imprime cabeçalho formatado"""
    print(f"\n{'='*60}")
    print(f"🎯 {title}")
    print(f"{'='*60}")


def print_status(item, status, details=""):
    """📊 Imprime status formatado"""
    icon = "✅" if status else "❌"
    print(f"{icon} {item}")
    if details:
        print(f"   💡 {details}")


def check_python_version():
    """🐍 Verifica versão do Python"""
    version = sys.version_info
    required_major, required_minor = 3, 12
    
    is_valid = version.major >= required_major and version.minor >= required_minor
    
    print_status(
        f"Python {version.major}.{version.minor}.{version.micro}",
        is_valid,
        f"Requerido: Python {required_major}.{required_minor}+" if not is_valid else "Versão adequada"
    )
    
    return is_valid


def check_package_installed(package_name, import_name=None):
    """📦 Verifica se pacote está instalado"""
    if import_name is None:
        import_name = package_name.replace("-", "_")
    
    try:
        importlib.import_module(import_name)
        print_status(f"Pacote: {package_name}", True, "Instalado")
        return True
    except ImportError:
        print_status(f"Pacote: {package_name}", False, f"Execute: uv sync")
        return False


def check_env_variable(var_name):
    """🔑 Verifica variável de ambiente"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass
    
    value = os.getenv(var_name)
    is_set = bool(value and value.strip())
    
    print_status(
        f"Variável: {var_name}",
        is_set,
        "Configurada" if is_set else f"Configure no .env: {var_name}=sua_chave"
    )
    
    return is_set


def check_file_exists(file_path):
    """📄 Verifica se arquivo existe"""
    exists = os.path.exists(file_path)
    print_status(
        f"Arquivo: {file_path}",
        exists,
        "Encontrado" if exists else "Não encontrado"
    )
    return exists


def test_gemini_connection():
    """🧪 Testa conexão com Gemini API"""
    try:
        import google.generativeai as genai
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print_status("Conexão Gemini", False, "API key não configurada")
            return False
        
        genai.configure(api_key=api_key.strip())
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Teste simples
        response = model.generate_content("Say 'test ok'")
        
        print_status("Conexão Gemini", True, "API funcionando corretamente")
        return True
        
    except Exception as e:
        print_status("Conexão Gemini", False, f"Erro: {str(e)[:50]}")
        return False


def check_crewai_setup():
    """🤖 Verifica setup do CrewAI"""
    try:
        from crewai import Agent, Task, Crew
        print_status("CrewAI Setup", True, "Imports funcionando")
        return True
    except ImportError as e:
        print_status("CrewAI Setup", False, f"Execute: uv sync")
        return False


def check_project_structure():
    """📁 Verifica estrutura do projeto"""
    required_files = [
        "src/crew_avaliadora.py",
        "src/analyze_repo.py",
        "pyproject.toml",
        ".env.example"
    ]
    
    required_dirs = [
        "tests",
        "utils",
        "outputs",
        "config",
        "templates"
    ]
    
    all_good = True
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            print_status(f"Arquivo: {file_path}", False, "Não encontrado")
            all_good = False
    
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            print_status(f"Diretório: {dir_path}", False, "Não encontrado")
            all_good = False
    
    if all_good:
        print_status("Estrutura do Projeto", True, "Todos os arquivos presentes")
    
    return all_good


def run_health_check():
    """🏥 Executa verificação completa de saúde"""
    print_header("CREW HEALTH CHECK - Análise Completa")
    print(f"📅 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = {}
    
    # Verificações
    print_header("1. AMBIENTE PYTHON")
    results['python'] = check_python_version()
    
    print_header("2. PACOTES ESSENCIAIS")
    results['crewai'] = check_package_installed("crewai")
    results['google_ai'] = check_package_installed("google-generativeai", "google.generativeai")
    results['dotenv'] = check_package_installed("python-dotenv", "dotenv")
    results['pytest'] = check_package_installed("pytest")
    
    print_header("3. VARIÁVEIS DE AMBIENTE")
    results['api_key'] = check_env_variable("GEMINI_API_KEY")
    
    print_header("4. ESTRUTURA DO PROJETO")
    results['structure'] = check_project_structure()
    
    print_header("5. SETUP CREWAI")
    results['crewai_setup'] = check_crewai_setup()
    
    print_header("6. TESTE DE CONEXÃO (OPCIONAL)")
    if results.get('api_key'):
        print("⏳ Testando conexão com Gemini (pode levar alguns segundos)...")
        results['gemini'] = test_gemini_connection()
    else:
        print_status("Teste Gemini", False, "Pulado - API key não configurada")
        results['gemini'] = False
    
    # Resumo final
    print_header("RESUMO FINAL")
    
    total_checks = len(results)
    passed_checks = sum(1 for v in results.values() if v)
    
    print(f"\n📊 Resultado: {passed_checks}/{total_checks} verificações passaram")
    
    if passed_checks == total_checks:
        print("\n✅ SISTEMA PRONTO! Tudo funcionando perfeitamente.")
        print("🚀 Você pode executar: uv run python src/crew_avaliadora.py")
        return True
    elif passed_checks >= total_checks * 0.7:
        print("\n⚠️ SISTEMA PARCIALMENTE PRONTO. Algumas configurações faltando.")
        print("🔧 Corrija os itens marcados com ❌ acima.")
        return False
    else:
        print("\n❌ SISTEMA NÃO PRONTO. Muitas configurações faltando.")
        print("📖 Consulte o README.md para instruções de setup.")
        return False


if __name__ == "__main__":
    try:
        success = run_health_check()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Verificação interrompida pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erro durante verificação: {e}")
        sys.exit(1)
