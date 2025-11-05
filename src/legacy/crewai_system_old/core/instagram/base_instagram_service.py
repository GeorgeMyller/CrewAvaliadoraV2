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



import time
import json
import logging
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import random

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


class MediaError(Exception):
    """Raised when there are issues with the media"""

    def __init__(self, message, error_code=None, error_subcode=None, fbtrace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)


class TemporaryServerError(Exception):
    """Raised for temporary server issues"""

    def __init__(self, message, error_code=None, error_subcode=None, fbtrace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)


class InstagramAPIError(Exception):
    """Base class for Instagram API errors"""

    def __init__(self, message, error_code=None, error_subcode=None, fbtrace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)


class RateLimitHandler:
    """Handles rate limiting with exponential backoff"""

    INITIAL_DELAY = 5  # Initial delay in seconds (increased from 2)
    MAX_DELAY = 3600  # Maximum delay in seconds (1 hour)
    MAX_ATTEMPTS = 5  # Maximum retry attempts
    RATE_LIMIT_CODES = [4, 17, 32, 613]  # Extended list of rate limit error codes
    RATE_LIMIT_SUBCODES = [2207051]  # Specific subcode for application request limit

    @classmethod
    def is_rate_limit_error(cls, error_code, error_subcode=None):
        """Check if an error is related to rate limiting"""
        if error_code in cls.RATE_LIMIT_CODES:
            if error_subcode is None or error_subcode in cls.RATE_LIMIT_SUBCODES:
                return True
        return False

    @classmethod
    def calculate_backoff_time(cls, attempt, base_delay=None):
        """Calculate backoff time with jitter"""
        if base_delay is None:
            base_delay = cls.INITIAL_DELAY

        # For application request limit (subcode 2207051), use longer delays
        if attempt == 0:
            delay = 300  # Start with 5 minutes for first attempt
        else:
            delay = min(cls.MAX_DELAY, base_delay * (2**attempt))

        # Add jitter (±25%) to avoid thundering herd problem
        jitter = random.uniform(0.75, 1.25)
        return delay * jitter


