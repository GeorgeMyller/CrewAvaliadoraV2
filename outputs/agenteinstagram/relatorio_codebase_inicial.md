# 📊 Relatório Técnico da Codebase
**Gerado em:** 2025-11-02 14:37:47
**Diretório analisado:** `/var/folders/g1/7nfb0bns5zbftz_zqwwbbyjw0000gn/T/crew_analysis_agenteinstagram_ou026v2z`
**Total de arquivos:** 84
**Tamanho total:** 841.68 KB

## 📈 Distribuição por Extensão

- **.py**: 49 arquivos (364.02 KB)
- **.txt**: 15 arquivos (154.05 KB)
- **.md**: 10 arquivos (36.19 KB)
- **no_extension**: 4 arquivos (11.59 KB)
- **.png**: 2 arquivos (272.02 KB)
- **.json**: 1 arquivos (174.00 B)
- **.toml**: 1 arquivos (599.00 B)
- **.example**: 1 arquivos (533.00 B)
- **.html**: 1 arquivos (2.54 KB)

## 📁 Estrutura de Diretórios

- `src/instagram`: 24 arquivos (606.85 KB)
- `root`: 14 arquivos (79.02 KB)
- `tests`: 7 arquivos (7.76 KB)
- `src/utils`: 6 arquivos (14.95 KB)
- `src/agent_social_media.egg-info`: 6 arquivos (6.63 KB)
- `src/services`: 6 arquivos (66.88 KB)
- `docs/installation`: 3 arquivos (1.91 KB)
- `docs/troubleshooting`: 3 arquivos (10.87 KB)
- `docs/guides`: 3 arquivos (9.11 KB)
- `docs/api`: 3 arquivos (6.37 KB)
- `src`: 3 arquivos (949.00 B)
- `src/handlers`: 3 arquivos (15.95 KB)
- `monitoring_templates`: 1 arquivos (2.54 KB)
- `docs`: 1 arquivos (3.61 KB)
- `assets`: 1 arquivos (8.31 KB)

## 📖 README / Descrição do Projeto

### Conteúdo de README.md

```
# Agent Social Media - CrewAI2 📱🤖

## Português 🇧🇷

### Descrição do Projeto
Este projeto é uma ferramenta de automação social media que integra CrewAI e Gemini para gerenciar postagens no Instagram. Oferece geração inteligente de legendas, processamento de imagens e suporte a múltiplos formatos de mídia.

> **Origem do Projeto**: Este projeto foi inspirado pelo livro [CrewAI 2 - Intermediário](https://physia.com.br) do Professor Sandeco, que apresenta conceitos avançados de automação e IA colaborativa para desenvolvimento de agentes inteligentes.

### Funcionalidades Principais 🚀
- Geração de legendas usando CrewAI
- Descrição de imagens com API Gemini
- Processamento de imagens e vídeos
- Suporte a carrosséis do Instagram
- Interface web via Streamlit
- API REST para integrações

### Pré-requisitos 📋
- Python 3.10+
- FFmpeg para processamento de vídeos
- Conta Instagram Business/Creator
- Chave API Gemini
- UV (gerenciador de pacotes Python)

### Como Usar 🚀

#### Interface Gráfica (Recomendado)
1. Instale as dependências:
   ```bash
   uv sync
   ```
2. Execute a interface Streamlit:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Acesse em `http://localhost:8501`

#### API (Webhooks)
1. Instale o UV e crie ambiente virtual:
   ```bash
   pip install uv
   uv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   uv sync
   ```
2. Configure o `.env` com suas credenciais
3. Inicie o servidor Flask

### Estrutura do Projeto 📂
- `app.py`: Endpoints Flask
- `instagram/`: Módulos de integração Instagram
- `crew_post_instagram.py`: Configuração CrewAI
- `message.py`: Processamento de mensagens
- `streamlit_app.py`: Interface gráfica

### Licença
MIT License - Veja LICENSE para detalhes.

---

## English 🇺🇸

### Project Description
This project is a comprehensive tool for automating and managing social media posts, with a special focus on Instagram. It integrates the CrewAI library to generate creative captions, along with robust image processing features – including filters, border addition, image upload via Imgur, and Instagram posting. It also features intelligent image description using Google's Gemini API, message processing (text, audio, image, and document) and integration with the Evolution API.

> **Project Origin**: This project was inspired by Professor Sandeco's book [CrewAI 2 - Intermediate](https://physia.com.br), which presents advanced concepts of automation and collaborative AI for developing intelligent agents.

### Main Features 🚀
- Caption generation with CrewAI
- Image processing: filters, corrections, and border additions
- Image upload using Imgur
- Instagram post publishing
- Intelligent image description with Gemini API
- Message processing and sending via Evolution API
- Flask endpoints for webhooks and service integration

### How to Use 🚀

#### Graphical Interface (Recommended)
1. Install dependencies:
   ```bash
   uv sync
   ```
2. Run the Streamlit interface:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Access the web interface at `http://localhost:8501`
4. Use the sidebar to configure:
   - Writing style
   - Narrative person
   - Sentiment
   - Emoji and informal language usage
