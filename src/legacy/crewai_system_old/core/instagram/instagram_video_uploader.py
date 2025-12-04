"""
Módulo para validação e upload de vídeos para Instagram Reels via Imgur.
Classes:
    VideoUploader:
        Classe responsável por validar vídeos conforme os requisitos do Instagram Reels,
        realizar upload para o Imgur e excluir vídeos enviados.
        Métodos:
            __init__():
                Inicializa o cliente Imgur usando variáveis de ambiente.
            validate_video(video_path: str) -> Tuple[bool, str]:
                Valida o vídeo informado de acordo com os requisitos de duração, formato,
                dimensões e proporção de aspecto do Instagram Reels.
                Retorna uma tupla indicando se o vídeo é válido e uma mensagem explicativa.
            upload_video(video_path: str) -> Optional[dict]:
                Realiza o upload do vídeo para o Imgur após validação.
                Retorna um dicionário com informações do upload (incluindo URL) ou None em caso de erro.
            delete_video(delete_hash: str) -> bool:
                Exclui um vídeo do Imgur utilizando o hash de exclusão.
                Retorna True se a exclusão for bem-sucedida, False caso contrário.

"""

import logging
import os

import moviepy.editor as mp
from dotenv import load_dotenv
from imgurpython import ImgurClient

logger = logging.getLogger(__name__)


class VideoUploader:
    """
    Class for handling video uploads and validation for Instagram Reels.
    """

    REELS_CONFIG = {
        "aspect_ratio": "9:16",  # Proporção de aspecto padrão para Reels (vertical)
        "min_duration": 3,  # Duração mínima em segundos
        "max_duration": 90,  # Duração máxima em segundos
        "recommended_duration": 30,  # Duração recomendada pela Meta
        "min_width": 300,  # Largura mínima em pixels (reduzida para aceitar vídeos do WhatsApp)
        "recommended_width": 1080,  # Largura recomendada em pixels
        "recommended_height": 1920,  # Altura recomendada em pixels
        "video_formats": ["mp4"],  # Formatos suportados
        "video_codecs": ["h264"],  # Codecs de vídeo recomendados
        "audio_codecs": ["aac"],  # Codecs de áudio recomendados
    }

    def __init__(self):
        """Initialize with Imgur client."""
        load_dotenv()
        self.imgur_client = ImgurClient(
            os.getenv("IMGUR_CLIENT_ID"), os.getenv("IMGUR_CLIENT_SECRET")
        )

    def validate_video(self, video_path: str) -> tuple[bool, str]:
        """
        Validates video against Instagram Reels requirements.

        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        try:
            if not os.path.exists(video_path):
                return False, "Video file not found"

            if not video_path.lower().endswith((".mp4", ".mov", ".avi")):
                return False, "Unsupported video format"

            video = mp.VideoFileClip(video_path)

            # Check duration
            duration = video.duration
            if duration < self.REELS_CONFIG["min_duration"]:
                return (
                    False,
                    f"Video too short ({duration}s). Minimum duration is {self.REELS_CONFIG['min_duration']}s",
                )
            if duration > self.REELS_CONFIG["max_duration"]:
                return (
                    False,
                    f"Video too long ({duration}s). Maximum duration is {self.REELS_CONFIG['max_duration']}s",
                )

            # Check dimensions and aspect ratio
            width, height = video.size
            if width < self.REELS_CONFIG["min_width"]:
                return (
                    False,
                    f"Video width too small ({width}px). Minimum width is {self.REELS_CONFIG['min_width']}px",
                )

            # Aspect ratio check more flexible - accept both portrait and landscape
            aspect_ratio = height / width
            is_portrait = aspect_ratio > 1.0  # Height > Width (portrait)
            is_landscape = aspect_ratio < 1.0  # Width > Height (landscape)
            is_square = abs(aspect_ratio - 1.0) < 0.1  # Approximately square

            # Accept portrait (preferred), square, or not too wide landscape videos
            if not (is_portrait or is_square or (is_landscape and aspect_ratio > 0.5)):
                return (
                    False,
                    f"Video aspect ratio too extreme ({width}x{height}). Use portrait, square, or moderately wide videos",
                )

            # Close the video to free resources
            video.close()

            return True, "Video meets all requirements"

        except Exception as e:
            logger.error(f"Error validating video: {str(e)}")
            return False, f"Error validating video: {str(e)}"

    def upload_video(self, video_path: str) -> dict | None:
        """
        Uploads video to Imgur.

        Returns:
            Optional[dict]: Upload response with URL if successful
        """
        try:
            # First validate the video
            is_valid, message = self.validate_video(video_path)
            if not is_valid:
                logger.error(f"Video validation failed: {message}")
                return None

            logger.info(f"Uploading video to Imgur: {video_path}")
            response = self.imgur_client.upload_from_path(video_path)

            if not response or "link" not in response:
                logger.error("Failed to get upload URL from Imgur")
                return None

            logger.info(f"Video uploaded successfully. URL: {response['link']}")
            return response

        except Exception as e:
            logger.error(f"Error uploading video: {str(e)}")
            return None

    def delete_video(self, delete_hash: str) -> bool:
        """
        Deletes a video from Imgur using its delete hash.

        Returns:
            bool: True if deletion was successful
        """
        try:
            if not delete_hash:
                return False

            logger.info(f"Deleting video with hash: {delete_hash}")
            return bool(self.imgur_client.delete_image(delete_hash))

        except Exception as e:
            logger.error(f"Error deleting video: {str(e)}")
            return False
