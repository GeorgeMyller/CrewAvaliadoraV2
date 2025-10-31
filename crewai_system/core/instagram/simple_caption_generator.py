""" 
Módulo para geração simplificada de legendas para Instagram utilizando a API Gemini da Google Generative AI.
Este módulo oferece uma classe principal, SimpleInstagramCaptionGenerator, que permite criar legendas cativantes, profissionais e irreverentes para postagens no Instagram, especialmente voltadas para o contexto corporativo e de transformação digital da empresa AcessoIA. O gerador utiliza parâmetros personalizáveis como gênero, estilo, sentimento, tamanho, uso de emojis e gírias, além de seguir diretrizes específicas para referência à empresa, tom de voz e inclusão de hashtags relevantes.
Caso a API Gemini não esteja disponível ou configurada, o módulo fornece um mecanismo de fallback com templates pré-definidos para diferentes gêneros de legenda.
Principais classes:
- SimpleInstagramCaptionGenerator: Responsável pela geração das legendas, utilizando a API Gemini ou fallback.
- InstagramPostCrew: Wrapper para compatibilidade com sistemas existentes, como CrewAI.
Dependências:
- google.generativeai (opcional)
- dotenv
- logging
- os
Uso:
Inicialize a classe SimpleInstagramCaptionGenerator e utilize o método generate_caption passando um dicionário de parâmetros para obter uma legenda personalizada para Instagram.

"""
import os
import logging
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class SimpleInstagramCaptionGenerator:
    """
    Gerador de legendas simplificado para Instagram usando Gemini
    """

    def __init__(self):
        """Inicializa o gerador com a API do Gemini"""
        if not GEMINI_AVAILABLE:
            logger.warning("Google Generative AI não disponível, usando fallback")
            self.model = None
            return
            
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            logger.warning("GEMINI_API_KEY não encontrado, usando fallback")
            self.model = None
            return
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash')
        except Exception as e:
            logger.error(f"Erro ao configurar Gemini: {e}, usando fallback")
            self.model = None

    def generate_caption(self, inputs):
        """
        Gera uma legenda para Instagram baseada nos inputs fornecidos
        
        Args:
            inputs (dict): Dicionário com parâmetros para geração
        
        Returns:
            str: Legenda gerada
        """
        
        # Extrair parâmetros dos inputs
        genero = inputs.get("genero", "Corporativo")
        caption = inputs.get("caption", "Nova postagem")
        describe = inputs.get("describe", "Imagem interessante")
        estilo = inputs.get("estilo", "Divertido, Alegre, Sarcástico e descontraído")
        pessoa = inputs.get("pessoa", "Terceira pessoa do singular")
        sentimento = inputs.get("sentimento", "Positivo")
        tamanho = inputs.get("tamanho", "200 palavras")
        emojs = inputs.get("emojs", "sim")
        girias = inputs.get("girias", "sim")

        # Se o modelo não está disponível, usar fallback
        if not self.model:
            return self._generate_fallback_caption(caption, describe, genero)

        # Criar prompt estruturado
        prompt = f"""
Você é um especialista em criação de conteúdo para Instagram da AcessoIA, uma empresa de transformação digital e capacitação em IA.

**MISSÃO:** Criar uma legenda cativante, profissional e irreverente para Instagram.

**CONTEXTO DA EMPRESA:**
A AcessoIA é líder em capacitação corporativa em IA, oferecendo workshops, treinamentos e soluções de transformação digital. Nosso tom é descolado, sarcástico mas profissional, sempre destacando os benefícios da IA para produtividade e inclusão digital.

**PARÂMETROS PARA A LEGENDA:**
- Gênero: {genero}
- Caption base: {caption}
- Descrição da imagem: {describe}
- Estilo: {estilo}
- Pessoa: {pessoa}
- Sentimento: {sentimento}
- Tamanho: {tamanho}
- Usar emojis: {emojs}
- Usar gírias: {girias}

**DIRETRIZES OBRIGATÓRIAS:**
1. Evite as palavras "nunca", "sempre" e "garanto"
2. Referencie a AcessoIA na terceira pessoa de forma natural
3. Destaque benefícios da IA para produtividade e mercado de trabalho
4. Use tom irreverente mas profissional
5. Inclua 2-3 hashtags relevantes
6. Mantenha o foco em transformação digital corporativa

**EXEMPLOS DE TRANSFORMAÇÃO:**
- "Estou testando código" → "AcessoIA está otimizando repositórios com insights avançados"
- "Meu projeto está indo bem" → "AcessoIA está acelerando a transformação digital dos clientes"

**ESTRUTURA DESEJADA:**
- Abertura cativante relacionada à imagem
- Conexão com expertise da AcessoIA
- Benefício/valor para o público corporativo
- Call to action ou reflexão final
- Hashtags relevantes

Gere uma legenda seguindo essas diretrizes:
"""

        try:
            if GEMINI_AVAILABLE and self.model:
                response = self.model.generate_content(prompt)
                return response.text.strip()
            else:
                return self._generate_fallback_caption(caption, describe, genero)
        except Exception as e:
            logger.error(f"Erro ao gerar legenda com Gemini: {e}")
            return self._generate_fallback_caption(caption, describe, genero)

    def _generate_fallback_caption(self, caption, describe, genero):
        """Gera uma legenda básica quando o Gemini não está disponível"""
        
        # Templates básicos baseados no gênero
        templates = {
            "Corporativo": "🚀 A AcessoIA está revolucionando a transformação digital corporativa! {caption}\n\n💡 Quando falamos de {describe}, pensamos em como a IA pode otimizar processos e gerar resultados excepcionais.\n\n✨ Capacitação • Inovação • Produtividade\n\n#AcessoIA #TransformacaoDigital #InteligenciaArtificial",
            
            "Tecnológico": "💻 Olha só o que a AcessoIA está aprontando agora! {caption}\n\n🔧 {describe} é só mais um exemplo de como a tecnologia pode acelerar a inovação corporativa.\n\n🎯 Porque treinar equipes em IA não é luxo, é necessidade!\n\n#TechInnovation #AcessoIA #AITraining",
            
            "Educacional": "📚 A AcessoIA não para de surpreender! {caption}\n\n🎓 {describe} mostra como o conhecimento em IA pode transformar carreiras e abrir portas no mercado.\n\n💪 Inclusão digital que gera resultados reais!\n\n#EducacaoDigital #AcessoIA #FuturoDoTrabalho"
        }
        
        template = templates.get(genero, templates["Corporativo"])
        return template.format(caption=caption, describe=describe)


# Compatibilidade com o código existente
class InstagramPostCrew:
    """Wrapper para compatibilidade com código existente"""
    
    def __init__(self):
        self.generator = SimpleInstagramCaptionGenerator()
    
    def kickoff(self, inputs):
        """Método para compatibilidade com CrewAI"""
        return self.generator.generate_caption(inputs)