class BaseInstagramService:
    """Base class for Instagram API services with common functionality"""

    API_VERSION = "v23.0"  # Atualizado para Graph API v23.0 (https://developers.facebook.com/docs/instagram-platform/changelog)
    base_url = f"https://graph.facebook.com/{API_VERSION}"
    min_request_interval = 1  # Minimum seconds between requests

    def __init__(self, access_token, ig_user_id):
        """Initialize with access token and Instagram user ID"""
        self.access_token = access_token
        self.ig_user_id = ig_user_id
        self.last_request_time = 0
        self.rate_limit_window = {}

        # Configure session with retries
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,  # Number of retries for failed requests
            backoff_factor=0.5,  # Factor to apply between attempts
            status_forcelist=[500, 502, 503, 504],  # HTTP status codes to retry on
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def _make_request(
        self, method, endpoint, params=None, data=None, headers=None, retry_attempt=0
    ):
        """Make an API request with enhanced rate limiting and error handling"""
        url = f"{self.base_url}/{endpoint}"

        # Add access token to params
        if params is None:
            params = {}
        params["access_token"] = self.access_token

        # Respect rate limits with minimum interval between requests
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        if elapsed < self.min_request_interval:
            time.sleep(self.min_request_interval - elapsed)

        try:
            logger.info(f"Making {method} request to {endpoint}")
            if data:
                logger.info(f"With data: {data}")

            response = self.session.request(
                method, url, params=params, data=data, headers=headers
            )
            self.last_request_time = time.time()

            # Process rate limit headers if present
            if "x-business-use-case-usage" in response.headers:
                self._process_rate_limit_headers(response.headers)

            # Log response status
            logger.info(f"Response status: {response.status_code}")

            if response.status_code == 403:
                try:
                    error_json = response.json()
                    if "error" in error_json:
                        error = error_json["error"]
                        error_code = error.get("code")
                        error_subcode = error.get("error_subcode")
                        error_message = error.get("message", "")
                        fb_trace_id = error.get("fbtrace_id")

                        logger.error(
                            f"{error_code} {error_message} (Subcode: {error_subcode})"
                        )

                        # Handle application request limit specifically
                        if error_subcode == 2207051:
                            retry_seconds = 300  # Start with 5 minutes
                            if retry_attempt < RateLimitHandler.MAX_ATTEMPTS:
                                backoff_time = RateLimitHandler.calculate_backoff_time(
                                    retry_attempt, retry_seconds
                                )
                                logger.warning(
                                    f"Application request limit reached. Backing off for {backoff_time:.2f} seconds. Attempt {retry_attempt+1}/{RateLimitHandler.MAX_ATTEMPTS}"
                                )
                                time.sleep(backoff_time)
                                return self._make_request(
                                    method,
                                    endpoint,
                                    params,
                                    data,
                                    headers,
                                    retry_attempt + 1,
                                )
                        else:
                            retry_seconds = (
                                300  # Default retry_seconds if not set above
                            )

                        raise RateLimitError(
                            error_message,
                            retry_seconds,
                            error_code,
                            error_subcode,
                            fb_trace_id,
                        )

                except ValueError:
                    raise InstagramAPIError("Failed to parse error response")

            response.raise_for_status()
            result = response.json() if response.content else None

            if result and "error" in result:
                error = result["error"]
                error_code = error.get("code")
                error_message = error.get("message", "")
                error_subcode = error.get("error_subcode")
                fb_trace_id = error.get("fbtrace_id")

                if error_code in [190, 104]:  # Token errors
                    raise AuthenticationError(
                        error_message, error_code, error_subcode, fb_trace_id
                    )
                elif error_code in [200, 10, 803]:  # Permission errors
                    raise PermissionError(
                        error_message, error_code, error_subcode, fb_trace_id
                    )
                elif RateLimitHandler.is_rate_limit_error(error_code, error_subcode):
                    retry_seconds = self._get_retry_after(error)
                    if retry_attempt < RateLimitHandler.MAX_ATTEMPTS:
                        backoff_time = RateLimitHandler.calculate_backoff_time(
                            retry_attempt, retry_seconds
                        )
                        logger.warning(
                            f"Rate limit hit. Backing off for {backoff_time:.2f} seconds. Attempt {retry_attempt+1}/{RateLimitHandler.MAX_ATTEMPTS}"
                        )
                        time.sleep(backoff_time)
                        return self._make_request(
                            method, endpoint, params, data, headers, retry_attempt + 1
                        )
                    raise RateLimitError(
                        error_message,
                        retry_seconds,
                        error_code,
                        error_subcode,
                        fb_trace_id,
                    )
                elif error_code in [1, 2]:  # Temporary server errors
                    raise TemporaryServerError(
                        error_message, error_code, error_subcode, fb_trace_id
                    )
                else:
                    raise InstagramAPIError(
                        error_message, error_code, error_subcode, fb_trace_id
                    )

            return result

        except requests.exceptions.RequestException as e:
            # Tentar obter mais detalhes do erro da resposta
            error_details = f"Request failed: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_response = e.response.json()
                    if 'error' in error_response:
                        error_info = error_response['error']
                        error_message = error_info.get('message', 'Unknown error')
                        error_code = error_info.get('code', 'Unknown code')
                        error_subcode = error_info.get('error_subcode', 'No subcode')
                        error_details = f"Instagram API Error - Code: {error_code}, Subcode: {error_subcode}, Message: {error_message}"
                        logger.error(f"Detailed API error: {error_details}")
                except Exception as parse_error:
                    logger.error(f"Could not parse error response: {e.response.text} - Parse error: {parse_error}")
            
            logger.error(error_details)
            raise InstagramAPIError(error_details)

    def _process_rate_limit_headers(self, headers):
        """Process rate limit information from response headers"""
        usage_header = headers.get("x-business-use-case-usage")
        if usage_header:
            try:
                usage_data = json.loads(usage_header)
                for app_id, metrics in usage_data.items():
                    if isinstance(metrics, list) and metrics:
                        rate_data = metrics[0]
                        if "estimated_time_to_regain_access" in rate_data:
                            self.rate_limit_window[app_id] = (
                                time.time()
                                + rate_data["estimated_time_to_regain_access"]
                            )
            except json.JSONDecodeError:
                logger.warning("Failed to parse rate limit headers")

    def _get_retry_after(self, error):
        """Extract retry after time from error response"""
        # Default retry time increased to 5 minutes for application request limit
        retry_seconds = 300

        # Check for specific error subcodes
        if error.get("error_subcode") == 2207051:  # Application request limit
            retry_seconds = 900  # 15 minutes

        # Try to extract time from error message
        message = error.get("message", "").lower()
        if "minutes" in message:
            try:
                import re

                time_match = re.search(r"(\d+)\s*minutes?", message)
                if time_match:
                    retry_seconds = int(time_match.group(1)) * 60
            except Exception as e:
                logger.warning(f"Failed to extract retry time from error message: {e}")
                pass

        return retry_seconds

    def check_token_permissions(self):
        """Check if the access token has the necessary permissions"""
        try:
            response = self._make_request(
                "GET", "debug_token", params={"input_token": self.access_token}
            )
            if not response or "data" not in response:
                return False, ["Unable to verify token"]

            token_data = response["data"]
            if not token_data.get("is_valid", False):
                return False, ["Token is invalid or expired"]

            scopes = set(token_data.get("scopes", []) or [])

            # Two possible permission sets depending on login type
            # Facebook Login for Instagram Graph API
            fb_login_required = {"instagram_basic", "instagram_content_publishing"}
            # Instagram Login (Business)
            ig_login_required = {
                "instagram_business_basic",
                "instagram_business_content_publishing",
            }

            has_fb_set = fb_login_required.issubset(scopes)
            has_ig_set = ig_login_required.issubset(scopes)

            if has_fb_set or has_ig_set:
                return True, []

            # Report the closest missing set to guide configuration
            missing_fb = sorted(list(fb_login_required - scopes))
            missing_ig = sorted(list(ig_login_required - scopes))
            missing = missing_fb if len(missing_fb) <= len(missing_ig) else missing_ig

            return False, missing

        except Exception as e:
            logger.error(f"Error checking token permissions: {e}")
            return False, [str(e)]

    def get_app_usage_info(self):
        """Get current app usage and rate limit information"""
        try:
            result = requests.get(
                f"{self.base_url}/me",
                params={
                    "access_token": self.access_token,
                    "debug": "all",
                    "fields": "id,name",
                },
                timeout=30
            )

            headers = result.headers
            debug_info = result.json().get("__debug", {})

            usage_info = {
                "app_usage": debug_info.get("app_usage", {}),
                "page_usage": debug_info.get("page_usage", {}),
                "headers": {
                    "x-app-usage": headers.get("x-app-usage"),
                    "x-ad-account-usage": headers.get("x-ad-account-usage"),
                    "x-business-use-case-usage": headers.get(
                        "x-business-use-case-usage"
                    ),
                    "x-fb-api-version": headers.get("facebook-api-version"),
                },
            }

            return usage_info
        except Exception as e:
            logging.error(f"Error getting usage info: {str(e)}")
            return {"error": str(e)}

    def debug_token(self):
        """Return debug information for the current access token (wrapper around debug_token endpoint)."""
        try:
            return self._make_request(
                "GET", "debug_token", params={"input_token": self.access_token}
            )
        except Exception as e:
            logger.error(f"Error debugging token: {e}")
            raise

    def post_story(self, media_url: str, media_type: str = "IMAGE"):
        """
        Publica uma mídia como uma História no Instagram.

        Args:
            media_url (str): A URL pública da imagem (JPEG) ou vídeo.
            media_type (str): O tipo de mídia, 'IMAGE' ou 'VIDEO'.

        Returns:
            dict: A resposta da API após a publicação.
        """
        logger.info(f"Iniciando publicação de Story com a mídia: {media_url}")

        # Etapa 1: Criar contêiner de mídia para a História
        container_params = {
            "media_type": "STORIES",
        }
        if media_type.upper() == "IMAGE":
            container_params["image_url"] = media_url
        elif media_type.upper() == "VIDEO":
            container_params["video_url"] = media_url
        else:
            raise ValueError("media_type deve ser 'IMAGE' ou 'VIDEO'")

        try:
            container_response = self._make_request(
                "POST", f"{self.ig_user_id}/media", data=container_params
            )
            container_id = container_response.get("id")
            if not container_id:
                raise InstagramAPIError("Falha ao criar o contêiner de mídia para o Story.")
            logger.info(f"Contêiner de Story criado com ID: {container_id}")

            # Etapa 2: Verificar o status do contêiner
            if not self._check_container_status(container_id):
                raise MediaError("O contêiner do Story não ficou pronto a tempo.")

            # Etapa 3: Publicar o contêiner
            publish_response = self._make_request(
                "POST", f"{self.ig_user_id}/media_publish", data={"creation_id": container_id}
            )
            logger.info("Story publicado com sucesso!")
            return publish_response

        except (InstagramAPIError, MediaError) as e:
            logger.error(f"Erro ao publicar o Story: {e}")
            raise

    def _check_container_status(self, container_id: str, timeout: int = 300, check_interval: int = 5) -> bool:
        """
        Verifica o status de um contêiner de mídia até que esteja pronto ou o tempo limite seja atingido.

        Args:
            container_id (str): O ID do contêiner de mídia.
            timeout (int): Tempo máximo de espera em segundos.
            check_interval (int): Intervalo entre as verificações em segundos.

        Returns:
            bool: True se o contêiner estiver pronto, False caso contrário.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                status_response = self._make_request("GET", container_id, params={"fields": "status_code"})
                status_code = status_response.get("status_code")
                logger.info(f"Status do contêiner {container_id}: {status_code}")

                if status_code == "FINISHED":
                    return True
                elif status_code in ["ERROR", "EXPIRED"]:
                    logger.error(f"Falha no processamento do contêiner {container_id} com status: {status_code}")
                    return False
                
                time.sleep(check_interval)

            except InstagramAPIError as e:
                logger.error(f"Erro ao verificar o status do contêiner {container_id}: {e}")
                # Se o erro for grave, pode ser melhor interromper
                return False
        
        logger.warning(f"Tempo limite de {timeout}s atingido para o contêiner {container_id}.")
        return False


# Exemplo de uso
if __name__ == "__main__":
    # Substitua com seu token de acesso e ID de usuário do Instagram
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    IG_USER_ID = "YOUR_IG_USER_ID"

    # Inicialize o serviço
    instagram_service = BaseInstagramService(ACCESS_TOKEN, IG_USER_ID)

    # Verifique as permissões do token
    is_valid, missing_permissions = instagram_service.check_token_permissions()
    if is_valid:
        print("Token has all required permissions.")
    else:
        print(f"Token is missing permissions: {missing_permissions}")

    # Obtenha informações de uso do aplicativo
    usage_info = instagram_service.get_app_usage_info()
    print("App Usage Info:", json.dumps(usage_info, indent=2))
