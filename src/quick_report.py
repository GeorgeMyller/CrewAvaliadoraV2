#!/usr/bin/env python3
"""
Quick Codebase Report Generator - Sem chamadas API
Gera relatório estrutural rápido para input da CrewAI
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Configurações
IGNORE_FOLDERS = {'.venv', 'node_modules', '__pycache__', 'backup', '.git', 'temp', 'logs', 'dist', 'build', '.pytest_cache', '.ruff_cache'}
IGNORE_EXTENSIONS = {'.log', '.lock', '.pyc', '.pyo', '.tmp', '.cache', '.DS_Store'}
MAX_FILE_SIZE = 1024 * 1024  # 1MB

def scan_directory(base_path: str) -> dict:
    """Escaneia diretório e coleta estatísticas"""
    stats = {
        'total_files': 0,
        'total_size': 0,
        'by_extension': defaultdict(lambda: {'count': 0, 'size': 0}),
        'by_directory': defaultdict(lambda: {'count': 0, 'size': 0}),
        'files': []
    }
    
    base = Path(base_path)
    
    for root, dirs, files in os.walk(base):
        # Remove ignored dirs
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
        
        rel_root = Path(root).relative_to(base)
        
        for filename in files:
            filepath = Path(root) / filename
            
            # Skip ignored extensions
            if filepath.suffix.lower() in IGNORE_EXTENSIONS:
                continue
            
            try:
                size = filepath.stat().st_size
                
                # Skip large files
                if size > MAX_FILE_SIZE:
                    continue
                
                stats['total_files'] += 1
                stats['total_size'] += size
                
                ext = filepath.suffix or 'no_extension'
                stats['by_extension'][ext]['count'] += 1
                stats['by_extension'][ext]['size'] += size
                
                dir_name = str(rel_root) if str(rel_root) != '.' else 'root'
                stats['by_directory'][dir_name]['count'] += 1
                stats['by_directory'][dir_name]['size'] += size
                
                stats['files'].append({
                    'path': str(filepath.relative_to(base)),
                    'size': size,
                    'ext': ext
                })
                
            except Exception as e:
                print(f"⚠️ Erro ao processar {filepath}: {e}", file=sys.stderr)
    
    return stats

def format_size(bytes_size):
    """Formata tamanho em bytes para string legível"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} TB"

def read_file_content(filepath: Path, max_lines: int = 100) -> str:
    """Lê conteúdo de arquivo com limite de linhas"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()[:max_lines]
            content = ''.join(lines)
            if len(lines) >= max_lines:
                content += f"\n... (truncado após {max_lines} linhas)\n"
            return content
    except Exception as e:
        return f"[Erro ao ler arquivo: {e}]"

def generate_report(base_path: str, output_file: str):
    """Gera relatório markdown"""
    
    print(f"📊 Escaneando: {base_path}")
    stats = scan_directory(base_path)
    base = Path(base_path)
    
    # Gera relatório
    report = []
    report.append("# 📊 Relatório Técnico da Codebase\n")
    report.append(f"**Gerado em:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Diretório analisado:** `{base_path}`\n")
    report.append(f"**Total de arquivos:** {stats['total_files']}\n")
    report.append(f"**Tamanho total:** {format_size(stats['total_size'])}\n\n")
    
    # Estatísticas por extensão
    report.append("## 📈 Distribuição por Extensão\n\n")
    sorted_exts = sorted(stats['by_extension'].items(), 
                        key=lambda x: x[1]['count'], reverse=True)
    
    for ext, data in sorted_exts[:20]:  # Top 20
        report.append(f"- **{ext}**: {data['count']} arquivos ({format_size(data['size'])})\n")
    
    report.append("\n## 📁 Estrutura de Diretórios\n\n")
    sorted_dirs = sorted(stats['by_directory'].items(),
                        key=lambda x: x[1]['count'], reverse=True)
    
    for dir_name, data in sorted_dirs[:30]:  # Top 30
        report.append(f"- `{dir_name}`: {data['count']} arquivos ({format_size(data['size'])})\n")
    
    # NOVO: Lê e inclui conteúdo do README se existir
    report.append("\n## 📖 README / Descrição do Projeto\n\n")
    readme_found = False
    for readme_name in ['README.md', 'README.txt', 'README', 'readme.md']:
        readme_path = base / readme_name
        if readme_path.exists():
            report.append(f"### Conteúdo de {readme_name}\n\n")
            content = read_file_content(readme_path, max_lines=200)
            report.append(f"```\n{content}\n```\n\n")
            readme_found = True
            break
    
    if not readme_found:
        report.append("*Nenhum README encontrado*\n\n")
    
    # NOVO: Lê arquivos principais de código
    report.append("\n## 💻 Código Principal\n\n")
    
    # Procura por arquivos de entrada comuns
    entry_points = ['main.py', 'app.py', '__main__.py', 'index.py', 'run.py', 'setup.py', 'pyproject.toml', 'package.json']
    found_entry = False
    
    for entry in entry_points:
        entry_path = base / entry
        if entry_path.exists():
            report.append(f"### {entry}\n\n")
            content = read_file_content(entry_path, max_lines=100)  # Aumentado para 100
            report.append(f"```\n{content}\n```\n\n")
            found_entry = True
            break
    
    if not found_entry:
        report.append("*Nenhum arquivo de entrada principal identificado*\n\n")
    
    # MELHORADO: Lista TODOS os arquivos Python/JS principais com snippets MAIORES
    report.append("\n## 📄 Arquivos de Código Detalhados\n\n")
    report.append("*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*\n\n")
    
    code_files = [f for f in stats['files'] if f['ext'] in ['.py', '.js', '.ts', '.java', '.go', '.rs', '.cpp', '.c', '.rb']]
    sorted_code = sorted(code_files, key=lambda x: x['size'], reverse=True)[:10]  # Aumentado para 10 arquivos
    
    for file_info in sorted_code:
        filepath = base / file_info['path']
        if filepath.exists() and 'test' not in file_info['path'].lower():  # Pula arquivos de teste
            report.append(f"### {file_info['path']} ({format_size(file_info['size'])})\n\n")
            content = read_file_content(filepath, max_lines=80)  # Aumentado para 80 linhas
            report.append(f"```python\n{content}\n```\n\n")
    
    # Lista todos arquivos (mais resumido)
    report.append("\n## 📂 Lista Completa de Arquivos\n\n")
    sorted_files = sorted(stats['files'], key=lambda x: x['size'], reverse=True)
    
    for file in sorted_files[:50]:  # Top 50
        report.append(f"- `{file['path']}` ({format_size(file['size'])})\n")
    
    report.append("\n---\n")
    report.append("*Relatório gerado automaticamente para análise CrewAI*\n")
    report.append(f"\n**IMPORTANTE:** Este relatório contém código real do projeto. ")
    report.append(f"A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.\n")
    
    # Salva relatório
    content = ''.join(report)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Relatório gerado: {output_file}")
    print(f"📊 Total processado: {stats['total_files']} arquivos")
    print(f"📄 Conteúdo incluído: README + {len(sorted_code)} arquivos de código com ~80 linhas cada")

def main():
    if len(sys.argv) < 2:
        print("Uso: python quick_report.py <diretorio>")
        sys.exit(1)
    
    base_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "relatorio_codebase.md"
    
    if not os.path.exists(base_path):
        print(f"❌ Diretório não encontrado: {base_path}")
        sys.exit(1)
    
    generate_report(base_path, output_file)

if __name__ == "__main__":
    main()
