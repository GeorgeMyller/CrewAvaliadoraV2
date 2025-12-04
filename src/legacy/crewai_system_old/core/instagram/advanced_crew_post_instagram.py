"""
AdvancedInstagramPostCrew
-------------------------
Classe avançada para criação de postagens no Instagram utilizando CrewAI, permitindo perfis de agentes personalizados conforme configuração de grupo.
Classes:
--------
AdvancedInstagramPostCrew:
    - Permite configurar agentes CrewAI com perfis personalizados para geração de legendas e hashtags de postagens no Instagram.
    - Suporta configuração por grupo, incluindo voz da marca, estilo de conteúdo, público-alvo e categorias de hashtags.
    - Utiliza LLM Gemini se chave de API estiver disponível.
    - Métodos principais:
        __init__(group_config): Inicializa a configuração do agente e LLM.
        create_crew(): Configura agentes e tarefas para geração de postagens.
        kickoff(inputs): Executa o processo de geração de postagem, processando insumos e retornando legenda e hashtags.
        get_profile_info(): Retorna informações do perfil do agente atual.
Funções:
--------
create_instagram_crew_for_group(group_config):
    - Cria uma instância de AdvancedInstagramPostCrew para um grupo específico.
Classes de Compatibilidade:
--------------------------
InstagramPostCrew:
    - Wrapper para compatibilidade com código existente, utilizando configuração padrão.
Uso:
----
Permite criar postagens autênticas e envolventes para Instagram, adaptando o estilo e perfil do agente conforme necessidades do grupo.
Advanced Instagram Post Crew - Configuração personalizada por grupo
Permite diferentes perfis de agentes CrewAI baseados na configuração do grupo


"""

import logging
import os
from typing import Any

from crewai import LLM, Agent, Crew, Process, Task
from dotenv import load_dotenv
from src.agent_social_media.core.instagram.base_instagram_service import (
    BaseInstagramService,
    InstagramAPIError,
    MediaError,
)

load_dotenv()
logger = logging.getLogger(__name__)