5. Upload an image and add an optional caption
6. Click "Post to Instagram" to publish

#### API (Webhooks)
1. Install UV:
   ```bash
   pip install uv
   ```
2. Create the virtual environment:
   ```bash
   uv venv
   ```
3. Activate the virtual environment (use `venv\Scripts\activate` on Windows):
   ```bash
   source venv/bin/activate
   ```
4. Synchronize dependencies and launch the application:
   ```bash
   uv sync
   ```

### Project Structure 📂
- `app.py`: Flask endpoints for message processing.
- `instagram/` folder: Modules for creating posts, image uploading, filters, border additions and image description.
- `crew_post_instagram.py`: CrewAI configuration and caption generation tasks.
- `message.py` and `send_message.py`: Message processing and sending.
- `paths.py`: File path configurations.
- `streamlit_app.py`: Graphical interface for post management
- Other auxiliary files and scripts.

### Contribution
Contributions are welcome! Feel free to open issues and pull requests for improvements and fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

Happy coding! 😄
```


## 💻 Código Principal

### app.py

```
from src.services.message import Message
from src.utils.image_decode_save import ImageDecodeSaver
from src.utils.video_decode_save import VideoDecodeSaver  # Added import for video processing
from src.services.instagram_send import InstagramSend
from src.instagram.instagram_reels_publisher import ReelsPublisher  # Importe a classe ReelsPublisher
from flask import Flask, request, jsonify
import subprocess
import os
import time
import traceback
import threading
import re
from datetime import datetime

from src.utils.paths import Paths  # Add this import

# Import our queue exceptions for error handling
from src.services.post_queue import RateLimitExceeded, ContentPolicyViolation

# Import monitoring server starter
from monitor import start_monitoring_server

from src.instagram.filter import FilterImage
from src.services.send import sender #Para enviar mensagens de volta
from src.instagram.describe_video_tool import VideoDescriber  # Importar a classe VideoDescriber
from src.instagram.describe_carousel_tool import CarouselDescriber  # Importar a classe CarouselDescriber
from src.instagram.crew_post_instagram import InstagramPostCrew  # Importar a classe InstagramPostCrew
from src.instagram.image_validator import InstagramImageValidator  # Add this import
from src.services.post_notification import PostCompletionNotifier
from src.services.post_queue import post_queue

app = Flask(__name__)

# Initialize required directories
os.makedirs(os.path.join(Paths.ROOT_DIR, "temp_videos"), exist_ok=True)
os.makedirs(os.path.join(Paths.ROOT_DIR, "temp"), exist_ok=True)

# Create assets directory if it doesn't exist
assets_dir = os.path.join(Paths.ROOT_DIR, "assets")
os.makedirs(assets_dir, exist_ok=True)

# Define border image with full path
border_image_path = os.path.join(assets_dir, "moldura.png")

# Check if border image exists, if not, set it to None to make it optional
if not os.path.exists(border_image_path):
    print(f"⚠️ Aviso: Imagem de borda não encontrada em {border_image_path}")
    border_image_path = None

# Variáveis de estado para o modo carrossel
is_carousel_mode = False
carousel_images = []
carousel_start_time = 0
carousel_caption = ""
CAROUSEL_TIMEOUT = 300  # 5 minutos em segundos
MAX_CAROUSEL_IMAGES = 10

@app.route("/messages-upsert", methods=['POST'])
def webhook():
    global is_carousel_mode, carousel_images, carousel_start_time, carousel_caption

    try:
        data = request.get_json()

        msg = Message(data)
        texto = msg.get_text()
        
        #Verificar se o número é de um grupo valido.
        if msg.scope == Message.SCOPE_GROUP:
            print(f"Grupo: {msg.group_id}")
            if str(msg.group_id) != "120363383673368986":  #Use != para a comparação, e a string correta.
                return jsonify({"status": "processed, but ignored"}), 200 #Retorna 200 para o webhook não reenviar.
        
        # Lógica do Modo Carrossel
        # Iniciar modo carrossel com comando "carrossel" ou "carousel"
        carousel_command = re.match(r'^carrosse?l\s*(.*)', texto.lower() if texto else "") if texto else None
        if carousel_command:
            is_carousel_mode = True
            carousel_images = []
            carousel_caption = carousel_command.group(1).strip() if carousel_command.group(1) else ""
            carousel_start_time = time.time()
            
            instructions = (
                "🎠 *Modo carrossel ativado!*\n\n"
                "- Envie as imagens que deseja incluir no carrossel (2-10 imagens)\n"
                "- Para definir uma legenda, envie \"legenda: sua legenda aqui\"\n"
                "- Quando terminar, envie \"postar\" para publicar o carrossel\n"
                "- Para cancelar, envie \"cancelar\"\n\n"
                "O modo carrossel será desativado automaticamente após 5 minutos de inatividade."
            )
            
            if carousel_caption:
                sender.send_text(number=msg.remote_jid, 
                                msg=f"{instructions}\n\nLegenda inicial definida: {carousel_caption}")
            else:
                sender.send_text(number=msg.remote_jid, msg=instructions)
            
            return jsonify({"status": "Modo carrossel ativado"}), 200

        if is_carousel_mode:

