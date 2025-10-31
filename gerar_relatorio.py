import os
import sys
import time
import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ======================
# CONFIGURAÇÕES
# ======================
IGNORE_FOLDERS = {'.venv', 'node_modules', '__pycache__', 'backup', 'backups', '.git', 'temp', 'logs', '.git', 'user_configs', 'user_analysis', 'user_captions', 'caption_analysis'}
IGNORE_EXTENSIONS = {'.log', '.lock', '.pyc', '.pyo', '.egg-info', '.tmp', '.cache'}
MAX_CHARS_PER_FILE = 6000
API_KEY = os.getenv("GEMINI_API_KEY")  # Defina sua chave no ambiente
VERBOSE = False  # Será definido via argumento

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("⚠️ AVISO: GEMINI_API_KEY não encontrada. Resumos serão simulados.")

# ======================
# FUNÇÕES AUXILIARES
# ======================

def listar_arquivos(base_dir):
    """Lista todos os arquivos, ignorando pastas irrelevantes."""
    arquivos = []
    total_ignorados = 0
    
    if VERBOSE:
        print(f"🔍 Percorrendo diretório: {base_dir}")
    
    for root, dirs, files in os.walk(base_dir):
        # Remove pastas ignoradas da lista
        dirs_originais = dirs.copy()
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
        
        if VERBOSE and len(dirs_originais) != len(dirs):
            ignoradas = set(dirs_originais) - set(dirs)
            print(f"  📂 Ignorando pastas: {', '.join(ignoradas)}")
        
        for file in files:
            arquivo_path = Path(root) / file
            
            # Ignora arquivos por extensão
            if arquivo_path.suffix.lower() in IGNORE_EXTENSIONS:
                total_ignorados += 1
                continue
                
            # Ignora arquivos muito grandes (>1MB)
            try:
                if arquivo_path.stat().st_size > 1024 * 1024:
                    if VERBOSE:
                        print(f"  ⚠️ Arquivo muito grande ignorado: {arquivo_path}")
                    total_ignorados += 1
                    continue
            except Exception:
                pass
                
            arquivos.append(arquivo_path)
    
    if VERBOSE:
        print(f"✅ Encontrados {len(arquivos)} arquivos para análise")
        print(f"🚫 Ignorados {total_ignorados} arquivos por tamanho/extensão")
    
    return arquivos

def classificar_arquivo(path):
    """Classifica o arquivo por tipo."""
    nome = path.name.lower()
    ext = path.suffix.lower()
    if "test" in nome:
        return "testes"
    if path.parts[0] == "docs" or ext in {".md", ".rst"}:
        return "documentacao"
    if ext in {".py", ".js", ".ts", ".java", ".go"}:
        return "codigo"
    if ext in {".yml", ".yaml", ".json", ".ini", ".env"}:
        return "configuracao"
    return "outros"

def ler_arquivo(path):
    """Lê conteúdo de um arquivo com limite de tamanho."""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(MAX_CHARS_PER_FILE)
    except Exception as e:
        return f"[ERRO ao ler o arquivo: {e}]"

def resumir_com_gemini(conteudo, caminho):
    """Usa o Gemini 2.5 Flash para gerar resumo."""
    if not API_KEY:
        return f"[SIMULADO] Arquivo {caminho.name} - Resumo indisponível (sem API key)"
    
    prompt = f"""
Você é um assistente técnico que lê código e documentação.
Analise o seguinte arquivo: {caminho}

Tarefas:
1. Resuma o que ele faz.
2. Explique o papel dele no projeto.
3. Liste possíveis melhorias.

Arquivo:
{conteudo}
"""
    try:
        if VERBOSE:
            print(f"  🤖 Analisando com Gemini: {caminho}")
        
        model = genai.GenerativeModel("gemini-2.5-flash")
        resp = model.generate_content(prompt)
        
        if VERBOSE:
            print(f"  ✅ Resumo gerado para: {caminho}")
        
        return resp.text
    except Exception as e:
        error_msg = f"[ERRO ao resumir com Gemini: {e}]"
        if VERBOSE:
            print(f"  ❌ {error_msg}")
        return error_msg

