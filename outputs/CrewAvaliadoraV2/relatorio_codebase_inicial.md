# 📊 Relatório Técnico da Codebase
**Gerado em:** 2025-12-04 18:34:45
**Diretório analisado:** `/var/folders/g1/7nfb0bns5zbftz_zqwwbbyjw0000gn/T/crew_analysis_CrewAvaliadoraV2_lluwyuvk`
**Total de arquivos:** 122
**Tamanho total:** 1.36 MB

## 📈 Distribuição por Extensão

- **.py**: 61 arquivos (527.16 KB)
- **.md**: 32 arquivos (490.35 KB)
- **.yaml**: 8 arquivos (52.53 KB)
- **no_extension**: 6 arquivos (955.00 B)
- **.toml**: 3 arquivos (3.47 KB)
- **.sh**: 3 arquivos (3.83 KB)
- **.example**: 2 arquivos (2.92 KB)
- **.txt**: 2 arquivos (124.00 B)
- **.png**: 2 arquivos (296.98 KB)
- **.json**: 1 arquivos (2.00 KB)
- **.ini**: 1 arquivos (100.00 B)
- **.yml**: 1 arquivos (9.37 KB)

## 📁 Estrutura de Diretórios

- `src/legacy/crewai_system_old/core/instagram`: 31 arquivos (638.92 KB)
- `src/legacy/crewai_system_old/scripts`: 10 arquivos (66.46 KB)
- `root`: 9 arquivos (41.09 KB)
- `src`: 5 arquivos (42.74 KB)
- `outputs/htmltopdf-batch-mac`: 4 arquivos (67.99 KB)
- `src/legacy`: 4 arquivos (54.45 KB)
- `src/legacy/crewai_system_old`: 4 arquivos (16.50 KB)
- `utils`: 3 arquivos (16.64 KB)
- `src/legacy/crew_avaliadora_old`: 3 arquivos (3.09 KB)
- `src/legacy/crew_avaliadora_old/src/latest_ai_development`: 3 arquivos (4.19 KB)
- `src/legacy/latest_ai_development`: 3 arquivos (3.09 KB)
- `src/legacy/latest_ai_development/src/latest_ai_development`: 3 arquivos (4.15 KB)
- `tests`: 2 arquivos (3.00 KB)
- `docs`: 2 arquivos (14.31 KB)
- `outputs/agenteinstagram`: 2 arquivos (65.08 KB)
- `outputs/AprenderEscrita`: 2 arquivos (29.12 KB)
- `outputs/groups_evo_crewai-escolher-envio-para-grupo-ou-para-meu-numero`: 2 arquivos (63.10 KB)
- `outputs/CrewAvaliadoraV2`: 2 arquivos (83.81 KB)
- `outputs/Continuador`: 2 arquivos (49.33 KB)
- `src/security`: 2 arquivos (1.93 KB)
- `src/legacy/crew_avaliadora_old/src/latest_ai_development/tools`: 2 arquivos (631.00 B)
- `src/legacy/crew_avaliadora_old/src/latest_ai_development/config`: 2 arquivos (10.41 KB)
- `src/legacy/latest_ai_development/src/latest_ai_development/tools`: 2 arquivos (631.00 B)
- `src/legacy/latest_ai_development/src/latest_ai_development/config`: 2 arquivos (1.40 KB)
- `src/legacy/crewai_system_old/config`: 2 arquivos (13.97 KB)
- `src/legacy/crewai_system_old/docs`: 2 arquivos (19.13 KB)
- `config`: 1 arquivos (16.86 KB)
- `scripts`: 1 arquivos (463.00 B)
- `.github`: 1 arquivos (12.28 KB)
- `.github/workflows`: 1 arquivos (9.37 KB)

## 📖 README / Descrição do Projeto

### Conteúdo de README.md

```
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

... (truncado após 200 linhas)

```


## 💻 Código Principal

### pyproject.toml

```
[project]
name = "crewavaliadora"
version = "0.1.0"
description = "AI-powered codebase analysis system using CrewAI and Google Gemini"
readme = "README.md"
requires-python = ">=3.12"
authors = [
    {name = "CrewAvaliadora Team"}
]
keywords = ["crewai", "gemini", "code-analysis", "ai", "llm"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Quality Assurance",
]
dependencies = [
    "crewai[google-genai]>=0.157.0",
    "crewai-tools>=0.60.0",
    "google-generativeai>=0.8.5",
    "guardrails-ai>=0.5.0",
    "h2>=4.3.0",
    "litellm>=1.37.14",
    "pypdf>=6.4.0",
    "python-dotenv>=1.1.1",
    "pyyaml>=6.0.2",
    "ruff>=0.14.3",
    "safety>=3.7.0",
    "starlette>=0.50.0",
    "streamlit",
    "urllib3>=2.5.0",
    "watchdog>=6.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-mock>=3.12.0",
    "ruff>=0.1.9",
    "mypy>=1.7.0",
    "bandit>=1.7.5",
    "pre-commit>=3.5.0",
    "types-PyYAML>=6.0.12.12",
]

[tool.ruff]
line-length = 100
target-version = "py312"
exclude = ["src/legacy"]

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = [
    "E501", # line too long (handled by formatter)
    "B008", # do not perform function calls in argument defaults
    "C901", # too complex
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
ignore_missing_imports = true
explicit_package_bases = true
exclude = ["src/legacy"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v"

[tool.bandit]
exclude_dirs = ["tests", ".venv", "venv"]
skips = ["B101"]  # Skip assert warnings in tests

[tool.coverage.run]
omit = [
    "tests/*",
    ".venv/*",
    "venv/*",
    "*/__pycache__/*",
]

[[tool.uv.index]]

... (truncado após 100 linhas)

```


