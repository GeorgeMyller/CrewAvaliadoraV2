# CrewAvaliadora 🚀

## 🇧🇷 Português

Sistema de análise de codebase alimentado por IA usando 6 agentes especializados com Google Gemini 2.5 Flash e framework CrewAI.

### 🎯 Visão Geral

CrewAvaliadora é uma ferramenta abrangente de análise de codebase que usa inteligência artificial para fornecer code reviews de nível profissional, análise de arquitetura, avaliações de qualidade e relatórios de viabilidade comercial.

---

## 🇺🇸 English

AI-powered codebase analysis system using 6 specialized agents powered by Google Gemini 2.5 Flash and CrewAI framework.

### 🎯 Overview

CrewAvaliadora is a comprehensive codebase analysis tool that uses artificial intelligence to provide professional-grade code reviews, architecture analysis, quality assessments, and business viability reports.

### 🌟 Principais Recursos | Key Features

**🇧🇷 Português:**
- **6 Agentes IA Especializados**: Arquiteto de Software, Engenheiro de QA, Redator Técnico, Gerente de Produto, Especialista Legal e Engenheiro de IA
- **Análise Abrangente**: Arquitetura, qualidade de código, documentação, viabilidade comercial, conformidade legal e otimização de IA
- **Controle de Custos**: Rastreamento de custos de API e limitação de taxa integrados
- **Pronto para Produção**: Suite de testes completa, pipeline CI/CD e ferramentas profissionais
- **Saída Flexível**: Gera relatórios markdown detalhados com insights acionáveis

**🇺🇸 English:**
- **6 Specialized AI Agents**: Software Architect, QA Engineer, Technical Writer, Product Manager, Legal Specialist, and AI Engineer
- **Comprehensive Analysis**: Architecture, code quality, documentation, business viability, legal compliance, and AI optimization
- **Cost-Controlled**: Built-in API cost tracking and rate limiting
- **Production-Ready**: Complete test suite, CI/CD pipeline, and professional tooling
- **Flexible Output**: Generates detailed markdown reports with actionable insights

## 🚀 Início Rápido | Quick Start

### 🇧🇷 Pré-requisitos | 🇺🇸 Prerequisites

- Python 3.12+
- uv package manager
- Google Gemini API key

### 🇧🇷 Instalação | 🇺🇸 Installation

```bash
# Clone o repositório | Clone the repository
git clone <repository-url>
cd CrewAvaliadora

# Instale as dependências | Install dependencies
uv sync

# Configure o ambiente | Configure environment
cp .env.example .env
# 🇧🇷 Edite .env e adicione sua GEMINI_API_KEY
# 🇺🇸 Edit .env and add your GEMINI_API_KEY
```

### 🇧🇷 Obter Chave API | 🇺🇸 Get API Key

