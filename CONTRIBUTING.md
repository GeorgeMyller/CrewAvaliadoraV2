# Contributing to CrewAvaliadora

Thank you for your interest in contributing to CrewAvaliadora! This document provides guidelines and instructions for contributing.

## 🎯 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the project's coding standards

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- uv package manager
- Git
- A Gemini API key

### Setup Development Environment

```bash
# Clone the repository
git clone <repository-url>
cd CrewAvaliadora

# Install dependencies
uv sync --all-extras --dev

# Copy and configure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run tests to verify setup
uv run pytest tests/ -v
```

## 📝 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 2. Make Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Update tests as needed
- Update documentation if changing functionality

### 3. Run Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_basic.py -v
```

### 4. Lint and Format

```bash
# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Type checking
uv run mypy . --ignore-missing-imports
```

### 5. Commit Changes

```bash
git add .
git commit -m "feat: add new feature"
# or
git commit -m "fix: resolve issue #123"
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Reference to related issues
- Screenshots if UI changes
- Test results

## 🧪 Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names
- Test both success and failure cases
- Mock external API calls

Example:
```python
def test_setup_gemini_with_api_key():
    """Test that setup_gemini configures correctly with valid API key."""
    with patch.dict(os.environ, {"GEMINI_API_KEY": "test_key_123"}):
        model = setup_gemini()
        assert model is not None
```

### Running Tests

```bash
# All tests
uv run pytest

# With verbose output
uv run pytest -v

# Specific test
uv run pytest tests/test_basic.py::test_project_structure

# Skip slow tests
uv run pytest -m "not slow"
```

## 📚 Documentation

### Code Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Include type hints

Example:
```python
def analyze_file(file_path: Path, max_chars: int = 6000) -> str:
    """
    Analyze a single file using Gemini API.
    
    Args:
        file_path: Path to the file to analyze
        max_chars: Maximum characters to read from file
        
    Returns:
        Analysis text from Gemini
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is too large
    """
    pass
```

### README Updates

Update relevant README files when:
- Adding new features
- Changing configuration options
- Modifying installation steps
- Adding dependencies

## 🏗️ Architecture Guidelines

### Project Structure

```
CrewAvaliadora/
├── tests/              # Test suite
├── utils/              # Utility modules
├── outputs/            # Generated reports (gitignored)
├── crew_avaliadora/    # CrewAI project
└── crewai_system/      # System documentation
```

### Code Organization

- Keep functions small and focused
- Use meaningful variable names
- Separate concerns (analysis, reporting, API calls)
- Avoid duplication
- Use type hints

### Error Handling

- Use specific exception types
- Provide helpful error messages
- Log errors appropriately
- Clean up resources in finally blocks

Example:
```python
try:
    result = api_call()
except APIError as e:
    logger.error(f"API call failed: {e}")
    raise
except Exception as e:
    logger.exception("Unexpected error")
    raise
finally:
    cleanup_resources()
```

## 🔒 Security

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate all user inputs
- Sanitize file paths
- Review dependencies for vulnerabilities

## 📊 Performance

- Respect API rate limits
- Track API costs
- Cache results when appropriate
- Use async operations for I/O
- Profile before optimizing

## 🐛 Reporting Issues

When reporting issues, include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces
- Relevant logs

## 💡 Feature Requests

For feature requests:
- Describe the problem you're trying to solve
- Explain your proposed solution
- Discuss alternatives considered
- Note any breaking changes

## 📞 Getting Help

- Check existing documentation
- Search closed issues
- Ask in discussions
- Tag maintainers if urgent

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

Thank you for contributing to CrewAvaliadora! 🚀
