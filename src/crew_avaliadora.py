#!/usr/bin/env python3
"""
🚀 CrewAI Avaliação Completa V2 - Com Configuração YAML
========================================================

Versão melhorada que usa configuração YAML para agentes e tasks.
Sistema plug-and-play para análise profissional de codebase usando Gemini 2.5 Flash.
"""

import logging
import os

# Import custom utilities
import sys
from datetime import datetime
from pathlib import Path

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))
from crewai_tools import DirectoryReadTool, FileReadTool

from src.tools.custom_tools import CheckDependenciesTool, ExecuteTestsTool, GrepTool, RunLinterTool
from utils.config_loader import load_config

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()


class CodebaseAnalysisCrewV2:
    """
    🤝 CrewAI para Avaliação Completa de Codebase - Versão 2

    Usa configuração YAML para definir agentes e tasks.
    Permite fácil customização sem mexer no código.
    """

    def __init__(
        self,
        gemini_api_key: str | None = None,
        config_path: str | None = None,
        repo_path: str | None = None,
    ):
        """
        Inicializa a crew com configuração YAML e Gemini 2.5 Flash

        Args:
            gemini_api_key: API key do Gemini (se None, usa GEMINI_API_KEY do .env)
            config_path: Caminho para crew_config.yaml (se None, usa config/crew_config.yaml)
            repo_path: Caminho para o repositório clonado (necessário para ferramentas de análise dinâmica)
        """
        # Carrega API key
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError(
                "❌ GEMINI_API_KEY não encontrada! Configure no .env ou passe como parâmetro"
            )

        self.gemini_api_key = self.gemini_api_key.strip()
        logger.info(f"✅ GEMINI_API_KEY carregada: {self.gemini_api_key[:10]}...")

        # Configura environment variables para CrewAI
        os.environ["GEMINI_API_KEY"] = self.gemini_api_key
        if "MODEL" not in os.environ:
            os.environ["MODEL"] = "gemini/gemini-2.5-flash"

        # Define caminho padrão da configuração relativo ao projeto
        if config_path is None:
            config_path = str(Path(__file__).parent.parent / "config" / "crew_config.yaml")

        self.repo_path = repo_path

        # Carrega configuração YAML
        try:
            self.config = load_config(str(config_path))
            logger.info(f"✅ Configuração carregada: {self.config.get_crew_name()}")
        except Exception as e:
            logger.error(f"❌ Erro ao carregar configuração: {e}")
            raise

        # Cria agentes e tasks a partir da configuração
        # Initialize tools
        self.grep_tool: GrepTool | None = None

        if self.repo_path:
            self.file_read_tool = FileReadTool(root_dir=self.repo_path)
            self.directory_read_tool = DirectoryReadTool(directory=self.repo_path)
            self.grep_tool = GrepTool(repo_path=self.repo_path)
        else:
            self.file_read_tool = FileReadTool()
            self.directory_read_tool = DirectoryReadTool()
            self.grep_tool = None

        self.agents = self._create_agents_from_config()
        self.tasks = self._create_tasks_from_config()

    def _create_agents_from_config(self) -> dict[str, Agent]:
        """🎭 Cria agentes a partir da configuração YAML"""
        agents = {}

        agents_config = self.config.get_all_agents()
        logger.info(f"📋 Criando {len(agents_config)} agentes...")

        for agent_key, agent_data in agents_config.items():
            try:
                tools: list = []
                if "tools" in agent_data:
                    if "file_search" in agent_data["tools"]:
                        tools.append(self.file_read_tool)
                        tools.append(self.directory_read_tool)
                        if self.grep_tool:
                            tools.append(self.grep_tool)
                    if "run_linter" in agent_data["tools"] and self.repo_path:
                        tools.append(RunLinterTool(repo_path=self.repo_path))
                    if "check_dependencies" in agent_data["tools"] and self.repo_path:
                        tools.append(CheckDependenciesTool(repo_path=self.repo_path))
                    if "execute_tests" in agent_data["tools"] and self.repo_path:
                        tools.append(ExecuteTestsTool(repo_path=self.repo_path))

                llm = None
                if "llm" in agent_data:
                    # This is a simplified example. In a real scenario, you would
                    # initialize a new LLM instance based on the config.
                    # For now, we'll just log it.
                    logger.info(
                        f"Agent {agent_data['name']} uses a custom model: {agent_data['llm'].get('model')}"
                    )

                agent = Agent(
                    role=f"{agent_data.get('emoji', '')} {agent_data['role']}",
                    goal=agent_data["goal"],
                    backstory=agent_data["backstory"],
                    verbose=True,
                    max_iter=agent_data.get("max_iterations", 3),
                    allow_delegation=agent_data.get("delegation", False),
                    tools=tools,
                    llm=llm,  # Assign the custom LLM
                )
                agents[agent_key] = agent
                logger.info(f"✅ Agente criado: {agent_data['name']}")
            except Exception as e:
                logger.error(f"❌ Erro ao criar agente {agent_key}: {e}")
                raise

        return agents

    def _create_tasks_from_config(self) -> dict[str, Task]:
        """📝 Cria tasks a partir da configuração YAML"""
        tasks = {}

        tasks_config = self.config.get_all_tasks()
        logger.info(f"📋 Criando {len(tasks_config)} tasks...")

        for task_key, task_data in tasks_config.items():
            try:
                # Encontra o agente correspondente
                agent_key = task_data.get("agent")
                if agent_key not in self.agents:
                    logger.warning(f"⚠️ Agente '{agent_key}' não encontrado para task '{task_key}'")
                    continue

                task = Task(
                    description=task_data["description"],
                    expected_output=task_data["expected_output"],
                    agent=self.agents[agent_key],
                )
                tasks[task_key] = task
                logger.info(f"✅ Task criada: {task_data['name']}")
            except Exception as e:
                logger.error(f"❌ Erro ao criar task {task_key}: {e}")
                raise

        return tasks

    def analyze_codebase(
        self,
        codebase_report: str,
        output_file: str | None = None,
        diff_content: str | None = None,
    ) -> str:
        """
        🔍 Executa análise completa da codebase

        Args:
            codebase_report: Relatório inicial da codebase gerado por gerar_relatorio.py
            output_file: Arquivo para salvar o relatório final
            diff_content: Conteúdo do git diff para análise incremental (opcional)

        Returns:
            Relatório final ultra-profissional
        """

        logger.info("🚀 Iniciando análise completa da codebase...")

        # Security Check
        from src.security.guardrails import InputGuard

        guard = InputGuard()

        # Validate codebase report content (prevent injection via file content)
        is_valid, error = guard.validate_prompt(codebase_report)
        if not is_valid:
            logger.error(f"⛔ Security Violation: {error}")
            raise ValueError(f"Security Violation: {error}")

        if diff_content:
            is_valid, error = guard.validate_prompt(diff_content)
            if not is_valid:
                logger.error(f"⛔ Security Violation in Diff: {error}")
                raise ValueError(f"Security Violation in Diff: {error}")

        # Prepara inputs para as tasks
        inputs = {
            "codebase_report": codebase_report,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "diff_context": diff_content
            if diff_content
            else "Nenhuma alteração incremental fornecida (análise completa do estado atual).",
        }

        # Cria crew
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=list(self.tasks.values()),
            process=Process.sequential,
            verbose=True,
        )

        # Setup logging to file
        log_dir = Path(__file__).parent.parent / "outputs" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"crew_execution_{timestamp}.log"

        # File handler
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)

        try:
            logger.info(f"📝 Log sendo salvo em: {log_file}")
            logger.info(f"📊 Input codebase report size: {len(codebase_report)} chars")
            logger.info(f"👥 Agentes na crew: {len(crew.agents)}")
            logger.info(f"📋 Tasks na crew: {len(crew.tasks)}")

            # Log das tasks configuradas
            for i, task in enumerate(crew.tasks, 1):
                logger.info(f"  Task {i}: {task.description[:100]}...")

            logger.info("🎬 Executando crew.kickoff()...")

            # Executa análise
            result = crew.kickoff(inputs=inputs)

            logger.info("✅ crew.kickoff() finalizado!")
            logger.info(f"📦 Tipo do resultado: {type(result)}")
            logger.info(f"📦 Atributos do resultado: {dir(result)}")

            # Extrai texto do resultado (CrewOutput)
            if hasattr(result, "raw"):
                result_text = str(result.raw)
                logger.info(f"✅ Extraído result.raw ({len(result_text)} chars)")
            elif hasattr(result, "output"):
                result_text = str(result.output)
                logger.info(f"✅ Extraído result.output ({len(result_text)} chars)")
            else:
                result_text = str(result)
                logger.info(f"✅ Usando str(result) ({len(result_text)} chars)")

            logger.info(f"📄 Primeiros 500 chars do resultado:\n{result_text[:500]}")

            # Salva resultado
            if output_file:
                logger.info(f"💾 Salvando relatório em: {output_file}")
                self._save_report(result_text, output_file)

            logger.info("✅ Análise completa finalizada!")
            return result_text

        except Exception as e:
            logger.error(f"❌ Erro durante análise: {e}")
            import traceback

            logger.error(f"❌ Traceback:\n{traceback.format_exc()}")
            raise
        finally:
            # Remove file handler
            logger.removeHandler(file_handler)
            file_handler.close()

    def _save_report(self, result_text: str, output_file: str):
        """💾 Salva relatório final diretamente (sem template)"""
        try:
            logger.info("💾 Iniciando salvamento do relatório...")
            logger.info(f"📏 Tamanho do result_text: {len(result_text)} chars")
            logger.info(f"📝 Primeiras 300 chars:\n{result_text[:300]}")

            os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)

            # Valida que há conteúdo
            if not result_text or len(result_text.strip()) < 100:
                raise ValueError(f"Relatório vazio ou muito curto ({len(result_text)} chars)")

            logger.info(f"💾 Escrevendo arquivo: {output_file}")

            # Salva arquivo diretamente
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(result_text)

            # Valida que arquivo foi escrito
            if not os.path.exists(output_file):
                raise OSError(f"Arquivo {output_file} não foi criado")

            file_size = os.path.getsize(output_file)
            if file_size == 0:
                raise OSError(f"Arquivo {output_file} está vazio")

            logger.info(f"✅ Relatório salvo em: {output_file} ({file_size:,} bytes)")

            # Lê de volta para confirmar
            with open(output_file, encoding="utf-8") as f:
                saved_content = f.read()
                logger.info(f"✅ Confirmado: arquivo contém {len(saved_content)} chars")

        except Exception as e:
            logger.error(f"❌ Erro ao salvar relatório: {e}")
            import traceback

            logger.error(f"❌ Traceback:\n{traceback.format_exc()}")
            raise


