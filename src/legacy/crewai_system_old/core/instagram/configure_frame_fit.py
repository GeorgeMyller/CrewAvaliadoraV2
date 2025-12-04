#!/usr/bin/env python3

"""
Este módulo fornece funcionalidades para testar e configurar modos de enquadramento de imagens em molduras,
especialmente para uso em redes sociais como Instagram. Ele permite criar imagens de teste com diferentes
proporções (quadrada, paisagem, retrato), aplicar molduras utilizando diferentes modos de ajuste ("fill", "fit", "stretch"),
e salvar os resultados para comparação visual. Também inclui utilitário para configurar o modo padrão de enquadramento
em um arquivo de configuração.
Funções principais:
- create_test_images: Gera imagens de teste com gradientes e diferentes proporções.
- test_fit_modes: Aplica molduras às imagens de teste usando diferentes modos de enquadramento e gera relatório dos resultados.
- configure_fit_mode: Salva o modo de enquadramento escolhido em um arquivo de configuração.
- main: Executa o fluxo de teste e configuração, orientando o usuário sobre como aplicar os modos.
Requisitos:
- Pillow (PIL) para manipulação de imagens.
- Estrutura de diretórios esperada para assets e src.
Uso recomendado:
Execute o script para gerar imagens de teste, aplicar molduras e comparar visualmente os resultados dos diferentes modos.
Configure o modo padrão conforme sua preferência para uso em outros módulos do projeto.

"""

import os
import sys
import tempfile
from pathlib import Path

from PIL import Image

# Adicionar diretório do projeto ao Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))


def create_test_images():
    """Cria diferentes tipos de imagens para teste"""

    test_images = []

    # 1. Imagem quadrada (1:1)
    square_img = Image.new("RGB", (600, 600))
    for x in range(600):
        for y in range(600):
            # Gradiente azul
            r = int(50 + (x / 600) * 100)
            g = int(100 + (y / 600) * 100)
            b = 255
            square_img.putpixel((x, y), (r, g, b))

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_square:
        square_path = tmp_square.name
    square_img.save(square_path, "JPEG", quality=95)
    test_images.append(("Quadrada (1:1)", square_path))

    # 2. Imagem paisagem (16:9)
    landscape_img = Image.new("RGB", (800, 450))
    for x in range(800):
        for y in range(450):
            # Gradiente verde
            r = int(100 + (x / 800) * 100)
            g = 255
            b = int(50 + (y / 450) * 100)
            landscape_img.putpixel((x, y), (r, g, b))

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_landscape:
        landscape_path = tmp_landscape.name
    landscape_img.save(landscape_path, "JPEG", quality=95)
    test_images.append(("Paisagem (16:9)", landscape_path))

    # 3. Imagem retrato (9:16)
    portrait_img = Image.new("RGB", (450, 800))
    for x in range(450):
        for y in range(800):
            # Gradiente vermelho
            r = 255
            g = int(100 + (x / 450) * 100)
            b = int(50 + (y / 800) * 100)
            portrait_img.putpixel((x, y), (r, g, b))

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_portrait:
        portrait_path = tmp_portrait.name
    portrait_img.save(portrait_path, "JPEG", quality=95)
    test_images.append(("Retrato (9:16)", portrait_path))

    print("📷 Imagens de teste criadas:")
    for name, path in test_images:
        with Image.open(path) as img:
            print(f"   {name}: {img.size} - {path}")

    return test_images