... (truncado após 100 linhas)

```


## 📄 Arquivos de Código Detalhados

*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*

### src/services/instagram_send.py (35.08 KB)

```python
import os
import time
import requests
import logging
import warnings

# Suppress specific SyntaxWarnings from MoviePy
warnings.filterwarnings("ignore", category=SyntaxWarning, 
                       module="moviepy\\.config_defaults")
warnings.filterwarnings("ignore", category=SyntaxWarning, 
                       module="moviepy\\.video\\.io\\.ffmpeg_reader")
warnings.filterwarnings("ignore", category=SyntaxWarning, 
                       module="moviepy\\.video\\.io\\.sliders")

from src.instagram.crew_post_instagram import InstagramPostCrew
from src.instagram.describe_image_tool import ImageDescriber
from src.instagram.instagram_post_service import InstagramPostService
from src.instagram.border import ImageWithBorder
from src.instagram.filter import FilterImage
from src.utils.paths import Paths
from src.instagram.image_uploader import ImageUploader
from PIL import Image

# Import new queue system
from src.services.post_queue import post_queue, RateLimitExceeded
from src.instagram.instagram_post_publisher import PostPublisher
# Import carousel normalizer from reference implementation
from src.instagram.carousel_normalizer import CarouselNormalizer

# Set up logging
logger = logging.getLogger('InstagramSend')

class InstagramSend:
    # Keep track of rate limits
    last_rate_limit_time = 0
    rate_limit_window = 3600  # 1 hour window for rate limiting
    max_rate_limit_hits = 52  # Maximum number of rate limit hits before enforcing longer delays
    
    @staticmethod
    def queue_post(image_path, caption, inputs=None) -> str:
        """
        Queue an image to be posted to Instagram asynchronously
        
        Args:
            image_path (str): Path to the image file
            caption (str): Caption text
            inputs (dict): Optional configuration for post generation
            
        Returns:
            str: Job ID for tracking the post status
        """
        # Validate inputs before queuing
        if not caption or caption.lower() == "none":
            caption = "A AcessoIA está transformando processos com IA! 🚀"
            print(f"Caption vazia ou 'None'. Usando caption padrão: '{caption}'")

        # Validate image path
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Arquivo de imagem não encontrado: {image_path}")
            
        # Add to queue and return job ID
        job_id = post_queue.add_job(image_path, caption, inputs)
        return job_id
    
    @staticmethod
    def queue_reels(video_path, caption, inputs=None) -> str:
        """
        Queue a video to be posted to Instagram as a reel asynchronously
        
        Args:
            video_path (str): Path to the video file
            caption (str): Caption text
            inputs (dict): Optional configuration for post generation
            
        Returns:
            str: Job ID for tracking the post status
        """
        # Validate inputs before queuing
        if not caption or caption.lower() == "none":
            caption = "A AcessoIA está transformando processos com IA! 🚀 #reels #ai"

... (truncado após 80 linhas)

```

### app.py (34.81 KB)

```python
from src.services.message import Message
from src.utils.image_decode_save import ImageDecodeSaver
from src.utils.video_decode_save import VideoDecodeSaver  # Added import for video processing
from src.services.instagram_send import InstagramSend
from src.instagram.instagram_reels_publisher import ReelsPublisher  # Importe a classe ReelsPublisher
from flask import Flask, request, jsonify
import subprocess
import os
import time
import traceback
import threading
import re
from datetime import datetime

from src.utils.paths import Paths  # Add this import

# Import our queue exceptions for error handling
from src.services.post_queue import RateLimitExceeded, ContentPolicyViolation

# Import monitoring server starter
from monitor import start_monitoring_server

from src.instagram.filter import FilterImage
from src.services.send import sender #Para enviar mensagens de volta
from src.instagram.describe_video_tool import VideoDescriber  # Importar a classe VideoDescriber
from src.instagram.describe_carousel_tool import CarouselDescriber  # Importar a classe CarouselDescriber
from src.instagram.crew_post_instagram import InstagramPostCrew  # Importar a classe InstagramPostCrew
from src.instagram.image_validator import InstagramImageValidator  # Add this import
from src.services.post_notification import PostCompletionNotifier
from src.services.post_queue import post_queue

app = Flask(__name__)

# Initialize required directories
os.makedirs(os.path.join(Paths.ROOT_DIR, "temp_videos"), exist_ok=True)
os.makedirs(os.path.join(Paths.ROOT_DIR, "temp"), exist_ok=True)

# Create assets directory if it doesn't exist
assets_dir = os.path.join(Paths.ROOT_DIR, "assets")
os.makedirs(assets_dir, exist_ok=True)

# Define border image with full path
border_image_path = os.path.join(assets_dir, "moldura.png")

# Check if border image exists, if not, set it to None to make it optional
if not os.path.exists(border_image_path):
    print(f"⚠️ Aviso: Imagem de borda não encontrada em {border_image_path}")
    border_image_path = None

# Variáveis de estado para o modo carrossel
is_carousel_mode = False
carousel_images = []
carousel_start_time = 0
carousel_caption = ""
CAROUSEL_TIMEOUT = 300  # 5 minutos em segundos
MAX_CAROUSEL_IMAGES = 10

