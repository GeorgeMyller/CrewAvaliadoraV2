# 📊 Relatório Técnico da Codebase
**Gerado em:** 2025-11-22 21:19:29
**Diretório analisado:** `/var/folders/g1/7nfb0bns5zbftz_zqwwbbyjw0000gn/T/crew_analysis_AprenderEscrita__nnwwmsa`
**Total de arquivos:** 12
**Tamanho total:** 50.46 KB

## 📈 Distribuição por Extensão

- **.py**: 5 arquivos (3.13 KB)
- **no_extension**: 3 arquivos (374.00 B)
- **.md**: 2 arquivos (46.69 KB)
- **.toml**: 1 arquivos (199.00 B)
- **.example**: 1 arquivos (79.00 B)

## 📁 Estrutura de Diretórios

- `root`: 7 arquivos (47.33 KB)
- `aprenderescrita`: 5 arquivos (3.13 KB)

## 📖 README / Descrição do Projeto

### Conteúdo de README.md

```
# AprenderEscrita

Este projeto automatiza a extração de legendas de publicações de uma conta profissional do Instagram, utilizando a **Instagram Graph API v23**. O objetivo é gerar um arquivo `legendas.md` contendo as legendas, datas, tipos de mídia e links permanentes das publicações, facilitando a análise e o arquivamento do conteúdo.

## Funcionalidades

- **Conexão com a Instagram Graph API v23**: Obtém as publicações mais recentes de uma conta profissional.
- **Geração de Arquivo Markdown**: Cria automaticamente o arquivo `legendas.md` com as informações extraídas.
- **Suporte a Múltiplos Tipos de Mídia**: Processa imagens e vídeos, incluindo suas respectivas URLs.
- **Configuração Flexível**: Utiliza variáveis de ambiente para gerenciar as credenciais da API de forma segura.
- **Tratamento de Erros**: Fornece feedback claro sobre falhas de conexão ou autenticação com a API.

## Estrutura do Projeto

```
/
├── .env.example      # Exemplo de arquivo para variáveis de ambiente
├── .gitignore        # Arquivos e diretórios ignorados pelo Git
├── main.py           # Script principal que executa a extração
├── pyproject.toml    # Metadados e dependências do projeto
├── README.md         # Este arquivo
└── uv.lock           # Arquivo de lock do gerenciador de pacotes uv
```

## Requisitos

- Python 3.8+
- Conta de Desenvolvedor do Facebook
- Conta Profissional do Instagram
- Token de acesso válido para a Instagram Graph API v23

## Como Usar

### 1. Clone o Repositório

```sh
git clone <url-do-repositorio>
cd AprenderEscrita
```

### 2. Crie e Ative um Ambiente Virtual

Recomendamos o uso de `uv` para criar e gerenciar o ambiente virtual:

```sh
uv venv
source .venv/bin/activate
```

### 3. Configure as Variáveis de Ambiente

Copie o arquivo `.env.example` para um novo arquivo chamado `.env` e preencha com suas credenciais:

```sh
cp .env.example .env
```

Edite o arquivo `.env` com suas informações:

```env
INSTAGRAM_USER_ID=seu_user_id
INSTAGRAM_ACCESS_TOKEN=seu_access_token
```

### 4. Instale as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no `pyproject.toml`:

```sh
uv pip install -e .
```

### 5. Execute o Script

Para iniciar a extração, execute o script `main.py`:

```sh
python3 -m aprenderescrita.main
```

Após a execução, o arquivo `legendas.md` será criado na raiz do projeto com as publicações extraídas.

## Referências

- [Documentação Oficial da Instagram Graph API](https://developers.facebook.com/docs/instagram-platform)
- [Como Criar um App no Facebook Developers](https://developers.facebook.com/docs/instagram-platform/create-an-instagram-app)

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

Desenvolvido por **George Myller**.
```


## 💻 Código Principal

### pyproject.toml

```
[project]
name = "aprenderescrita"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "requests",
    "python-dotenv",
]

```


