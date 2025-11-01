# 🎯 Reorganização da Estrutura de Outputs

## ✅ Mudanças Implementadas

### 1. Estrutura Organizada por Projeto

Agora todas as saídas são organizadas em pastas específicas por projeto:

```
outputs/
└── {nome_do_projeto}_{timestamp}/
    ├── reports/           # Relatórios consolidados
    ├── metadata/          # Metadados JSON
    └── per_file_reports/  # Análises individuais
```

### 2. Identificação Automática do Projeto

O sistema agora extrai automaticamente o nome do projeto de:
- URLs do GitHub (ex: `github.com/user/my-project` → `my-project`)
- Caminhos locais (ex: `/path/to/my-project` → `my-project`)
- Diretório atual como fallback

### 3. Principais Melhorias

#### a) Novo Parâmetro `project_name`
```python
crew = CodebaseAnalysisCrew(project_name="my-project")
```

#### b) Método de Extração
```python
project_name = CodebaseAnalysisCrew.extract_project_name_from_path(path)
```

## 📦 Exemplo de Uso

### Main Interativo
```bash
python crew_avaliacao_completa.py
```

O sistema agora pergunta pelo caminho/URL e identifica automaticamente o projeto.

---

**Data**: 2025-11-01  
**Status**: ✅ Implementado