@app.route("/messages-upsert", methods=['POST'])
def webhook():
    global is_carousel_mode, carousel_images, carousel_start_time, carousel_caption

    try:
        data = request.get_json()

        msg = Message(data)
        texto = msg.get_text()
        
        #Verificar se o número é de um grupo valido.
        if msg.scope == Message.SCOPE_GROUP:
            print(f"Grupo: {msg.group_id}")
            if str(msg.group_id) != "120363383673368986":  #Use != para a comparação, e a string correta.
                return jsonify({"status": "processed, but ignored"}), 200 #Retorna 200 para o webhook não reenviar.
        
        # Lógica do Modo Carrossel
        # Iniciar modo carrossel com comando "carrossel" ou "carousel"
        carousel_command = re.match(r'^carrosse?l\s*(.*)', texto.lower() if texto else "") if texto else None
        if carousel_command:
            is_carousel_mode = True
            carousel_images = []
            carousel_caption = carousel_command.group(1).strip() if carousel_command.group(1) else ""

... (truncado após 80 linhas)

```

### src/instagram/instagram_carousel_service.py (27.70 KB)

```python
import os
import time
import json
import logging
import random
from typing import Dict, Any, Optional, List
from datetime import datetime
from dotenv import load_dotenv
from src.instagram.base_instagram_service import (
    BaseInstagramService, AuthenticationError, PermissionError,
    RateLimitError, MediaError, TemporaryServerError, InstagramAPIError
)

logger = logging.getLogger('InstagramCarouselService')

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
        self.errors = []
        self.last_error_time = 0
        self.backoff_base = 60  # Start with 1 minute
        self.max_backoff = 3600  # Max 1 hour

    def record_error(self) -> float:
        """Record an error and return the backoff time in seconds"""
        current_time = time.time()
        self.errors = [t for t in self.errors if current_time - t < 3600]  # Keep last hour
        self.errors.append(current_time)
        self.last_error_time = current_time
        
        # Calculate exponential backoff based on number of recent errors
        delay = min(self.backoff_base * (2 ** len(self.errors)), self.max_backoff)
        return delay + random.uniform(0, 10)  # Add jitter

    def should_backoff(self) -> bool:
        """Check if we should still be backing off"""
        if not self.errors:
            return False
        return time.time() - self.last_error_time < self.get_backoff_time()

    def get_backoff_time(self) -> float:
        """Get the current backoff time in seconds"""
        if not self.errors:
            return 0
        return self.backoff_base * (2 ** len(self.errors))

class InstagramCarouselService(BaseInstagramService):
    """Classe para gerenciar o upload e publicação de carrosséis no Instagram."""

    SUPPORTED_MEDIA_TYPES = ["image/jpeg", "image/png"]
    MAX_MEDIA_SIZE = 8 * 1024 * 1024  # 8MB in bytes
    API_VERSION = 'v22.0'  # Using latest API version

    # Class-level rate limit state
    _rate_limit_state = RateLimitState()

    def __init__(self, access_token=None, ig_user_id=None):
        load_dotenv()
        access_token = access_token or os.getenv('INSTAGRAM_API_KEY')
        ig_user_id = ig_user_id or os.getenv("INSTAGRAM_ACCOUNT_ID")
        
        if not access_token or not ig_user_id:
            raise ValueError(
                "Credenciais incompletas. Defina INSTAGRAM_API_KEY e "
                "INSTAGRAM_ACCOUNT_ID nas variáveis de ambiente ou forneça-os diretamente."
            )
            
        super().__init__(access_token, ig_user_id)
        self.token_expires_at = None
        self.instagram_account_id = ig_user_id
        self._validate_token()


... (truncado após 80 linhas)

```

### src/instagram/instagram_video_processor.py (25.69 KB)

```python
import os
from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips
from moviepy.video.fx.resize import resize
from moviepy.video.tools.cuts import find_video_period
from moviepy.config import change_settings
import tempfile
from typing import Dict, Any
import logging
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip
from PIL import Image
from datetime import datetime
import subprocess
import re
import json
from pathlib import Path
from typing import Optional
import moviepy.editor as mp
from moviepy.video.fx.all import resize
from src.utils.paths import Paths

# Defina um diretório temporário para o moviepy usar (opcional, mas recomendado)
# change_settings({"TEMP_DIR": "/caminho/para/seu/diretorio/temporario"}) # Linux/macOS
# change_settings({"TEMP_DIR": "C:\\caminho\\para\\seu\\diretorio\\temporario"}) # Windows

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Apply patch for Pillow 10+ compatibility
def _apply_pillow_patch():
    """Apply compatibility patch for Pillow 10+ with MoviePy"""
    if not hasattr(Image, 'ANTIALIAS'):
        if hasattr(Image, 'LANCZOS'):
            Image.ANTIALIAS = Image.LANCZOS
        elif hasattr(Image.Resampling) and hasattr(Image.Resampling, 'LANCZOS'):
            Image.ANTIALIAS = Image.Resampling.LANCZOS