class AdvancedInstagramPostCrew:
    """
    Classe avançada para criar postagens no Instagram utilizando CrewAI
    com perfis de agentes personalizados baseados na configuração do grupo.
    """

    def __init__(self, group_config: dict[str, Any] | None = None, crew: Crew | None = None):
        """
        Inicializa os serviços, ferramentas, e configura os agentes e tarefas
        baseado na configuração do grupo.

        Args:
            group_config: Configuração específica do grupo contendo perfil do agente
            crew: Uma instância de Crew pré-configurada (para testes).
        """
        self.group_config = group_config or {}
        self.agent_profile = self._extract_agent_profile()

        # Configurar LLM Gemini para CrewAI
        gemini_api_key = self._get_gemini_api_key()
        if gemini_api_key:
            self.llm_captioner = LLM(model="gemini/gemini-2.0-flash", api_key=gemini_api_key)
        else:
            logger.warning("⚠️  GEMINI_API_KEY não encontrada - usando LLM padrão")
            self.llm_captioner = None

        # Usar a crew injetada ou criar uma nova
        if crew:
            self.crew = crew
        else:
            self.create_crew()

        # Inicializar o serviço do Instagram para postagem
        access_token = self.group_config.get("instagram_access_token") or os.getenv(
            "INSTAGRAM_ACCESS_TOKEN"
        )
        ig_user_id = self.group_config.get("instagram_user_id") or os.getenv("INSTAGRAM_USER_ID")

        if not access_token or not ig_user_id:
            logger.warning(
                "⚠️  Token de acesso ou ID de usuário do Instagram não configurado. A postagem direta estará desativada."
            )
            self.instagram_service = None
        else:
            self.instagram_service = BaseInstagramService(access_token, ig_user_id)

    def _get_gemini_api_key(self) -> str | None:
        """Obtém a chave da API do Gemini da configuração do grupo ou variável de ambiente"""
        return (
            self.group_config.get("gemini_api_key")
            or os.getenv("ACESSOAI_GEMINI_API_KEY")
            or os.getenv("GEMINI_API_KEY")
        )

    def _extract_agent_profile(self) -> dict[str, Any]:
        """Extrai o perfil do agente da configuração do grupo"""
        return self.group_config.get("crewai_agent_profile", self._get_default_profile())

    def _get_default_profile(self) -> dict[str, Any]:
        """Perfil padrão caso não haja configuração específica"""
        return {
            "profile_name": "Default Instagram Creator",
            "agent_role": "Você é um Criador de Conteúdo para Instagram",
            "agent_goal": "Escrever legendas divertidas, sempre envolventes para postagens no Instagram com hashtags relevantes. Evite utilizar as palavras 'nunca', 'sempre' e 'garanto'.",
            "agent_backstory": "Você é um assistente de IA super descolado, divertido e sarcástico, com um humor afiado e um talento especial de criar legendas cativantes, bem-humorada e criativa. Sua missão é transformar os insumos fornecidos em uma legenda única e cativante, sempre combinando irreverência e estilo.",
            "brand_voice": "Generic",
            "content_style": "Divertido e descontraído",
            "target_audience": "Público geral do Instagram",
            "hashtag_categories": ["#Instagram", "#Content", "#SocialMedia", "#Engagement"],
        }

    def _build_task_description(self) -> str:
        """Constrói a descrição da task baseada no perfil do agente"""
        profile = self.agent_profile

        base_description = f"""
Criar uma postagem no Instagram usando os seguintes insumos, seguindo o perfil específico:

**PERFIL DO AGENTE: {profile["profile_name"]}**
- Voz da marca: {profile["brand_voice"]}
- Estilo de conteúdo: {profile["content_style"]}
- Público-alvo: {profile["target_audience"]}

**Recebendo os seguintes insumos:**  
1. **Insumo principal:**  
   - Gênero: Indica o estilo de palavras e abordagem.  
   - Caption: Uma breve ideia inicial ou descrição.  
   - Tamanho: Define o comprimento da legenda em palavras.  

2. **Insumos secundários:**  
   - Descrição da imagem: Detalhamento do conteúdo da imagem gerado por IA.  
   - Estilo de escrita: O tom desejado para a legenda.  
   - Pessoa: Define a perspectiva usada na legenda (primeira, segunda ou terceira pessoa).  
   - Sentimento: Indica o tom emocional (padrão é positivo).  
   - Emojis: Define se emojis podem ser usados.  
   - Gírias: Indica se gírias podem ser incluídas.  

**INSTRUÇÕES ESPECÍFICAS DO PERFIL:**
"""

        # Adicionar instruções personalizadas se existirem
        if "custom_instructions" in profile:
            custom = profile["custom_instructions"]
            base_description += f"\n- Tom: {custom.get('tone', 'Padrão')}"

            if custom.get("avoid_corporate_speak"):
                base_description += "\n- EVITAR linguagem corporativa formal"

            if custom.get("focus_personal_stories"):
                base_description += "\n- FOCAR em histórias pessoais e momentos autênticos"

            if custom.get("use_first_person"):
                base_description += "\n- USAR primeira pessoa ('eu', 'meu', 'minha')"

            if "personal_touches" in custom:
                base_description += "\n- Características pessoais:"
                for touch in custom["personal_touches"]:
                    base_description += f"\n  • {touch}"

        # Adicionar categorias de hashtags específicas
        hashtag_cats = profile.get("hashtag_categories", [])
        if hashtag_cats:
            base_description += f"""

**HASHTAGS PREFERENCIAIS:**
Use preferencialmente hashtags destas categorias: {", ".join(hashtag_cats)}
"""

        base_description += """

**DIRETRIZES GERAIS:**
1. Combine todos os insumos de forma natural e criativa
2. O insumo principal tem maior relevância na geração do texto
3. Adicione de 5 a 10 hashtags relacionadas ao conteúdo
4. Mantenha coerência com o perfil específico do agente
5. Crie conteúdo autêntico e envolvente

Gênero: {genero}
Caption: {caption}
Descrição da imagem: {describe}
Estilo: {estilo}
Pessoa: {pessoa}
Sentimento: {sentimento}
Tamanho: {tamanho}
Usar emojis: {emojs}
Usar gírias: {girias}
"""

        return base_description

    def create_crew(self):
        """
        Configura os agentes e tarefas da Crew para gerar postagens no Instagram
        baseado no perfil específico do grupo.
        """
        profile = self.agent_profile

        # Agente para criação de legendas com perfil personalizado
        captioner = Agent(
            role=profile["agent_role"],
            goal=profile["agent_goal"],
            backstory=profile["agent_backstory"],
            allow_delegation=False,
            llm=self.llm_captioner,
            verbose=True,
        )

        # Tarefa de criação de legendas personalizada
        captioner_task = Task(
            description=self._build_task_description(),
            expected_output=(
                f"Uma postagem formatada para o Instagram seguindo o perfil '{profile['profile_name']}' que inclua:\n"
                "1. Uma legenda autêntica e envolvente que integre os insumos.\n"
                "2. Uma lista de 5 a 10 hashtags relevantes e populares.\n"
                f"3. Tom coerente com o estilo: {profile['content_style']}\n"
                f"4. Direcionada para: {profile['target_audience']}"
            ),
            agent=captioner,
        )

        # Configura a Crew com os agentes e tarefas
        self.crew = Crew(
            agents=[captioner],
            tasks=[captioner_task],
            process=Process.sequential,
        )

    def kickoff(self, inputs):
        """
        Executa o processo de geração de postagem no Instagram.

        Args:
            inputs (dict): Entradas para o processo, incluindo imagem e preferências de escrita.

        Returns:
            str: Postagem gerada com legenda e hashtags.
        """
        # Processar inputs (mesmo processamento do original)
        if not isinstance(inputs, dict):
            if isinstance(inputs, str) and "<genero>" in inputs:
                try:
                    import re

                    patterns = {
                        "genero": r"<genero>(.*?)</genero>",
                        "caption": r"<caption>(.*?)</caption>",
                        "describe": r"<describe>(.*?)</describe>",
                        "estilo": r"<estilo>(.*?)</estilo>",
                        "pessoa": r"<pessoa>(.*?)</pessoa>",
                        "sentimento": r"<sentimento>(.*?)</sentimento>",
                        "tamanho": r"<tamanho>(.*?)</tamanho>",
                        "emojs": r"<emojs>(.*?)</emojs>",
                        "girias": r"<girias>(.*?)</girias>",
                    }

                    parsed_inputs = {}
                    for key, pattern in patterns.items():
                        match = re.search(pattern, inputs, re.DOTALL)
                        if match:
                            parsed_inputs[key] = match.group(1).strip()

                    if parsed_inputs:
                        inputs = parsed_inputs
                    else:
                        raise ValueError("Não foi possível analisar a entrada como XML")
                except Exception as e:
                    logger.error(f"Erro ao converter entrada XML: {str(e)}")
                    inputs = self._get_default_inputs()
            else:
                inputs = self._get_default_inputs()

        # Garantir que todas as chaves necessárias existam
        default_values = self._get_default_inputs()
        for key, default_value in default_values.items():
            if key not in inputs or not inputs[key]:
                inputs[key] = default_value

        resultado = self.crew.kickoff(inputs=inputs)

        # NOVA CORREÇÃO: Detectar #story automaticamente na legenda gerada
        if resultado.raw and "#story" in resultado.raw.lower():
            logger.info("🎯 Hashtag #story detectada na legenda gerada!")

            # Verificar se há mídia para postar como story
            media_url = inputs.get("media_url") or inputs.get("image_url")
            if media_url and self.instagram_service:
                try:
                    logger.info(f"📱 Postando Story automaticamente: {media_url}")
                    self.instagram_service.post_story(media_url, "IMAGE")
                    logger.info("✅ Story postado com sucesso!")
                    return f"Story postado! Legenda original: {resultado.raw}"
                except Exception as e:
                    logger.error(f"❌ Erro ao postar Story automaticamente: {e}")
                    return f"Erro ao postar Story: {e}"
            else:
                logger.warning("⚠️ Story detectado mas sem mídia ou serviço Instagram disponível")

        # Postagem normal se não for story
        media_url = inputs.get("media_url")
        if media_url and self.instagram_service:
            try:
                self.post_media(media_url, resultado.raw)
            except (InstagramAPIError, MediaError) as e:
                logger.error(f"Falha ao postar mídia no Instagram: {e}")

        return resultado.raw

    def post_media(self, media_url: str, caption: str):
        """
        Decide se posta um Story ou uma mídia no feed com base na legenda.

        Args:
            media_url (str): URL da mídia a ser postada.
            caption (str): Legenda gerada, que pode conter #story.
        """
        if "#story" in caption.lower():
            logger.info("Detectada a hashtag #story. Tentando postar como um Story.")
            if self.instagram_service:
                # Extrair o tipo de mídia da URL (simplificado)
                media_type = (
                    "VIDEO" if any(ext in media_url for ext in [".mp4", ".mov"]) else "IMAGE"
                )
                self.instagram_service.post_story(media_url, media_type)
            else:
                logger.warning("⚠️ Serviço Instagram não configurado para postar Story")
        else:
            logger.info("Nenhuma hashtag #story detectada. Postando no feed.")
            # Aqui você chamaria a função existente para postar no feed
            # Exemplo: self.instagram_service.post_feed_media(media_url, caption)
            # Como a função de postagem no feed não está definida aqui, apenas logamos.
            print(f"Simulando postagem no feed com URL: {media_url} e legenda: {caption}")

    def _get_default_inputs(self) -> dict[str, str]:
        """Valores padrão para inputs"""
        return {
            "genero": "Neutro",
            "caption": "Imagem para Instagram",
            "describe": "Imagem para redes sociais",
            "estilo": "Divertido e descontraído",
            "pessoa": "Terceira pessoa",
            "sentimento": "Positivo",
            "tamanho": "200 palavras",
            "emojs": "sim",
            "girias": "sim",
        }

    def get_profile_info(self) -> dict[str, Any]:
        """Retorna informações sobre o perfil do agente atual"""
        return {
            "profile_name": self.agent_profile["profile_name"],
            "brand_voice": self.agent_profile["brand_voice"],
            "content_style": self.agent_profile["content_style"],
            "target_audience": self.agent_profile["target_audience"],
            "hashtag_categories": self.agent_profile.get("hashtag_categories", []),
            "group_id": self.group_config.get("group_id", "N/A"),
            "group_name": self.group_config.get("group_name", "N/A"),
        }


# Função de fábrica para compatibilidade com código existente
def create_instagram_crew_for_group(group_config: dict[str, Any] | None = None):
    """
    Cria uma instância do AdvancedInstagramPostCrew para um grupo específico

    Args:
        group_config: Configuração do grupo contendo perfil do agente

    Returns:
        AdvancedInstagramPostCrew: Instância configurada para o grupo
    """
    return AdvancedInstagramPostCrew(group_config)


# Classe para compatibilidade com código existente (usando configuração padrão)
class InstagramPostCrew(AdvancedInstagramPostCrew):
    """Wrapper para compatibilidade com código existente"""

    def __init__(self):
        super().__init__(group_config=None)
