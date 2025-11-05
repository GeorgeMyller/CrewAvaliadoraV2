"""
Módulo de processamento de imagens para uso em redes sociais (Instagram).
Este módulo fornece funcionalidades para:
- Validação de arquivos de imagem, verificando formato, dimensões e integridade.
- Tentativa de reparo de imagens corrompidas.
- Processamento de imagens, incluindo redimensionamento, aplicação de filtros do Instagram (via pilgram) e otimização para publicação.
- Limpeza de diretórios temporários, removendo arquivos antigos, corrompidos ou inválidos.
- Aplicação de bordas personalizadas em imagens, ajustando proporções e transparências.
Principais classes e métodos:
- FilterImage.validate_image: Valida se o arquivo é uma imagem suportada e íntegra.
- FilterImage.repair_image: Tenta reparar imagens corrompidas e salva uma versão recuperada.
- FilterImage.process: Processa a imagem, aplicando validação, reparo, filtro Instagram e otimização.
- FilterImage.clean_temp_directory: Remove arquivos temporários antigos ou inválidos de um diretório.
- FilterImage.apply_border: Aplica uma borda personalizada à imagem, ajustando proporções e transparências.
Dependências:
- Pillow (PIL)
- pilgram
- logging
Uso recomendado para automação de postagens e preparação de imagens para redes sociais.



"""

import sys
import os
import time
import shutil
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import os
from PIL import Image, UnidentifiedImageError
import pilgram

logger = logging.getLogger(__name__)


