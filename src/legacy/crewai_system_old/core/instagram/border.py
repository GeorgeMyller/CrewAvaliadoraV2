"""
Este módulo fornece a classe ImageWithBorder para adicionar bordas personalizadas a imagens usando a biblioteca Pillow (PIL).
Classes:
    ImageWithBorder:
        Métodos estáticos para criar imagens com bordas, ajustando o modo de encaixe conforme necessário.
Métodos:
    create_bordered_image(image_path, border_path, output_path, target_size=None, fit_mode="border_to_image"):
        Cria uma imagem com borda, ajustando o modo de encaixe conforme especificado.
        Modos disponíveis:
            - "border_to_image": Redimensiona a borda para o tamanho da imagem (recomendado).
            - "fill": Preenche toda a moldura, podendo cortar a imagem.
            - "fit": Mantém a imagem inteira, podendo deixar espaços vazios.
            - "stretch": Estica a imagem para preencher a moldura, podendo distorcer.
        Salva o resultado no caminho especificado.
    _fit_border_to_image(image, border):
        Ajusta a moldura ao tamanho da imagem, preservando a imagem original.
    _resize_to_fill(image, target_size):
        Redimensiona a imagem para preencher completamente o tamanho alvo, cortando partes se necessário.
    _resize_to_fit(image, target_size):
        Redimensiona a imagem para caber completamente no tamanho alvo, mantendo proporção e podendo deixar espaços vazios.
Dependências:
    - Pillow (PIL)
    - logging
Uso:
    Ideal para criar imagens para redes sociais com bordas personalizadas, mantendo flexibilidade nos modos de encaixe.

"""

from PIL import Image
import logging

logger = logging.getLogger(__name__)