## 📄 Arquivos de Código Detalhados

*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*

### aprenderescrita/client.py (1.31 KB)

```python
import requests

from . import config


def get_instagram_posts():
    """
    Obtém as últimas publicações de uma conta profissional do Instagram.
    """
    endpoint = f"https://{config.HOST_URL}/{config.API_VERSION}/{config.IG_USER_ID}/media"
    params = {
        "fields": "caption,media_type,timestamp,permalink,media_url",
        "limit": config.LIMIT,
        "access_token": config.ACCESS_TOKEN,
    }

    print(f"A fazer uma requisição para: {endpoint}")

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Levanta um erro para status HTTP 4xx/5xx
        data = response.json()

        if "error" in data:
            error = data["error"]
            print(f"Erro da API do Instagram: {error['message']} (Código: {error['code']})")
            return None

        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        try:
            error_data = response.json().get("error", {})
            if "message" in error_data:
                print(f"Detalhes do erro: {error_data['message']}")
        except ValueError:
            pass
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao obter publicações do Instagram: {e}")
        return None

```

### aprenderescrita/writer.py (1.09 KB)

```python
from . import config


def write_captions_to_markdown(posts_data):
    """
    Escreve as legendas e metadados das publicações em um arquivo Markdown.
    """
    if not posts_data or "data" not in posts_data:
        print("Nenhuma publicação encontrada ou erro ao obter dados.")
        return

    with open(config.LEGENDAS_MD_PATH, "w", encoding="utf-8") as file:
        for post in posts_data["data"]:
            caption = post.get("caption", "")
            media_type = post.get("media_type", "")
            timestamp = post.get("timestamp", "")
            permalink = post.get("permalink", "")
            media_url = post.get("media_url", "")

            file.write(f"### {timestamp}\n")
            file.write(f"**Tipo de mídia:** {media_type}\n")
            file.write(f"[Ver publicação]({permalink})\n")
            if media_type == "IMAGE":
                file.write(f"![Imagem]({media_url})\n")
            elif media_type == "VIDEO":
                file.write(f"[Vídeo]({media_url})\n")
            file.write(f"{caption}\n\n")

    print(f"Legendas salvas em: {config.LEGENDAS_MD_PATH}")

```

### aprenderescrita/main.py (431.00 B)

```python
from . import client, config, writer


def main():
    """
    Função principal para executar o script.
    """
    if config.IG_USER_ID == "seu_user_id" or config.ACCESS_TOKEN == "seu_access_token":
        print("ERRO: Por favor, configure suas credenciais no arquivo .env.")
        return

    posts_data = client.get_instagram_posts()
    writer.write_captions_to_markdown(posts_data)

if __name__ == "__main__":
    main()

```

### aprenderescrita/config.py (311.00 B)

```python
import os

from dotenv import load_dotenv

load_dotenv()

HOST_URL = "graph.facebook.com"
API_VERSION = "v23.0"
IG_USER_ID = os.getenv("INSTAGRAM_USER_ID")
ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
LIMIT = 50
LEGENDAS_MD_PATH = os.path.join(os.path.dirname(os.path.abspath("__file__")), "legendas.md")

```

### aprenderescrita/__init__.py (0.00 B)

```python

```


## 📂 Lista Completa de Arquivos

- `legendas.md` (43.83 KB)
- `README.md` (2.87 KB)
- `aprenderescrita/client.py` (1.31 KB)
- `aprenderescrita/writer.py` (1.09 KB)
- `aprenderescrita/main.py` (431.00 B)
- `aprenderescrita/config.py` (311.00 B)
- `.cache_ggshield` (210.00 B)
- `pyproject.toml` (199.00 B)
- `.gitignore` (159.00 B)
- `.env.example` (79.00 B)
- `.python-version` (5.00 B)
- `aprenderescrita/__init__.py` (0.00 B)

---
*Relatório gerado automaticamente para análise CrewAI*

**IMPORTANTE:** Este relatório contém código real do projeto. A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.
