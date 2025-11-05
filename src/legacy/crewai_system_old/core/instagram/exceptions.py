"""
Definição de exceções personalizadas para erros relacionados à integração com o Instagram.

Classes:
    InstagramError:
        Classe base para todas as exceções relacionadas ao Instagram.
        Permite armazenar código de erro, subcódigo e ID de rastreamento do Facebook.

    AuthenticationError:
        Exceção para falhas de autenticação (token expirado, inválido, etc).

    PermissionError:
        Exceção para erros relacionados a permissões (escopos ausentes, etc).

    RateLimitError:
        Exceção lançada quando os limites de requisição da API são excedidos.
        Permite definir o tempo de espera para nova tentativa.

    MediaError:
        Exceção para erros relacionados a mídia (formato, tamanho, falhas de upload).

    TemporaryServerError:
        Exceção para erros temporários do servidor do Instagram que podem ser reprocessados.

    CarouselError:
        Classe base para erros relacionados a carrosséis.
        Permite indicar se o erro é passível de nova tentativa.

    ValidationError:
        Exceção lançada quando há falha na validação de mídia ou dados.

    ConfigurationError:
        Exceção para erros de configuração (credenciais ausentes, etc).

"""


class InstagramError(Exception):
    """Base exception class for all Instagram-related errors."""

    def __init__(self, message, error_code=None, error_subcode=None, fbtrace_id=None):
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)

    def __str__(self):
        base_message = super().__str__()
        if self.error_code or self.error_subcode or self.fbtrace_id:
            return f"{base_message} (Code: {self.error_code}, Subcode: {self.error_subcode}, Trace ID: {self.fbtrace_id})"
        return base_message


class AuthenticationError(InstagramError):
    """Raised for authentication failures (token expired, invalid, etc)."""

    pass


class PermissionError(InstagramError):
    """Raised for permission-related errors (missing scopes, etc)."""

    pass


class RateLimitError(InstagramError):
    """Raised when API rate limits are exceeded."""

    def __init__(
        self,
        message,
        retry_seconds=300,
        error_code=None,
        error_subcode=None,
        fbtrace_id=None,
    ):
        super().__init__(message, error_code, error_subcode, fbtrace_id)
        self.retry_seconds = retry_seconds


class MediaError(InstagramError):
    """Raised for media-related errors (format, size, upload failures)."""

    pass


class TemporaryServerError(InstagramError):
    """Raised for temporary Instagram server errors that may be retried."""

    pass


class CarouselError(InstagramError):
    """Base class for carousel-related errors."""

    def __init__(
        self,
        message,
        error_code=None,
        error_subcode=None,
        fbtrace_id=None,
        retriable=False,
    ):
        super().__init__(message, error_code, error_subcode, fbtrace_id)
        self.retriable = retriable


class ValidationError(InstagramError):
    """Raised when media or data validation fails."""

    pass


class ConfigurationError(InstagramError):
    """Raised for configuration-related errors (missing credentials, etc)."""

    pass
