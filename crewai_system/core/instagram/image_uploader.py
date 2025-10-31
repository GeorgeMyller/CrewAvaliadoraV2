""" 
Módulo para upload e deleção de imagens no Imgur.

Classes:
    ImageUploader:
        Classe responsável por realizar o upload de imagens (a partir de caminho de arquivo ou string Base64) e deletar imagens no Imgur utilizando as credenciais da API.

Métodos:
    __init__(client_id: str, client_secret: str):

    _validate_response(response):
        Valida a resposta do upload do Imgur, garantindo que os campos obrigatórios estejam presentes e não vazios.

    upload_from_path(image_path: str) -> dict:
        Realiza o upload de uma imagem localizada no sistema de arquivos para o Imgur.
        Retorna um dicionário com id, url e deletehash da imagem enviada.

    upload_from_base64(image_base64: str) -> dict:
        Realiza o upload de uma imagem fornecida como string Base64 para o Imgur.
        Retorna um dicionário com id, url e deletehash da imagem enviada.

    delete_image(deletehash: str) -> bool:
        Deleta uma imagem no Imgur utilizando o deletehash.
        Retorna True se a imagem foi deletada com sucesso, False caso contrário.

Exceções:
    ValueError: Credenciais ausentes ou resposta inválida do Imgur.
    FileNotFoundError: Arquivo de imagem não encontrado.
    ImgurClientError: Erros específicos da API do Imgur.
    Exception: Outros erros inesperados durante upload ou deleção.

Dependências:
    - os, io, time, base64, tempfile, logging, sys
    - PIL (Pillow)
    - dotenv
    - imgurpython

Uso:
    Instancie ImageUploader com client_id e client_secret do Imgur.
    Utilize os métodos para upload e deleção de imagens conforme necessário.

"""

import os
import io
import time
import base64
from PIL import Image
import logging

# sys.path manipulations are unnecessary in a properly packaged project; keep imports clean.

import tempfile
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from typing import Dict


