# 📊 Relatório Técnico da Codebase
**Gerado em:** 2025-11-02 12:28:58
**Diretório analisado:** `/var/folders/g1/7nfb0bns5zbftz_zqwwbbyjw0000gn/T/crew_analysis_groups_evo_crewai-escolher-envio-para-grupo-ou-para-meu-numero_5i_1id58`
**Total de arquivos:** 80
**Tamanho total:** 384.49 KB

## 📈 Distribuição por Extensão

- **.py**: 37 arquivos (255.25 KB)
- **.md**: 23 arquivos (104.73 KB)
- **no_extension**: 8 arquivos (6.60 KB)
- **.sh**: 4 arquivos (10.86 KB)
- **.conf**: 2 arquivos (1.24 KB)
- **.yml**: 2 arquivos (1.22 KB)
- **.toml**: 1 arquivos (844.00 B)
- **.example**: 1 arquivos (817.00 B)
- **.csv**: 1 arquivos (1.68 KB)
- **.ini**: 1 arquivos (1.30 KB)

## 📁 Estrutura de Diretórios

- `root`: 20 arquivos (25.12 KB)
- `docs/development/migration-reports`: 10 arquivos (45.84 KB)
- `src/whatsapp_manager/core`: 8 arquivos (67.68 KB)
- `tools`: 6 arquivos (22.36 KB)
- `src/whatsapp_manager/utils`: 5 arquivos (61.34 KB)
- `tests`: 4 arquivos (19.31 KB)
- `tests/integration`: 4 arquivos (16.12 KB)
- `src/whatsapp_manager/ui/pages`: 4 arquivos (53.86 KB)
- `tests/functional`: 3 arquivos (8.62 KB)
- `docs/architecture`: 3 arquivos (9.63 KB)
- `docs/deployment`: 2 arquivos (10.69 KB)
- `docs/api`: 2 arquivos (13.40 KB)
- `src/whatsapp_manager/ui`: 2 arquivos (9.16 KB)
- `src/whatsapp_manager/infrastructure/api`: 2 arquivos (9.30 KB)
- `tests/fixtures`: 1 arquivos (5.62 KB)
- `docs`: 1 arquivos (3.82 KB)
- `docs/guides`: 1 arquivos (2.62 KB)
- `src`: 1 arquivos (0.00 B)
- `src/whatsapp_manager`: 1 arquivos (0.00 B)

## 📖 README / Descrição do Projeto

### Conteúdo de README.md

```
# WhatsApp Group Manager and Summarizer 🚀

Sistema automatizado para gerenciamento e sumarização de grupos do WhatsApp usando Evolution API e CrewAI para análise inteligente de mensagens.

## 📋 Sobre o Projeto

Este projeto oferece uma solução completa para:
- **Gerenciamento de grupos** do WhatsApp via Evolution API
- **Sumarização inteligente** de mensagens usando CrewAI
- **Interface web** para configuração e monitoramento
- **Agendamento automático** de resumos
- **Exportação de dados** para análise

## Como Executar com Docker 🐳

Este projeto inclui suporte completo para execução via Docker e Docker Compose, facilitando a configuração e o deploy do ambiente Streamlit.

### Requisitos Específicos
- **Python 3.12** (a imagem base é `python:3.12.10-slim`)
- Todas as dependências são instaladas automaticamente via `pyproject.toml` durante o build da imagem Docker usando `uv`
- Docker e Docker Compose instalados

### Variáveis de Ambiente Obrigatórias
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```env
EVO_BASE_URL=<sua_base_url>
EVO_API_TOKEN=<seu_api_token>
EVO_INSTANCE_NAME=<seu_instance_name>
EVO_INSTANCE_TOKEN=<seu_instance_token>
```

### Como Executar com Docker Compose

1. **Construa e inicie o serviço:**
    ```sh
    docker compose up --build
    ```
    Isso irá:
    - Construir a imagem Docker com todas as dependências do projeto
    - Iniciar o serviço `app` executando Streamlit na porta padrão
    - Configurar volumes para persistência de dados

2. **Acesse a interface:**
    - O Streamlit estará disponível em [http://localhost:8501](http://localhost:8501)

### Configurações Especiais
- O serviço roda com suporte a cron para tarefas agendadas
- Volumes configurados para persistir dados entre reinicializações
- Timezone configurado para Europe/Lisbon
- Supervisord para gerenciar múltiplos processos
- Apenas a porta **8501** é exposta (padrão do Streamlit)

---

## Execução Local (sem Docker) 💻

### Requisitos
- Python 3.12.7 ou superior
- uv (recomendado) ou pip

### Instalação
```bash
# Clone o repositório
git clone <repository-url>
cd groups_evo_crewai-escolher-envio-para-grupo-ou-para-meu-numero

# Instale as dependências usando uv (recomendado)
uv pip install .