**🇧🇷 Português:**
1. Visite [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crie uma chave API gratuita
3. Adicione ao arquivo `.env`

**🇺🇸 English:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a free API key
3. Add to `.env` file

### 🇧🇷 Verificar Saúde do Sistema | 🇺🇸 Verify System Health

```bash
# 🇧🇷 Execute verificação de saúde para confirmar configuração
# 🇺🇸 Run health check to verify everything is configured correctly
uv run python utils/health_check.py

# 🇧🇷 Isto verificará:
# 🇺🇸 This will check:
# - Python version / Versão do Python
# - Required packages / Pacotes necessários
# - Environment variables / Variáveis de ambiente
# - Project structure / Estrutura do projeto
# - Gemini API connection / Conexão com API Gemini
```

### 🇧🇷 Executar Análise | 🇺🇸 Run Analysis

```bash
# 🇧🇷 Analisar diretório atual (limitado a 3 arquivos para teste)
# 🇺🇸 Analyze current directory (limited to 3 files for testing)
uv run python crew_avaliacao_completa.py

# 🇧🇷 Gerar relatório básico
# 🇺🇸 Generate basic report
uv run python gerar_relatorio.py .
```

## 📊 Relatórios Gerados | Generated Reports

**🇧🇷 Português:**

Os relatórios são salvos em `outputs/reports/` e incluem:

- Resumo executivo com pontuação geral de qualidade
- Análise de arquitetura e recomendações
- Avaliação de qualidade de código
- Auditoria de documentação
- Avaliação de viabilidade comercial
- Revisão de conformidade legal
- Sugestões de otimização de IA
- Roadmap em 3 fases (0-3, 3-6, 6-12 meses)
- Quick wins (alto impacto, baixo esforço)
- Top 5 riscos críticos com planos de mitigação

**🇺🇸 English:**

Reports are saved to `outputs/reports/` and include:

- Executive summary with overall quality score
- Architecture analysis and recommendations
- Code quality assessment
- Documentation audit
- Business viability evaluation
- Legal compliance review
- AI optimization suggestions
- Roadmap in 3 phases (0-3, 3-6, 6-12 months)
- Quick wins (high impact, low effort)
- Top 5 critical risks with mitigation plans

## 🏗️ Estrutura do Projeto | Project Structure

```
CrewAvaliadora/
├── src/
│   ├── crew_avaliadora.py       # 🇧🇷 Sistema principal | 🇺🇸 Main system
│   └── legacy/                  # 🇧🇷 Código arquivado | 🇺🇸 Archived code
├── config/
│   └── crew_config.yaml         # 🇧🇷 Config agentes | 🇺🇸 Agent config
├── utils/                       # 🇧🇷 Módulos utilitários | 🇺🇸 Utility modules
│   ├── api_cost_tracker.py      # 🇧🇷 Rastreamento custos | 🇺🇸 Cost tracking
│   ├── config_loader.py         # 🇧🇷 Carregador YAML | 🇺🇸 YAML loader
│   ├── health_check.py          # 🇧🇷 Diagnósticos | 🇺🇸 Diagnostics
│   └── template_engine.py       # 🇧🇷 Renderização | 🇺🇸 Report rendering
├── templates/
│   └── template_relatorio_final_v2.md  # 🇧🇷 Template Jinja2 | 🇺🇸 Jinja2 template
├── outputs/                     # 🇧🇷 Relatórios gerados | 🇺🇸 Generated reports
│   ├── reports/                 # 🇧🇷 Relatórios finais | 🇺🇸 Final reports
│   ├── analysis/                # 🇧🇷 Dados brutos | 🇺🇸 Raw data
│   ├── logs/                    # 🇧🇷 Logs execução | 🇺🇸 Execution logs
│   └── metadata/                # 🇧🇷 Métricas API | 🇺🇸 API metrics
├── tests/                       # 🇧🇷 Testes | 🇺🇸 Test suite
└── docs/                        # 🇧🇷 Documentação | 🇺🇸 Documentation
```

## 🧪 Testes | Testing

**🇧🇷 Português:**
```bash
# Executar todos os testes
uv run pytest tests/ -v

# Executar arquivo de teste específico
uv run pytest tests/test_basic.py -v

# Com cobertura
uv run pytest --cov=src tests/
```

**🇺🇸 English:**
```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_basic.py -v

# With coverage
uv run pytest --cov=src tests/
```

## 🛠️ Desenvolvimento | Development

### 🇧🇷 Configurar Ambiente de Desenvolvimento | 🇺🇸 Setup Development Environment

```bash
# 🇧🇷 Instalar dependências de dev | 🇺🇸 Install dev dependencies
uv sync --dev

# 🇧🇷 Instalar hooks pre-commit | 🇺🇸 Install pre-commit hooks
uv run pre-commit install

# 🇧🇷 Executar linting | 🇺🇸 Run linting
uv run ruff check .
uv run ruff format .

# 🇧🇷 Verificação de tipos | 🇺🇸 Type checking
uv run mypy . --ignore-missing-imports
```

### 🇧🇷 Contribuindo | 🇺🇸 Contributing

**🇧🇷 Português:** Veja [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes detalhadas.

**🇺🇸 English:** See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 Documentação | Documentation

**🇧🇷 Português:**
- [README_CREW.md](README_CREW.md) - Documentação detalhada do sistema CrewAI
- [CONTRIBUTING.md](CONTRIBUTING.md) - Diretrizes de contribuição
- [PROJECT_REVIEW.md](PROJECT_REVIEW.md) - Revisão do projeto

**🇺🇸 English:**
- [README_CREW.md](README_CREW.md) - Detailed CrewAI system documentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [PROJECT_REVIEW.md](PROJECT_REVIEW.md) - Project review

## 💰 Gerenciamento de Custos API | API Cost Management

**🇧🇷 Português:**

O sistema inclui rastreamento de custos integrado:
- Limite padrão: $5 USD por execução
- Máximo de 100 chamadas de API por execução
- Limitação de taxa: 60 chamadas/minuto
- Métricas de custo salvas em `outputs/metadata/`

Configure limites no `.env`:
```bash
MAX_API_CALLS_PER_RUN=100
MAX_COST_PER_RUN_USD=5.00
```

**🇺🇸 English:**

The system includes built-in cost tracking:
- Default limit: $5 USD per run
- Maximum 100 API calls per run
- Rate limiting: 60 calls/minute
- Cost metrics saved to `outputs/metadata/`

Configure limits in `.env`:
```bash
MAX_API_CALLS_PER_RUN=100
MAX_COST_PER_RUN_USD=5.00
```

## 🔒 Segurança | Security

**🇧🇷 Português:**
- Chaves API armazenadas em variáveis de ambiente (nunca no código)
- Hooks pre-commit verificam segredos
- Scanning de segurança Bandit no CI/CD
- Validação e sanitização de entrada

**🇺🇸 English:**
- API keys stored in environment variables (never in code)
- Pre-commit hooks scan for secrets
- Bandit security scanning in CI/CD
- Input validation and sanitization

## 📈 Pipeline CI/CD

**🇧🇷 Português:**

Testes automatizados a cada push:
- Testes unitários com pytest
- Linting de código com ruff
- Verificação de tipos com mypy
- Scanning de segurança com bandit
- Relatório de cobertura

**🇺🇸 English:**

Automated testing on every push:
- Unit tests with pytest
- Code linting with ruff
- Type checking with mypy
- Security scanning with bandit
- Coverage reporting

## 🤝 Os 6 Agentes IA | The 6 AI Agents

| 🇧🇷 Português | 🇺🇸 English | 🎯 Foco | Focus |
|---------------|-------------|---------|-------|
| 🏗️ **Arquiteto de Software** | **Software Architect** | Padrões arquiteturais, escalabilidade, integrações | Architecture patterns, scalability, integrations |
| 🧪 **Engenheiro QA** | **QA Engineer** | Cobertura de testes, qualidade, vulnerabilidades | Test coverage, quality, vulnerabilities |
| 📄 **Redator Técnico** | **Technical Writer** | Qualidade da documentação, guias | Documentation quality, guides |
| 🚀 **Gerente de Produto** | **Product Manager** | Prontidão de mercado, viabilidade comercial | Market readiness, business viability |
| ⚖️ **Especialista Legal** | **Legal Specialist** | Conformidade LGPD/GDPR, riscos | LGPD/GDPR compliance, risks |
| 🤖 **Engenheiro de IA** | **AI Engineer** | Otimização LLM, engenharia de prompts | LLM optimization, prompt engineering |

## 📊 Exemplo de Saída | Example Output

```markdown
# 🇧🇷 Resumo Executivo | 🇺🇸 Executive Summary
Pontuação Geral de Qualidade | Overall Quality Score: 78/100

**🇧🇷 Pontos Fortes | 🇺🇸 Strengths:**
- Integração API bem documentada | Well-documented API integration
- Arquitetura modular de agentes | Modular agent architecture
- Boa manipulação de erros | Good error handling

**🇧🇷 Problemas Críticos | 🇺🇸 Critical Issues:**
1. Falta cobertura de testes | Missing test coverage (Prioridade | Priority: HIGH)
2. Sem limitação de taxa | No rate limiting (Prioridade | Priority: HIGH)
...
```

## 🔧 Configuração | Configuration

**🇧🇷 Variáveis de ambiente principais:**

**🇺🇸 Key environment variables:**

```bash
# 🇧🇷 Obrigatório | 🇺🇸 Required
GEMINI_API_KEY=your_api_key_here

# 🇧🇷 Opcional | 🇺🇸 Optional
MODEL=gemini/gemini-2.5-flash
MAX_FILES_TO_ANALYZE=300
MAX_FILE_SIZE_BYTES=2097152
OUTPUT_DIR=outputs/reports
LOG_LEVEL=INFO
```

## 📦 Dependências | Dependencies

**🇧🇷 Principais:**

**🇺🇸 Core:**

- `crewai>=0.157.0` - Multi-agent framework
- `google-generativeai>=0.8.5` - Gemini API
- `python-dotenv>=1.1.1` - Environment management

**🇧🇷 Desenvolvimento:**

**🇺🇸 Dev:**

- `pytest>=7.4.0` - Testing framework
- `ruff>=0.1.9` - Linting and formatting
- `mypy>=1.7.0` - Type checking
- `pre-commit>=3.5.0` - Git hooks

## 🐛 Resolução de Problemas | Troubleshooting

### 🇧🇷 Erro de Chave API | 🇺🇸 API Key Error

```bash
# 🇧🇷 Verificar se a chave está definida | 🇺🇸 Verify key is set
echo $GEMINI_API_KEY

# 🇧🇷 Ou verificar arquivo .env | 🇺🇸 Or check .env file
cat .env
```

### 🇧🇷 Erros de Importação | 🇺🇸 Import Errors

```bash
# 🇧🇷 Reinstalar dependências | 🇺🇸 Reinstall dependencies
uv sync --reinstall
```

### 🇧🇷 Problemas de Permissão | 🇺🇸 Permission Issues

```bash
# 🇧🇷 Garantir que diretórios de saída existam
# 🇺🇸 Ensure output directories exist
mkdir -p outputs/reports outputs/metadata
```

## 📄 Licença | License

**🇧🇷 Português:** Licença MIT - Veja o arquivo LICENSE para detalhes.

**🇺🇸 English:** MIT License - See LICENSE file for details.

## 🙏 Agradecimentos | Acknowledgments

**🇧🇷 Construído com:**

**🇺🇸 Built with:**

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent orchestration
- [Google Gemini](https://ai.google.dev/) - Large language model
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

---

**🇧🇷 Desenvolvido com ❤️ usando CrewAI + Google Gemini 2.5 Flash**

**🇺🇸 Developed with ❤️ using CrewAI + Google Gemini 2.5 Flash**
