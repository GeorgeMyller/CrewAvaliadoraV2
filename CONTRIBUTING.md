# 🤝 Contribuindo para o CrewAvaliadora | Contributing to CrewAvaliadora

## 🇧🇷 Português

Obrigado pelo seu interesse em contribuir para o CrewAvaliadora! Este documento fornece diretrizes e instruções para contribuição.

## 🇺🇸 English

Thank you for your interest in contributing to CrewAvaliadora! This document provides guidelines and instructions for contributing.

---

## 🎯 Código de Conduta | Code of Conduct

**🇧🇷 Português:**
- Seja respeitoso e inclusivo
- Foque em feedback construtivo
- Ajude outros a aprender e crescer
- Siga os padrões de codificação do projeto

**🇺🇸 English:**
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the project's coding standards

## 🚀 Começando | Getting Started

### 🇧🇷 Pré-requisitos | 🇺🇸 Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Git
- Uma chave API do Gemini | A Gemini API key

### 🇧🇷 Configurar Ambiente de Desenvolvimento | 🇺🇸 Setup Development Environment

```bash
# 🇧🇷 Clonar o repositório | 🇺🇸 Clone the repository
git clone <repository-url>
cd CrewAvaliadora

# 🇧🇷 Instalar dependências | 🇺🇸 Install dependencies
uv sync --dev

# 🇧🇷 Copiar e configurar ambiente | 🇺🇸 Copy and configure environment
cp .env.example .env
# 🇧🇷 Edite .env e adicione sua GEMINI_API_KEY
# 🇺🇸 Edit .env and add your GEMINI_API_KEY

# 🇧🇷 Instalar hooks pre-commit | 🇺🇸 Install pre-commit hooks
uv run pre-commit install

# 🇧🇷 Executar testes para verificar instalação | 🇺🇸 Run tests to verify setup
uv run pytest tests/ -v
```

## 📝 Fluxo de Desenvolvimento | Development Workflow

### 🇧🇷 1. Criar um Branch | 🇺🇸 1. Create a Branch

```bash
git checkout -b feature/nome-da-sua-funcionalidade
# 🇧🇷 ou | 🇺🇸 or
git checkout -b fix/numero-issue-descricao
```

### 🇧🇷 2. Fazer Alterações | 🇺🇸 2. Make Changes

**🇧🇷 Português:**
- Escreva código limpo e legível
- Siga as diretrizes de estilo PEP 8
- Adicione docstrings a funções e classes
- Atualize testes conforme necessário
- Atualize documentação se alterar funcionalidade

**🇺🇸 English:**
- Write clean, readable code
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Update tests as needed
- Update documentation if changing functionality

### 🇧🇷 3. Executar Testes | 🇺🇸 3. Run Tests

```bash
# 🇧🇷 Executar todos os testes | 🇺🇸 Run all tests
uv run pytest tests/ -v

# 🇧🇷 Executar arquivo de teste específico | 🇺🇸 Run specific test file
uv run pytest tests/test_basic.py -v
```

### 🇧🇷 4. Lint e Formatação | 🇺🇸 4. Lint and Format

```bash
# 🇧🇷 Formatar código | 🇺🇸 Format code
uv run ruff format .

# 🇧🇷 Verificar linting | 🇺🇸 Check linting
uv run ruff check .

# 🇧🇷 Verificação de tipos | 🇺🇸 Type checking
uv run mypy . --ignore-missing-imports
```

### 🇧🇷 5. Commit das Alterações | 🇺🇸 5. Commit Changes

```bash
git add .
git commit -m "feat: adicionar nova funcionalidade"
# 🇧🇷 ou | 🇺🇸 or
git commit -m "fix: resolver issue #123"
```

**🇧🇷 Use mensagens de commit convencionais:**

**🇺🇸 Use conventional commit messages:**

- `feat:` - 🇧🇷 para novas funcionalidades | 🇺🇸 for new features
- `fix:` - 🇧🇷 para correções de bugs | 🇺🇸 for bug fixes
- `docs:` - 🇧🇷 para alterações em documentação | 🇺🇸 for documentation changes
- `test:` - 🇧🇷 para adições/alterações de testes | 🇺🇸 for test additions/changes
- `refactor:` - 🇧🇷 para refatoração de código | 🇺🇸 for code refactoring
- `chore:` - 🇧🇷 para tarefas de manutenção | 🇺🇸 for maintenance tasks

### 🇧🇷 6. Push e Criar Pull Request | 🇺🇸 6. Push and Create Pull Request

```bash
git push origin feature/nome-da-sua-funcionalidade
```

**🇧🇷 Então crie um Pull Request no GitHub com:**

**🇺🇸 Then create a Pull Request on GitHub with:**

- 🇧🇷 Descrição clara das alterações | 🇺🇸 Clear description of changes
- 🇧🇷 Referência a issues relacionadas | 🇺🇸 Reference to related issues
- 🇧🇷 Screenshots se houver alterações de UI | 🇺🇸 Screenshots if UI changes
- 🇧🇷 Resultados dos testes | 🇺🇸 Test results

## 🧪 Diretrizes de Teste | Testing Guidelines

### 🇧🇷 Escrevendo Testes | 🇺🇸 Writing Tests

**🇧🇷 Português:**
- Coloque testes no diretório `tests/`
- Nomeie arquivos de teste `test_*.py`
- Nomeie funções de teste `test_*`
- Use nomes de teste descritivos
- Teste casos de sucesso e falha
- Faça mock de chamadas de API externas

**🇺🇸 English:**
- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names
- Test both success and failure cases
- Mock external API calls

## 📚 Documentação | Documentation

### 🇧🇷 Documentação de Código | 🇺🇸 Code Documentation

**🇧🇷 Português:**
- Adicione docstrings a todas as funções e classes públicas
- Use docstrings no estilo Google
- Inclua type hints

**🇺🇸 English:**
- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Include type hints

## 🏗️ Diretrizes de Arquitetura | Architecture Guidelines

### 🇧🇷 Estrutura do Projeto | 🇺🇸 Project Structure

```
CrewAvaliadora/
├── src/                # 🇧🇷 Código fonte principal | 🇺🇸 Main source code
├── config/             # 🇧🇷 Arquivos de configuração | 🇺🇸 Configuration files
├── tests/              # 🇧🇷 Suite de testes | 🇺🇸 Test suite
├── utils/              # 🇧🇷 Módulos utilitários | 🇺🇸 Utility modules
├── templates/          # 🇧🇷 Templates de relatório | 🇺🇸 Report templates
├── outputs/            # 🇧🇷 Relatórios gerados | 🇺🇸 Generated reports
└── docs/               # 🇧🇷 Documentação | 🇺🇸 Documentation
```

### 🇧🇷 Organização de Código | 🇺🇸 Code Organization

**🇧🇷 Português:**
- Mantenha funções pequenas e focadas
- Use nomes de variáveis significativos
- Separe preocupações (análise, relatórios, chamadas API)
- Evite duplicação
- Use type hints

**🇺🇸 English:**
- Keep functions small and focused
- Use meaningful variable names
- Separate concerns (analysis, reporting, API calls)
- Avoid duplication
- Use type hints

## 🐛 Reportando Issues | Reporting Issues

**🇧🇷 Ao reportar issues, inclua:**
- Versão do Python
- Sistema operacional
- Passos para reproduzir
- Comportamento esperado vs real
- Logs relevantes

**🇺🇸 When reporting issues, include:**
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs

---

**🇧🇷 Obrigado por contribuir para o CrewAvaliadora! 🚀**

**🇺🇸 Thank you for contributing to CrewAvaliadora! 🚀**