# Ou usando pip
pip install .

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

### Executar a Aplicação
```bash
# Interface Streamlit principal
uv run streamlit run src/whatsapp_manager/ui/main_app.py

# Ou use as tasks configuradas no VS Code
# Task: "Start Streamlit App"
```

## 🛠️ Funcionalidades Principais

- **Gerenciamento de Grupos**: Listar, filtrar e selecionar grupos do WhatsApp
- **Sumarização Inteligente**: Análise de mensagens usando CrewAI
- **Agendamento**: Configurar resumos automáticos por grupo
- **Interface Web**: Dashboard intuitivo para todas as operações
- **Exportação**: Dados dos grupos em formato CSV
- **Logs Detalhados**: Monitoramento completo das operações

## 📁 Estrutura do Projeto

```
src/whatsapp_manager/
├── core/           # Lógica principal do negócio
├── infrastructure/ # Integrações externas (APIs)
├── presentation/   # Camada de apresentação
├── shared/         # Utilitários compartilhados
├── ui/            # Interface Streamlit
└── utils/         # Utilitários gerais
```

## 🔧 Configuração Avançada

### Variáveis de Ambiente Opcionais
```env
# OpenAI para CrewAI (opcional)
OPENAI_API_KEY=<sua_chave_openai>

# Configurações de log
LOG_LEVEL=INFO
DEBUG=false

# Configurações específicas
WHATSAPP_NUMBER=<seu_numero_whatsapp>
```

## 📖 Documentação

Para documentação completa, consulte:
- [Documentação da API](docs/api/evolution-api.md)
- [Guia de Uso CLI](docs/guides/cli-usage.md)
- [Arquitetura do Sistema](docs/architecture/README.md)
- [Guia de Deploy](docs/deployment/README.md)

## 🤝 Contribuindo

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para guidelines de contribuição.

## 📄 Licença

Este projeto está licenciado sob [LICENSE](LICENSE).

---

## How to Run with Docker 🐳

This project provides full support for running via Docker and Docker Compose, making it easy to set up the Streamlit environment.

### Specific Requirements
- **Python 3.12** (the base image is `python:3.12.10-slim`)
- All dependencies are installed automatically from `pyproject.toml` during the Docker image build using `uv`
- Docker and Docker Compose installed

### Required Environment Variables
Create a `.env` file in the project root with the following variables:
```env
EVO_BASE_URL=<your_base_url>
EVO_API_TOKEN=<your_api_token>
EVO_INSTANCE_NAME=<your_instance_name>
EVO_INSTANCE_TOKEN=<your_instance_token>
```

### How to Run with Docker Compose
1. **Build and start the service:**
    ```sh
    docker compose up --build
    ```
    This will:
    - Build the Docker image with all project dependencies
    - Start the `app` service running Streamlit on the default port
    - Configure volumes for data persistence