# Apply the patch immediately
_apply_pillow_patch()

class VideoProcessor:

    @staticmethod
    def get_video_info(video_path: str) -> Dict[str, Any]:
        """
        Get video information using moviepy instead of ffprobe.
        
        Args:
            video_path: Path to the video file
            
        Returns:
            Dictionary with video metadata
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        try:
            # Use moviepy instead of ffprobe
            with VideoFileClip(video_path) as clip:
                width = int(clip.size[0])
                height = int(clip.size[1])
                duration = float(clip.duration)
                
                # Get file size
                file_size_bytes = os.path.getsize(video_path)
                file_size_mb = file_size_bytes / (1024 * 1024)
                
                # Get format/container from file extension
                _, ext = os.path.splitext(video_path)
                format_name = ext.lower().strip('.')
                
                return {
                    'width': width,
                    'height': height,
                    'duration': duration,
                    'file_size_mb': file_size_mb,
                    'format': format_name,
                    'aspect_ratio': width / height if height else 0
                }
        except Exception as e:

... (truncado após 80 linhas)

```

### streamlit_app.py (21.68 KB)

```python
import streamlit as st
import os
import time
import tempfile
import random
from PIL import Image
from src.services.instagram_send import InstagramSend
from src.instagram.image_validator import InstagramImageValidator
from src.utils.paths import Paths
from src.instagram.filter import FilterImage
from datetime import datetime

st.set_page_config(page_title="Instagram Agent", layout="wide")
st.title('Instagram Agent 📷')
st.caption('Agente para automação de Instagram')

# Inicialização de diretórios necessários
os.makedirs(os.path.join(Paths.ROOT_DIR, "temp_videos"), exist_ok=True)
os.makedirs(os.path.join(Paths.ROOT_DIR, "temp"), exist_ok=True)
assets_dir = os.path.join(Paths.ROOT_DIR, "assets")
os.makedirs(assets_dir, exist_ok=True)

# Define border image with full path
border_image_path = os.path.join(assets_dir, "moldura.png")
if not os.path.exists(border_image_path):
    st.warning(f"⚠️ Aviso: Imagem de borda não encontrada em {border_image_path}")
    border_image_path = None

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Publicar Foto", "Publicar Reels", "Publicar Carrossel", "Monitorar Fila", "Debug"])

with tab1:
    st.header('Publicar Foto no Instagram')
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # File uploader
        uploaded_file = st.file_uploader("Escolha uma imagem", type=['jpg', 'jpeg', 'png'], key="photo_uploader")
        
        # Caption input
        caption = st.text_area("Legenda (opcional)", 
                              placeholder="Digite uma legenda para sua foto ou deixe em branco para gerar automaticamente",
                              key="photo_caption")
        
        # Options for AI-enhanced captions
        st.subheader("Opções para legenda gerada por IA")
        col_style, col_person = st.columns(2)
        
        with col_style:
            style_options = st.selectbox(
                'Estilo da legenda',
                ('Divertido e alegre', 'Profissional e sério', 'Inspirador e motivacional', 'Informativo e educativo')
            )
            
        with col_person:
            person_options = st.selectbox(
                'Pessoa do discurso',
                ('Primeira pessoa (eu/nós)', 'Segunda pessoa (você/vocês)', 'Terceira pessoa (ele/ela/eles)')
            )
        
        col_sentiment, col_limit = st.columns(2)
        
        with col_sentiment:
            sentiment = st.select_slider(
                'Sentimento',
                options=['Muito Negativo', 'Negativo', 'Neutro', 'Positivo', 'Muito Positivo'],
                value='Positivo'
            )
            
        with col_limit:
            word_limit = st.slider('Limite de palavras', 30, 300, 150)
            
        col_emoji, col_slang = st.columns(2)
        
        with col_emoji:
            use_emojis = st.toggle('Usar emojis', value=True)
            
        with col_slang:
            use_slang = st.toggle('Usar gírias/linguagem casual', value=True)
        

... (truncado após 80 linhas)

```

### src/instagram/image_validator.py (17.15 KB)

```python
from PIL import Image
import os
import logging
import tempfile
import time

logger = logging.getLogger(__name__)

class InstagramImageValidator:
    """
    Validates images for Instagram posting requirements.
    Performs checks required by Instagram's API for various post types.
    """
    
    # Instagram API requirements
    MIN_IMG_SIZE = 320  # Minimum size in pixels (each dimension)
    MAX_IMG_SIZE = 1440  # Maximum size in pixels (each dimension)
    CAROUSEL_RATIO_TOLERANCE = 0.02  # 2% tolerance for aspect ratio consistency
    
    # Instagram supported aspect ratios
    MIN_ASPECT_RATIO = 0.8  # 4:5 portrait orientation
    MAX_ASPECT_RATIO = 1.91  # Landscape orientation
    
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
            return (False, "Carrossel precisa de pelo menos 2 imagens") if not auto_normalize else (False, "Carrossel precisa de pelo menos 2 imagens", [])
        
        if len(image_paths) > 10:  # Instagram maximum
            return (False, "Máximo de 10 imagens permitidas no carrossel") if not auto_normalize else (False, "Máximo de 10 imagens permitidas no carrossel", [])
        
        # If auto_normalize is enabled, normalize images before validation
        if auto_normalize:
            normalized_paths = cls.normalize_for_carousel(image_paths)
            if normalized_paths:
                validation_result, message = cls.validate_for_carousel(normalized_paths, auto_normalize=False)
                return validation_result, message, normalized_paths
            return False, "Falha ao normalizar imagens", []
        
        # Track aspect ratios for consistency check
        aspect_ratios = []
        invalid_images = []
        
        for i, img_path in enumerate(image_paths):
            try:
                if not os.path.exists(img_path):
                    invalid_images.append(f"Imagem {i+1}: arquivo não encontrado")
                    continue
                    
                with Image.open(img_path) as img:
                    width, height = img.size
                    
                    # Check dimensions
                    if width < cls.MIN_IMG_SIZE or height < cls.MIN_IMG_SIZE:
                        invalid_images.append(f"Imagem {i+1}: tamanho muito pequeno ({width}x{height})")
                        continue
                    
                    if width > cls.MAX_IMG_SIZE or height > cls.MAX_IMG_SIZE:
                        invalid_images.append(f"Imagem {i+1}: tamanho muito grande ({width}x{height})")
                        continue
                        
                    # Calculate aspect ratio
                    aspect_ratio = width / height
                    aspect_ratios.append(aspect_ratio)
                    
                    # Check format (Instagram accepts JPEG)
                    if img.format not in ['JPEG', 'JPG']:
                        logger.warning(f"Imagem {i+1} não está em formato JPEG/JPG. Formato atual: {img.format}")
                    

... (truncado após 80 linhas)

```

### src/instagram/instagram_post_service.py (16.01 KB)

```python
import os
import time
import json
import logging
import random
from datetime import datetime
from dotenv import load_dotenv
from imgurpython import ImgurClient
from src.instagram.base_instagram_service import (
    BaseInstagramService, AuthenticationError, PermissionError,
    RateLimitError, MediaError, TemporaryServerError, InstagramAPIError
)

logger = logging.getLogger('InstagramPostService')

class InstagramPostService(BaseInstagramService):
    """Service for posting images to Instagram."""

    def __init__(self, access_token=None, ig_user_id=None):
        load_dotenv()
        access_token = access_token or (
            os.getenv('INSTAGRAM_API_KEY') or
            os.getenv('INSTAGRAM_ACCESS_TOKEN') or
            os.getenv('FACEBOOK_ACCESS_TOKEN')
        )
        ig_user_id = ig_user_id or os.getenv("INSTAGRAM_ACCOUNT_ID")
        
        if not access_token or not ig_user_id:
            raise ValueError(
                "Credenciais incompletas. Defina INSTAGRAM_API_KEY e "
                "INSTAGRAM_ACCOUNT_ID nas variáveis de ambiente ou forneça-os diretamente."
            )

        super().__init__(access_token, ig_user_id)
        self.state_file = 'api_state.json'
        self.pending_containers = {}
        self.stats = {
            'successful_posts': 0,
            'failed_posts': 0,
            'rate_limited_posts': 0
        }
        self._load_state()
        
        # Attempt to process any pending containers from previous runs
        self._process_pending_containers()

    def _load_state(self):
        """Load persisted state from file"""
        try:
            if os.path.exists(self.state_file):
                with open(self.state_file, 'r') as f:
                    state = json.load(f)
                    self.pending_containers = state.get('pending_containers', {})
                    self.stats = state.get('stats', {
                        'successful_posts': 0,
                        'failed_posts': 0,
                        'rate_limited_posts': 0
                    })
                    logger.info(f"Loaded {len(self.pending_containers)} pending containers from state file")
        except Exception as e:
            logger.error(f"Error loading state: {e}")
            self.pending_containers = {}
            self.stats = {
                'successful_posts': 0,
                'failed_posts': 0,
                'rate_limited_posts': 0
            }

    def _save_state(self):
        """Save current state to file"""
        try:
            state = {
                'pending_containers': self.pending_containers,
                'stats': self.stats,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.state_file, 'w') as f:
                json.dump(state, f, indent=2)
            logger.info(f"Saved state with {len(self.pending_containers)} pending containers")
        except Exception as e:

... (truncado após 80 linhas)

```

### src/instagram/carousel_poster.py (15.56 KB)

```python
# src/instagram/carousel_poster.py

import os
import time
import logging
import mimetypes
from typing import List, Tuple, Callable, Dict, Optional
from dotenv import load_dotenv
from src.instagram.instagram_carousel_service import InstagramCarouselService, RateLimitError
from src.instagram.image_uploader import ImageUploader  # Para upload das imagens

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# --- Exceções Personalizadas (Opcional, mas recomendado) ---
class CarouselError(Exception):
    """Base class for carousel-related errors."""
    def __init__(self, message, error_code=None, error_subcode=None, fb_trace_id=None, is_retriable=False):
        super().__init__(message)
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fb_trace_id = fb_trace_id
        self.is_retriable = is_retriable
    
    def __str__(self):
        details = []
        if self.error_code:
            details.append(f"Code: {self.error_code}")
        if self.error_subcode:
            details.append(f"Subcode: {self.error_subcode}")
        if self.fb_trace_id:
            details.append(f"FB Trace ID: {self.fb_trace_id}")
        
        if details:
            return f"{super().__str__()} ({', '.join(details)})"
        return super().__str__()

class AuthenticationError(CarouselError):
    """Raised when there's an issue with authentication (codes 102, 190, etc)."""

