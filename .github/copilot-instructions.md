# CrewAvaliadora - Copilot Instructions for AI Coding Agents

## 🎯 Project Overview

**CrewAvaliadora** is a production-grade multi-agent AI system that analyzes codebases using 6 specialized agents powered by Google Gemini 2.5 Flash and the CrewAI framework. The system generates professional-grade analysis reports across architecture, quality, documentation, business viability, legal compliance, and AI optimization dimensions.

### Core Architecture Pattern
- **YAML-driven configuration**: Agents and tasks defined in `config/crew_config.yaml` (not hardcoded)
- **Modular agent design**: 6 independent specialized agents orchestrated sequentially via CrewAI
- **Template-based reporting**: Output rendered through `templates/template_relatorio_final_v2.md`
- **Cost-controlled execution**: Built-in API tracking in `utils/api_cost_tracker.py` with $5 USD default limit

## 📁 Critical File Organization

```
CrewAvaliadora/
├── src/crew_avaliadora.py           # Main system (YAML config → agents → Crew orchestration)
├── config/crew_config.yaml          # Single source of truth for agents/tasks configuration
├── utils/
│   ├── config_loader.py             # YAML parsing + validation
│   ├── health_check.py              # Diagnostic utilities
│   └── template_engine.py           # Report rendering engine
├── templates/template_relatorio_final_v2.md  # Jinja2-based report template
├── outputs/
│   ├── reports/                     # Final analysis reports (md)
│   ├── analysis/                    # Raw analysis data
│   ├── logs/                        # Execution logs with timestamps
│   └── metadata/                    # API usage metrics (JSON)
├── tests/test_basic.py              # Basic structure tests (gap: needs functional tests)
└── legacy/                          # Archived old code (do NOT modify)
```

## 🔑 Key Architectural Patterns & Decisions

### 1. Configuration-Driven Architecture
**Pattern**: All agent definitions (roles, goals, tasks) live in `config/crew_config.yaml`, not hardcoded in Python.

**When modifying agents**:
- Never hardcode agent definitions in `crew_avaliadora.py`
- Always update `config/crew_config.yaml` first, then regenerate agents via `_create_agents_from_config()`
- Each agent has: `name`, `emoji`, `role`, `goal`, `backstory`, `max_iterations`, `delegation`

**Example**:
```yaml
agents:
  arquiteto_software:
    name: "ArquitetoSoftwareSenior"
    emoji: "🏗️"
    role: "Arquiteto de Software Sênior"
    goal: "Analisar profundamente a arquitetura..."
    backstory: "Arquiteto com 10+ anos..."
    max_iterations: 3
    delegation: false
```

### 2. Sequential Crew Process (Not Hierarchical)
**Pattern**: Agents execute sequentially via `Process.sequential`, with each task feeding output to next agent.

**Why**: Ensures clear dependency chain for agent reasoning. Last agent (typically Software Architect) consolidates all findings.

**When extending**: 
- Order matters: Place analysis agents before consolidation agents
- Current order: Architect → QA → Writer → PM → Legal → AI Engineer
- Add new agents in logical sequence, don't expect parallel execution

### 3. YAML Task Definitions with Expected Output
**Pattern**: Each task has clear `description` and `expected_output` fields that guide agent behavior.

**Critical convention**:
```yaml
tasks:
  task_name:
    agent: "agent_key"
    name: "Human-readable name"
    description: "Multi-line detailed instructions for the agent"
    expected_output: "Structured format of expected deliverable"
```

**When creating tasks**: Be explicit about output format in `expected_output` (structure, sections, tone)

### 4. Cost Control & Rate Limiting
**Pattern**: Every API call tracked via environment variables and checked before execution.

**Configuration** (in `.env`):
```bash
MAX_API_CALLS_PER_RUN=100
MAX_COST_PER_RUN_USD=5.00
GEMINI_API_KEY=your_key_here
MODEL=gemini/gemini-2.5-flash  # Always use flash for cost efficiency
```

**When debugging cost issues**:
- Check `outputs/metadata/` for JSON logs of API calls
- Reduce `max_iterations` in agent config (default: 3) to reduce calls
- Switch to `gemini-2.5-flash` if using heavier model
- Never remove cost tracking - it's essential for production use