2. **Access the interface:**
    - Streamlit will be available at [http://localhost:8501](http://localhost:8501)

### Special Configuration
- The service runs with cron support for scheduled tasks
- Volumes configured for data persistence between restarts
- Timezone set to Europe/Lisbon
- Supervisord for managing multiple processes
- Only **port 8501** is exposed (Streamlit default)

```


## 💻 Código Principal

### pyproject.toml

```
[project]
name = "groups-evo-crewai"
version = "0.1.0"
description = "WhatsApp Group Manager and Summarizer"
readme = "README.md"
requires-python = ">=3.12.7"
dependencies = [
    "crewai>=0.100.0",
    "crewai-tools>=0.32.1",
    "evolutionapi>=0.0.9",
    "streamlit>=1.41.1",
    "watchdog>=3.0.0",
    "pandas>=2.2.0",
    "python-dotenv>=1.0.0",
    "schedule>=1.2.0",
    "requests>=2.31.0",
    "python-dateutil>=2.8.2",
    "plotly>=6.0.1",
]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
# backend-path is not strictly necessary if setuptools is in default path

[tool.setuptools.packages.find]
where = ["src"]
include = ["whatsapp_manager*"]
# namespaces = false # Optional: default is true, which is fine for src-layout
# exclude = [] # Optional: if you had specific sub-packages to exclude

```


## 📄 Arquivos de Código Detalhados

*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*

### src/whatsapp_manager/utils/task_scheduler.py (31.66 KB)

```python
"""
Sistema de Agendamento de Tarefas Multiplataforma / Cross-platform Task Scheduling System

PT-BR:
Este módulo implementa um sistema de agendamento de tarefas que funciona em Windows, 
Linux e macOS. Fornece funcionalidades para criar, remover e listar tarefas agendadas,
adaptando-se automaticamente ao sistema operacional em uso.

EN:
This module implements a task scheduling system that works on Windows, Linux, and macOS.
Provides functionality to create, remove, and list scheduled tasks,
automatically adapting to the operating system in use.
"""

import os
import subprocess
import platform
from datetime import datetime

def is_running_in_docker():
    """
    PT-BR:
    Detecta se o código está rodando dentro de um contêiner Docker.
    
    Returns:
        bool: True se estiver rodando no Docker, False caso contrário

    EN:
    Detects if the code is running inside a Docker container.
    
    Returns:
        bool: True if running in Docker, False otherwise
    """
    # Log da verificação para facilitar debug
    log_dir = "/app/data" if os.path.exists("/app/data") else "/tmp"
    log_path = os.path.join(log_dir, "docker_detection.log")
    
    def log_detection(message, result):
        try:
            with open(log_path, "a") as log_file:
                log_file.write(f"[{datetime.now()}] {message}: {result}\n")
        except:
            pass  # Falhar silenciosamente se não conseguir logar
    
    # Primeiro teste: verifica ambiente Docker via variável de ambiente (mais confiável)
    docker_env = os.environ.get('DOCKER_ENV', '').lower() == 'true'
    log_detection("DOCKER_ENV environment variable", docker_env)
    if docker_env:
        return True
    
    # Segundo teste: verifica se existem arquivos típicos do Docker
    docker_indicators = [
        '/.dockerenv',
        '/proc/1/cgroup'
    ]
    
    for indicator in docker_indicators:
        if os.path.exists(indicator):
            if indicator == '/proc/1/cgroup':
                try:
                    with open(indicator, 'r') as f:
                        content = f.read()
                        docker_cgroup = 'docker' in content or 'containerd' in content
                        log_detection(f"Docker indicator {indicator}", docker_cgroup)
                        if docker_cgroup:
                            return True
                except Exception as e:
                    log_detection(f"Error reading {indicator}", str(e))
            else:
                log_detection(f"Docker indicator {indicator} exists", True)
                return True
    
    # Terceiro teste: verifica o nome do host
    try:
        with open('/etc/hostname', 'r') as f:
            hostname = f.read().strip()
            docker_hostname = hostname.startswith('container') or hostname.startswith('docker')
            log_detection(f"Hostname check ({hostname})", docker_hostname)
            if docker_hostname:
                return True

... (truncado após 80 linhas)

```

### src/whatsapp_manager/ui/pages/4_Dashboard.py (20.69 KB)

```python
import calendar
from datetime import datetime
from datetime import timedelta
import os
import re

# Third-party library imports
import pandas as pd
import plotly.express as px
import streamlit as st

# Set page configuration with customized theme
st.set_page_config(
    page_title='WhatsApp Summary Dashboard',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'About': "WhatsApp Group Summary Analytics Dashboard - Developed by Sandeco"
    }
)

# Add custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #075E54;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .chart-container {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display application header with WhatsApp-style green color
st.markdown('<h1 class="main-header">📊 WhatsApp Group Summary Analytics Dashboard</h1>', unsafe_allow_html=True)

# Define Project Root assuming this file is src/whatsapp_manager/ui/pages/4_Dashboard.py
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
LOG_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "log_summary.txt")

def parse_log_entries(log_content):
    """
    Parses the log content which may contain multiple entries per line.
    Splits each line into individual log entries and parses them.
    """
    log_entries = []
    
    # First, try to split multiple entries that might be on a single line
    # We know each entry starts with a timestamp pattern like [YYYY-MM-DD HH:MM:SS.ffffff]
    entry_pattern = r"(\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\].*?)(?=\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]|$)"
    
    for line in log_content.strip().split('\n'):
        if line.startswith('//'):  # Skip comment lines
            continue
            
        entries = re.findall(entry_pattern, line)

... (truncado após 80 linhas)

```

### src/whatsapp_manager/core/group_controller.py (19.16 KB)

```python
"""
Controlador de Grupos do WhatsApp / WhatsApp Groups Controller

PT-BR:
Esta classe gerencia grupos do WhatsApp, incluindo cache local, consultas à API Evolution
e configurações de resumos automáticos. Fornece funcionalidades para buscar, filtrar
e atualizar informações dos grupos.

EN:
This class manages WhatsApp groups, including local caching, Evolution API queries,
and automatic summary settings. Provides functionality to fetch, filter,
and update group information.
"""

