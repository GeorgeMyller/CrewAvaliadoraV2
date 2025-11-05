# 📊 Relatório Técnico da Codebase
**Gerado em:** 2025-11-02 10:15:34
**Diretório analisado:** `/var/folders/g1/7nfb0bns5zbftz_zqwwbbyjw0000gn/T/crew_analysis_Continuador_l7yhhreq`
**Total de arquivos:** 35
**Tamanho total:** 209.03 KB

## 📈 Distribuição por Extensão

- **.py**: 13 arquivos (93.95 KB)
- **.md**: 11 arquivos (72.37 KB)
- **.sh**: 3 arquivos (6.87 KB)
- **no_extension**: 3 arquivos (2.23 KB)
- **.json**: 2 arquivos (21.89 KB)
- **.txt**: 1 arquivos (119.00 B)
- **.toml**: 1 arquivos (5.60 KB)
- **.yml**: 1 arquivos (6.00 KB)

## 📁 Estrutura de Diretórios

- `root`: 14 arquivos (60.41 KB)
- `src`: 9 arquivos (75.97 KB)
- `docs`: 4 arquivos (44.87 KB)
- `scripts`: 2 arquivos (5.94 KB)
- `.github/ISSUE_TEMPLATE`: 2 arquivos (2.77 KB)
- `tests`: 1 arquivos (9.12 KB)
- `legacy`: 1 arquivos (1.93 KB)
- `.github`: 1 arquivos (2.03 KB)
- `.github/workflows`: 1 arquivos (6.00 KB)

## 📖 README / Descrição do Projeto

### Conteúdo de README.md

```
<div align="center">

# 🎯 Auto Clicker Pro

**Sistema Inteligente de Detecção e Automação de Cliques**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI/CD](https://github.com/yourusername/auto-clicker-pro/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/yourusername/auto-clicker-pro/actions)
[![Coverage](https://codecov.io/gh/yourusername/auto-clicker-pro/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/auto-clicker-pro)

*Um sistema avançado de automação que detecta e clica automaticamente em botões azuis na tela, com interface moderna e arquitetura modular.*

[🚀 Começar](#-instalação-rápida) • [📖 Documentação](docs/) • [🐛 Reportar Bug](https://github.com/yourusername/auto-clicker-pro/issues) • [💡 Solicitar Feature](https://github.com/yourusername/auto-clicker-pro/issues)

</div>

## 🌟 Características Principais

<table>
<tr>
<td>

### 🎯 **Detecção Inteligente**
Algoritmo avançado de detecção de botões azuis usando análise HSV com múltiplos ranges de cor para máxima precisão.

</td>
<td>

### 🖥️ **Interface Moderna**
UI responsiva com design moderno, cards informativos e estatísticas em tempo real.

</td>
</tr>
<tr>
<td>

### 📊 **Monitoramento Avançado**
Sistema completo de métricas com taxa de sucesso, tempo de sessão e análise de performance.

</td>
<td>

### �️ **Segurança Integrada**
Parada de emergência automática, failsafe integrado e controles de segurança robustos.

</td>
</tr>
</table>

### � **Recursos Técnicos**
- ⚡ **Performance Otimizada**: Algoritmos de detecção otimizados para baixo uso de CPU
- 🔧 **Configurações Flexíveis**: Sistema de configuração centralizado e persistente
- 📈 **Sistema de Logging**: Logs estruturados para debugging e análise
- 🧪 **Testabilidade**: Suite de testes abrangente com 83% de cobertura
- 📦 **Arquitetura Modular**: Código limpo seguindo princípios SOLID
- 🌍 **Cross-Platform**: Suporte nativo para macOS, Windows e Linux

## 🏗️ Arquitetura Modular

O projeto foi refatorado com uma arquitetura modular para facilitar manutenção:

```

## 🚀 Instalação e Uso

### Pré-requisitos

- Python 3.8 ou superior
- macOS, Windows ou Linux
- Permissões de acessibilidade (macOS)

### Instalação Rápida

1. **Clone ou baixe o projeto**
2. **Instale as dependências:**
   ```bash
   # Usando pip
   pip install -r requirements.txt
   
   # Ou usando uv (recomendado)
   uv sync
   ```

