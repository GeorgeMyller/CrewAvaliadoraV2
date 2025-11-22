# 📊 Relatório Técnico da Codebase
**Gerado em:** 2025-11-22 15:07:58
**Diretório analisado:** `/var/folders/g1/7nfb0bns5zbftz_zqwwbbyjw0000gn/T/crew_analysis_htmltopdf-batch-mac_hacirsci`
**Total de arquivos:** 8
**Tamanho total:** 2.98 KB

## 📈 Distribuição por Extensão

- **no_extension**: 4 arquivos (487.00 B)
- **.py**: 2 arquivos (1.47 KB)
- **.toml**: 1 arquivos (201.00 B)
- **.md**: 1 arquivos (851.00 B)

## 📁 Estrutura de Diretórios

- `root`: 6 arquivos (2.98 KB)
- `input`: 1 arquivos (0.00 B)
- `output`: 1 arquivos (0.00 B)

## 📖 README / Descrição do Projeto

### Conteúdo de README.md

```
# htmltopdf

Ferramenta para converter arquivos HTML em PDF em lote usando Google Chrome headless.

## Estrutura de Pastas
- `input/`: coloque aqui todos os arquivos `.html` que deseja converter.
- `output/`: os arquivos PDF convertidos serão salvos aqui.

## Como usar
1. Certifique-se de ter o Google Chrome instalado no macOS.
2. Coloque os arquivos HTML na pasta `input`.
3. Execute o script:
   ```sh
   python converter_html_para_pdf_selenium.py
   ```
   Os PDFs serão gerados na pasta `output`.

## Requisitos
- Python 3.8+
- Google Chrome
- (Opcional) Ambiente virtual Python
- Pacote `selenium` (instalado via `pip install selenium`)

## Observações
- O script usa o Chrome via linha de comando para conversão, não depende de bibliotecas externas problemáticas.
- Ajuste o caminho do Chrome no script se necessário.

## Licença
MIT

```


## 💻 Código Principal

### main.py

```
def main():
    print("Hello from htmltopdf!")

    
if __name__ == "__main__":
    main()

```


## 📄 Arquivos de Código Detalhados

*Esta seção contém amostras dos principais arquivos de código para análise detalhada.*

### converter_html_para_pdf_selenium.py (1.38 KB)

```python
import os
from glob import glob
from pathlib import Path
from selenium.webdriver.chrome.options import Options

# Pastas de entrada e saída
PASTA_INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input')
PASTA_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

# Configuração do Chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Encontra todos os arquivos .html na pasta de entrada
html_files = glob(os.path.join(PASTA_INPUT, '*.html'))

# Caminho do Chrome (ajuste se necessário)
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

for html_path in html_files:
    nome_arquivo = Path(html_path).stem
    pdf_path = os.path.join(PASTA_OUTPUT, f'{nome_arquivo}.pdf')
    try:
        # Comando para converter HTML em PDF usando Chrome headless
        cmd = f'"{chrome_path}" --headless --disable-gpu --print-to-pdf="{pdf_path}" "file://{html_path}"'
        result = os.system(cmd)
        if result == 0:
            print(f'Convertido: {html_path} -> {pdf_path}')
        else:
            print(f'Erro ao converter {html_path}: código {result}')
    except Exception as e:
        print(f'Erro ao converter {html_path}: {e}')

print('Conversão concluída.')

```

### main.py (91.00 B)

```python
def main():
    print("Hello from htmltopdf!")

    
if __name__ == "__main__":
    main()

```


## 📂 Lista Completa de Arquivos

- `converter_html_para_pdf_selenium.py` (1.38 KB)
- `README.md` (851.00 B)
- `.gitignore` (482.00 B)
- `pyproject.toml` (201.00 B)
- `main.py` (91.00 B)
- `.python-version` (5.00 B)
- `input/.gitkeep` (0.00 B)
- `output/.gitkeep` (0.00 B)

---
*Relatório gerado automaticamente para análise CrewAI*

**IMPORTANTE:** Este relatório contém código real do projeto. A análise deve ser baseada EXCLUSIVAMENTE no código e documentação fornecidos acima.