# ======================
# SCRIPT PRINCIPAL
# ======================

def gerar_relatorio(base_dir, saida):
    arquivos = listar_arquivos(base_dir)
    relatorios = {"codigo": [], "documentacao": [], "configuracao": [], "testes": [], "outros": []}
    
    if VERBOSE:
        print(f"\n📊 Iniciando análise de {len(arquivos)} arquivos...")
    
    total_processados = 0
    for i, arquivo in enumerate(arquivos, 1):
        if VERBOSE:
            print(f"\n[{i}/{len(arquivos)}] 📄 Processando: {arquivo}")
        
        categoria = classificar_arquivo(arquivo)
        
        if VERBOSE:
            print(f"  📋 Categoria: {categoria}")
        
        conteudo = ler_arquivo(arquivo)
        resumo = resumir_com_gemini(conteudo, arquivo)
        relatorios[categoria].append({"arquivo": str(arquivo), "resumo": resumo})
        
        total_processados += 1
        
        # Progresso a cada 10 arquivos quando não verbose
        if not VERBOSE and total_processados % 10 == 0:
            print(f"📊 Progresso: {total_processados}/{len(arquivos)} arquivos processados...")

    # Salva relatório
    if VERBOSE:
        print(f"\n💾 Salvando relatório em: {saida}")
    
    with open(saida, "w", encoding="utf-8") as out:
        out.write("# 📊 Relatório Técnico da Codebase\n\n")
        out.write(f"**Gerado em:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write(f"**Total de arquivos analisados:** {total_processados}\n\n")
        
        # Sumário por categoria
        out.write("## 📋 Resumo por Categoria\n\n")
        for categoria, itens in relatorios.items():
            if itens:
                out.write(f"- **{categoria.capitalize()}:** {len(itens)} arquivos\n")
        out.write("\n---\n\n")
        
        # Detalhes por categoria
        for categoria, itens in relatorios.items():
            if not itens:
                continue
            out.write(f"## Categoria: {categoria.capitalize()}\n\n")
            for item in itens:
                out.write(f"### Arquivo: `{item['arquivo']}`\n\n")
                out.write(f"{item['resumo']}\n\n")
                out.write("---\n\n")
    
    print(f"[OK] Relatório gerado em: {saida}")
    print(f"📊 Total processado: {total_processados} arquivos")
    
    # Sumário final
    for categoria, itens in relatorios.items():
        if itens:
            print(f"  📁 {categoria.capitalize()}: {len(itens)} arquivos")

if __name__ == "__main__":
    # Parse argumentos
    if len(sys.argv) < 2:
        print("Uso: python gerar_relatorio.py <diretorio_do_projeto> [saida.md] [--verbose|-v]")
        print("\nExemplo:")
        print("  python gerar_relatorio.py . --verbose")
        print("  python gerar_relatorio.py src relatorio_src.md -v")
        sys.exit(1)

    # Processa argumentos
    args = sys.argv[1:]
    base_dir = args[0]
    
    # Detecta verbose
    if "--verbose" in args or "-v" in args:
        VERBOSE = True
        args = [arg for arg in args if arg not in ["--verbose", "-v"]]
    
    # Nome do arquivo de saída
    saida = args[1] if len(args) > 1 else "relatorio_codebase.md"
    
    if VERBOSE:
        print("🚀 MODO VERBOSE ATIVADO")
        print(f"📁 Diretório: {base_dir}")
        print(f"📄 Arquivo de saída: {saida}")
        print(f"🔑 API Gemini: {'✅ Configurada' if API_KEY else '❌ Não encontrada'}")
        print("-" * 50)

    gerar_relatorio(base_dir, saida)