## 📄 Arquivos de Código Detalhados

*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*

### src/legacy/crew_avaliacao_completa.py (37.36 KB)

```python
#!/usr/bin/env python3
"""
🚀 CrewAI Avaliação Completa de Codebase
========================================

Sistema plug-and-play para análise profissional de codebase usando Gemini 2.5 Flash.
Gera relatórios ultra-profissionais para devs juniores e seniores.

Fluxo: Codebase → Script Python → Relatório → CrewAI → Relatório Ultra-Profissional
"""

from crewai import Agent, Crew, Process, Task

try:
    import crewai_tools

    HAVE_CREWAI_TOOLS = True
except Exception:
    crewai_tools = None
    HAVE_CREWAI_TOOLS = False
import json
import logging
import os
import re
from datetime import datetime

from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()


class CodebaseAnalysisCrew:
    """
    🤝 CrewAI para Avaliação Completa de Codebase

    Roles especializados:
    📐 Arquiteto de Software
    🧪 Engenheiro de Qualidade
    📄 Documentador Técnico
    🚀 Product Manager
    ⚖️ Especialista Legal
    🤖 Engenheiro de IA
    """

    def __init__(self, gemini_api_key: str | None = None, project_name: str | None = None):
        """Inicializa a crew com configuração Gemini 2.5 Flash"""
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError(
                "❌ GEMINI_API_KEY não encontrada! Configure no .env ou passe como parâmetro"
            )

        # Remove espaços em branco da API key se houver
        self.gemini_api_key = self.gemini_api_key.strip()

        logger.info(f"✅ GEMINI_API_KEY carregada: {self.gemini_api_key[:10]}...")

        # Set environment variables for CrewAI's built-in LLM handling
        # Following the pattern from latest_ai_development example
        os.environ["GEMINI_API_KEY"] = self.gemini_api_key
        if "MODEL" not in os.environ:
            os.environ["MODEL"] = "gemini/gemini-2.5-flash"

        # CrewAI will automatically handle LLM instantiation from env vars
        # No need for manual LLM() instantiation
        self.llm = None

        # Setup output directory structure
        self.project_name = project_name or "unknown_project"
        self.output_base_dir = self._setup_output_directory()

        # Tools para leitura de arquivos (só instanciaremos ferramentas reais se disponíveis)
        if HAVE_CREWAI_TOOLS and crewai_tools is not None:
            try:
                self.file_tool = crewai_tools.FileReadTool()

... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/image_validator.py (28.70 KB)

```python
"""
Este módulo fornece a classe InstagramImageValidator para validação e processamento de imagens conforme os requisitos oficiais do Instagram.
Funcionalidades principais:
- Validação de imagens para diferentes tipos de postagens (feed, stories, reels, carrossel), incluindo checagem de dimensões, proporção, formato e tamanho do arquivo.
- Normalização automática de imagens para carrossel, garantindo proporções consistentes e dimensões adequadas.
- Redimensionamento e otimização de imagens para atender aos limites da plataforma.
- Correção inteligente do aspect ratio baseada no tipo de conteúdo.
- Processamento completo de fotos individuais, simulando o fluxo de publicação via API do Instagram.
- Métodos utilitários para validação detalhada e recomendações de ajustes conforme as regras da API oficial.
Requisitos:
- Pillow (PIL) para manipulação de imagens.
- Logging para registro de operações e erros.
Uso recomendado para automação de publicações, validação prévia de conteúdo e integração com fluxos de mídia social.


"""

import logging
import os
import time

from PIL import Image

logger = logging.getLogger(__name__)