### 5. Template Engine for Report Generation
**Pattern**: Final reports rendered via Jinja2 template in `utils/template_engine.py`.

**Template location**: `templates/template_relatorio_final_v2.md`

**When modifying reports**:
- Edit template, not the crew output directly
- Template receives context dict with keys like `project_name`, `timestamp`, `analysis_output`
- Always preserve template structure when customizing sections

## 🚀 Development Workflows

### Running Analysis (Complete Flow)
```bash
# Health check first (verifies config + API key)
uv run python utils/health_check.py

# Analyze current directory
# 1. Generates base report: gerar_relatorio.py .
# 2. Runs CrewAI analysis: python src/crew_avaliadora.py
# Full flow: uv run python src/analyze_repo.py
```

### Adding a New Specialized Agent

1. **Define in YAML** (`config/crew_config.yaml`):
```yaml
agents:
  security_specialist:
    name: "SecuritySpecialist"
    emoji: "🔐"
    role: "Security Specialist"
    goal: "Identify vulnerabilities and security risks"
    backstory: "Senior security architect..."
    max_iterations: 3
```

2. **Add corresponding task**:
```yaml
tasks:
  security_audit:
    agent: "security_specialist"
    name: "Security Audit"
    description: "Analyze codebase for security vulnerabilities..."
    expected_output: "List of vulnerabilities with severity levels"
```

3. **No Python changes needed** - system auto-discovers via `_create_agents_from_config()`

### Modifying Agent Behavior

- **Temperature control**: Currently 0.3 (conservative). Higher = more creative
- **Max iterations**: Controls agentic loops (currently 3). More = higher cost
- **Backstory quality**: Critical - detailed backstories lead to better analysis
- **Goal clarity**: Be specific about what agent should accomplish

## 🧪 Testing & Quality Standards

### Current Test Coverage (Gap Alert!)
Only 4 basic structure tests exist in `tests/test_basic.py`:
- `test_project_structure()` - directory existence
- `test_config_files()` - config file presence
- `test_main_scripts()` - script existence
- `test_imports()` - module imports

**When adding features**: Add functional tests following this pattern:
```python
def test_config_loader():
    """Test YAML config loading and validation"""
    from utils.config_loader import load_config
    config = load_config()
    assert config.get_crew_name() == "AvaliacaoCodebaseStartupProfissional"
    assert len(config.get_all_agents()) == 6
```

### Linting & Formatting Standards
```bash
# All Python files must pass:
uv run ruff check .        # Code quality rules
uv run ruff format .       # Auto-formatting (100 line length)
uv run mypy . --ignore-missing-imports  # Type hints
```

**Project settings** (from `pyproject.toml`):
- Line length: 100
- Target: Python 3.12+
- Quote style: double
- Disabled: E501 (long lines - handled by formatter)

## 🔌 Integration Points & External Dependencies

### Google Gemini API Integration
**How it works**:
1. API key from `.env` → `os.environ["GEMINI_API_KEY"]`
2. CrewAI automatically uses configured model: `gemini/gemini-2.5-flash`
3. Requests batched and rate-limited to 60 calls/minute

**When troubleshooting API failures**:
- Verify key in `.env`: `echo $GEMINI_API_KEY`
- Check rate limits: see `outputs/metadata/` for call logs
- Use health_check: `uv run python utils/health_check.py`

### CrewAI Framework
**Version**: 0.157.0+  
**Key classes used**: `Agent`, `Task`, `Crew`, `Process`

**Important patterns**:
- Always use `Process.sequential` (not hierarchical) for current workflow
- Agent delegation disabled (`delegation: false`) - each agent works independently
- Task outputs feed into next task automatically

### Python Dotenv
**Used for**: Loading `GEMINI_API_KEY` and other config from `.env`  
**Pattern**: `load_dotenv()` called once at startup in `crew_avaliadora.py`

## 📐 Project-Specific Conventions

### 1. Emoji-Driven UI
- Agents have emojis (🏗️ Architect, 🔬 QA, 📚 Writer, 🎯 PM, ⚖️ Legal, 🧠 AI)
- Output formatting uses emoji prefixes (✅ ✖️ ⚠️ 📊 etc.)
- **When logging/printing**: Use this convention for consistency