class PermissionError(CarouselError):
    """Raised when there's an issue with permissions (codes 10, 200, 203, etc)."""

class ThrottlingError(CarouselError):
    """Raised when API rate limits are hit (codes 4, 17, 32, 613, etc)."""
    def __init__(self, message, error_code=None, error_subcode=None, fb_trace_id=None, retry_after=None):
        super().__init__(message, error_code, error_subcode, fb_trace_id, True)
        self.retry_after = retry_after  # Default to 5 minutes if not specified

class ImageValidationError(CarouselError):
    """Raised when an image fails validation."""

class ImageUploadError(CarouselError):
    """Raised when an image fails to upload."""

class CarouselCreationError(CarouselError):
    """Raised when the carousel container fails to be created."""

class CarouselPublishError(CarouselError):
    """Raised when the carousel fails to publish."""

class ServerError(CarouselError):
    """Raised when Instagram/Facebook server errors occur (codes 1, 2, etc)."""
    def __init__(self, message, error_code=None, error_subcode=None, fb_trace_id=None):
        super().__init__(message, error_code, error_subcode, fb_trace_id, True)  # Server errors are generally retriable
# --- Fim das Exceções ---

def validate_carousel_images(image_paths: List[str], validator_func: Callable[[str], bool]) -> Tuple[List[str], List[str]]:
    """Valida uma lista de imagens para o carrossel.

    Args:
        image_paths: Uma lista de caminhos de arquivos de imagem.
        validator_func: Uma função que valida um único arquivo de imagem.

    Returns:
        Uma tupla contendo duas listas: (imagens válidas, imagens inválidas).
    """

