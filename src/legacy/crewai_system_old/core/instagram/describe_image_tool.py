""""
Módulo para gerar descrições detalhadas de imagens utilizando o modelo Gemini da Google.

Classes:
    ImageDescriber:
        Classe utilitária para descrever imagens a partir de uma URL utilizando a API Gemini.

Métodos:
    describe(image_url: str, api_key: str) -> str:
        Gera uma descrição detalhada da imagem fornecida, incluindo contexto do ambiente,
        expressões faciais predominantes, elementos marcantes, identificação de ambiente
        (dia/noite, aberto/fechado, festa/calmo) e ações das pessoas presentes.
        Retorna uma string com a descrição gerada ou uma mensagem de erro em caso de falha.

Dependências:
    - google.generativeai
    - dotenv
    - requests
    - base64
    - logging

Uso:
    Carregue as variáveis de ambiente, forneça a URL da imagem e a chave da API Gemini
    para obter uma descrição detalhada da imagem.

"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
import requests  # Added for fetching image data
import base64  # Added for base64 encoding
import logging

logger = logging.getLogger(__name__)

load_dotenv()  # Carregar variáveis de ambiente do arquivo .env
class ImageDescriber:
    @staticmethod
    def describe(image_url: str, api_key: str) -> str:
        """
        Gera uma descrição detalhada para a imagem fornecida.

        Args:
            image_url (str): URL da imagem a ser analisada.
            api_key (str): Chave da API do Gemini.

        Returns:
            str: Descrição gerada para a imagem.
        """
        # Configurar o cliente Gemini
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel(
            "gemini-2.0-flash"
        )  # Usando modelo atualizado que suporta visão

        # Fazer a solicitação à API do Gemini
        try:
            # Fetch and encode the image from the URL with custom headers
            headers = {"User-Agent": "Mozilla/5.0"}
            image_response = requests.get(image_url, headers=headers, timeout=30)
            image_response.raise_for_status()
            encoded_image = base64.b64encode(image_response.content).decode("utf-8")
        except Exception as e:
            return f"Erro ao obter a imagem: {e}"

        prompt_text = """
                Me dê uma ideia do contexto do ambiente da imagem e do que está ocorrendo na imagem.
                Quais são as expressões faciais predominantes (feliz, triste, neutro, etc.)?                                 
                Qual é a expressão emocional delas? 
                Além disso, descreva qualquer objeto ou elemento marcante na cena.
                Tente identificar se é dia ou noite, ambiente aberto ou fechado,
                de festa ou calmo. O que as pessoas estão fazendo?
            """

        try:
            describe = model.generate_content(
                {
                    "parts": [
                        {"text": prompt_text},
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": encoded_image,  # Updated to use base64 encoded image content
                            }
                        },
                    ]
                }
            )

            # Extraindo a descrição da resposta
            try:
                return describe.text.strip()
            except (AttributeError, IndexError) as e:
                return f"Erro ao processar a descrição da imagem: {e}"

        except Exception as e:
            logger.error(f"Erro detalhado: {str(e)}")
            return f"Erro ao processar a descrição da imagem: {e}"