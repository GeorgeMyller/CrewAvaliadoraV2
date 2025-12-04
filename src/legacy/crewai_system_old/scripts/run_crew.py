import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai_tools import FileReadTool
from dotenv import load_dotenv

load_dotenv()

# LLM (usando seu Gemini definido no ambiente)
llm = LLM(provider="google", model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

# Tool para leitura de arquivo
file_tool = FileReadTool()

# Agentes especializados
agents = {
    "arquiteto": Agent(
        role="Arquiteto de Software",
        goal="Analise arquitetura, fluxos e padrões para escalabilidade",
        backstory="Arquiteto experiente em automações e APIs sociais.",
        tools=[file_tool],
        llm=llm,
    ),
    "qa_engineer": Agent(
        role="Engenheiro de Qualidade",
        goal="Avalie cobertura de testes, qualidade de código e riscos técnicos",
        backstory="Especialista em testes e pipelines CI/CD.",
        tools=[file_tool],
        llm=llm,
    ),
    "documentador": Agent(
        role="Documentador Técnico",
        goal="Verifique e melhore documentação para onboarding e uso",
        backstory="Especialista em documentação e clareza técnica.",
        tools=[file_tool],
        llm=llm,
    ),
    "pm": Agent(
        role="Product Manager",
        goal="Avalie readiness para SaaS e sugira roadmap",
        backstory="Product Manager com experiência em produtos digitais.",
        tools=[file_tool],
        llm=llm,
    ),
    "legal": Agent(
        role="Especialista Legal",
        goal="Analise riscos legais (APIs, LGPD/GDPR) e sugira mitigação",
        backstory="Advogado especializado em tecnologia.",
        tools=[file_tool],
        llm=llm,
    ),
    "ia_engineer": Agent(
        role="Engenheiro de IA",
        goal="Otimize pipeline IA (legendas, filtros, personalização)",
        backstory="Engenheiro de IA com experiência em LLMs e visão computacional.",
        tools=[file_tool],
        llm=llm,
    ),
}

# Definição de tarefas, uma por agente
tasks = [
    Task(
        description="Use FileReadTool para ler relatorio_codebase_turbinado.md. Analise arquitetura e sugira melhorias.",
        expected_output="Parágrafo com análise arquitetural clara e recomendações.",
        agent=agents["arquiteto"],
    ),
    Task(
        description="Leia o relatório. Avalie qualidade de código e cobertura de testes.",
        expected_output="Comentários e recomendações sobre qualidade e testes.",
        agent=agents["qa_engineer"],
    ),
    Task(
        description="Leia o relatório. Avalie documentação existente e proponha melhorias.",
        expected_output="Resumo dos pontos fortes e lacunas da documentação.",
        agent=agents["documentador"],
    ),
    Task(
        description="Leia o relatório. Avalie maturidade do produto para SaaS e proponha roadmap.",
        expected_output="Avaliação de readiness e proposta de roadmap.",
        agent=agents["pm"],
    ),
    Task(
        description="Leia o relatório. Analise riscos legais e conformidade.",
        expected_output="Análise de riscos legais e sugestões de compliance.",
        agent=agents["legal"],
    ),
    Task(
        description="Leia o relatório. Analise o componente IA e sugira otimizações.",
        expected_output="Sugestões técnicas para o pipeline de IA.",
        agent=agents["ia_engineer"],
    ),
]

# Montagem da Crew
crew = Crew(agents=list(agents.values()), tasks=tasks, process=Process.sequential)

if __name__ == "__main__":
    output = crew.kickoff()
    with open("relatorio_final_startup.md", "w", encoding="utf-8") as f:
        f.write(output)
    print("✅ Relatório final gerado em 'relatorio_final_startup.md'")
