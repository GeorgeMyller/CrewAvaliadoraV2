# 📁 Outputs Directory

Este diretório contém todas as análises de codebase geradas pelo sistema CrewAI Avaliadora.

## 📂 Estrutura

Cada análise cria uma pasta com a seguinte estrutura:

```
outputs/
└── {nome_do_projeto}_{timestamp}/
    ├── reports/
    │   ├── relatorio_final_{timestamp}.md       # Relatório consolidado final
    │   └── relatorio_final_fallback_{timestamp}.md  # Relatório fallback (se necessário)
    ├── metadata/
    │   └── metadata_analise_{timestamp}.json    # Metadados da análise
    └── per_file_reports/
        ├── arquivo1_{timestamp}.md              # Análise individual do arquivo 1
        ├── arquivo2_{timestamp}.md              # Análise individual do arquivo 2
        └── ...
```

## 🏷️ Nomenclatura

- **Nome do Projeto**: Extraído automaticamente da URL do GitHub ou do caminho local
- **Timestamp**: Formato `YYYYMMDD_HHMMSS` para fácil ordenação cronológica

## 📊 Conteúdo

### Reports
Relatórios consolidados gerados pela crew de agentes especializados, contendo análise completa da codebase.

### Metadata
Informações técnicas sobre a análise: timestamp, número de arquivos analisados, agentes utilizados, etc.

### Per File Reports
Análises individuais de cada arquivo da codebase, geradas antes da consolidação final.

## 🔍 Exemplo

Para o repositório `https://github.com/user/my-awesome-project` analisado em 01/11/2025 às 17:30:45:

```
outputs/
└── my-awesome-project_20251101_173045/
    ├── reports/
    │   └── relatorio_final_20251101_173045.md
    ├── metadata/
    │   └── metadata_analise_20251101_173045.json
    └── per_file_reports/
        ├── main.py_20251101_173045.md
        ├── config.yaml_20251101_173045.md
        └── README.md_20251101_173045.md
```

## 🧹 Manutenção

Você pode deletar pastas antigas para liberar espaço. Cada pasta é independente e autocontida.
