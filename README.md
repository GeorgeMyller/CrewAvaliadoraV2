# CrewAvaliadora

AI-powered codebase analysis system using 6 specialized agents powered by Google Gemini 2.5 Flash and CrewAI framework.

## 🎯 Overview

CrewAvaliadora is a comprehensive codebase analysis tool that uses artificial intelligence to provide professional-grade code reviews, architecture analysis, quality assessments, and business viability reports.

### Key Features

- **6 Specialized AI Agents**: Software Architect, QA Engineer, Technical Writer, Product Manager, Legal Specialist, and AI Engineer
- **Comprehensive Analysis**: Architecture, code quality, documentation, business viability, legal compliance, and AI optimization
- **Cost-Controlled**: Built-in API cost tracking and rate limiting
- **Production-Ready**: Complete test suite, CI/CD pipeline, and professional tooling
- **Flexible Output**: Generates detailed markdown reports with actionable insights

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- uv package manager
- Google Gemini API key

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd CrewAvaliadora

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### Get API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a free API key
3. Add to `.env` file

### Verify System Health

```bash
# Run health check to verify everything is configured correctly
uv run python utils/health_check.py

# This will check:
# - Python version
# - Required packages
# - Environment variables
# - Project structure
# - Gemini API connection
```

### Run Analysis

```bash
# Analyze current directory (limited to 3 files for testing)
uv run python crew_avaliacao_completa.py

# Generate basic report
uv run python gerar_relatorio.py .
```

## 📊 Generated Reports

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

## 🏗️ Project Structure

```
CrewAvaliadora/
├── tests/                      # Test suite
├── utils/                      # Utility modules
│   ├── api_cost_tracker.py    # API cost tracking & rate limiting
│   └── codebase_analyzer.py   # Consolidated analysis utilities
├── outputs/                    # Generated reports (gitignored)
│   ├── reports/               # Analysis reports
│   └── metadata/              # API usage metrics
├── crew_avaliadora/           # CrewAI project structure
├── crewai_system/             # System documentation
├── avaliacao_gemini.py        # Gemini integration
├── crew_avaliacao_completa.py # Main analysis system
├── gerar_relatorio.py         # Report generator
└── .env.example               # Environment template
```

## 🧪 Testing

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_basic.py -v
```

## 🛠️ Development

### Setup Development Environment

```bash
# Install dev dependencies
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install

# Run linting
uv run ruff check .
uv run ruff format .

# Run type checking
uv run mypy . --ignore-missing-imports
```

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 Documentation

- [README_CREW.md](README_CREW.md) - Detailed CrewAI system documentation
- [crewai_system/README.md](crewai_system/README.md) - System architecture
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Implementation status

## 💰 API Cost Management

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

## 🔒 Security

- API keys stored in environment variables (never in code)
- Pre-commit hooks scan for secrets
- Bandit security scanning in CI/CD
- Input validation and sanitization

## 📈 CI/CD Pipeline

Automated testing on every push:
- Unit tests with pytest
- Code linting with ruff
- Type checking with mypy
- Security scanning with bandit
- Coverage reporting

## 🤝 The 6 AI Agents

1. **🏗️ Software Architect** - Architecture patterns, scalability, integrations
2. **🧪 QA Engineer** - Test coverage, code quality, vulnerabilities
3. **📄 Technical Writer** - Documentation quality, onboarding guides
4. **🚀 Product Manager** - Market readiness, business viability, monetization
5. **⚖️ Legal Specialist** - LGPD/GDPR compliance, API terms, risk mitigation
6. **🤖 AI Engineer** - LLM optimization, prompt engineering, cost efficiency

## 📊 Example Output

```markdown
# Executive Summary
Overall Quality Score: 78/100

**Strengths:**
- Well-documented API integration
- Modular agent architecture
- Good error handling

**Critical Issues:**
1. Missing test coverage (Priority: HIGH)
2. No rate limiting (Priority: HIGH)
...
```

## 🔧 Configuration

Key environment variables:

```bash
# Required
GEMINI_API_KEY=your_api_key_here

# Optional
MODEL=gemini/gemini-2.5-flash
MAX_FILES_TO_ANALYZE=300
MAX_FILE_SIZE_BYTES=2097152
OUTPUT_DIR=outputs/reports
LOG_LEVEL=INFO
```

## 📦 Dependencies

Core:
- `crewai>=0.157.0` - Multi-agent framework
- `google-generativeai>=0.8.5` - Gemini API
- `python-dotenv>=1.1.1` - Environment management

Dev:
- `pytest>=7.4.0` - Testing framework
- `ruff>=0.1.9` - Linting and formatting
- `mypy>=1.7.0` - Type checking
- `pre-commit>=3.5.0` - Git hooks

## 🐛 Troubleshooting

**API Key Error:**
```bash
# Verify key is set
echo $GEMINI_API_KEY

# Or check .env file
cat .env
```

**Import Errors:**
```bash
# Reinstall dependencies
uv sync --reinstall
```

**Permission Issues:**
```bash
# Ensure output directories exist
mkdir -p outputs/reports outputs/metadata
```

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Built with:
- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent orchestration
- [Google Gemini](https://ai.google.dev/) - Large language model
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

---

**Developed with ❤️ using CrewAI + Google Gemini 2.5 Flash**