class ImageWithBorder:
    @staticmethod
    def create_bordered_image(
        image_path, border_path, output_path, target_size=None, fit_mode="border_to_image"
    ):
        """
        Cria a imagem com a borda e salva no caminho especificado.

        Args:
            image_path (str): Caminho da imagem base.
            border_path (str): Caminho da borda.
            output_path (str): Caminho para salvar a imagem resultante.
            target_size (tuple): Dimensão alvo (largura, altura). Se None, usa dimensões da imagem.
            fit_mode (str): Como ajustar:
                          - "border_to_image": Ajusta moldura ao tamanho da imagem (NOVO - RECOMENDADO)
                          - "fill": Preenche toda a moldura (pode cortar imagem)
                          - "fit": Mantém imagem inteira (pode ter espaços vazios)
                          - "stretch": Estica a imagem (pode distorcer)
        Returns:
            str: Caminho da imagem resultante.
        """
        logger.info(f"🖼️ Criando imagem com moldura - Modo: {fit_mode}")
        
        # Abrir a imagem e a borda
        image = Image.open(image_path)
        border = Image.open(border_path)

        logger.info(f"📊 Imagem original - Size: {image.size}, Format: {image.format}, Mode: {image.mode}")
        logger.info(f"📊 Moldura original - Size: {border.size}, Format: {border.format}, Mode: {border.mode}")

        # Convert image to RGB if it's RGBA
        if image.mode in ("RGBA", "LA"):
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[-1])
            image = background
            logger.info("🔄 Imagem convertida para RGB")

        # NOVA LÓGICA: Ajustar moldura ao tamanho da imagem
        if fit_mode == "border_to_image":
            result = ImageWithBorder._fit_border_to_image(image, border)
            
        # Modos antigos (mantidos para compatibilidade)
        else:
            # Se target_size não foi especificado, usar dimensões da borda
            if target_size is None:
                target_size = border.size
                logger.info(f"📏 Usando dimensões da moldura como target: {target_size}")

            # Ajustar a imagem baseado no modo escolhido
            if fit_mode == "fill":
                processed_image = ImageWithBorder._resize_to_fill(image, target_size)
            elif fit_mode == "fit":
                processed_image = ImageWithBorder._resize_to_fit(image, target_size)
            elif fit_mode == "stretch":
                processed_image = image.resize(target_size, Image.Resampling.LANCZOS)
            else:
                processed_image = ImageWithBorder._resize_to_fill(image, target_size)

            logger.info(f"📊 Imagem processada - Size: {processed_image.size}, Mode: {processed_image.mode}")

            # Criar imagem resultado com as dimensões da borda
            result = Image.new("RGB", border.size, (255, 255, 255))
            
            # Calcular posição para centralizar a imagem processada na moldura
            paste_x = (border.size[0] - processed_image.size[0]) // 2
            paste_y = (border.size[1] - processed_image.size[1]) // 2
            
            # Colar a imagem processada
            result.paste(processed_image, (paste_x, paste_y))

            # Aplicar a borda com transparência se necessário
            if border.mode == "RGBA":
                mask = border.split()[3]
                result.paste(border.convert("RGB"), (0, 0), mask=mask)
                logger.info("🎨 Moldura com transparência aplicada")
            else:
                result.paste(border.convert("RGB"), (0, 0))
                logger.info("🎨 Moldura opaca aplicada")

        logger.info(f"📊 Resultado final - Size: {result.size}, Mode: {result.mode}")

        # Salvar a imagem resultante
        result.save(output_path, format="JPEG", quality=95)
        logger.info(f"✅ Imagem com moldura salva: {output_path}")
        
        return output_path

    @staticmethod
    def _fit_border_to_image(image, border):
        """
        NOVA FUNCIONALIDADE: Ajusta a moldura ao tamanho da imagem.
        A imagem permanece intacta e a moldura é redimensionada.
        """
        img_width, img_height = image.size
        border_width, border_height = border.size
        
        logger.info(f"🔄 Ajustando moldura ({border_width}x{border_height}) para imagem ({img_width}x{img_height})")
        
        # Redimensionar a moldura para o tamanho exato da imagem
        resized_border = border.resize((img_width, img_height), Image.Resampling.LANCZOS)
        logger.info(f"📏 Moldura redimensionada para: {resized_border.size}")
        
        # Criar resultado com o tamanho da imagem original
        result = Image.new("RGB", (img_width, img_height), (255, 255, 255))
        
        # Colar a imagem original (sem alterações)
        result.paste(image, (0, 0))
        logger.info("📷 Imagem original colada (sem cortes)")
        
        # Aplicar a moldura redimensionada
        if resized_border.mode == "RGBA":
            # Use o canal alpha da borda como máscara
            mask = resized_border.split()[3]
            result.paste(resized_border.convert("RGB"), (0, 0), mask=mask)
            logger.info("🎨 Moldura redimensionada com transparência aplicada")
        else:
            # Borda sem transparência - aplicar diretamente
            result.paste(resized_border.convert("RGB"), (0, 0))
            logger.info("🎨 Moldura redimensionada opaca aplicada")
        
        logger.info("✅ Moldura ajustada ao tamanho da imagem - IMAGEM PRESERVADA COMPLETAMENTE")
        return result

    @staticmethod
    def _resize_to_fill(image, target_size):
        """
        Redimensiona a imagem para preencher completamente o target_size,
        cortando partes se necessário (mantém proporção).
        """
        target_width, target_height = target_size
        img_width, img_height = image.size
        
        # Calcular escalas para largura e altura
        scale_w = target_width / img_width
        scale_h = target_height / img_height
        
        # Usar a maior escala para garantir que preencha completamente
        scale = max(scale_w, scale_h)
        
        # Redimensionar com a escala calculada
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Se redimensionado for maior que target, fazer crop central
        if new_width > target_width or new_height > target_height:
            left = (new_width - target_width) // 2
            top = (new_height - target_height) // 2
            right = left + target_width
            bottom = top + target_height
            resized_image = resized_image.crop((left, top, right, bottom))
        
        return resized_image

    @staticmethod
    def _resize_to_fit(image, target_size):
        """
        Redimensiona a imagem para caber completamente no target_size,
        mantendo proporção (pode ter espaços vazios).
        """
        target_width, target_height = target_size
        img_width, img_height = image.size
        
        # Calcular escalas para largura e altura
        scale_w = target_width / img_width
        scale_h = target_height / img_height
        
        # Usar a menor escala para garantir que caiba completamente
        scale = min(scale_w, scale_h)
        
        # Redimensionar com a escala calculada
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        return resized_image