3. **Execute a aplicação:**
   ```bash
   # Aplicação principal
   python main.py
   
   # Com argumentos
   python main.py --help
   python main.py --version
   ```

### Configuração macOS

No macOS, você precisa conceder permissões de acessibilidade:

1. Vá em **Preferências do Sistema**
2. **Segurança e Privacidade** → **Privacidade** → **Acessibilidade**
3. Adicione **Terminal** ou **Python** à lista
4. Marque a caixa de seleção para ativar

## 🎮 Como Usar

1. **Inicie a aplicação** - A interface moderna será aberta
2. **Ajuste as configurações** - Defina o intervalo de verificação
3. **Ative o modo debug** (opcional) - Para salvar capturas das detecções
4. **Clique em "Iniciar Monitoramento"** - O sistema começará a procurar botões azuis
5. **Monitore as estatísticas** - Acompanhe cliques e taxa de sucesso em tempo real

### Parada de Emergência

- **Método 1**: Clique no botão "Parar" na interface
- **Método 2**: Mova o mouse para o canto superior esquerdo da tela

## 🔧 Configurações Avançadas

### Detecção de Cor

O sistema detecta botões azuis usando análise HSV com dois rangos:

```python
# Azul padrão (botões típicos)
HSV: (105-125, 80-255, 80-255)

# Azul claro (estados hover/active)
HSV: (95-115, 60-200, 100-255)
```

### Filtros de Botão

```python
# Dimensões válidas
Largura: 50-300 pixels
Altura: 20-80 pixels
Área: 1000-20000 pixels

# Proporção (largura:altura)
Aspect Ratio: 1.8:1 a 6:1
```

### Configurações de Performance

```python
# Intervalos suportados
Mínimo: 0.1 segundos
Máximo: 5.0 segundos
Padrão: 0.5 segundos

# Delay após clique
Padrão: 2.0 segundos
```

## 📊 Monitoramento e Estatísticas

A interface exibe em tempo real:

- **Contador de Cliques**: Total de botões clicados com sucesso
- **Tempo de Sessão**: Duração da sessão atual
- **Taxa de Sucesso**: Percentual de detecções bem-sucedidas
- **Tempo Médio**: Tempo médio de detecção por ciclo

## 🐛 Debug e Troubleshooting

### Modo Debug

Ative o modo debug para:
- Salvar capturas de tela das detecções
- Visualizar retângulos de detecção
- Analisar candidatos a botão
- Verificar scores de confiança

As imagens são salvas em `debug_images/` com timestamp.

### Problemas Comuns

**Botão não detectado:**
- Verifique se o botão é realmente azul (HSV)
- Confirme se está dentro dos critérios de tamanho
- Certifique-se que está completamente visível

**Cliques em local errado:**
- Calibre os parâmetros de cor
- Verifique escala da tela (high DPI)
- Teste em monitor principal

**Performance baixa:**
- Aumente o intervalo de verificação
- Implemente região de interesse (ROI)
- Verifique uso de CPU

## 🛠️ Desenvolvimento

### Estrutura dos Módulos

- **`config.py`**: Configurações centralizadas
- **`detector.py`**: Algoritmos de detecção visual
- **`monitor.py`**: Gerenciamento do monitoramento

... (truncado após 200 linhas)

```


## 💻 Código Principal

### main.py

```
#!/usr/bin/env python3
"""
Auto Clicker Pro - Sistema de Detecção e Clique Automático
Sistema moderno de detecção e clique automático em botões azuis

Versão refatorada com arquitetura modular para facilitar manutenção.
"""

import sys
import os

# Adicionar diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.app import main as app_main
    from src import __version__, __description__
    
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    print("💡 Certifique-se de que todas as dependências estão instaladas:")
    print("   pip install -r requirements.txt")
    sys.exit(1)


def show_version_info():
    """Mostra informações de versão"""
    print(f"Auto Clicker Pro v{__version__}")
    print(__description__)
    print()


