# Análise do arquivo: reports_by_file/reports_by_file_crewai_system_scripts_demo_crew_avaliacao.py_20250817_124016.md_20250817_124538.md

❌ Erro ao analisar /Volumes/SSD-EXTERNO/2025/CrewAvaliadora/reports_by_file/reports_by_file_crewai_system_scripts_demo_crew_avaliacao.py_20250817_124016.md_20250817_124538.md: litellm.APIConnectionError: Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
Traceback (most recent call last):
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/main.py", line 2675, in completion
    model_response = vertex_chat_completion.completion(  # type: ignore
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/llms/vertex_ai/gemini/vertex_and_google_ai_studio_gemini.py", line 1811, in completion
    _auth_header, vertex_project = self._ensure_access_token(
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/llms/vertex_ai/vertex_llm_base.py", line 266, in _ensure_access_token
    return self.get_access_token(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/llms/vertex_ai/vertex_llm_base.py", line 437, in get_access_token
    raise e
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/llms/vertex_ai/vertex_llm_base.py", line 430, in get_access_token
    _credentials, credential_project_id = self.load_auth(
                                          ^^^^^^^^^^^^^^^
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/llms/vertex_ai/vertex_llm_base.py", line 114, in load_auth
    creds, creds_project_id = self._credentials_from_default_auth(
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/litellm/llms/vertex_ai/vertex_llm_base.py", line 160, in _credentials_from_default_auth
    return google_auth.default(scopes=scopes)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/SSD-EXTERNO/2025/CrewAvaliadora/.venv/lib/python3.12/site-packages/google/auth/_default.py", line 685, in default
    raise exceptions.DefaultCredentialsError(_CLOUD_SDK_MISSING_CREDENTIALS)
google.auth.exceptions.DefaultCredentialsError: Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