def main():
    """🎯 Função principal de execução"""
    import sys

    print("=" * 60)
    print("🚀 CrewAI - Avaliação Completa de Codebase V2")
    print("=" * 60)
    print()

    # Verifica health check primeiro
    print("🏥 Recomendação: Execute 'uv run python utils/health_check.py' primeiro")
    print()

    # Inicializa crew
    try:
        crew = CodebaseAnalysisCrewV2()
        print(f"✅ Crew '{crew.config.get_crew_name()}' inicializada!")
        print(f"👥 Agentes: {len(crew.agents)}")
        print(f"📝 Tasks: {len(crew.tasks)}")
        print()
    except Exception as e:
        print(f"❌ Erro ao inicializar crew: {e}")
        sys.exit(1)

    # Carrega relatório base
    base_report_path = "relatorio_codebase_inicial.md"
    if not os.path.exists(base_report_path):
        print(f"⚠️ Relatório base não encontrado: {base_report_path}")
        print("📝 Execute primeiro: uv run python gerar_relatorio.py .")
        sys.exit(1)

    with open(base_report_path, encoding="utf-8") as f:
        codebase_report = f.read()

    print(f"📄 Relatório base carregado ({len(codebase_report)} chars)")
    print()

    # Executa análise
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"relatorio_final_startup_{timestamp}.md"  # Salva na raiz para consistência

    print("🔍 Iniciando análise completa (isso pode levar alguns minutos)...")
    print()

    try:
        crew.analyze_codebase(codebase_report, output_file)

        # Valida que o relatório foi gerado corretamente
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            with open(output_file, encoding="utf-8") as f:
                num_lines = len(f.readlines())

            print()
            print("=" * 60)
            print("✅ ANÁLISE COMPLETA!")
            print("=" * 60)
            print(f"📄 Relatório salvo em: {output_file}")
            print(f"📊 Tamanho: {file_size:,} bytes / {num_lines} linhas")

            if file_size < 1000:
                print("⚠️ ATENÇÃO: Relatório muito pequeno, pode estar incompleto!")
            elif num_lines < 50:
                print("⚠️ ATENÇÃO: Relatório com poucas linhas, pode estar incompleto!")
            else:
                print("✅ Relatório parece completo e bem formatado!")
            print()
        else:
            print()
            print("=" * 60)
            print("❌ ERRO: Arquivo não foi criado!")
            print("=" * 60)
            sys.exit(1)

    except Exception as e:
        print()
        print("=" * 60)
        print("❌ ERRO NA ANÁLISE")
        print("=" * 60)
        print(f"Erro: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