import sys
import os
import json
from dotenv import load_dotenv
from datetime import datetime
from evolutionapi.client import EvolutionClient
from evolutionapi.exceptions import EvolutionAuthenticationError, EvolutionAPIError
from .group import Group
import pandas as pd
from .message_sandeco import MessageSandeco
from ..utils.task_scheduler import TaskScheduled, is_running_in_docker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class GroupController:
    def __init__(self):
        """
        PT-BR:
        Inicializa o controlador com configurações do ambiente e validações.
        Configura conexão com API Evolution e caminhos de arquivos locais.

        EN:
        Initializes the controller with environment settings and validations.
        Sets up Evolution API connection and local file paths.
        """
        # Environment setup / Configuração do ambiente
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(env_path, override=True)

        # API Configuration / Configuração da API
        self.base_url = os.getenv("EVO_BASE_URL", 'http://localhost:8081')
        self.api_token = os.getenv("EVO_API_TOKEN")
        self.instance_id = os.getenv("EVO_INSTANCE_NAME")
        self.instance_token = os.getenv("EVO_INSTANCE_TOKEN")

        # File paths / Caminhos dos arquivos
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        self.csv_file = os.path.join(project_root, "data", "group_summary.csv")
        self.cache_file = os.path.join(project_root, "data", "groups_cache.json")

        if not all([self.api_token, self.instance_id, self.instance_token]):
            raise ValueError("API_TOKEN, INSTANCE_NAME ou INSTANCE_TOKEN não configurados. / API_TOKEN, INSTANCE_NAME or INSTANCE_TOKEN not configured.")
        # Garantir non-null types para o type checker
        assert self.api_token is not None and self.instance_id is not None and self.instance_token is not None

        if is_running_in_docker():
            # Docker container -> host machine
            self.base_url = os.getenv("EVO_BASE_URL", 'http://host.docker.internal:8081')
        else:
            # Local machine
            self.base_url = os.getenv("EVO_BASE_URL", 'http://localhost:8081')

        print(f"Inicializando EvolutionClient com URL / Initializing EvolutionClient with URL: {self.base_url}")
        self.client = EvolutionClient(base_url=self.base_url, api_token=self.api_token)
        self.groups = []

    def _load_cache(self):
        """
        PT-BR:
        Carrega dados do cache local para otimizar requisições.
        Retorna None se o cache estiver inválido ou não existir.

        EN:
        Loads data from local cache to optimize requests.
        Returns None if cache is invalid or doesn't exist.
        """

... (truncado após 80 linhas)

```

### src/whatsapp_manager/ui/pages/3_English.py (17.05 KB)

```python
import os
import time as t # Standard library time aliased
from datetime import time # datetime.time
from datetime import date # datetime.date
from datetime import datetime # datetime.datetime

# Third-party library imports
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Local application/library imports
# Define Project Root assuming this file is in src/whatsapp_manager/ui/pages/
# Navigate four levels up to reach the project root.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# Add src to Python path for imports
import sys
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

# Import local modules
from whatsapp_manager.core.group_controller import GroupController
from whatsapp_manager.utils.groups_util import GroupUtils
from whatsapp_manager.utils.task_scheduler import TaskScheduled
from whatsapp_manager.core.send_sandeco import SendSandeco

# --- Light Theme CSS ---
# Define Project Root assuming this file is src/whatsapp_manager/ui/pages/3_English.py
# Navigate four levels up to reach the project root.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# Adjust sys.path if necessary for Streamlit's execution context
import sys
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

from whatsapp_manager.core.group_controller import GroupController
from whatsapp_manager.utils.groups_util import GroupUtils
from whatsapp_manager.utils.task_scheduler import TaskScheduled
from whatsapp_manager.core.send_sandeco import SendSandeco


# --- Light Theme CSS ---
st.set_page_config(page_title='WhatsApp Group Resumer - EN', layout='wide')

# This page is the English version of the app

# Load environment variables
env_path = os.path.join(PROJECT_ROOT, '.env')
# st.write(f"Loading .env from: {env_path}") # Optional: for debugging
load_dotenv(env_path, override=True)


st.markdown("""

""", unsafe_allow_html=True)

# Initialize core components
@st.cache_data(ttl=300)  # Cache for 5 minutes
def initialize_components():
    """Initialize GroupController with proper error handling and fallback modes."""
    try:
        # Initialize GroupController
        control = GroupController()
        
        # Simple status check by trying to fetch groups
        try:
            groups = control.fetch_groups()
            mode = "online"
            st.success("✅ **System initialized successfully**")
        except Exception as e:
            # Try to get groups from cache/local data
            try:
                groups = control.get_groups()  # Try to get cached groups
                mode = "offline" 
                st.warning("⚠️ **Offline mode active** - Using local data")
            except Exception:
                groups = []
                mode = "offline"

... (truncado após 80 linhas)

```

### src/whatsapp_manager/utils/task_scheduler_docker.py (16.29 KB)

```python
"""
Sistema de Agendamento de Tarefas para Docker / Docker Task Scheduling System

PT-BR:
Este módulo implementa um sistema simplificado de agendamento de tarefas 
específico para o ambiente Docker Linux. Funciona exclusivamente com cron.

EN:
This module implements a simplified task scheduling system 
specific for Docker Linux environment. Works exclusively with cron.
"""

