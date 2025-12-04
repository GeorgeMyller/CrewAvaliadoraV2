"""
Módulo para gerar descrições detalhadas de imagens em um carrossel do Instagram utilizando o modelo Gemini da Google.

Classes:
    CarouselDescriber:
        Classe utilitária para analisar uma lista de imagens e retornar descrições contextuais e emocionais de cada uma.

Métodos:
    describe(image_paths: list) -> str:
        Recebe uma lista de caminhos de imagens, processa cada uma utilizando o modelo Gemini, e retorna uma descrição detalhada sobre o ambiente, expressões faciais, emoções, objetos marcantes, contexto (dia/noite, aberto/fechado, festa/calmo) e ações das pessoas presentes nas imagens.

Dependências:
    - dotenv para carregar variáveis de ambiente (.env)
    - google.generativeai para integração com o modelo Gemini
    - base64 para codificação das imagens
    - logging para registro de erros

Exceções:
    - Retorna mensagens de erro caso o arquivo de imagem não exista ou não possa ser lido/processado.

Uso:
    Ideal para gerar descrições automáticas de carrosséis de imagens para redes sociais, especialmente Instagram.


"""

import base64
import logging
import os

import google.generativeai as genai
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


class CarouselDescriber:
    @staticmethod
    def describe(image_paths: list) -> str:
        """
        Gera uma descrição detalhada para todas as imagens fornecidas no carrossel.

        Args:
            image_paths (list): Lista de caminhos das imagens a serem analisadas.

        Returns:
            str: Descrição gerada para as imagens do carrossel.
        """
        load_dotenv()  # Carregar variáveis de ambiente do arquivo .env

        # Configurar o cliente Gemini
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.0-flash")  # Usando o modelo que suporta imagens

        descriptions = []

        for image_path in image_paths:
            # Verificar se o arquivo existe
            if not os.path.exists(image_path):
                descriptions.append(
                    f"Erro: O arquivo de imagem não existe no caminho: {image_path}"
                )
                continue

            try:
                # Ler o arquivo de imagem diretamente do caminho local
                with open(image_path, "rb") as image_file:
                    image_bytes = image_file.read()
                    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
            except Exception as e:
                descriptions.append(f"Erro ao ler o arquivo de imagem: {e}")
                continue

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
                                    "data": encoded_image,
                                }
                            },
                        ]
                    }
                )

                # Extraindo a descrição da resposta
                try:
                    descriptions.append(describe.text.strip())
                except (AttributeError, IndexError) as e:
                    descriptions.append(f"Erro ao processar a descrição da imagem: {e}")

            except Exception as e:
                logger.error(f"Erro detalhado: {str(e)}")
                descriptions.append(f"Erro ao processar a descrição da imagem: {e}")

        return "\n".join(descriptions)
