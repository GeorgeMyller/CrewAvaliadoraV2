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
- [uv](https://github.com/astral-sh/uv) package manager
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
uv run python src/utils/health_check.py
```

### 🇧🇷 Executar Análise | 🇺🇸 Run Analysis

```bash
# 🇧🇷 Iniciar aplicação Streamlit (Interface Gráfica)
# 🇺🇸 Start Streamlit application (GUI)
uv run streamlit run src/streamlit_app.py

# 🇧🇷 Ou executar via linha de comando
# 🇺🇸 Or run via command line
uv run python src/main.py
```

## 📊 Relatórios Gerados | Generated Reports

**🇧🇷 Português:**

Os relatórios são salvos em `outputs/` e incluem:

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

Reports are saved to `outputs/` and include:

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
│   ├── analyze_repo.py          # 🇧🇷 Lógica de análise | 🇺🇸 Analysis logic
│   ├── streamlit_app.py         # 🇧🇷 Interface Web | 🇺🇸 Web Interface
│   ├── config/                  # 🇧🇷 Configurações | 🇺🇸 Configuration
│   ├── crew/                    # 🇧🇷 Definição dos Agentes | 🇺🇸 Agent Definitions
│   ├── security/                # 🇧🇷 Segurança | 🇺🇸 Security
│   ├── tools/                   # 🇧🇷 Ferramentas | 🇺🇸 Tools
│   └── utils/                   # 🇧🇷 Utilitários | 🇺🇸 Utilities
├── docs/                        # 🇧🇷 Documentação | 🇺🇸 Documentation
├── outputs/                     # 🇧🇷 Relatórios gerados | 🇺🇸 Generated reports
├── tests/                       # 🇧🇷 Testes | 🇺🇸 Test suite
└── pyproject.toml               # 🇧🇷 Dependências | 🇺🇸 Dependencies
```

## 🧪 Testes | Testing

**🇧🇷 Português:**
```bash
# Executar todos os testes
uv run pytest tests/ -v

# Com cobertura
uv run pytest --cov=src tests/
```

**🇺🇸 English:**
```bash
# Run all tests
uv run pytest tests/ -v

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
- [docs/README.md](docs/README.md) - Índice da documentação
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - Arquitetura do sistema
- [CONTRIBUTING.md](CONTRIBUTING.md) - Diretrizes de contribuição

**🇺🇸 English:**
- [docs/README.md](docs/README.md) - Documentation index
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - System architecture
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

## 💰 Gerenciamento de Custos API | API Cost Management

**🇧🇷 Português:**

O sistema inclui rastreamento de custos integrado:
- Limite padrão: $5 USD por execução
- Máximo de 100 chamadas de API por execução
- Limitação de taxa: 60 chamadas/minuto

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
