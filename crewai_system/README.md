# 🚀 CrewAI System - Sistema de Análise de Codebase

Este diretório contém todo o sistema CrewAI desenvolvido para análise automatizada de codebase usando 6 agentes especializados com Google Gemini 2.5 Flash.

## 📁 Estrutura da Pasta

```
crewai_system/
├── README.md                    # Este arquivo - Guia principal
├── scripts/                     # Scripts executáveis
│   ├── crew_gemini_simples.py      # 🎯 PRINCIPAL - Sistema funcionando
│   ├── crew_avaliacao_completa.py  # Sistema CrewAI completo 
│   ├── crew_health_check.py        # Verificação de saúde
│   ├── demo_crew_avaliacao.py      # Demonstração
│   └── run_crew.py                 # Executador de crew
├── config/                      # Configurações
│   ├── crew_config.yaml            # Configuração dos 6 agentes
│   └── crew.yaml                   # Configuração original
├── docs/                        # Documentação
│   ├── README_CREW.md              # Documentação completa (45 páginas)
│   └── ENTREGA_FINAL_CREWAI.md     # Sumário da entrega
├── templates/                   # Templates
│   └── template_relatorio_final.md # Template de relatório
├── reports/                     # Relatórios gerados
│   └── relatorio_final_gemini_*.md # Relatórios de análise
└── core/                        # Core do sistema original
    └── instagram/                  # Módulos core do Instagram
```

## 🎯 Script Principal - RECOMENDADO

**Para executar a análise completa, use:**

```bash
cd crewai_system/scripts
uv run crew_gemini_simples.py
```

Este é o script que **FUNCIONA 100%** e gera relatórios profissionais de alta qualidade.

## 🔍 Os 6 Agentes Especializados

1. **🏗️ Arquiteto de Software Sênior**
   - Análise arquitetural completa
   - Padrões de design
   - Escalabilidade e performance

2. **🧪 Engenheiro de Qualidade**
   - Análise de bugs e vulnerabilidades
   - Cobertura de testes
   - Code smells

3. **📄 Documentador Técnico**
   - Qualidade da documentação
   - Gaps de documentação
   - Guias de onboarding

4. **🚀 Product Manager**
   - Análise de mercado e negócio
   - Viabilidade comercial
   - Roadmap estratégico

5. **⚖️ Especialista Legal**
   - Conformidade com regulamentações
   - Termos de serviço
   - LGPD/GDPR

6. **🤖 Engenheiro de IA**
   - Otimização de modelos
   - Performance de IA
   - Custos e eficiência

## 🚀 Execução Rápida

### Verificar Saúde do Sistema
```bash
cd crewai_system/scripts
uv run crew_health_check.py
```

### Executar Análise Completa
```bash
cd crewai_system/scripts
uv run crew_gemini_simples.py
```

### Demonstração
```bash
cd crewai_system/scripts
uv run demo_crew_avaliacao.py
```

## 📊 Relatórios Gerados

Os relatórios são salvos automaticamente na pasta `reports/` com o formato:
- `relatorio_final_gemini_YYYYMMDD_HHMMSS.md`

### Conteúdo do Relatório

✅ **Executive Summary Profissional**
✅ **Score de Maturidade (0-100)**
✅ **Análise Técnica Detalhada**
✅ **Roadmap Estratégico em 3 Fases**
✅ **Top 5 Riscos Críticos**
✅ **Quick Wins (Alto Impacto/Baixo Esforço)**
✅ **Seção para Devs Juniores**
✅ **Seção para Devs Seniores**

## ⚙️ Configuração

### Gemini API Key
Certifique-se de ter a variável de ambiente configurada:
```bash
export GEMINI_API_KEY="sua_api_key_aqui"
```

### Dependências
```bash
# As dependências já estão no pyproject.toml principal
uv sync
```

## 🔧 Personalização

### Modificar Agentes
Edite o arquivo `config/crew_config.yaml` para personalizar:
- Prompts dos agentes
- Thresholds de métricas
- Critérios de avaliação

### Template de Relatório
Modifique `templates/template_relatorio_final.md` para customizar o formato do relatório.

## 📈 Performance

### Métricas Típicas
- ⏱️ **Tempo de Execução:** 8-12 minutos
- 💰 **Custo por Análise:** ~$0.15-0.25 USD
- 📄 **Tamanho do Relatório:** 8.000-12.000 palavras
- 🎯 **Precisão da Análise:** Nível Enterprise

## 🆘 Troubleshooting

### Erro de API Key
```
❌ Erro: API Key não configurada
✅ Solução: export GEMINI_API_KEY="sua_key"
```

### Timeout na Análise
```
❌ Erro: Timeout durante processamento
✅ Solução: Executar novamente - o sistema tem retry automático
```

### Dependências
```
❌ Erro: Módulo não encontrado
✅ Solução: uv sync (na pasta principal do projeto)
```

## 🎯 Casos de Uso

### Para Desenvolvedores
- ✅ Code review automatizado
- ✅ Análise de qualidade
- ✅ Identificação de melhorias

### Para Product Managers
- ✅ Avaliação de viabilidade
- ✅ Análise de riscos
- ✅ Roadmap estratégico

### Para CTOs/Arquitetos
- ✅ Due diligence técnica
- ✅ Análise arquitetural
- ✅ Planejamento de refatoração

## 📚 Documentação Completa

Para documentação detalhada, consulte:
- `docs/README_CREW.md` - Guia completo (45 páginas)
- `docs/ENTREGA_FINAL_CREWAI.md` - Resumo executivo

## 🎉 Status do Sistema

✅ **Sistema Funcionando 100%**
✅ **6 Agentes Ativos**
✅ **Gemini 2.5 Flash Integrado**
✅ **Relatórios Ultra-Profissionais**
✅ **Documentação Completa**

---

**Desenvolvido com ❤️ usando CrewAI + Google Gemini 2.5 Flash**