import os
import subprocess
from datetime import datetime

class TaskScheduled:
    @staticmethod
    def validate_python_script(python_script_path):
        """
        PT-BR:
        Verifica se o script Python especificado existe no sistema.
        
        Parâmetros:
            python_script_path: Caminho do script a ser validado
            
        Raises:
            FileNotFoundError: Se o script não for encontrado

        EN:
        Validates if the specified Python script exists in the system.
        
        Parameters:
            python_script_path: Path to script to validate
            
        Raises:
            FileNotFoundError: If script is not found
        """
        if not os.path.exists(python_script_path):
            raise FileNotFoundError(f"Script Python não encontrado / Python script not found: '{python_script_path}'")

    @staticmethod
    def create_task(task_name, python_script_path, schedule_type='DAILY', date=None, time='22:00'):
        """
        PT-BR:
        Cria uma tarefa agendada no cron do Linux (Docker).
        
        Parâmetros:
            task_name: Nome da tarefa
            python_script_path: Caminho do script Python
            schedule_type: Tipo de agendamento ('DAILY' ou 'ONCE')
            date: Data para execução única (formato: YYYY-MM-DD)
            time: Horário de execução (formato: HH:MM)
            
        Raises:
            Exception: Para erros de agendamento

        EN:
        Creates a scheduled task in Linux cron (Docker).
        
        Parameters:
            task_name: Task name
            python_script_path: Python script path
            schedule_type: Schedule type ('DAILY' or 'ONCE')
            date: Date for one-time execution (format: YYYY-MM-DD)
            time: Execution time (format: HH:MM)
            
        Raises:
            Exception: For scheduling errors
        """
        TaskScheduled.validate_python_script(python_script_path)

        # No Docker, sempre usamos python3
        python_executable = "python3"
        
        # Log the scheduling attempt
        log_path = "/app/data/cron_scheduling.log"
        with open(log_path, "a") as log_file:
            log_file.write(f"[{datetime.now()}] Scheduling task: {task_name}\n")
        

... (truncado após 80 linhas)

```

### src/whatsapp_manager/ui/pages/2_Portuguese.py (16.11 KB)

```python
import os
import time as t # Standard library time aliased
from datetime import time # datetime.time
from datetime import date # datetime.date
from datetime import datetime # datetime.datetime

# Third-party library imports
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Local application/library imports
# Define Project Root assuming this file is in src/whatsapp_manager/ui/pages/
# Navigate four levels up to reach the project root.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# Add src to Python path for imports
import sys
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

# Import local modules
from whatsapp_manager.core.group_controller import GroupController
from whatsapp_manager.utils.groups_util import GroupUtils
from whatsapp_manager.utils.task_scheduler import TaskScheduled
from whatsapp_manager.core.send_sandeco import SendSandeco

# --- Light Theme CSS ---
# Define Project Root assuming this file is src/whatsapp_manager/ui/pages/2_Portuguese.py
# Navigate four levels up to reach the project root.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# Adjust sys.path if necessary for Streamlit's execution context,
# though direct imports from whatsapp_manager should work if src is in PYTHONPATH
# or if Streamlit runs from the project root and picks up src.
# For robustness, especially if running pages directly or in some deployments:
import sys
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

from whatsapp_manager.core.group_controller import GroupController
from whatsapp_manager.utils.groups_util import GroupUtils
from whatsapp_manager.utils.task_scheduler import TaskScheduled
from whatsapp_manager.core.send_sandeco import SendSandeco


# --- Light Theme CSS ---
st.set_page_config(page_title='WhatsApp Group Resumer - PT', layout='wide')

# This page is the Portuguese version of the app

# Load environment variables
env_path = os.path.join(PROJECT_ROOT, '.env')
# st.write(f"Carregando .env de: {env_path}") # Optional: for debugging
load_dotenv(env_path, override=True)


st.markdown("""
   
""", unsafe_allow_html=True)

# Initialize core components
@st.cache_data(ttl=300)  # Cache for 5 minutes
def initialize_components():
    """Initialize GroupController with proper error handling and fallback modes."""
    try:
        # Initialize GroupController
        control = GroupController()
        
        # Simple status check by trying to fetch groups
        try:
            groups = control.fetch_groups()
            mode = "online"
            st.success("✅ **Sistema inicializado com sucesso**")
        except Exception as e:
            # Try to get groups from cache/local data
            try:
                groups = control.get_groups()  # Try to get cached groups
                mode = "offline" 
                st.warning("⚠️ **Modo offline ativo** - Usando dados locais")

... (truncado após 80 linhas)