class ImageUploader:
    def __init__(self, client_id: str, client_secret: str):
        """
        Inicializa o cliente Imgur com as credenciais fornecidas.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.max_retries = 3
        self.retry_delay = 2  # seconds

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "As credenciais do Imgur (client_id, client_secret) são obrigatórias."
            )

        self.client = ImgurClient(self.client_id, self.client_secret)
        self.logger = logging.getLogger(self.__class__.__name__)

    def _validate_response(self, response):
        """
        Validates the upload response from Imgur
        """
        required_fields = ["id", "link", "deletehash"]
        for field in required_fields:
            if field not in response:
                raise ValueError(
                    f"Campo obrigatório '{field}' não encontrado na resposta do Imgur"
                )
            if not response[field]:
                raise ValueError(f"Campo '{field}' está vazio na resposta do Imgur")

    def upload_from_path(self, image_path: str) -> Dict[str, str]:
        """
        Faz o upload de uma imagem localizada no sistema de arquivos.

        :param image_path: Caminho absoluto da imagem a ser enviada.
        :return: Dicionário contendo id, url, e deletehash da imagem enviada.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"O arquivo especificado não foi encontrado: {image_path}"
            )

        retry_count = 0
        while retry_count < self.max_retries:
            try:
                uploaded_image = self.client.upload_from_path(
                    image_path, config=None, anon=True
                )

                # Validar resposta
                self._validate_response(uploaded_image)

                # Log do deletehash para debug
                self.logger.info(
                    f"Upload bem sucedido. ID: {uploaded_image['id']}, Deletehash: {uploaded_image['deletehash']}"
                )

                return {
                    "id": uploaded_image["id"],
                    "url": uploaded_image["link"],
                    "deletehash": uploaded_image["deletehash"],
                    "image_path": image_path,
                }
            except ImgurClientError as e:
                self.logger.warning(
                    f"Erro do cliente Imgur durante upload (tentativa {retry_count + 1}/{self.max_retries}): {str(e)}"
                )
                retry_count += 1
                if retry_count < self.max_retries:
                    self.logger.info(
                        f"Tentando novamente em {self.retry_delay} segundos..."
                    )
                    time.sleep(self.retry_delay * retry_count)  # Exponential backoff
                else:
                    self.logger.error(
                        f"Falha após {self.max_retries} tentativas. Último erro: {e}"
                    )
                    raise
            except Exception as e:
                self.logger.error(
                    f"Erro inesperado durante upload (tentativa {retry_count + 1}/{self.max_retries}): {str(e)}"
                )
                retry_count += 1
                if retry_count < self.max_retries:
                    self.logger.info(
                        f"Tentando novamente em {self.retry_delay} segundos..."
                    )
                    time.sleep(self.retry_delay * retry_count)  # Exponential backoff
                else:
                    self.logger.error(
                        f"Falha após {self.max_retries} tentativas. Último erro: {e}"
                    )
                    raise
        # Se o loop terminar sem sucesso (sem raise), considerar como falha
        raise RuntimeError("Limite de tentativas excedido ao enviar imagem ao Imgur")

    def upload_from_base64(self, image_base64: str) -> Dict[str, str]:
        """
        Faz o upload de uma imagem fornecida como string Base64.

        :param image_base64: String contendo os dados da imagem em Base64.
        :return: Dicionário contendo id, url, e deletehash da imagem enviada.
        """
        try:
            # Decodificar Base64 para bytes
            image_data = base64.b64decode(image_base64)

            # Abrir a imagem em memória para verificar a qualidade
            image = Image.open(io.BytesIO(image_data))

            # Salvar a imagem como PNG sem compressão em um arquivo temporário
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
                image.save(temp_image.name, format="PNG", optimize=False)
                temp_image_path = temp_image.name
                self.logger.info(f"Imagem temporária salva em: {temp_image_path}")

            # Fazer o upload usando o caminho do arquivo temporário
            try:
                result = self.upload_from_path(temp_image_path)

                # Limpar arquivo temporário após upload bem-sucedido
                if os.path.exists(temp_image_path):
                    os.remove(temp_image_path)
                    self.logger.info(f"Arquivo temporário removido: {temp_image_path}")

                return result
            except Exception as e:
                self.logger.error(f"Erro no upload da imagem base64: {str(e)}")
                if os.path.exists(temp_image_path):
                    os.remove(temp_image_path)
                raise
        except Exception as e:
            self.logger.error(f"Erro ao processar imagem base64: {str(e)}")
            raise

    def delete_image(self, deletehash: str) -> bool:
        """
        Deleta uma imagem no Imgur usando o deletehash com retry logic.

        :param deletehash: Código único fornecido pelo Imgur no momento do upload.
        :return: True se a imagem foi deletada com sucesso, False caso contrário.
        """
        if not deletehash:
            self.logger.warning("Tentativa de deleção com deletehash nulo ou vazio")
            return False

        self.logger.info(f"Tentando deletar imagem com deletehash: {deletehash}")

        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    self.logger.info(
                        f"Tentativa {attempt + 1} de {self.max_retries} para deletar imagem..."
                    )
                    time.sleep(self.retry_delay * (2**attempt))  # Exponential backoff

                result = self.client.delete_image(deletehash)
                if result:
                    self.logger.info(
                        f"Imagem deletada com sucesso após {attempt + 1} tentativa(s)"
                    )
                    return True

            except ImgurClientError as e:
                if hasattr(e, "status_code") and e.status_code == 404:
                    self.logger.info(
                        f"Imagem não encontrada (404) com deletehash: {deletehash}"
                    )
                    return True  # Consider it a success if image doesn't exist
                elif attempt < self.max_retries - 1:
                    self.logger.warning(
                        f"Erro do Imgur ao deletar imagem (tentativa {attempt + 1}): {str(e)}"
                    )
                    continue
                else:
                    self.logger.error(
                        f"Todas as tentativas de deleção falharam para deletehash: {deletehash}"
                    )
                    return False

            except Exception as e:
                if attempt < self.max_retries - 1:
                    self.logger.warning(
                        f"Erro inesperado ao deletar imagem (tentativa {attempt + 1}): {str(e)}"
                    )
                    continue
                else:
                    self.logger.error(f"Erro fatal ao tentar deletar imagem: {str(e)}")
                    return False

        return False