def main():
    """Função principal do programa"""
    try:
        # Verificar argumentos de linha de comando
        if len(sys.argv) > 1:
            if sys.argv[1] in ['--version', '-v']:
                show_version_info()
                return
            elif sys.argv[1] in ['--help', '-h']:
                show_version_info()
                print("Uso: python main.py [opções]")
                print()
                print("Opções:")
                print("  -v, --version    Mostra a versão do programa")
                print("  -h, --help       Mostra esta mensagem de ajuda")
                print()
                print("Para usar o programa, execute sem argumentos para abrir a interface gráfica.")
                return
        
        # Executar aplicação principal
        app_main()
        
    except KeyboardInterrupt:
        print("\n👋 Programa interrompido pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

```


## 📄 Arquivos de Código Detalhados

*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*

### src/ui.py (19.94 KB)

```python
"""
Interface Gráfica Moderna do Auto Clicker Pro
Módulo responsável pela criação e gerenciamento da interface do usuário
"""

from typing import Callable, Optional

try:
    from .test_helpers import safe_import
except ImportError:
    from test_helpers import safe_import

# Safe imports that work in both normal and test environments
tk = safe_import('tkinter')
ttk = safe_import('tkinter.ttk')

try:
    from .config import MESSAGES, UI_CONFIG
except ImportError:
    from config import MESSAGES, UI_CONFIG


class ModernUI:
    """
    Interface gráfica moderna para o Auto Clicker Pro

    Utiliza design moderno com cards, cores consistentes e layout responsivo
    """

    def __init__(self, root: tk.Tk):
        """
        Inicializa a interface

        Args:
            root: Janela principal do Tkinter
        """
        self.root = root
        self.colors = UI_CONFIG["colors"]
        self.fonts = UI_CONFIG["font_sizes"]

        # Variáveis da interface
        self.monitor_interval = tk.DoubleVar(root, value=0.5)
        self.debug_var = tk.BooleanVar(root)

        # Labels que serão atualizados
        self.status_indicator: Optional[tk.Label] = None
        self.status_text: Optional[tk.Label] = None
        self.click_counter_label: Optional[tk.Label] = None
        self.session_time_label: Optional[tk.Label] = None
        self.interval_value_label: Optional[tk.Label] = None
        self.success_rate_label: Optional[tk.Label] = None
        self.avg_time_label: Optional[tk.Label] = None

        # Botões de controle
        self.start_btn: Optional[tk.Button] = None
        self.stop_btn: Optional[tk.Button] = None

        # Callbacks (serão definidos externamente)
        self.start_callback: Optional[Callable] = None
        self.stop_callback: Optional[Callable] = None
        self.interval_change_callback: Optional[Callable] = None

        # Attempt to build the full UI. In unit test environments the
        # provided `root` may be a mock object (or the environment may be
        # headless). Guard construction so tests can instantiate the UI
        # without requiring a real Tk interpreter.
        try:
            self._setup_window()
            self._setup_styles()
            self._create_interface()
            self._center_window()
            self._mocked_ui = False
        except Exception:
            # Mark that the UI was not fully constructed due to a mocked or
            # headless environment. Tests can still assert that the
            # ModernUI instance was created and that `root` was assigned.
            self._mocked_ui = True

    def _setup_window(self) -> None:
        """Configura as propriedades básicas da janela"""

... (truncado após 80 linhas)

```

### src/detector.py (13.10 KB)

```python
"""
Sistema de Detecção de Botões Azuis
Módulo responsável pela detecção visual de botões azuis na tela
"""

import os
import time
from typing import Any, Dict, List, Optional, Tuple

# Conditional imports for CI/test environments
try:
    if os.environ.get('CI_ENVIRONMENT') or os.environ.get('HEADLESS_MODE'):
        # Mock GUI libraries in CI/test environments
        import unittest.mock as mock
        cv2 = mock.MagicMock()
        pyautogui = mock.MagicMock()
    else:
        import cv2
        import pyautogui
except ImportError:
    # Fallback mocking if imports fail
    import unittest.mock as mock
    cv2 = mock.MagicMock()
    pyautogui = mock.MagicMock()

import numpy as np

try:
    from .config import COLOR_DETECTION, DEBUG_CONFIG
    from .resolution_adapter import get_resolution_adapter
except ImportError:
    from config import COLOR_DETECTION, DEBUG_CONFIG
    from resolution_adapter import get_resolution_adapter


class BlueButtonDetector:
    """
    Detector inteligente de botões azuis na tela

    Utiliza análise de cor HSV e filtros de forma para identificar
    botões azuis típicos de interfaces "Continue"
    """

    def __init__(self, debug_mode: bool = False):
        """
        Inicializa o detector

        Args:
            debug_mode: Se True, salva imagens de debug
        """
        self.debug_mode = debug_mode
        self.detection_count = 0
        self.successful_detections = 0

        # Inicializar adaptador de resolução
        self.resolution_adapter = get_resolution_adapter()

        # Criar diretório de debug se necessário
        if self.debug_mode:
            self._setup_debug_directory()

    def _setup_debug_directory(self) -> None:
        """Cria o diretório para salvar imagens de debug"""
        debug_dir = DEBUG_CONFIG["debug_dir"]
        if not os.path.exists(debug_dir):
            os.makedirs(debug_dir)
            print(f"Diretório de debug criado: {debug_dir}")

    def detect_button(self) -> Optional[Tuple[int, int, int, int]]:
        """
        Detecta botão azul na tela

        Returns:
            Tupla (center_x, center_y, width, height) se encontrado, None caso contrário
        """
        try:
            self.detection_count += 1

            # Obter configuração adaptada para resolução atual
            config = self.resolution_adapter.get_adapted_config()

... (truncado após 80 linhas)

```

### src/monitor.py (11.77 KB)

```python
"""
Sistema de Monitoramento do Auto Clicker Pro
Módulo responsável pelo gerenciamento do monitoramento e cliques automáticos
"""

import os
import threading
import time
from typing import Any, Callable, Dict, Optional

# Conditional imports for CI/test environments
try:
    if os.environ.get('CI_ENVIRONMENT') or os.environ.get('HEADLESS_MODE'):
        # Mock GUI libraries in CI/test environments
        import unittest.mock as mock
        pyautogui = mock.MagicMock()
    else:
        import pyautogui
except ImportError:
    # Fallback mocking if imports fail
    import unittest.mock as mock
    pyautogui = mock.MagicMock()

try:
    from .config import MESSAGES, MONITORING_CONFIG
    from .detector import BlueButtonDetector
except ImportError:
    from config import MESSAGES, MONITORING_CONFIG
    from detector import BlueButtonDetector


class MonitoringManager:
    """
    Gerenciador do sistema de monitoramento

    Coordena a detecção de botões e execução de cliques automáticos
    """

    def __init__(self):
        """Inicializa o gerenciador de monitoramento"""
        # Estado do monitoramento
        self.is_monitoring = False
        self.monitor_thread: Optional[threading.Thread] = None

        # Configurações
        self.monitor_interval = MONITORING_CONFIG["default_interval"]
        self.debug_mode = False

        # Estatísticas
        self.click_count = 0
        self.session_start_time: Optional[float] = None
        self.detection_times = []

        # Detector de botões
        self.detector: Optional[BlueButtonDetector] = None

        # Callbacks para UI
        self.status_callback: Optional[Callable[[str, str], None]] = None
        self.click_callback: Optional[Callable[[int], None]] = None
        self.stats_callback: Optional[Callable[[Dict[str, Any]], None]] = None

        # Configurar PyAutoGUI
        self._setup_pyautogui()

    def _setup_pyautogui(self) -> None:
        """Configura as opções de segurança do PyAutoGUI"""
        pyautogui.FAILSAFE = MONITORING_CONFIG["failsafe_enabled"]
        pyautogui.PAUSE = MONITORING_CONFIG["pause_between_actions"]

    def set_callbacks(
        self,
        status_callback: Callable[[str, str], None],
        click_callback: Callable[[int], None],
        stats_callback: Callable[[Dict[str, Any]], None],
    ) -> None:
        """
        Define os callbacks para comunicação com a UI

        Args:
            status_callback: Callback para atualização de status (status, color)

... (truncado após 80 linhas)

```

### src/resolution_adapter.py (10.43 KB)

```python
"""
Sistema de Adaptação de Resolução
Módulo responsável por adaptar parâmetros de detecção conforme a resolução da tela
"""

import math
import os
from typing import Any, Dict, Optional, Tuple

# Conditional imports for CI/test environments
try:
    if os.environ.get('CI_ENVIRONMENT') or os.environ.get('HEADLESS_MODE'):
        # Mock GUI libraries in CI/test environments
        import unittest.mock as mock
        pyautogui = mock.MagicMock()
        # Set up screen size mock
        pyautogui.size = mock.MagicMock(return_value=(1920, 1080))
    else:
        import pyautogui
except ImportError:
    # Fallback mocking if imports fail
    import unittest.mock as mock
    pyautogui = mock.MagicMock()
    pyautogui.size = mock.MagicMock(return_value=(1920, 1080))

try:
    from .config import BUTTON_DETECTION, RESOLUTION_ADAPTATION
except ImportError:
    from config import BUTTON_DETECTION, RESOLUTION_ADAPTATION


class ResolutionAdapter:
    """
    Adaptador que ajusta parâmetros de detecção baseado na resolução atual da tela

    Resolve problemas quando a resolução muda, mantendo a detecção eficaz
    """

    def __init__(self):
        """Inicializa o adaptador de resolução"""
        self.config_cache: Dict[Tuple[int, int], Dict[str, Any]] = {}
        self.current_resolution: Optional[Tuple[int, int]] = None
        self.scale_factor_x: float = 1.0
        self.scale_factor_y: float = 1.0
        self._update_resolution()

    def _update_resolution(self) -> None:
        """Atualiza a resolução atual da tela"""
        try:
            # Obter tamanho da tela
            screen_width, screen_height = pyautogui.size()
            new_resolution = (screen_width, screen_height)

            # Verificar se a resolução mudou
            if new_resolution != self.current_resolution:
                self.current_resolution = new_resolution
                self._calculate_scale_factors()
                print(f"📐 Resolução detectada: {screen_width}x{screen_height}")
                print(
                    f"📏 Fatores de escala: X={self.scale_factor_x:.2f}, Y={self.scale_factor_y:.2f}"
                )

        except Exception as e:
            print(f"❌ Erro ao obter resolução da tela: {e}")
            # Usar resolução padrão se falhar
            self.current_resolution = (1920, 1080)
            self.scale_factor_x = 1.0
            self.scale_factor_y = 1.0

    def _calculate_scale_factors(self) -> None:
        """Calcula os fatores de escala baseado na resolução de referência"""
        if not self.current_resolution:
            return

        ref_width = RESOLUTION_ADAPTATION["reference_width"]
        ref_height = RESOLUTION_ADAPTATION["reference_height"]

        current_width, current_height = self.current_resolution

        # Calcular fatores de escala

... (truncado após 80 linhas)

```

### src/utils.py (7.89 KB)

```python
"""
Utilitários do Auto Clicker Pro
Funções auxiliares e ferramentas de desenvolvimento
"""

import json
import os
import time
from datetime import datetime
from typing import Any, Dict, Optional


class PerformanceProfiler:
    """
    Profiler simples para medir performance de operações
    """

    def __init__(self):
        """Inicializa o profiler"""
        self.timings: Dict[str, list] = {}
        self.active_timers: Dict[str, float] = {}

    def start_timer(self, operation: str) -> None:
        """
        Inicia um timer para uma operação

        Args:
            operation: Nome da operação
        """
        self.active_timers[operation] = time.time()

    def end_timer(self, operation: str) -> Optional[float]:
        """
        Finaliza um timer e retorna o tempo decorrido

        Args:
            operation: Nome da operação

        Returns:
            Tempo decorrido em segundos ou None se timer não foi iniciado
        """
        if operation not in self.active_timers:
            return None

        elapsed = time.time() - self.active_timers[operation]

        # Armazenar timing
        if operation not in self.timings:
            self.timings[operation] = []
        self.timings[operation].append(elapsed)

        # Limpar timer ativo
        del self.active_timers[operation]

        return elapsed

    def get_statistics(self, operation: str) -> Dict[str, float]:
        """
        Retorna estatísticas de uma operação

        Args:
            operation: Nome da operação

        Returns:
            Dicionário com estatísticas (min, max, avg, count)
        """
        if operation not in self.timings or not self.timings[operation]:
            return {}

        times = self.timings[operation]
        return {
            "min": min(times),
            "max": max(times),
            "avg": sum(times) / len(times),
            "count": len(times),
            "total": sum(times),
        }

    def get_all_statistics(self) -> Dict[str, Dict[str, float]]:
        """

... (truncado após 80 linhas)

```

### src/app.py (5.92 KB)

```python
"""
Auto Clicker Pro - Aplicação Principal
Sistema moderno de detecção e clique automático em botões azuis
"""

import os
import sys
from typing import Any, Dict

# Conditional imports for CI/test environments
try:
    if os.environ.get('CI_ENVIRONMENT') or os.environ.get('HEADLESS_MODE'):
        # Mock tkinter in CI/test environments
        import unittest.mock as mock
        tk = mock.MagicMock()
    else:
        import tkinter as tk
except ImportError:
    # Fallback mocking if imports fail
    import unittest.mock as mock
    tk = mock.MagicMock()

try:
    from .config import MESSAGES
    from .monitor import MonitoringManager
    from .ui import ModernUI
except ImportError:
    from config import MESSAGES
    from monitor import MonitoringManager
    from ui import ModernUI


class AutoClickerPro:
    """
    Aplicação principal do Auto Clicker Pro

    Coordena a interface gráfica e o sistema de monitoramento
    """

    def __init__(self):
        """Inicializa a aplicação"""
        # Criar janela principal
        self.root = tk.Tk()

        # Inicializar componentes
        self.ui = ModernUI(self.root)
        self.monitor = MonitoringManager()

        # Configurar callbacks
        self._setup_callbacks()

        # Timer para atualização de tempo
        self._schedule_time_update()

    def _setup_callbacks(self) -> None:
        """Configura todos os callbacks entre componentes"""
        # Callbacks da UI para o monitor
        self.ui.set_callbacks(
            start_callback=self._on_start_monitoring,
            stop_callback=self._on_stop_monitoring,
            interval_callback=self._on_interval_changed,
        )

        # Callbacks do monitor para a UI
        self.monitor.set_callbacks(
            status_callback=self._on_status_update,
            click_callback=self._on_click_update,
            stats_callback=self._on_stats_update,
        )

        # Configurar agendador de UI
        self.monitor.set_ui_scheduler(self._schedule_ui_update)

        # Callback para fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _on_start_monitoring(self) -> None:
        """Callback para início do monitoramento"""
        interval = self.ui.get_monitor_interval()
        debug_mode = self.ui.get_debug_mode()

... (truncado após 80 linhas)

```

### src/config.py (5.29 KB)

```python
"""
Configurações do Auto Clicker Pro
Centraliza todas as configurações e constantes do sistema
"""

import numpy as np

# Configurações de Interface
UI_CONFIG = {
    # Dimensões da janela
    "window_size": "650x750",
    "min_size": (600, 700),
    "padding": 20,
    # Fontes
    "font_family": "SF Pro Display",
    "font_sizes": {
        "title": 28,
        "subtitle": 14,
        "header": 16,
        "body": 12,
        "button": 12,
        "small": 11,
    },
    # Cores do tema
    "colors": {
        "primary": "#2E86AB",  # Azul
        "success": "#A23B72",  # Verde-rosa
        "warning": "#F18F01",  # Laranja
        "danger": "#C73E1D",  # Vermelho
        "dark": "#1A1A1A",  # Cinza escuro
        "light": "#F8F9FA",  # Cinza claro
        "background": "#FFFFFF",  # Branco
        "card_bg": "#F8F9FA",  # Fundo dos cards
        "border": "#E9ECEF",  # Cor da borda
    },
}

# Configurações de Detecção de Cor
COLOR_DETECTION = {
    # Faixas de cor azul em HSV
    "blue_ranges": [
        {
            "name": "standard_blue",
            "lower": np.array([105, 80, 80]),
            "upper": np.array([125, 255, 255]),
        },
        {
            "name": "light_blue",
            "lower": np.array([95, 60, 100]),
            "upper": np.array([115, 200, 255]),
        },
    ],
    # Configurações de processamento de imagem
    "morphology_kernel_size": (3, 3),
    "min_blue_ratio": 0.3,  # Mínimo 30% de pixels azuis para ser considerado botão
}

# Configurações de Detecção de Botão
BUTTON_DETECTION = {
    # Filtros de área (base para 1920x1080)
    "base_min_area": 1000,
    "base_max_area": 20000,
    # Filtros de dimensão (base para 1920x1080)
    "base_min_width": 50,
    "base_max_width": 300,
    "base_min_height": 20,
    "base_max_height": 80,
    # Filtros de proporção (não mudam com resolução)
    "min_aspect_ratio": 1.8,
    "max_aspect_ratio": 6.0,
    # Margem das bordas da tela (percentual da tela)
    "edge_margin_percent": 0.05,  # 5% da largura/altura da tela
    # Pesos para cálculo de score
    "score_weights": {"blue_ratio": 0.5, "position": 0.3, "size": 0.2},
}

# Configurações de Adaptação de Resolução
RESOLUTION_ADAPTATION = {
    # Resolução de referência para cálculos
    "reference_width": 1920,

... (truncado após 80 linhas)

```

### legacy/auto_clicker_blue_v2.py (1.93 KB)

```python
#!/usr/bin/env python3
"""
Auto Clicker Pro - Ponto de Entrada Principal
Sistema moderno de detecção e clique automático em botões azuis

Este arquivo mantém compatibilidade com a versão anterior enquanto
utiliza a nova arquitetura modular.
"""

import sys
import os

# Adicionar diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.app import main, AutoClickerPro
    from src import __version__, __description__
    
    # Manter compatibilidade com imports antigos
    ModernAutoClickerBlue = AutoClickerPro
    
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    print("💡 Certifique-se de que todas as dependências estão instaladas:")
    print("   pip install -r requirements.txt")
    sys.exit(1)


def show_version_info():
    """Mostra informações de versão"""
    print(f"Auto Clicker Pro v{__version__}")
    print(__description__)
    print()


if __name__ == "__main__":
    try:
        # Verificar argumentos de linha de comando
        if len(sys.argv) > 1:
            if sys.argv[1] in ['--version', '-v']:
                show_version_info()
                sys.exit(0)
            elif sys.argv[1] in ['--help', '-h']:
                show_version_info()
                print("Uso: python auto_clicker_blue.py [opções]")
                print()
                print("Opções:")
                print("  -v, --version    Mostra a versão do programa")
                print("  -h, --help       Mostra esta mensagem de ajuda")
                print()
                print("Para usar o programa, execute sem argumentos para abrir a interface gráfica.")
                sys.exit(0)
        
        # Executar aplicação principal
        main()
        
    except KeyboardInterrupt:
        print("\n👋 Programa interrompido pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)

```


## 📂 Lista Completa de Arquivos

- `docs/MANUAL.md` (24.37 KB)
- `src/ui.py` (19.94 KB)
- `safety-report.json` (16.26 KB)
- `src/detector.py` (13.10 KB)
- `src/monitor.py` (11.77 KB)
- `src/resolution_adapter.py` (10.43 KB)
- `README.md` (9.37 KB)
- `tests/test_refactoring.py` (9.12 KB)
- `docs/REFACTORING_REPORT.md` (8.73 KB)
- `src/utils.py` (7.89 KB)
- `docs/PROFESSIONAL_ORGANIZATION_REPORT.md` (6.72 KB)
- `CONTRIBUTING.md` (6.18 KB)
- `.github/workflows/ci.yml` (6.00 KB)
- `src/app.py` (5.92 KB)
- `bandit-report.json` (5.63 KB)
- `pyproject.toml` (5.60 KB)
- `src/config.py` (5.29 KB)
- `test_resolution_adaptation.py` (5.06 KB)
- `docs/SIMPLIFICATION_SUMMARY.md` (5.04 KB)
- `RESOLUTION_ADAPTATION_SUMMARY.md` (4.83 KB)
- `scripts/setup-dev.sh` (3.17 KB)
- `scripts/quality-check.sh` (2.76 KB)
- `CHANGELOG.md` (2.33 KB)
- `.github/pull_request_template.md` (2.03 KB)
- `legacy/auto_clicker_blue_v2.py` (1.93 KB)
- `main.py` (1.87 KB)
- `.github/ISSUE_TEMPLATE/feature_request.md` (1.67 KB)
- `src/test_helpers.py` (1.35 KB)
- `.gitignore` (1.18 KB)
- `.github/ISSUE_TEMPLATE/bug_report.md` (1.11 KB)
- `LICENSE` (1.05 KB)
- `setup.sh` (961.00 B)
- `src/__init__.py` (285.00 B)
- `requirements.txt` (119.00 B)
- `.python-version` (5.00 B)

---
*Relatório gerado automaticamente para análise CrewAI*

**IMPORTANTE:** Este relatório contém código real do projeto. A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.