class InstagramImageValidator:
    """
    Validates images for Instagram posting requirements.
    Performs checks required by Instagram's API for various post types.
    """

    # Instagram API requirements atualizados com base na documentação oficial
    MIN_IMG_SIZE = 320  # Minimum size in pixels (each dimension)
    MAX_IMG_SIZE = 1440  # Maximum size in pixels (each dimension)
    CAROUSEL_RATIO_TOLERANCE = 0.02  # 2% tolerance for aspect ratio consistency

    # Instagram supported aspect ratios - REQUISITOS OFICIAIS
    # Feed Posts: 1.91:1 (landscape) até 4:5 (portrait)
    MIN_ASPECT_RATIO = 0.8  # 4:5 portrait orientation (1080x1350)
    MAX_ASPECT_RATIO = 1.91  # Landscape orientation (1080x566)
    SQUARE_RATIO = 1.0  # 1:1 square (1080x1080) - SEMPRE ACEITO

    # Stories e Reels: 9:16 (720x1280 mínimo)
    STORIES_RATIO = 9 / 16  # 0.5625 para stories/reels
    STORIES_MIN_WIDTH = 720
    STORIES_MIN_HEIGHT = 1280

    @classmethod
    def validate_for_carousel(cls, image_paths, auto_normalize=False):
        """
        Validates that all images meet Instagram's carousel requirements.

        Args:
            image_paths (list): List of paths to images to be included in carousel
            auto_normalize (bool): If True, automatically normalize images

        Returns:
            tuple: If auto_normalize is False: (is_valid, message)
                  If auto_normalize is True: (is_valid, message, normalized_paths)
        """
        if not image_paths or len(image_paths) < 2:
            return (
                (False, "Carrossel precisa de pelo menos 2 imagens")
                if not auto_normalize
                else (False, "Carrossel precisa de pelo menos 2 imagens", [])
            )

        if len(image_paths) > 10:  # Instagram maximum
            return (
                (False, "Máximo de 10 imagens permitidas no carrossel")
                if not auto_normalize
                else (False, "Máximo de 10 imagens permitidas no carrossel", [])
            )

        # If auto_normalize is enabled, normalize images before validation
        if auto_normalize:
            normalized_paths = cls.normalize_for_carousel(image_paths)
            if normalized_paths:
                validation_result, message = cls.validate_for_carousel(

... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/instagram_video_processor.py (26.83 KB)

```python
"""
Módulo para processamento e otimização de vídeos para Instagram.

Este módulo fornece classes e funções para analisar, validar, otimizar e adaptar vídeos conforme as especificações do Instagram, incluindo tipos de post como "reels" e "carousel". Utiliza MoviePy e ffmpeg para manipulação de vídeo, além de ffprobe para extração avançada de metadados.

Principais funcionalidades:
- Análise de metadados de vídeo (duração, resolução, codecs, proporção, tamanho).
- Validação de vídeos conforme requisitos do Instagram.
- Otimização automática de vídeos (corte, redimensionamento, ajuste de proporção, codecs).
- Otimização forçada via ffmpeg para casos de incompatibilidade.
- Limpeza de arquivos temporários gerados durante o processamento.

Classes:
- VideoProcessor: Métodos estáticos para análise, validação e otimização de vídeos.
- InstagramVideoProcessor: Classe orientada a objeto para processamento completo de vídeos conforme especificações do Instagram.

Dependências:
- moviepy
- Pillow
- ffmpeg/ffprobe (opcional para otimização avançada)
- logging
- pathlib
- json
- datetime
- tempfile
- os

Uso recomendado:
Utilize as funções de validação antes de postar vídeos no Instagram para garantir conformidade com os requisitos da plataforma. Use os métodos de otimização para adaptar vídeos automaticamente quando necessário.

"""

import json
import logging
import os
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

import moviepy.editor as mp
from moviepy.editor import VideoFileClip
from PIL import Image
from src.agent_social_media.utils.media.paths import Paths

# Defina um diretório temporário para o moviepy usar (opcional, mas recomendado)
# change_settings({"TEMP_DIR": "/caminho/para/seu/diretorio/temporario"}) # Linux/macOS
# change_settings({"TEMP_DIR": "C:\\caminho\\para\\seu\\diretorio\\temporario"}) # Windows

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Apply patch for Pillow 10+ compatibility
def _apply_pillow_patch():
    """Apply compatibility patch for Pillow 10+ with MoviePy"""
    if not hasattr(Image, "ANTIALIAS"):
        if hasattr(Image, "LANCZOS"):
            Image.ANTIALIAS = Image.LANCZOS
        elif hasattr(Image.Resampling) and hasattr(Image.Resampling, "LANCZOS"):
            Image.ANTIALIAS = Image.Resampling.LANCZOS


# Apply the patch immediately
_apply_pillow_patch()


class VideoProcessor:
    @staticmethod
    def get_video_info(video_path: str) -> dict[str, Any]:
        """
        Get video information using moviepy instead of ffprobe.

        Args:
            video_path: Path to the video file

        Returns:
            Dictionary with video metadata

... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/instagram_carousel_service.py (26.15 KB)

```python
"""
Serviço para gerenciamento de upload e publicação de carrosséis no Instagram.

Este módulo fornece a classe `InstagramCarouselService`, que permite validar mídias,
criar containers de carrossel, verificar o status do processamento, publicar carrosséis
e gerenciar limites de taxa (rate limits) e permissões do token de acesso.

Principais funcionalidades:
- Validação de URLs de mídia e tipos suportados (JPEG, PNG) com tratamento de erros e backoff.
- Criação de containers filhos para cada imagem do carrossel.
- Criação do container principal do carrossel, incluindo legenda e associação dos filhos.
- Verificação do status do container até que esteja pronto para publicação.
- Publicação do carrossel no Instagram, com tratamento de erros e limites de taxa.
- Fluxo completo para postar carrosséis, incluindo tentativas automáticas em caso de falha.
- Verificação e atualização das permissões do token de acesso.
- Gerenciamento de limites de taxa com backoff exponencial e jitter.

Exceções customizadas:
- `CarouselCreationError`: Erros durante a criação do carrossel.

Classes auxiliares:
- `RateLimitState`: Gerencia o estado de limites de taxa e backoff.

Requisitos:
- O token de acesso deve possuir permissões "instagram_basic" e "instagram_content_publishing".
- URLs de mídia devem ser acessíveis, do tipo suportado e com tamanho máximo de 8MB.
- O número de mídias para carrossel deve estar entre 2 e 10.

Uso recomendado para automação de postagens de carrosséis em contas do Instagram via API.

"""

import logging
import os
import random
import time
from datetime import datetime

from dotenv import load_dotenv
from src.agent_social_media.core.instagram.base_instagram_service import (
    AuthenticationError,
    BaseInstagramService,
    InstagramAPIError,
    PermissionError,
    RateLimitError,
)

logger = logging.getLogger("InstagramCarouselService")


class CarouselCreationError(Exception):
    """Raised when there are issues creating a carousel"""

    def __init__(self, message, error_code=None, error_subcode=None, fb_trace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fb_trace_id = fb_trace_id
        super().__init__(message)


class RateLimitState:
    """Track rate limit state"""

    def __init__(self):
        self.last_error_time = 0
        self.error_count = 0
        self.backoff_until = 0
        self.min_delay = 60  # Start with 1 minute
        self.max_delay = 3600  # Max 1 hour delay

    def should_backoff(self) -> bool:
        """Check if we should still be backing off"""
        return time.time() < self.backoff_until

    def get_backoff_time(self) -> float:
        """Get how many seconds to wait"""
        if self.should_backoff():
            return self.backoff_until - time.time()
        return 0


... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/base_instagram_service.py (22.30 KB)

```python
"""

    BaseInstagramService fornece uma base robusta para interação com a Instagram Graph API, incluindo tratamento avançado de erros, controle de limite de requisições (rate limiting) e verificação de permissões.
Classes:
    - AuthenticationError: Erro de autenticação (ex: token inválido/expirado).
    - PermissionError: Erro quando o app não possui permissões necessárias.
    - RateLimitError: Erro quando o limite de requisições da API é excedido.
    - MediaError: Erro relacionado a problemas com mídia.
    - TemporaryServerError: Erro temporário do servidor.
    - InstagramAPIError: Exceção base para outros erros da API do Instagram.
    - RateLimitHandler: Classe utilitária para detectar erros de limite e calcular backoff exponencial com jitter.
BaseInstagramService:
    - API_VERSION: Versão da Instagram Graph API utilizada.
    - base_url: URL base para requisições.
    - min_request_interval: Intervalo mínimo entre requisições para evitar limites.
Métodos:
    - __init__(access_token, ig_user_id): Inicializa o serviço com token de acesso e ID do usuário Instagram, configurando sessão HTTP com retries.
    - _make_request(method, endpoint, params=None, data=None, headers=None, retry_attempt=0): Realiza requisição à API com tratamento de erros, controle de limite e tentativas automáticas.
    - _process_rate_limit_headers(headers): Processa informações de limite de uso dos headers da resposta.
    - _get_retry_after(error): Extrai tempo recomendado para nova tentativa a partir do erro.
    - check_token_permissions(): Verifica se o token possui permissões necessárias do Instagram.
    - get_app_usage_info(): Obtém informações atuais de uso do app e limites.
Uso:
    Herde de BaseInstagramService para implementar funcionalidades específicas da API do Instagram, aproveitando o tratamento de erros e controle de limite já implementados.


"""

import json
import logging
import random
import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("InstagramAPI")


class AuthenticationError(Exception):
    """Raised when there are issues with authentication"""

    def __init__(self, message, error_code=None, error_subcode=None, fbtrace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)


class PermissionError(Exception):
    """Raised when the app lacks necessary permissions"""

    def __init__(self, message, error_code=None, error_subcode=None, fbtrace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)


class RateLimitError(Exception):
    """Raised when rate limits are hit"""

    def __init__(
        self,
        message,
        retry_seconds=300,
        error_code=None,
        error_subcode=None,
        fbtrace_id=None,
    ):
        self.retry_seconds = retry_seconds
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)



... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/scripts/crew_avaliacao_completa.py (20.87 KB)

```python
#!/usr/bin/env python3
"""
🚀 CrewAI Avaliação Completa de Codebase
========================================

Sistema plug-and-play para análise profissional de codebase usando Gemini 2.5 Flash.
Gera relatórios ultra-profissionais para devs juniores e seniores.

Fluxo: Codebase → Script Python → Relatório → CrewAI → Relatório Ultra-Profissional
"""

import json
import logging
import os
from datetime import datetime

from crewai import LLM, Agent, Crew, Process, Task
from crewai_tools import DirectoryReadTool, FileReadTool
from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()


class CodebaseAnalysisCrew:
    """
    🤝 CrewAI para Avaliação Completa de Codebase

    Roles especializados:
    📐 Arquiteto de Software
    🧪 Engenheiro de Qualidade
    📄 Documentador Técnico
    🚀 Product Manager
    ⚖️ Especialista Legal
    🤖 Engenheiro de IA
    """

    def __init__(self, gemini_api_key: str | None = None):
        """Inicializa a crew com configuração Gemini 2.5 Flash"""
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("❌ GEMINI_API_KEY não encontrada! Configure no .env")

        # Configuração otimizada do Gemini 2.5 Flash
        self.llm = LLM(
            model="google/gemini-2.5-flash",
            api_key=self.gemini_api_key,
            temperature=0.3,  # Análise mais focada
            max_tokens=8192,  # Máximo para respostas detalhadas
        )

        # Tools para leitura de arquivos
        self.file_tool = FileReadTool()
        self.dir_tool = DirectoryReadTool()

        # Cria agentes especializados
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()

    def _create_agents(self) -> dict[str, Agent]:
        """🎭 Cria todos os agentes especializados"""

        agents = {
            # 📐 Arquiteto de Software
            "arquiteto": Agent(
                role="🏗️ Arquiteto de Software Sênior",
                goal="""Analisar profundamente a arquitetura da aplicação, identificando:
                - Padrões arquiteturais usados (MVC, Clean Architecture, etc.)
                - Qualidade das integrações com APIs externas
                - Escalabilidade e manutenibilidade do código
                - Pontos de falha e gargalos potenciais
                - Sugestões concretas de refatoração""",
                backstory="""Arquiteto de software com 10+ anos de experiência em sistemas distribuídos,
                APIs de redes sociais e automação. Especialista em Instagram Graph API v23, WhatsApp Business API
                e arquiteturas para SaaS. Conhece profundamente padrões como Repository, Factory, Observer e
                estratégias de rate limiting para APIs.""",

... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/filter.py (19.04 KB)

```python
"""
Módulo de processamento de imagens para uso em redes sociais (Instagram).
Este módulo fornece funcionalidades para:
- Validação de arquivos de imagem, verificando formato, dimensões e integridade.
- Tentativa de reparo de imagens corrompidas.
- Processamento de imagens, incluindo redimensionamento, aplicação de filtros do Instagram (via pilgram) e otimização para publicação.
- Limpeza de diretórios temporários, removendo arquivos antigos, corrompidos ou inválidos.
- Aplicação de bordas personalizadas em imagens, ajustando proporções e transparências.
Principais classes e métodos:
- FilterImage.validate_image: Valida se o arquivo é uma imagem suportada e íntegra.
- FilterImage.repair_image: Tenta reparar imagens corrompidas e salva uma versão recuperada.
- FilterImage.process: Processa a imagem, aplicando validação, reparo, filtro Instagram e otimização.
- FilterImage.clean_temp_directory: Remove arquivos temporários antigos ou inválidos de um diretório.
- FilterImage.apply_border: Aplica uma borda personalizada à imagem, ajustando proporções e transparências.
Dependências:
- Pillow (PIL)
- pilgram
- logging
Uso recomendado para automação de postagens e preparação de imagens para redes sociais.



"""

import logging
import os
import shutil
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import os

import pilgram
from PIL import Image, UnidentifiedImageError

logger = logging.getLogger(__name__)


class FilterImage:
    @staticmethod
    def validate_image(image_path):
        """
        Valida se o arquivo é uma imagem válida e pode ser processada.

        Args:
            image_path (str): Caminho para o arquivo de imagem

        Returns:
            bool: True se a imagem é válida, False caso contrário
        """
        try:
            # Verificar se o arquivo existe
            if not os.path.exists(image_path):
                logger.error(f"Erro: Arquivo não encontrado: {image_path}")
                return False

            # Verificar se o arquivo não está vazio
            if os.path.getsize(image_path) == 0:
                logger.error(f"Erro: Arquivo vazio: {image_path}")
                return False

            # Tentar abrir a imagem
            with Image.open(image_path) as img:
                # Verificar se é uma imagem válida tentando acessar suas propriedades
                img.verify()

            # Reabrir para uso (verify() fecha o arquivo)
            with Image.open(image_path) as img:
                # Verificar formato suportado
                if img.format not in ["JPEG", "PNG", "WEBP", "BMP"]:
                    logger.error(f"Erro: Formato não suportado: {img.format}")
                    return False

                # Verificar dimensões mínimas
                if img.size[0] < 10 or img.size[1] < 10:
                    logger.error(f"Erro: Imagem muito pequena: {img.size}")
                    return False


... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/instagram_post_service.py (18.93 KB)

```python
"""
Serviço para publicação de imagens no Instagram, com gerenciamento de containers de mídia, tratamento de limites de taxa (rate limit), persistência de estado e estatísticas de publicação.

Classes:
    InstagramPostService:
        Serviço para postar imagens no Instagram, utilizando containers de mídia e publicação via API.
        - Gerencia containers pendentes e tentativas automáticas de publicação em caso de rate limit.
        - Persiste estado de containers e estatísticas em arquivo local.
        - Fornece métodos para criar containers, verificar status, publicar mídia, obter permalink e consultar posts pendentes.

Principais métodos:
    __init__(access_token, ig_user_id):
        Inicializa o serviço, carrega estado persistido e processa containers pendentes.

    _load_state():
        Carrega o estado dos containers pendentes e estatísticas de publicação a partir de arquivo.

    _save_state():
        Persiste o estado atual dos containers pendentes e estatísticas em arquivo.

    _update_stats(success=False, rate_limited=False):
        Atualiza estatísticas de publicação (sucesso, falha, rate limit).

    _process_pending_containers():
        Processa containers pendentes, tentando publicar aqueles prontos e gerenciando tentativas em caso de rate limit.

    create_media_container(image_url, caption):
        Cria um container de mídia para publicação de imagem.

    check_container_status(container_id):
        Verifica o status do container de mídia.

    wait_for_container_status(container_id, max_attempts=30, delay=10):
        Aguarda o processamento do container até estar pronto para publicação, com backoff exponencial.

    publish_media(media_container_id):
        Publica o container de mídia no Instagram, tratando rate limit e persistindo containers pendentes.

    get_post_permalink(post_id):
        Obtém o permalink de um post publicado.

    post_image(image_url, caption):
        Fluxo completo para publicação de imagem: cria container, aguarda processamento, publica e retorna resultado.

    get_pending_posts():
        Retorna lista de containers pendentes, com informações sobre próximas tentativas e erros.
"""

import json
import logging
import os
import random
import time
from datetime import datetime

from src.agent_social_media.core.instagram.base_instagram_service import (
    BaseInstagramService,
    InstagramAPIError,
    RateLimitError,
)

logger = logging.getLogger("InstagramPostService")


class InstagramPostService(BaseInstagramService):
    """Service for posting images to Instagram."""

    def __init__(self, access_token: str, ig_user_id: str):
        if not access_token or not ig_user_id:
            raise ValueError(
                "As credenciais do Instagram (access_token, ig_user_id) são obrigatórias."
            )

        super().__init__(access_token, ig_user_id)
        self.state_file = "api_state.json"
        self.pending_containers = {}
        self.stats = {"successful_posts": 0, "failed_posts": 0, "rate_limited_posts": 0}
        self._load_state()

        # Attempt to process any pending containers from previous runs

... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/carousel_poster.py (17.99 KB)

```python
# src/instagram/carousel_poster.py

"""
Módulo para validação, upload e publicação de carrosséis de imagens no Instagram.

Este módulo fornece funções para:
- Validar imagens para uso em carrosséis do Instagram.
- Fazer upload das imagens para um serviço externo (ex: Imgur).
- Limpar imagens enviadas (exclusão).
- Publicar carrosséis no Instagram, incluindo tratamento de erros e tentativas automáticas.

Exceções personalizadas são definidas para facilitar o tratamento de erros comuns, como problemas de autenticação, permissões, limites de taxa, validação de imagens, erros de upload, criação e publicação de carrosséis, e erros de servidor.

Principais funções:
- validate_carousel_images: Valida uma lista de imagens para o carrossel.
- upload_carousel_images: Realiza o upload das imagens e retorna informações sobre o processo.
- cleanup_uploaded_images: Exclui imagens previamente enviadas.
- post_carousel_to_instagram: Publica um carrossel no Instagram utilizando URLs das imagens já enviadas, com lógica de tentativas e tratamento detalhado de erros.

Requisitos:
- As imagens devem estar nos formatos JPEG ou PNG.
- O carrossel deve conter entre 2 e 10 imagens.
- A legenda do carrossel será truncada para 2200 caracteres se exceder este limite.

Exceções:
- CarouselError: Base para todas as exceções relacionadas ao carrossel.
- AuthenticationError: Problemas de autenticação.
- PermissionError: Problemas de permissão.
- ThrottlingError: Limite de taxa atingido.
- ImageValidationError: Imagem inválida.
- ImageUploadError: Falha no upload da imagem.
- CarouselCreationError: Falha na criação do container do carrossel.
- CarouselPublishError: Falha na publicação do carrossel.
- ServerError: Erros de servidor do Instagram/Facebook.

Uso típico:
1. Validar imagens.
2. Fazer upload das imagens.
3. Publicar o carrossel no Instagram utilizando as URLs das imagens enviadas.
4. (Opcional) Limpar imagens enviadas do serviço externo.

"""

import logging
import mimetypes
import os
import time
from collections.abc import Callable

from dotenv import load_dotenv
from src.agent_social_media.core.instagram.image_uploader import (
    ImageUploader,
)  # Para upload das imagens
from src.agent_social_media.core.instagram.instagram_carousel_service import (
    InstagramCarouselService,
    RateLimitError,
)

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


# --- Exceções Personalizadas (Opcional, mas recomendado) ---
class CarouselError(Exception):
    """Base class for carousel-related errors."""

    def __init__(
        self,
        message,
        error_code=None,
        error_subcode=None,
        fb_trace_id=None,
        is_retriable=False,
    ):
        super().__init__(message)
        self.error_code = error_code
        self.error_subcode = error_subcode

... (truncado após 80 linhas)

```

### src/legacy/crewai_system_old/core/instagram/carousel_normalizer.py (17.50 KB)

```python
"""
Classe utilitária para normalização de imagens para carrosséis do Instagram.

O Instagram exige que todas as imagens de um carrossel tenham a mesma proporção (aspect ratio).
Esta classe fornece métodos para:

- Obter a proporção de uma imagem.
- Obter informações detalhadas de uma imagem (dimensões, formato, tamanho do arquivo, etc).
- Validar se uma imagem atende aos requisitos do Instagram (dimensões mínimas/máximas, proporção suportada, tamanho do arquivo).
- Encontrar a proporção mais comum entre um conjunto de imagens.
- Determinar a melhor proporção recomendada pelo Instagram para um conjunto de imagens.
- Redimensionar imagens para os limites máximos permitidos pelo Instagram.
- Normalizar uma imagem para uma proporção alvo, realizando crop e resize conforme necessário.
- Encontrar a melhor proporção alvo para normalizar um conjunto de imagens.
- Normalizar todas as imagens de um carrossel para a mesma proporção, garantindo compatibilidade com o Instagram.

Constantes de requisitos do Instagram:
- Proporções recomendadas: quadrada (1:1), retrato (4:5), paisagem (1.91:1).
- Faixa de proporção suportada: mínimo 0.8 (4:5), máximo 1.91 (1.91:1).
- Dimensões mínimas/máximas: 320x320px até 1440x1440px.
- Tamanho máximo do arquivo: 8MB.

Todos os métodos são estáticos e podem ser utilizados independentemente.

"""

import logging
import os
import tempfile
from typing import Optional

from PIL import Image, UnidentifiedImageError

logger = logging.getLogger("CarouselNormalizer")


class CarouselNormalizer:
    """
    Utility class to normalize images for Instagram carousels.
    Instagram requires all images in a carousel to have the same aspect ratio.
    """

    # Instagram recommended aspect ratios
    RECOMMENDED_RATIOS = {
        "square": 1.0,  # 1:1
        "portrait": 0.8,  # 4:5
        "landscape": 1.91,  # 1.91:1
    }

    # Instagram's supported aspect ratio range
    MIN_ASPECT_RATIO = 0.8  # 4:5 portrait (width/height)
    MAX_ASPECT_RATIO = 1.91  # 1.91:1 landscape

    # Instagram's size requirements
    MIN_WIDTH = 320
    MAX_WIDTH = 1440
    MIN_HEIGHT = 320
    MAX_HEIGHT = 1440

    # Maximum file size (in bytes)
    MAX_FILE_SIZE = 8 * 1024 * 1024  # 8MB

    @staticmethod
    def get_image_aspect_ratio(image_path: str) -> float:
        """Get the aspect ratio of an image (width/height)"""
        if not os.path.exists(image_path):
            logger.error(f"Image file not found: {image_path}")
            return 0

        try:
            with Image.open(image_path) as img:
                width, height = img.size
                return round(width / height, 3)
        except UnidentifiedImageError:
            logger.error(f"Could not identify image file: {image_path}")
            return 0
        except Exception as e:
            logger.error(f"Error getting aspect ratio for {image_path}: {str(e)}")
            return 0


... (truncado após 80 linhas)

```


## 📂 Lista Completa de Arquivos

- `src/legacy/crewai_system_old/core/instagram/moldura.png` (227.81 KB)
- `src/legacy/crewai_system_old/core/instagram/moldura2.png` (69.17 KB)
- `outputs/CrewAvaliadoraV2/relatorio_codebase_inicial.md` (46.76 KB)
- `outputs/agenteinstagram/relatorio_codebase_inicial.md` (43.40 KB)
- `outputs/groups_evo_crewai-escolher-envio-para-grupo-ou-para-meu-numero/relatorio_codebase_inicial.md` (39.82 KB)
- `src/legacy/crew_avaliacao_completa.py` (37.36 KB)
- `outputs/CrewAvaliadoraV2/relatorio_final_CrewAvaliadoraV2_20251204_104347.md` (37.05 KB)
- `outputs/Continuador/relatorio_codebase_inicial.md` (29.42 KB)
- `src/legacy/crewai_system_old/core/instagram/image_validator.py` (28.70 KB)
- `src/legacy/crewai_system_old/core/instagram/instagram_video_processor.py` (26.83 KB)
- `src/legacy/crewai_system_old/core/instagram/instagram_carousel_service.py` (26.15 KB)
- `outputs/groups_evo_crewai-escolher-envio-para-grupo-ou-para-meu-numero/relatorio_final_groups_evo_crewai-escolher-envio-para-grupo-ou-para-meu-numero_20251102_122900.md` (23.28 KB)
- `outputs/htmltopdf-batch-mac/relatorio_final_htmltopdf-batch-mac_20251122_150800.md` (22.80 KB)
- `src/legacy/crewai_system_old/core/instagram/base_instagram_service.py` (22.30 KB)
- `outputs/agenteinstagram/relatorio_final_agenteinstagram_20251102_143749.md` (21.67 KB)
- `outputs/AprenderEscrita/relatorio_final_AprenderEscrita_20251122_211931.md` (21.19 KB)
- `outputs/htmltopdf-batch-mac/relatorio_final_htmltopdf-batch-mac_20251122_150036.md` (21.12 KB)
- `src/legacy/crewai_system_old/scripts/crew_avaliacao_completa.py` (20.87 KB)
- `outputs/htmltopdf-batch-mac/relatorio_final_htmltopdf-batch-mac_20251122_150334.md` (20.29 KB)
- `outputs/Continuador/relatorio_final_Continuador_20251102_101535.md` (19.91 KB)
- `src/legacy/crewai_system_old/core/instagram/filter.py` (19.04 KB)
- `src/legacy/crewai_system_old/core/instagram/instagram_post_service.py` (18.93 KB)
- `src/legacy/crewai_system_old/core/instagram/carousel_poster.py` (17.99 KB)
- `src/legacy/crewai_system_old/core/instagram/carousel_normalizer.py` (17.50 KB)
- `config/crew_config.yaml` (16.86 KB)
- `src/legacy/crewai_system_old/core/instagram/advanced_crew_post_instagram.py` (16.04 KB)
- `src/crew_avaliadora.py` (15.71 KB)
- `src/legacy/crewai_system_old/templates/template_relatorio_final.md` (14.97 KB)
- `src/legacy/crewai_system_old/core/instagram/instagram_reels_publisher.py` (14.50 KB)
- `README.md` (13.08 KB)
- `src/legacy/crewai_system_old/core/instagram/discover_instagram_ids.py` (13.05 KB)
- `templates/template_relatorio_final_v2.md` (12.98 KB)
- `src/legacy/crewai_system_old/core/instagram/crew_post_instagram.py` (12.80 KB)
- `.github/copilot-instructions.md` (12.28 KB)
- `CONTRIBUTING.md` (11.66 KB)
- `src/streamlit_app.py` (11.33 KB)
- `README_CREW.md` (10.62 KB)
- `src/legacy/crewai_system_old/core/instagram/debug_carousel.py` (10.33 KB)
- `src/legacy/crewai_system_old/docs/README_CREW.md` (10.27 KB)
- `docs/ARCHITECTURE.md` (10.26 KB)
- `src/legacy/crewai_system_old/config/crew_config.yaml` (9.89 KB)
- `src/legacy/crewai_system_old/scripts/crew_config.yaml` (9.89 KB)
- `src/legacy/avaliacao_gemini.py` (9.82 KB)
- `src/legacy/crewai_system_old/scripts/crew_gemini_simples.py` (9.82 KB)
- `src/legacy/crewai_system_old/core/instagram/image_uploader.py` (9.41 KB)
- `.github/workflows/ci.yml` (9.37 KB)
- `src/legacy/crewai_system_old/core/instagram/border.py` (9.14 KB)
- `src/legacy/crewai_system_old/core/instagram/discover_instagram_accounts.py` (8.98 KB)
- `src/legacy/crewai_system_old/core/instagram/crew_factory.py` (8.86 KB)
- `src/legacy/crewai_system_old/docs/ENTREGA_FINAL_CREWAI.md` (8.85 KB)

---
*Relatório gerado automaticamente para análise CrewAI*

**IMPORTANTE:** Este relatório contém código real do projeto. A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.