... (truncado após 80 linhas)

```

### src/instagram/carousel_normalizer.py (14.89 KB)

```python
import os
import time
import logging
import tempfile
from typing import List, Tuple, Optional, Dict
from PIL import Image, UnidentifiedImageError
import numpy as np

logger = logging.getLogger('CarouselNormalizer')

class CarouselNormalizer:
    """
    Utility class to normalize images for Instagram carousels.
    Instagram requires all images in a carousel to have the same aspect ratio.
    """
    
    # Instagram recommended aspect ratios
    RECOMMENDED_RATIOS = {
        'square': 1.0,         # 1:1
        'portrait': 0.8,       # 4:5
        'landscape': 1.91      # 1.91:1
    }
    
    # Instagram's supported aspect ratio range
    MIN_ASPECT_RATIO = 0.8     # 4:5 portrait (width/height)
    MAX_ASPECT_RATIO = 1.91    # 1.91:1 landscape
    
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
    
    @staticmethod
    def get_image_info(image_path: str) -> Dict:
        """Get detailed information about an image"""
        if not os.path.exists(image_path):
            logger.error(f"Image file not found: {image_path}")
            return {}
            
        try:
            with Image.open(image_path) as img:
                file_size = os.path.getsize(image_path)
                file_size_mb = file_size / (1024 * 1024)
                width, height = img.size
                aspect_ratio = round(width / height, 3)
                
                return {
                    'path': image_path,
                    'format': img.format,
                    'mode': img.mode,
                    'width': width,
                    'height': height,
                    'aspect_ratio': aspect_ratio,
                    'file_size': file_size,
                    'file_size_mb': round(file_size_mb, 2)
                }
        except UnidentifiedImageError:
            logger.error(f"Could not identify image file: {image_path}")

... (truncado após 80 linhas)

```

### src/instagram/instagram_reels_publisher.py (14.08 KB)

```python
"""
Módulo especializado para publicação de Reels no Instagram
Implementado com base nos exemplos oficiais da Meta para publicação de Reels
Fonte: https://github.com/fbsamples/reels_publishing_apis

Este módulo implementa as melhores práticas e parâmetros específicos
para a publicação de Reels no Instagram.
"""

import os
import time
import json
import logging
import random
from datetime import datetime
from dotenv import load_dotenv
from imgurpython import ImgurClient
from moviepy.editor import VideoFileClip
from src.instagram.base_instagram_service import (
    BaseInstagramService, AuthenticationError, PermissionError, 
    RateLimitError, MediaError, TemporaryServerError, InstagramAPIError
)

logger = logging.getLogger('ReelsPublisher')