```

### src/whatsapp_manager/core/summary.py (12.69 KB)

```python
"""
Sistema de Geração e Envio de Resumos de Grupos / Group Message Summary Generation and Sending System

PT-BR:
Este módulo implementa a geração automática de resumos das mensagens dos grupos.
Processa as mensagens de um período específico e utiliza CrewAI para gerar
um resumo inteligente que é enviado de volta ao grupo.

EN:
This module implements automatic group message summary generation.
It processes messages from a specific time period and uses CrewAI to generate
an intelligent summary that is sent back to the group.
"""

import argparse
import os
import sys
import time
from datetime import datetime, timedelta # Keep as is, or split if strict one-per-line for all froms

# Define Project Root assuming this file is src/whatsapp_manager/core/summary.py
# Navigate three levels up to reach the project root from core.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Add src directory to Python path to enable absolute imports when running as script
import sys
src_path = os.path.join(PROJECT_ROOT, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Third-party library imports
from dotenv import load_dotenv

# Local application/library imports - try relative first, fallback to absolute
try:
    # This works when imported as a module
    from .group_controller import GroupController
    from .summary_crew import SummaryCrew
    from .send_sandeco import SendSandeco
except ImportError:
    # This works when executed as a script
    from whatsapp_manager.core.group_controller import GroupController
    from whatsapp_manager.core.summary_crew import SummaryCrew
    from whatsapp_manager.core.send_sandeco import SendSandeco

# Load environment variables / Carrega variáveis de ambiente
env_path = os.path.join(PROJECT_ROOT, '.env')
load_dotenv(env_path, override=True) # Added override=True for consistency

# Initialize logging system / Inicializa sistema de logging
try:
    from whatsapp_manager.utils.logger import get_logger, TaskExecutionMonitor
    logger = get_logger("summary_task", "DEBUG")
    task_monitor = TaskExecutionMonitor()
    task_monitor.log_environment_info()
except ImportError:
    # Fallback para print se o logger não estiver disponível
    logger = None
    task_monitor = None
    print("WARNING: Sistema de logging não disponível, usando print")

# Get WhatsApp number from environment / Obtém número do WhatsApp do ambiente
personal_number = os.getenv("WHATSAPP_NUMBER")
if personal_number:
    # Garante que o número está no formato correto
    personal_number = personal_number.strip()
    if not personal_number.endswith('@s.whatsapp'):
        personal_number = f"{personal_number}@s.whatsapp"

config_info = f"\nConfigurações carregadas:\nNúmero do WhatsApp: {personal_number}\nBase URL: {os.getenv('EVO_BASE_URL')}\nInstance Name: {os.getenv('EVO_INSTANCE_NAME')}"
if logger:
    logger.info(config_info)
else:
    print(config_info)

# Initialize SendSandeco / Inicializa SendSandeco
evo_send = SendSandeco()

# Command line argument initialization / Inicialização dos argumentos de linha de comando
parser = argparse.ArgumentParser(description="Group Summary Generator / Gerador de Resumos de Grupo")

... (truncado após 80 linhas)

```

### src/whatsapp_manager/core/message_sandeco.py (11.62 KB)

```python
import base64

"""
Processador de Mensagens do WhatsApp / WhatsApp Message Processor

PT-BR:
Esta classe processa e estrutura diferentes tipos de mensagens do WhatsApp (texto, áudio,
imagem e documentos), extraindo e organizando seus metadados e conteúdo.

EN:
This class processes and structures different types of WhatsApp messages (text, audio,
image, and documents), extracting and organizing their metadata and content.
"""

class MessageSandeco:
    # Message Types / Tipos de Mensagem
    TYPE_TEXT = "conversation"
    TYPE_AUDIO = "audioMessage"
    TYPE_IMAGE = "imageMessage"
    TYPE_DOCUMENT = "documentMessage"
    
    # Message Scopes / Escopos de Mensagem
    SCOPE_GROUP = "group"
    SCOPE_PRIVATE = "private"
    
    def __init__(self, raw_data):
        """
        PT-BR:
        Inicializa uma mensagem a partir dos dados brutos.
        
        Parâmetros:
            raw_data: Dados brutos da mensagem do WhatsApp

        EN:
        Initializes a message from raw data.
        
        Parameters:
            raw_data: Raw WhatsApp message data
        """
        if "data" not in raw_data:
            enveloped_data = {
                "event": None,
                "instance": None,
                "destination": None,
                "date_time": None,
                "server_url": None,
                "apikey": None,
                "data": raw_data
            }
        else:
            enveloped_data = raw_data
        
        self.data = enveloped_data
        self.extract_common_data()
        self.extract_specific_data()
    
    def extract_common_data(self):
        """
        PT-BR:
        Extrai metadados comuns da mensagem (remetente, timestamp, IDs, etc).
        Define os atributos básicos compartilhados por todos os tipos de mensagem.

        EN:
        Extracts common message metadata (sender, timestamp, IDs, etc).
        Sets basic attributes shared by all message types.
        """
        self.event = self.data.get("event")
        self.instance = self.data.get("instance")
        self.destination = self.data.get("destination")
        self.date_time = self.data.get("date_time")
        self.server_url = self.data.get("server_url")
        self.apikey = self.data.get("apikey")
        
        data = self.data.get("data", {})
        key = data.get("key", {})
        
        self.remote_jid = key.get("remoteJid")
        self.message_id = key.get("id")
        self.from_me = key.get("fromMe")
        self.push_name = data.get("pushName")

... (truncado após 80 linhas)

```

### src/whatsapp_manager/core/send_sandeco.py (10.03 KB)

```python
"""
Sistema de Envio de Mensagens WhatsApp / WhatsApp Message Sending System

PT-BR:
Este módulo implementa uma interface para envio de diferentes tipos de mensagens via WhatsApp
utilizando a API Evolution. Suporta envio de textos, PDFs, áudios, imagens, vídeos e documentos.
Fornece uma camada de abstração para facilitar a integração com a API.

EN:
This module implements an interface for sending different types of WhatsApp messages
using the Evolution API. Supports sending texts, PDFs, audio, images, videos and documents.
Provides an abstraction layer to facilitate API integration.
"""

import os
import time
import logging
from dotenv import load_dotenv
from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage, MediaMessage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SendSandeco:
    """
    PT-BR:
    Classe para gerenciamento de envio de mensagens WhatsApp.
    Utiliza credenciais do arquivo .env para autenticação com a API Evolution.
    
    EN:
    WhatsApp message sending management class.
    Uses credentials from .env file for Evolution API authentication.
    """
    
    def __init__(self) -> None:
        # Environment setup and client initialization / Configuração do ambiente e inicialização do cliente
        load_dotenv()
        self.evo_api_token = os.getenv("EVO_API_TOKEN")
        self.evo_instance_id = os.getenv("EVO_INSTANCE_NAME")
        self.evo_instance_token = os.getenv("EVO_INSTANCE_TOKEN")
        self.evo_base_url = os.getenv("EVO_BASE_URL")

        if not all([self.evo_api_token, self.evo_instance_id, self.evo_instance_token, self.evo_base_url]):
            raise EnvironmentError("Missing one or more required environment variables.")

        self.client = EvolutionClient(
            base_url=self.evo_base_url,
            api_token=self.evo_api_token
        )

    def _send_media(self, number, media_file, mediatype, mimetype, caption):
        if not os.path.exists(media_file):
            raise FileNotFoundError(f"Arquivo '{media_file}' não encontrado.")

        media_message = MediaMessage(
            number=number,
            mediatype=mediatype,
            mimetype=mimetype,
            caption=caption,
            fileName=os.path.basename(media_file),
            media=""
        )

        self.client.messages.send_media(
            self.evo_instance_id,
            media_message,
            self.evo_instance_token,
            media_file
        )

    def textMessage(self, number, msg, mentions=[]):
        """
        PT-BR:
        Envia uma mensagem de texto para o número especificado.
        
        Argumentos:
            number (str): Número do destinatário (formato: código do país + DDD + número, ex: 5511999999999)
            msg (str): Conteúdo da mensagem
            mentions (list): Lista de menções na mensagem

... (truncado após 80 linhas)

```

### src/whatsapp_manager/ui/main_app.py (9.16 KB)

```python
# Third-party library imports
import streamlit as st

st.set_page_config(page_title='WhatsApp Group Resumer', layout='wide')

# --- Light Theme CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

/* --- Light Professional Theme --- */

/* Base Styles */
body, .stApp {
    background-color: #FFFFFF; /* White Background */
    font-family: 'Inter', sans-serif;
    color: #1E1E1E; /* Dark Gray Text */
    font-size: 16px;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #1E1E1E; /* Dark Gray */
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 0.8em;
    line-height: 1.3;
}
h1.landing-title { /* Specific class for landing page title */
    font-size: 3.2em; /* Larger title */
    font-weight: 800;
    text-align: center;
    margin-bottom: 0.4em;
    color: #0D6EFD; /* Professional Blue */
}
p.landing-subtitle { /* Specific class for landing page subtitle */
    font-size: 1.35em;
    color: #555555; /* Medium Gray */
    text-align: center;
    margin-bottom: 3em;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
h2 { font-size: 1.8em; color: #0D6EFD; border-bottom: 2px solid #E0E0E0; padding-bottom: 0.3em; }
h3 { font-size: 1.4em; color: #333333; margin-bottom: 0.5em; }

/* Main Content Area */
.main > div { padding-top: 3rem; }
.block-container { max-width: 1100px; padding-left: 2rem; padding-right: 2rem; }

/* Feature Cards */
.feature-card {
    background-color: #FFFFFF; /* White Background */
    border-radius: 12px;
    padding: 30px 35px;
    margin-bottom: 25px;
    color: #1E1E1E;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); /* Softer shadow */
    border: 1px solid #E0E0E0; /* Light border */
    transition: box-shadow 0.3s ease, transform 0.3s ease;
    text-align: center;
    height: 100%; /* Make cards in a row equal height */
}
 .feature-card:hover {
    box-shadow: 0 6px 20px rgba(13, 110, 253, 0.15); /* Blue shadow on hover */
    transform: translateY(-5px);
 }
 .feature-card h3 {
     color: #0D6EFD; /* Blue Accent for feature titles */
     font-size: 1.6em;
     margin-bottom: 0.6em;
     border: none;
     padding-left: 0;
 }
 .feature-card p {
     color: #444444; /* Darker gray for feature description */

... (truncado após 80 linhas)

```


## 📂 Lista Completa de Arquivos

- `src/whatsapp_manager/utils/task_scheduler.py` (31.66 KB)
- `src/whatsapp_manager/ui/pages/4_Dashboard.py` (20.69 KB)
- `src/whatsapp_manager/core/group_controller.py` (19.16 KB)
- `src/whatsapp_manager/ui/pages/3_English.py` (17.05 KB)
- `src/whatsapp_manager/utils/task_scheduler_docker.py` (16.29 KB)
- `src/whatsapp_manager/ui/pages/2_Portuguese.py` (16.11 KB)
- `src/whatsapp_manager/core/summary.py` (12.69 KB)
- `src/whatsapp_manager/core/message_sandeco.py` (11.62 KB)
- `docs/api/evolution-api.md` (10.36 KB)
- `src/whatsapp_manager/core/send_sandeco.py` (10.03 KB)
- `src/whatsapp_manager/ui/main_app.py` (9.16 KB)
- `src/whatsapp_manager/infrastructure/api/evolution_client.py` (8.91 KB)
- `docs/development/migration-reports/ORGANIZED_STRUCTURE_FIXED.md` (7.47 KB)
- `docs/architecture/README.md` (7.35 KB)
- `src/whatsapp_manager/utils/logger.py` (6.94 KB)
- `tests/integration/test_api_connectivity.py` (6.83 KB)
- `tests/conftest.py` (6.80 KB)
- `src/whatsapp_manager/utils/groups_util.py` (6.46 KB)
- `docs/development/migration-reports/BRANCH_MAIN_VS_ORGANIZED_COMPARISON.md` (6.01 KB)
- `tools/delete_scheduled_tasks.py` (6.00 KB)
- `docs/deployment/README.md` (5.85 KB)
- `tests/README.md` (5.73 KB)
- `tests/fixtures/test_message_sandeco_conceptual.md` (5.62 KB)
- `tests/run_tests.sh` (5.47 KB)
- `README.md` (5.39 KB)
- `docs/development/migration-reports/STRUCTURE_COMPARISON.md` (5.22 KB)
- `src/whatsapp_manager/core/summary_crew.py` (5.17 KB)
- `docs/deployment/docker-debugging.md` (4.84 KB)
- `src/whatsapp_manager/core/summary_lite.py` (4.71 KB)
- `docs/development/migration-reports/FIXES_COMPLETED.md` (4.35 KB)
- `docs/development/migration-reports/DIAGNOSTIC_REPORT.md` (4.33 KB)
- `src/whatsapp_manager/core/group.py` (4.31 KB)
- `docs/development/migration-reports/DOCKER_SCHEDULER_FIX.md` (4.29 KB)
- `docs/development/migration-reports/COMPARISON_ANALYSIS.md` (4.25 KB)
- `tools/50_plus.py` (4.09 KB)
- `tests/functional/test_structure.py` (4.07 KB)
- `docs/development/migration-reports/CODEBASE_REORGANIZATION_PLAN.md` (3.84 KB)
- `docs/README.md` (3.82 KB)
- `docs/development/migration-reports/MIGRATION_PHASE1_COMPLETE.md` (3.79 KB)
- `tools/delete_all_resumo_tasks.py` (3.68 KB)
- `tests/integration/test_api_detailed.py` (3.66 KB)
- `tests/integration/test_alternative_urls.py` (3.19 KB)
- `tools/save_groups_to_csv.py` (3.13 KB)
- `docs/api/quick-reference.md` (3.04 KB)
- `tools/agendar_todos.py` (2.86 KB)
- `docs/guides/cli-usage.md` (2.62 KB)
- `tools/list_scheduled_tasks.py` (2.59 KB)
- `tests/integration/test_whatsapp_status.py` (2.44 KB)
- `tests/functional/test_imports_and_functionality.py` (2.43 KB)
- `docs/development/migration-reports/README.md` (2.30 KB)

---
*Relatório gerado automaticamente para análise CrewAI*

**IMPORTANTE:** Este relatório contém código real do projeto. A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.