class FilterImage:

    @staticmethod
    def validate_image(image_path):
        """
        Valida se o arquivo é uma imagem válida e pode ser processada.
        
        Args:
            image_path (str): Caminho para o arquivo de imagem
            
        Returns:
            bool: True se a imagem é válida, False caso contrário
        """
        try:
            # Verificar se o arquivo existe
            if not os.path.exists(image_path):
                logger.error(f"Erro: Arquivo não encontrado: {image_path}")
                return False
            
            # Verificar se o arquivo não está vazio
            if os.path.getsize(image_path) == 0:
                logger.error(f"Erro: Arquivo vazio: {image_path}")
                return False
            
            # Tentar abrir a imagem
            with Image.open(image_path) as img:
                # Verificar se é uma imagem válida tentando acessar suas propriedades
                img.verify()
                
            # Reabrir para uso (verify() fecha o arquivo)
            with Image.open(image_path) as img:
                # Verificar formato suportado
                if img.format not in ['JPEG', 'PNG', 'WEBP', 'BMP']:
                    logger.error(f"Erro: Formato não suportado: {img.format}")
                    return False
                
                # Verificar dimensões mínimas
                if img.size[0] < 10 or img.size[1] < 10:
                    logger.error(f"Erro: Imagem muito pequena: {img.size}")
                    return False
                    
            return True
            
        except UnidentifiedImageError:
            logger.error(f"Erro: Não é possível identificar a imagem: {image_path}")
            return False
        except Exception as e:
            logger.error(f"Erro ao validar imagem {image_path}: {e}")
            return False

    @staticmethod
    def repair_image(image_path):
        """
        Tenta reparar uma imagem corrompida.
        
        Args:
            image_path (str): Caminho para o arquivo de imagem
            
        Returns:
            str: Caminho para a imagem reparada ou None se não foi possível reparar
        """
        try:
            logger.info(f"Tentando reparar imagem: {image_path}")
            
            # Criar backup do arquivo original
            backup_path = f"{image_path}.backup"
            shutil.copy2(image_path, backup_path)
            
            # Tentar diferentes métodos de reparo
            with open(image_path, 'rb') as f:
                data = f.read()
            
            # Verificar se há dados suficientes
            if len(data) < 100:
                logger.warning("Arquivo muito pequeno para ser uma imagem válida")
                return None
            
            # Tentar forçar abertura com PIL em modo resiliente
            try:
                with Image.open(image_path) as img:
                    # Converter para RGB se necessário
                    if img.mode not in ('RGB', 'RGBA'):
                        img = img.convert('RGB')
                    
                    # Salvar a imagem reparada
                    repaired_path = f"{os.path.splitext(image_path)[0]}_repaired.jpg"
                    img.save(repaired_path, 'JPEG', quality=95)
                    
                    logger.info(f"Imagem reparada salva em: {repaired_path}")
                    return repaired_path
                    
            except Exception as repair_error:
                logger.error(f"Falha ao reparar com PIL: {repair_error}")
                return None
                
        except Exception as e:
            logger.error(f"Erro durante reparo da imagem: {e}")
            return None

    @staticmethod
    def process(image_path, apply_filter=True, filter_type="mayfair"):
        """
        Processa a imagem aplicando validação, reparo se necessário, filtro opcional,
        e otimizações para Instagram.
        
        Args:
            image_path (str): Caminho da imagem
            apply_filter (bool): Se deve aplicar filtro (padrão: True)
            filter_type (str): Tipo de filtro a aplicar (padrão: "mayfair")
        """
        try:
            logger.info(f"🔄 Iniciando processamento da imagem: {image_path}")
            logger.info(f"🎨 Configurações: aplicar_filtro={apply_filter}, tipo_filtro={filter_type}")
            
            # Validar a imagem primeiro
            if not FilterImage.validate_image(image_path):
                logger.warning(f"⚠️ Imagem inválida detectada: {image_path}")
                
                # Tentar reparar a imagem
                repaired_path = FilterImage.repair_image(image_path)
                if repaired_path:
                    image_path = repaired_path
                    logger.info(f"✅ Usando imagem reparada: {image_path}")
                else:
                    raise ValueError(f"Não foi possível processar a imagem: {image_path}")
            
            # Abrir a imagem
            with Image.open(image_path) as im:
                logger.info(f"📊 Original - Size: {im.size}, Format: {im.format}, Mode: {im.mode}")
                
                # Converter para RGB se necessário
                if im.mode not in ('RGB', 'RGBA'):
                    logger.info(f"🔄 Convertendo de {im.mode} para RGB")
                    im = im.convert('RGB')
                
                # Verificar e ajustar dimensões para Instagram (mínimo 320x320, máximo 1080x1350)
                width, height = im.size
                
                # Se a imagem for muito pequena, redimensionar mantendo proporção
                if width < 320 or height < 320:
                    logger.info(f"📏 Imagem muito pequena ({width}x{height}), redimensionando...")
                    scale = max(320/width, 320/height)
                    new_width = int(width * scale)
                    new_height = int(height * scale)
                    im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    logger.info(f"📏 Nova dimensão: {im.size}")
                
                # Se a imagem for muito grande, redimensionar
                elif width > 1080 or height > 1350:
                    logger.info(f"📏 Imagem muito grande ({width}x{height}), redimensionando...")
                    scale = min(1080/width, 1350/height)
                    new_width = int(width * scale)
                    new_height = int(height * scale)
                    im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    logger.info(f"📏 Nova dimensão: {im.size}")
                
                # Aplicar filtro se solicitado
                if apply_filter:
                    logger.info(f"🎨 Aplicando filtro {filter_type}...")
                    if filter_type == "mayfair":
                        filtered_image = pilgram.mayfair(im)
                    elif filter_type == "aden":
                        filtered_image = pilgram.aden(im)
                    elif filter_type == "brooklyn":
                        filtered_image = pilgram.brooklyn(im)
                    elif filter_type == "clarendon":
                        filtered_image = pilgram.clarendon(im)
                    elif filter_type == "earlybird":
                        filtered_image = pilgram.earlybird(im)
                    elif filter_type == "gingham":
                        filtered_image = pilgram.gingham(im)
                    elif filter_type == "hudson":
                        filtered_image = pilgram.hudson(im)
                    elif filter_type == "inkwell":
                        filtered_image = pilgram.inkwell(im)
                    elif filter_type == "lark":
                        filtered_image = pilgram.lark(im)
                    elif filter_type == "lofi":
                        filtered_image = pilgram.lofi(im)
                    elif filter_type == "moon":
                        filtered_image = pilgram.moon(im)
                    elif filter_type == "nashville":
                        filtered_image = pilgram.nashville(im)
                    elif filter_type == "perpetua":
                        filtered_image = pilgram.perpetua(im)
                    elif filter_type == "reyes":
                        filtered_image = pilgram.reyes(im)
                    elif filter_type == "rise":
                        filtered_image = pilgram.rise(im)
                    elif filter_type == "slumber":
                        filtered_image = pilgram.slumber(im)
                    elif filter_type == "stinson":
                        filtered_image = pilgram.stinson(im)
                    elif filter_type == "toaster":
                        filtered_image = pilgram.toaster(im)
                    elif filter_type == "valencia":
                        filtered_image = pilgram.valencia(im)
                    elif filter_type == "walden":
                        filtered_image = pilgram.walden(im)
                    elif filter_type == "willow":
                        filtered_image = pilgram.willow(im)
                    elif filter_type == "xpro2":
                        filtered_image = pilgram.xpro2(im)
                    else:
                        logger.warning(f"⚠️ Filtro {filter_type} não reconhecido, usando mayfair")
                        filtered_image = pilgram.mayfair(im)
                else:
                    logger.info("📷 Pulando aplicação de filtro")
                    filtered_image = im
                
                # Otimizar qualidade e tamanho
                logger.info("💾 Salvando imagem otimizada...")
                filtered_image.save(
                    image_path, 
                    'JPEG', 
                    quality=95, 
                    optimize=True, 
                    progressive=True
                )

                logger.info(f"✅ Processamento concluído - Size: {filtered_image.size}, Mode: {filtered_image.mode}")
                return image_path
            
        except UnidentifiedImageError as e:
            logger.error(f"❌ Erro: Não é possível identificar a imagem {image_path}: {e}")
            raise ValueError(f"Imagem corrompida ou formato inválido: {image_path}")
        except Exception as e:
            logger.error(f"❌ Erro ao processar imagem {image_path}: {e}")
            raise

    @staticmethod
    def clean_temp_directory(temp_dir, max_age_seconds=3600):
        """
        Limpa o diretório temporário removendo arquivos mais antigos que max_age_seconds.
        Também remove arquivos corrompidos ou inválidos.
        """
        if not os.path.exists(temp_dir):
            return
            
        now = time.time()
        cleaned_count = 0
        total_size_cleaned = 0
        
        logger.info(f"🧹 Iniciando limpeza do diretório: {temp_dir}")
        
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            
            if not os.path.isfile(file_path):
                continue
                
            try:
                file_age = now - os.path.getmtime(file_path)
                file_size = os.path.getsize(file_path)
                
                should_remove = False
                reason = ""
                
                # Verificar idade do arquivo
                if file_age > max_age_seconds:
                    should_remove = True
                    reason = f"arquivo antigo ({file_age/3600:.1f}h)"
                
                # Verificar se é uma imagem válida (apenas para arquivos de imagem)
                elif filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp')):
                    if not FilterImage.validate_image(file_path):
                        should_remove = True
                        reason = "imagem corrompida/inválida"
                
                # Verificar arquivos muito pequenos (provavelmente corrompidos)
                elif file_size < 100:
                    should_remove = True
                    reason = "arquivo muito pequeno"
                
                if should_remove:
                    os.remove(file_path)
                    cleaned_count += 1
                    total_size_cleaned += file_size
                    logger.info(f"🗑️ Removido: {filename} ({reason})")
                    
            except Exception as e:
                logger.warning(f"⚠️ Erro ao processar {filename}: {e}")
                try:
                    os.remove(file_path)
                    cleaned_count += 1
                    logger.info(f"🗑️ Removido arquivo problemático: {filename}")
                except Exception as remove_error:
                    logger.warning(f"⚠️ Erro ao remover arquivo problemático {filename}: {remove_error}")
                    pass
        
        if cleaned_count > 0:
            logger.info(f"✅ Limpeza concluída: {cleaned_count} arquivos removidos ({total_size_cleaned/1024:.1f} KB liberados)")
        else:
            logger.info("✅ Nenhum arquivo para limpar")

    @staticmethod
    def apply_border(image_path: str, border_path: str) -> str:
        """
        Aplica uma borda à imagem fornecida.

        Args:
            image_path (str): Caminho da imagem original.
            border_path (str): Caminho da imagem da borda.

        Returns:
            str: Caminho da imagem com a borda aplicada.
        """
        try:
            logger.info(f"🖼️ Aplicando borda: {border_path} na imagem: {image_path}")
            
            # Abrir a imagem original e a borda
            original_image = Image.open(image_path)
            border_image = Image.open(border_path)
            
            logger.info(f"📊 Imagem original - Size: {original_image.size}, Mode: {original_image.mode}")
            logger.info(f"📊 Borda original - Size: {border_image.size}, Mode: {border_image.mode}")

            # Convert original image to RGB if it's RGBA to avoid transparency issues
            if original_image.mode in ("RGBA", "LA"):
                background = Image.new("RGB", original_image.size, (255, 255, 255))
                background.paste(original_image, mask=original_image.split()[-1])
                original_image = background
                logger.info("🔄 Imagem convertida para RGB")

            # Calcular as dimensões da borda para manter proporção
            border_width, border_height = border_image.size
            original_width, original_height = original_image.size
            
            # Calcular corte central da imagem original para se adequar à borda
            # mantendo a proporção da borda
            border_ratio = border_width / border_height
            original_ratio = original_width / original_height
            
            if border_ratio > original_ratio:
                # Borda é mais larga proporcionalmente - ajustar pela altura
                new_height = original_height
                new_width = int(original_height * border_ratio)
            else:
                # Borda é mais alta proporcionalmente - ajustar pela largura  
                new_width = original_width
                new_height = int(original_width / border_ratio)
            
            # Redimensionar a imagem original para se adequar à borda
            if new_width != original_width or new_height != original_height:
                # Calcular corte central
                left = (original_width - new_width) // 2 if new_width < original_width else 0
                top = (original_height - new_height) // 2 if new_height < original_height else 0
                right = left + min(new_width, original_width)
                bottom = top + min(new_height, original_height)
                
                # Se precisar expandir, criar nova imagem com fundo branco
                if new_width > original_width or new_height > original_height:
                    expanded_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))
                    paste_x = (new_width - original_width) // 2
                    paste_y = (new_height - original_height) // 2
                    expanded_image.paste(original_image, (paste_x, paste_y))
                    resized_image = expanded_image
                else:
                    # Cortar a imagem
                    resized_image = original_image.crop((left, top, right, bottom))
                
                logger.info(f"📏 Imagem ajustada - Size: {resized_image.size}")
            else:
                resized_image = original_image
            
            # Redimensionar a imagem para o tamanho exato da borda
            final_image = resized_image.resize((border_width, border_height), Image.Resampling.LANCZOS)
            
            # Criar imagem resultado com fundo da imagem
            result = Image.new("RGB", (border_width, border_height))
            result.paste(final_image, (0, 0))

            # Aplicar a borda com transparência se necessário
            if border_image.mode == "RGBA":
                # Use o canal alpha da borda como máscara
                mask = border_image.split()[3]
                result.paste(border_image.convert("RGB"), (0, 0), mask=mask)
                logger.info("🎨 Borda com transparência aplicada")
            else:
                # Borda sem transparência - aplicar diretamente
                result.paste(border_image.convert("RGB"), (0, 0))
                logger.info("🎨 Borda opaca aplicada")

            # Salvar a imagem com a borda aplicada
            bordered_image_path = os.path.join(
                os.path.dirname(image_path), f"bordered_{os.path.basename(image_path)}"
            )
            result.save(bordered_image_path, format="JPEG", quality=95)
            
            logger.info(f"✅ Borda aplicada com sucesso: {bordered_image_path}")
            logger.info(f"📊 Resultado final - Size: {result.size}, Mode: {result.mode}")

            return bordered_image_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao aplicar borda à imagem: {e}")
            raise


# Exemplo de uso:
# filepath = os.path.join(Paths.ROOT_DIR, "temp", "temp-1733594830377.png")
# image = FilterImage.process(filepath)
# FilterImage.clean_temp_directory(os.path.join(Paths.ROOT_DIR, "temp"))