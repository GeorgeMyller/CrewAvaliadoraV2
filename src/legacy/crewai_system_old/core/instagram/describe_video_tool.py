"""
Módulo para geração de descrições detalhadas de vídeos utilizando o modelo Gemini da Google.
Classes:
    VideoDescriber:
        Classe utilitária para analisar vídeos locais e gerar descrições automáticas sobre o conteúdo, ambiente, expressões faciais, objetos marcantes e contexto emocional do vídeo. Utiliza a API Gemini para processar o vídeo e retornar uma descrição textual.
Dependências:
    - os: Manipulação de caminhos e arquivos.
    - google.generativeai: Integração com a API Gemini.
    - dotenv: Carregamento de variáveis de ambiente.
    - base64: Codificação do vídeo para envio à API.
    - logging: Registro de logs para rastreamento e depuração.
Uso:
    Chame VideoDescriber.describe(video_path) passando o caminho local do vídeo para obter uma descrição detalhada do conteúdo do vídeo.
Exceções e Tratamento de Erros:
    - Verifica se o caminho é uma URL.
    - Verifica se o arquivo existe e possui tamanho mínimo.
    - Trata erros de leitura do arquivo e comunicação com a API Gemini, retornando mensagens amigáveis ao usuário.

"""

import base64
import logging
import os

import google.generativeai as genai
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


class VideoDescriber:
    @staticmethod
    def describe(video_path: str) -> str:
        """
        Gera uma descrição detalhada para o vídeo fornecido.

        Args:
            video_path (str): Caminho local do vídeo a ser analisado.

        Returns:
            str: Descrição gerada para o vídeo.
        """
        # Log de debug para rastrear entrada
        logger.info(f"🎬 VideoDescriber: Analisando arquivo: {video_path}")

        # Verificar se é uma URL (não deveria ser!)
        if video_path.startswith("http"):
            error_msg = f"❌ VideoDescriber: Recebeu URL em vez de arquivo local: {video_path}"
            logger.error(error_msg)
            return f"Erro: O arquivo de vídeo não existe no caminho: {video_path}"

        load_dotenv()  # Carregar variáveis de ambiente do arquivo .env

        # Configurar o cliente Gemini
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.0-flash")  # Usando o modelo que suporta vídeos

        # Verificar se o arquivo existe
        if not os.path.exists(video_path):
            error_msg = f"❌ VideoDescriber: Arquivo não encontrado: {video_path}"
            logger.error(error_msg)
            return f"Erro: O arquivo de vídeo não existe no caminho: {video_path}"

        # Verificar se o arquivo tem tamanho mínimo
        file_size = os.path.getsize(video_path)
        if file_size < 1000:  # Menos de 1KB provavelmente não é um vídeo válido
            error_msg = f"❌ VideoDescriber: Arquivo muito pequeno ({file_size} bytes), pode não ser um vídeo válido"
            logger.error(error_msg)
            return "Vídeo muito pequeno ou formato inválido. Não foi possível analisar o conteúdo."

        logger.info(f"✅ VideoDescriber: Arquivo encontrado, tamanho: {file_size} bytes")

        try:
            # Ler o arquivo de vídeo diretamente do caminho local
            with open(video_path, "rb") as video_file:
                video_bytes = video_file.read()
                encoded_video = base64.b64encode(video_bytes).decode("utf-8")

            logger.info(f"✅ VideoDescriber: Vídeo codificado, tamanho: {len(encoded_video)} chars")
        except Exception as e:
            return f"Erro ao ler o arquivo de vídeo: {e}"

        prompt_text = """
                Me dê uma ideia do contexto do ambiente do vídeo e do que está ocorrendo no vídeo.
                Quais são as expressões faciais predominantes (feliz, triste, neutro, etc.)?                                 
                Qual é a expressão emocional delas? 
                Além disso, descreva qualquer objeto ou elemento marcante na cena.
                Tente identificar se é dia ou noite, ambiente aberto ou fechado,
                de festa ou calmo. O que as pessoas estão fazendo?
            """

        try:
            logger.info("🤖 VideoDescriber: Enviando para Gemini...")
            describe = model.generate_content(
                {
                    "parts": [
                        {"text": prompt_text},
                        {
                            "inline_data": {
                                "mime_type": "video/mp4",
                                "data": encoded_video,
                            }
                        },
                    ]
                }
            )

            # Extraindo a descrição da resposta
            try:
                result = describe.text.strip()
                logger.info(f"✅ VideoDescriber: Descrição obtida: {result[:100]}...")
                return result
            except (AttributeError, IndexError) as e:
                error_msg = f"❌ VideoDescriber: Erro ao processar resposta: {e}"
                logger.error(error_msg)
                return f"Erro ao processar a descrição do vídeo: {e}"

        except Exception as e:
            error_msg = str(e)
            # Truncar mensagens de erro muito longas da API
            if len(error_msg) > 500:
                error_msg = error_msg[:500] + "... [erro truncado]"

            logger.error(f"❌ VideoDescriber: Erro na API Gemini: {error_msg}")

            # Retornar uma mensagem mais amigável baseada no tipo de erro
            if "400" in error_msg:
                return "Erro: Formato de vídeo não suportado ou arquivo corrompido."
            elif "403" in error_msg or "quota" in error_msg.lower():
                return "Erro: Limite de uso da API atingido. Tente novamente mais tarde."
            elif "404" in error_msg:
                return "Erro: Modelo de IA não encontrado ou não disponível."
            else:
                return "Erro ao processar a descrição do vídeo: Falha na comunicação com a API."