### 2. Portuguese + English Mixing
- **Code comments**: Often in Portuguese (project original language)
- **Config**: Portuguese agent names and descriptions
- **Output**: English for professional reports
- **When contributing**: Use English for new code comments, respect existing Portuguese

### 3. Output Organization with Timestamps
```
outputs/
├── reports/relatorio_final_Continuador_20251101_181650.md
├── logs/crew_execution_20251101_181650.log
├── metadata/crew_execution_20251101_181650.json
└── analysis/...
```

**Convention**: All outputs use `YYYYMMDD_HHMMSS` timestamps for traceability

### 4. Logging Best Practices
- Use standard `logging` module (not print statements)
- Log level: `INFO` for progress, `DEBUG` for details, `ERROR` for failures
- Always include context (file sizes, counts, validation results)
- Example: `logger.info(f"✅ Config carregada: {self.config.get_crew_name()}")`

## ⚠️ Common Pitfalls & How to Avoid

### Pitfall 1: Hardcoding Agent Configuration
**Wrong**: Adding agent directly in Python
```python
# ❌ DON'T DO THIS
agent = Agent(role="Custom Role", goal="...", backstory="...")
```

**Right**: Add to `config/crew_config.yaml`, let system load it
```python
# ✅ DO THIS
agents = self._create_agents_from_config()
```

### Pitfall 2: Forgetting Cost Limits
**Risk**: Uncontrolled API spending  
**Prevention**: Always check `.env` has `MAX_COST_PER_RUN_USD=5.00`

### Pitfall 3: Using Stronger Model for Prototyping
**Risk**: 10x cost increase  
**Correct**: Always use `gemini/gemini-2.5-flash` unless explicitly testing

### Pitfall 4: Modifying Legacy Code
**Risk**: Breaking backward compatibility  
**Prevention**: Legacy code in `src/legacy/` is archived - don't change it. Create new files if needed.

### Pitfall 5: Missing Template Context
**Risk**: Blank sections in final report  
**Prevention**: Check `context` dict passed to `template_engine.render(context)` has all required keys

## 🎯 Common Tasks for AI Agents

### Task: Add a New Analysis Agent
1. Update `config/crew_config.yaml` - add agent definition + task
2. No Python changes needed
3. Run health check to validate config: `uv run python utils/health_check.py`
4. Test: `uv run python src/crew_avaliadora.py`

### Task: Fix Report Generation
1. Check template in `templates/template_relatorio_final_v2.md`
2. Verify context keys in `_save_report()` method
3. Test template rendering: Check output file created with content
4. Review logs in `outputs/logs/` for errors

### Task: Improve Performance
1. Reduce `max_iterations` in agent config (from 3 to 2)
2. Use `gemini-2.5-flash` (already configured)
3. Implement caching for repeated analyses
4. Profile with health_check: `uv run python utils/health_check.py`

### Task: Debug Failed Analysis
1. Check `.env` has valid `GEMINI_API_KEY`
2. Run health check: `uv run python utils/health_check.py`
3. Check logs: `tail -f outputs/logs/crew_execution_*.log`
4. Check metadata: `cat outputs/metadata/crew_execution_*.json`
5. Verify config syntax in `config/crew_config.yaml` (YAML must be valid)

## 📚 Reference Files for Key Patterns

| Pattern | File(s) | Key Classes/Functions |
|---------|---------|----------------------|
| Agent configuration | `config/crew_config.yaml` | N/A (YAML) |
| Crew orchestration | `src/crew_avaliadora.py` | `CodebaseAnalysisCrewV2` class |
| Config loading | `utils/config_loader.py` | `ConfigLoader`, `load_config()` |
| Report generation | `utils/template_engine.py` | `TemplateEngine` class |
| Health diagnostics | `utils/health_check.py` | Various check functions |
| Project structure | `pyproject.toml` | Dependencies, settings |

## 🚀 Before Starting Work

**Always run**:
```bash
# 1. Verify system health
uv run python utils/health_check.py

# 2. Check config syntax
python -c "from utils.config_loader import load_config; load_config()"

# 3. Run existing tests
uv run pytest tests/ -v
```

This ensures your environment is ready and catches configuration issues early.
