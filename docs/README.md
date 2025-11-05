# 🤖 CrewAI Avaliadora - Análise Profissional de Codebase

Sistema automatizado de análise de código usando CrewAI e Google Gemini 2.5 Flash. Avalia qualidade, segurança, performance e oferece recomendações detalhadas para desenvolvedores júnior e sênior.

## 🎯 Características

- ✅ **6 Agentes Especializados** - Arquiteto, Segurança, DevOps, Performance, Quality Assurance e Product Manager
- ✅ **Análise Profunda** - Avalia estrutura, código, dependências, segurança e performance
- ✅ **Relatórios Detalhados** - Reports profissionais com scores, insights e recomendações
- ✅ **Configurável via YAML** - Customize agentes e tasks sem mexer no código
- ✅ **Templates Personalizáveis** - Modifique formato dos relatórios facilmente

## 🚀 Quick Start

### 1. Setup

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/CrewAvaliadora.git
cd CrewAvaliadora

# Instale dependências
pip install -r requirements.txt

# Configure API Key
cp .env.example .env
# Edite .env e adicione sua GEMINI_API_KEY
```

### 2. Execute Análise

```bash
# Método 1: Script helper
./scripts/run_analysis.sh https://github.com/user/repo

# Método 2: Direto com Python
python src/crew_avaliadora.py https://github.com/user/repo
```

### 3. Verifique Resultados

```bash
# Relatórios ficam em:
outputs/reports/{project_name}_{date}/
  ├── relatorio_final.md    # Relatório principal
  └── metadata.json         # Metadados da análise
```

## 📁 Estrutura do Projeto

```
CrewAvaliadora/
├── src/                          # Código fonte
│   ├── crew_avaliadora.py       # Script principal
│   └── legacy/                   # Código antigo (referência)
├── config/                       # Configurações
│   ├── crew_config.yaml         # Definição de agentes/tasks
│   └── .env.example             # Template de variáveis
├── templates/                    # Templates de relatórios
│   └── relatorio_final_v2.md    # Template atual
├── utils/                        # Utilitários
│   ├── config_loader.py         # Carregador de YAML
│   ├── template_engine.py       # Engine de templates
│   └── health_check.py          # Diagnóstico do sistema
├── outputs/                      # Saídas geradas
│   ├── reports/                 # Relatórios finais
│   ├── analysis/                # Análises detalhadas
│   └── logs/                    # Logs de execução
├── tests/                        # Testes
└── docs/                         # Documentação
```

## ⚙️ Configuração Avançada

### Customizar Agentes

Edite `config/crew_config.yaml`:

```yaml
agents:
  arquiteto_senior:
    name: "Arquiteto Sênior"
    emoji: "🏗️"
    role: "Arquiteto de Software Sênior"
    goal: "Avaliar qualidade arquitetural..."
    backstory: "Arquiteto com 15+ anos..."
    max_iterations: 5
    delegation: false
```

### Customizar Relatório

Edite `templates/relatorio_final_v2.md` com seus placeholders:

```markdown
# {{PROJECT_NAME}} - Análise Completa

## 📊 Score Geral: {{GENERAL_SCORE}}/100
{{GENERAL_ANALYSIS}}
...
```

### Variáveis de Ambiente

```bash
# .env
GEMINI_API_KEY=your_api_key_here
MODEL=gemini/gemini-2.5-flash  # Opcional
LOG_LEVEL=INFO                  # DEBUG, INFO, WARNING, ERROR
```

## 🧪 Testes

```bash
# Executar todos os testes
pytest tests/

# Teste específico
pytest tests/test_basic.py

# Com cobertura
pytest --cov=src tests/
```

## 📖 Documentação Adicional

- [Arquitetura do Sistema](ARCHITECTURE.md)
- [Guia de Contribuição](../CONTRIBUTING.md)
- [Histórico do Projeto](project-history/)

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](../CONTRIBUTING.md) para detalhes.

## 📝 Licença

MIT License - veja LICENSE para detalhes.

## 🆘 Suporte

- 📧 Email: seu-email@example.com
- 🐛 Issues: https://github.com/seu-usuario/CrewAvaliadora/issues
- 📖 Docs: https://docs.seu-site.com

---

**Desenvolvido com ❤️ usando CrewAI e Google Gemini**