def test_fit_modes():
    """Testa diferentes modos de enquadramento"""

    try:
        from agent_social_media.core.instagram.border import ImageWithBorder

        print("🧪 TESTANDO MODOS DE ENQUADRAMENTO")
        print("=" * 60)

        # Verificar moldura
        frame_path = str(project_root / "assets" / "moldura.png")
        if not os.path.exists(frame_path):
            print(f"❌ Moldura não encontrada: {frame_path}")
            return False

        with Image.open(frame_path) as frame:
            print(f"🖼️ Moldura - Size: {frame.size}, Mode: {frame.mode}")

        # Criar imagens de teste
        test_images = create_test_images()

        # Modos de enquadramento
        fit_modes = [
            ("fill", "Preenche toda moldura (pode cortar)"),
            ("fit", "Mantém imagem completa (pode ter espaços)"),
            ("stretch", "Estica para preencher (pode distorcer)"),
        ]

        results = []

        for mode, description in fit_modes:
            print(f"\n🔹 Testando modo: {mode} - {description}")

            for img_name, img_path in test_images:
                print(f"   📸 Processando: {img_name}")

                # Criar nome do arquivo resultado
                output_name = f"result_{mode}_{img_name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace(':', 'x')}.jpg"
                with tempfile.NamedTemporaryFile(
                    suffix=f"_{output_name}", delete=False
                ) as tmp_output:
                    output_path = tmp_output.name

                try:
                    ImageWithBorder.create_bordered_image(
                        image_path=img_path,
                        border_path=frame_path,
                        output_path=output_path,
                        target_size=None,  # Usar dimensões da moldura
                        fit_mode=mode,
                    )

                    results.append((mode, img_name, output_path))
                    print(f"   ✅ Resultado: {output_path}")

                except Exception as e:
                    print(f"   ❌ Erro: {e}")

        # Relatório final
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO DOS TESTES")
        print("=" * 60)

        for mode, description in fit_modes:
            print(f"\n🔹 Modo {mode}: {description}")
            mode_results = [r for r in results if r[0] == mode]
            for _, img_name, output_path in mode_results:
                with Image.open(output_path) as result:
                    print(f"   {img_name}: {result.size} → {output_path}")

        print("\n💡 RECOMENDAÇÕES:")
        print("   • Use 'fill' se quiser que a imagem preencha toda a moldura")
        print("   • Use 'fit' se quiser preservar a imagem completa")
        print("   • Use 'stretch' apenas se não se importar com distorção")

        print("\n📁 Todos os resultados salvos em arquivos temporários")
        print("🔍 Compare visualmente para escolher o melhor modo!")

        return True

    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro durante teste: {e}")
        return False


def configure_fit_mode(mode="fill"):
    """
    Configura o modo de enquadramento padrão no sistema

    Args:
        mode (str): "fill", "fit", ou "stretch"
    """

    # Arquivo de configuração (você pode criar um config.py para isso)
    config_content = f'''
# Configuração de enquadramento de molduras
FRAME_FIT_MODE = "{mode}"

# Descrições dos modos:
# "fill": Preenche toda a moldura (pode cortar partes da imagem)
# "fit": Mantém a imagem completa (pode ter espaços vazios)
# "stretch": Estica para preencher (pode distorcer a imagem)
'''

    config_path = project_root / "frame_config.py"
    with open(config_path, "w") as f:
        f.write(config_content)

    print(f"✅ Modo de enquadramento configurado: {mode}")
    print(f"📝 Configuração salva em: {config_path}")


def main():
    """Executa os testes de enquadramento"""

    print("🖼️ CONFIGURADOR DE ENQUADRAMENTO DE MOLDURAS")
    print("🎯 Teste diferentes modos para encontrar o melhor ajuste")
    print("=" * 70)

    success = test_fit_modes()

    if success:
        print("\n" + "=" * 70)
        print("✅ TESTES CONCLUÍDOS COM SUCESSO")
        print("\n🔧 Para aplicar um modo específico, edite o código em:")
        print("   src/agent_social_media/core/services/instagram_send.py")
        print("   Mude o parâmetro fit_mode='fill' para:")
        print("   • fit_mode='fill' (recomendado para preencher a moldura)")
        print("   • fit_mode='fit' (para preservar a imagem completa)")
        print("   • fit_mode='stretch' (para esticar sem cortar)")

        # Configurar modo padrão como "fill" que geralmente dá melhores resultados
        configure_fit_mode("fill")
    else:
        print("❌ Falha nos testes")

    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