class ReelsPublisher(BaseInstagramService):
    """
    Classe especializada para publicação de Reels no Instagram.
    Implementa o fluxo completo de publicação conforme documentação oficial da Meta.
    """
    
    REELS_CONFIG = {
        'aspect_ratio': '9:16',     # Proporção de aspecto padrão para Reels (vertical)
        'min_duration': 3,          # Duração mínima em segundos
        'max_duration': 90,         # Duração máxima em segundos
        'recommended_duration': 30,  # Duração recomendada pela Meta
        'min_width': 500,           # Largura mínima em pixels
        'recommended_width': 1080,  # Largura recomendada em pixels
        'recommended_height': 1920, # Altura recomendada em pixels
        'video_formats': ['mp4'],   # Formatos suportados
        'video_codecs': ['h264'],   # Codecs de vídeo recomendados
        'audio_codecs': ['aac'],    # Codecs de áudio recomendados
    }
    
    REELS_ERROR_CODES = {
        2207026: "Formato de vídeo não suportado para Reels",
        2207014: "Duração de vídeo não compatível com Reels",
        2207013: "Proporção de aspecto do vídeo não é compatível com Reels",
        9007: "Permissão de publicação de Reels negada",
    }

    def __init__(self, access_token=None, ig_user_id=None):
        load_dotenv()
        access_token = access_token or (
            os.getenv('INSTAGRAM_API_KEY') or
            os.getenv('INSTAGRAM_ACCESS_TOKEN') or
            os.getenv('FACEBOOK_ACCESS_TOKEN')
        )
        ig_user_id = ig_user_id or os.getenv("INSTAGRAM_ACCOUNT_ID")
        
        if not access_token or not ig_user_id:
            raise ValueError(
                "Credenciais incompletas. Defina INSTAGRAM_ACCESS_TOKEN e "
                "INSTAGRAM_ACCOUNT_ID nas variáveis de ambiente ou forneça-os diretamente."
            )
            
        super().__init__(access_token, ig_user_id)

    def create_reels_container(self, video_url, caption, share_to_feed=True,
                             audio_name=None, thumbnail_url=None, user_tags=None):
        """Cria um container para Reels."""
        params = {
            'media_type': 'REELS',
            'video_url': video_url,
            'caption': caption,
            'share_to_feed': 'true' if share_to_feed else 'false'
        }
        
        if audio_name:
            params['audio_name'] = audio_name

... (truncado após 80 linhas)

```


## 📂 Lista Completa de Arquivos

- `src/instagram/moldura.png` (263.71 KB)
- `src/instagram/code_light.txt` (136.93 KB)
- `src/services/instagram_send.py` (35.08 KB)
- `app.py` (34.81 KB)
- `src/instagram/instagram_carousel_service.py` (27.70 KB)
- `src/instagram/instagram_video_processor.py` (25.69 KB)
- `streamlit_app.py` (21.68 KB)
- `src/instagram/image_validator.py` (17.15 KB)
- `src/instagram/instagram_post_service.py` (16.01 KB)
- `src/instagram/carousel_poster.py` (15.56 KB)
- `src/instagram/carousel_normalizer.py` (14.89 KB)
- `src/instagram/instagram_reels_publisher.py` (14.08 KB)
- `src/services/post_queue.py` (13.72 KB)
- `src/instagram/base_instagram_service.py` (13.18 KB)
- `src/instagram/crew_post_instagram.py` (11.06 KB)
- `src/services/message.py` (9.49 KB)
- `src/instagram/debug_carousel.py` (8.69 KB)
- `src/handlers/app.py` (8.45 KB)
- `assets/moldura.png` (8.31 KB)
- `src/instagram/video_processor.py` (8.00 KB)
- `src/instagram/image_uploader.py` (7.81 KB)
- `src/handlers/code_light.txt` (7.50 KB)
- `docs/troubleshooting/common.md` (6.72 KB)
- `src/utils/cleanup_utility.py` (6.28 KB)
- `.DS_Store` (6.00 KB)
- `docs/api/README.md` (5.72 KB)
- `src/agent_social_media.egg-info/PKG-INFO` (5.52 KB)
- `docs/guides/setup.md` (4.85 KB)
- `src/utils/code_light.txt` (4.67 KB)
- `src/services/send.py` (4.65 KB)
- `src/instagram/instagram_video_uploader.py` (4.42 KB)
- `src/instagram/instagram_post_publisher.py` (4.41 KB)
- `README.md` (4.32 KB)
- `docs/guides/media_validation.md` (4.26 KB)
- `monitor.py` (4.20 KB)
- `docs/troubleshooting/instagram.md` (4.14 KB)
- `src/services/post_notification.py` (3.94 KB)
- `docs/index.md` (3.61 KB)
- `src/instagram/describe_carousel_tool.py` (2.97 KB)
- `src/instagram/filter.py` (2.96 KB)
- `tests/code_light.txt` (2.82 KB)
- `src/instagram/describe_image_tool.py` (2.67 KB)
- `src/utils/video_decode_save.py` (2.64 KB)
- `monitoring_templates/dashboard.html` (2.54 KB)
- `src/instagram/describe_video_tool.py` (2.54 KB)
- `copy_md_to_txt.py` (2.51 KB)
- `copy_py_to_txt.py` (2.49 KB)
- `src/instagram/border.py` (2.39 KB)
- `src/instagram/exceptions.py` (2.07 KB)
- `tests/test_carousel.py` (2.01 KB)

---
*Relatório gerado automaticamente para análise CrewAI*

**IMPORTANTE:** Este relatório contém código real do projeto. A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.
