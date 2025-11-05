""" 
Este módulo fornece a classe InstagramImageValidator para validação e processamento de imagens conforme os requisitos oficiais do Instagram.
Funcionalidades principais:
- Validação de imagens para diferentes tipos de postagens (feed, stories, reels, carrossel), incluindo checagem de dimensões, proporção, formato e tamanho do arquivo.
- Normalização automática de imagens para carrossel, garantindo proporções consistentes e dimensões adequadas.
- Redimensionamento e otimização de imagens para atender aos limites da plataforma.
- Correção inteligente do aspect ratio baseada no tipo de conteúdo.
- Processamento completo de fotos individuais, simulando o fluxo de publicação via API do Instagram.
- Métodos utilitários para validação detalhada e recomendações de ajustes conforme as regras da API oficial.
Requisitos:
- Pillow (PIL) para manipulação de imagens.
- Logging para registro de operações e erros.
Uso recomendado para automação de publicações, validação prévia de conteúdo e integração com fluxos de mídia social.


"""


from PIL import Image
import os
import logging
import time

logger = logging.getLogger(__name__)


class InstagramImageValidator:
    """
    Validates images for Instagram posting requirements.
    Performs checks required by Instagram's API for various post types.
    """

    # Instagram API requirements atualizados com base na documentação oficial
    MIN_IMG_SIZE = 320  # Minimum size in pixels (each dimension)
    MAX_IMG_SIZE = 1440  # Maximum size in pixels (each dimension)
    CAROUSEL_RATIO_TOLERANCE = 0.02  # 2% tolerance for aspect ratio consistency

    # Instagram supported aspect ratios - REQUISITOS OFICIAIS
    # Feed Posts: 1.91:1 (landscape) até 4:5 (portrait)
    MIN_ASPECT_RATIO = 0.8  # 4:5 portrait orientation (1080x1350)
    MAX_ASPECT_RATIO = 1.91  # Landscape orientation (1080x566)
    SQUARE_RATIO = 1.0  # 1:1 square (1080x1080) - SEMPRE ACEITO
    
    # Stories e Reels: 9:16 (720x1280 mínimo)
    STORIES_RATIO = 9/16  # 0.5625 para stories/reels
    STORIES_MIN_WIDTH = 720
    STORIES_MIN_HEIGHT = 1280

    @classmethod
    def validate_for_carousel(cls, image_paths, auto_normalize=False):
        """
        Validates that all images meet Instagram's carousel requirements.

        Args:
            image_paths (list): List of paths to images to be included in carousel
            auto_normalize (bool): If True, automatically normalize images

        Returns:
            tuple: If auto_normalize is False: (is_valid, message)
                  If auto_normalize is True: (is_valid, message, normalized_paths)
        """
        if not image_paths or len(image_paths) < 2:
            return (
                (False, "Carrossel precisa de pelo menos 2 imagens")
                if not auto_normalize
                else (False, "Carrossel precisa de pelo menos 2 imagens", [])
            )

        if len(image_paths) > 10:  # Instagram maximum
            return (
                (False, "Máximo de 10 imagens permitidas no carrossel")
                if not auto_normalize
                else (False, "Máximo de 10 imagens permitidas no carrossel", [])
            )

        # If auto_normalize is enabled, normalize images before validation
        if auto_normalize:
            normalized_paths = cls.normalize_for_carousel(image_paths)
            if normalized_paths:
                validation_result, message = cls.validate_for_carousel(
                    normalized_paths, auto_normalize=False
                )
                return validation_result, message, normalized_paths
            return False, "Falha ao normalizar imagens", []

        # Track aspect ratios for consistency check
        aspect_ratios = []
        invalid_images = []

        for i, img_path in enumerate(image_paths):
            try:
                if not os.path.exists(img_path):
                    invalid_images.append(f"Imagem {i+1}: arquivo não encontrado")
                    continue

                with Image.open(img_path) as img:
                    width, height = img.size

                    # Check dimensions
                    if width < cls.MIN_IMG_SIZE or height < cls.MIN_IMG_SIZE:
                        invalid_images.append(
                            f"Imagem {i+1}: tamanho muito pequeno ({width}x{height})"
                        )
                        continue

                    if width > cls.MAX_IMG_SIZE or height > cls.MAX_IMG_SIZE:
                        invalid_images.append(
                            f"Imagem {i+1}: tamanho muito grande ({width}x{height})"
                        )
                        continue

                    # Calculate aspect ratio
                    aspect_ratio = width / height
                    aspect_ratios.append(aspect_ratio)

                    # Check format (Instagram accepts JPEG)
                    if img.format not in ["JPEG", "JPG"]:
                        logger.warning(
                            f"Imagem {i+1} não está em formato JPEG/JPG. Formato atual: {img.format}"
                        )

            except Exception as e:
                invalid_images.append(f"Imagem {i+1}: erro ao processar ({str(e)})")

        if invalid_images:
            return False, "Problemas encontrados:\n• " + "\n• ".join(invalid_images)

        # Check if all aspect ratios are similar (Instagram requires consistent ratios)
        if aspect_ratios:
            first_ratio = aspect_ratios[0]
            for i, ratio in enumerate(aspect_ratios[1:], 2):
                # Allow tolerance
                if (
                    abs(first_ratio - ratio) / first_ratio
                    > cls.CAROUSEL_RATIO_TOLERANCE
                ):
                    return (
                        False,
                        f"As imagens devem ter proporções similares. Imagem 1 ({first_ratio:.2f}:1) difere da imagem {i} ({ratio:.2f}:1)",
                    )

        return True, "Todas as imagens são válidas para o carrossel"

    @classmethod
    def normalize_for_carousel(cls, image_paths):
        """
        Normalizes a list of images for Instagram carousel use.
        Resizes images that exceed max dimensions and ensures consistent aspect ratios.

        Args:
            image_paths (list): List of paths to images

        Returns:
            list: List of paths to normalized images
        """
        if not image_paths or len(image_paths) < 2:
            return []

        normalized_paths = []
        valid_image_data = (
            []
        )  # Store (path, width, height, aspect_ratio) for valid images

        # First pass: collect valid images and their properties
        for path in image_paths:
            try:
                if not os.path.exists(path):
                    logger.error(f"Arquivo não encontrado: {path}")
                    continue

                with Image.open(path) as img:
                    width, height = img.size
                    aspect_ratio = width / height
                    valid_image_data.append((path, width, height, aspect_ratio))
            except Exception as e:
                logger.error(f"Erro ao processar imagem {path}: {str(e)}")

        if not valid_image_data:
            return []

        # Find the most common aspect ratio (or use the first one)
        # For simplicity, we'll use the first valid image's aspect ratio as target
        target_ratio = valid_image_data[0][3]

        # Second pass: resize and crop images to match target ratio and size limits
        for path, width, height, ratio in valid_image_data:
            try:
                # First resize if needed
                resized_path = cls.resize_for_instagram(path)

                # Now adjust aspect ratio if needed
                if (
                    abs(ratio - target_ratio) / target_ratio
                    > cls.CAROUSEL_RATIO_TOLERANCE
                ):
                    with Image.open(resized_path) as img:
                        width, height = img.size

                        # Create a new filename for the aspect-adjusted image
                        filename, ext = os.path.splitext(resized_path)
                        output_path = f"{filename}_adjusted{ext}"

                        # Calculate crop dimensions to match target ratio
                        if ratio > target_ratio:  # Image is wider than target
                            new_width = int(height * target_ratio)
                            left = (width - new_width) // 2
                            right = left + new_width
                            crop_box = (left, 0, right, height)
                        else:  # Image is taller than target
                            new_height = int(width / target_ratio)
                            top = (height - new_height) // 2
                            bottom = top + new_height
                            crop_box = (0, top, width, bottom)

                        # Crop and save
                        cropped_img = img.crop(crop_box)
                        cropped_img.save(output_path, quality=95)
                        normalized_paths.append(output_path)
                        logger.info(
                            f"Imagem ajustada para proporção alvo: {path} -> {output_path}"
                        )
                else:
                    # No aspect ratio adjustment needed
                    normalized_paths.append(resized_path)
            except Exception as e:
                logger.error(f"Falha ao normalizar imagem {path}: {str(e)}")

        return normalized_paths

    @classmethod
    def resize_for_instagram(cls, image_path, output_path=None):
        """
        Resizes an image to fit Instagram requirements if needed.

        Args:
            image_path (str): Path to the image file
            output_path (str, optional): Output path for the resized image

        Returns:
            str: Path to the resized image
        """
        if output_path is None:
            filename, ext = os.path.splitext(image_path)
            output_path = f"{filename}_resized{ext}"

        try:
            with Image.open(image_path) as img:
                width, height = img.size

                # Check if resizing is needed
                if width > cls.MAX_IMG_SIZE or height > cls.MAX_IMG_SIZE:
                    # Calculate new dimensions while maintaining aspect ratio
                    if width > height:
                        new_width = cls.MAX_IMG_SIZE
                        new_height = int(height * (cls.MAX_IMG_SIZE / width))
                    else:
                        new_height = cls.MAX_IMG_SIZE
                        new_width = int(width * (cls.MAX_IMG_SIZE / height))

                    # Resize image
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    img.save(output_path, quality=95)
                    logger.info(
                        f"Imagem redimensionada: {width}x{height} -> {new_width}x{new_height}"
                    )
                    return output_path

                # If no resizing needed, return original path
                return image_path

        except Exception as e:
            logger.error(f"Erro ao redimensionar imagem: {str(e)}")
            return image_path

    @classmethod
    def process_single_photo(cls, image_path, output_dir=None):
        """
        Process a single photo for Instagram following the container workflow:
        1. Validates the image
        2. Optimizes/resizes if needed (corresponds to container processing)
        3. Prepares for publication
        4. Returns the ready-to-publish image path

        Args:
            image_path (str): Path to the original image
            output_dir (str, optional): Directory to save processed image

        Returns:
            dict: {
                'status': str ('success', 'error'),
                'image_path': str (path to processed image),
                'message': str (details about processing),
                'original_path': str (original image path)
            }
        """
        result = {
            "status": "error",
            "original_path": image_path,
            "image_path": None,
            "message": "",
        }

        try:
            # 1. Check if file exists
            if not os.path.exists(image_path):
                result["message"] = "Arquivo não encontrado"
                logger.error(f"Image not found: {image_path}")
                return result

            # 2. Initial validation (simulates container creation)
            is_valid, issues = cls.validate_single_photo(image_path)
            if not is_valid:
                result["message"] = f"Validação falhou: {issues}"
                logger.warning(f"Image validation failed: {issues}")

                # Attempt to fix issues by optimizing (simulates container processing)
                logger.info(f"Attempting to optimize image: {image_path}")

            # 3. Processing phase (simulates IN_PROGRESS container status)
            logger.info(f"Processing image: {image_path}")
            processed_path = cls.optimize_for_instagram(image_path, output_dir)

            # 4. Final validation (simulates FINISHED container status)
            is_valid, issues = cls.validate_single_photo(processed_path)
            if not is_valid:
                result["message"] = (
                    f"Imagem processada ainda não atende requisitos: {issues}"
                )
                return result

            # 5. Ready for publication (simulates media_publish step)
            result["status"] = "success"
            result["image_path"] = processed_path
            result["message"] = "Imagem processada com sucesso e pronta para publicação"

            return result

        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            result["message"] = f"Erro ao processar imagem: {str(e)}"
            return result

    @classmethod
    def validate_single_photo(cls, image_path):
        """
        Validates a single photo against Instagram requirements.

        Args:
            image_path (str): Path to image file

        Returns:
            tuple: (is_valid, message)
        """
        issues = []

        try:
            if not os.path.exists(image_path):
                return False, "Arquivo não encontrado"

            with Image.open(image_path) as img:
                width, height = img.size

                # Check dimensions
                if width < cls.MIN_IMG_SIZE or height < cls.MIN_IMG_SIZE:
                    issues.append(f"Tamanho muito pequeno ({width}x{height})")

                if width > cls.MAX_IMG_SIZE or height > cls.MAX_IMG_SIZE:
                    issues.append(f"Tamanho muito grande ({width}x{height})")

                # Check aspect ratio
                aspect_ratio = width / height
                if aspect_ratio < cls.MIN_ASPECT_RATIO:
                    issues.append(f"Proporção muito estreita ({aspect_ratio:.2f}:1)")
                elif aspect_ratio > cls.MAX_ASPECT_RATIO:
                    issues.append(f"Proporção muito larga ({aspect_ratio:.2f}:1)")

                # Check format
                if img.format not in ["JPEG", "JPG", "PNG"]:
                    issues.append(f"Formato não suportado ({img.format})")

                # Check file size
                file_size_mb = os.path.getsize(image_path) / (1024 * 1024)
                if file_size_mb > 8:  # Instagram's 8MB limit
                    issues.append(f"Arquivo muito grande ({file_size_mb:.2f}MB)")

        except Exception as e:
            return False, f"Erro ao processar imagem: {str(e)}"

        if issues:
            return False, "; ".join(issues)
        return True, "Imagem válida para Instagram"

    @classmethod
    def optimize_for_instagram(cls, image_path, output_dir=None):
        """
        Optimize an image for Instagram by:
        1. Resizing to fit dimensions
        2. Correcting aspect ratio if needed
        3. Ensuring proper format

        Args:
            image_path (str): Path to original image
            output_dir (str, optional): Directory to save optimized image

        Returns:
            str: Path to optimized image
        """
        try:
            with Image.open(image_path) as img:
                # First resize if needed
                resized = cls.resize_for_instagram(image_path)

                # Generate output path
                if output_dir:
                    os.makedirs(output_dir, exist_ok=True)
                    base_name = os.path.basename(image_path)
                    optimized_path = os.path.join(
                        output_dir, f"optimized_{int(time.time())}_{base_name}"
                    )
                else:
                    filename, ext = os.path.splitext(resized)
                    optimized_path = f"{filename}_optimized{ext}"

                # Check aspect ratio and crop if needed
                with Image.open(resized) as img:
                    width, height = img.size
                    aspect_ratio = width / height

                    # Only fix aspect ratio if outside Instagram limits
                    if aspect_ratio < cls.MIN_ASPECT_RATIO:
                        # Too narrow, crop height
                        new_height = int(width / cls.MIN_ASPECT_RATIO)
                        top = (height - new_height) // 2
                        bottom = top + new_height
                        crop_box = (0, top, width, bottom)
                        img = img.crop(crop_box)

                    elif aspect_ratio > cls.MAX_ASPECT_RATIO:
                        # Too wide, crop width
                        new_width = int(height * cls.MAX_ASPECT_RATIO)
                        left = (width - new_width) // 2
                        right = left + new_width
                        crop_box = (left, 0, right, height)
                        img = img.crop(crop_box)

                    # Convert to RGB if needed
                    if img.mode not in ("RGB", "L"):
                        img = img.convert("RGB")

                    # Save as JPEG for best compatibility
                    img.save(optimized_path, format="JPEG", quality=95)
                    logger.info(f"Image optimized: {image_path} -> {optimized_path}")

                    return optimized_path

        except Exception as e:
            logger.error(f"Error optimizing image: {str(e)}")
            return image_path  # Return original if optimization fails

    @classmethod
    def fix_aspect_ratio(cls, image_path, output_path=None, content_type="feed"):
        """
        Corrige o aspect ratio de uma imagem para atender aos requisitos oficiais do Instagram.
        Usa estratégia inteligente baseada no tipo de conteúdo e dimensões originais.
        
        Args:
            image_path (str): Caminho para a imagem
            output_path (str, optional): Caminho de saída
            content_type (str): Tipo de conteúdo ("feed", "story", "reel", "carousel")
            
        Returns:
            str: Caminho da imagem corrigida
        """
        if output_path is None:
            filename, ext = os.path.splitext(image_path)
            output_path = f"{filename}_fixed_ratio{ext}"
            
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                current_ratio = width / height
                
                logger.info(f"Imagem original: {width}x{height}, ratio: {current_ratio:.3f}, tipo: {content_type}")
                
                # Determinar ratio alvo baseado no tipo de conteúdo e dimensões originais
                target_ratio = cls._determine_best_ratio(current_ratio, width, height, content_type)
                
                # Se já está dentro dos limites para o tipo de conteúdo, não precisa corrigir
                if cls._is_ratio_valid(current_ratio, content_type):
                    logger.info(f"Aspect ratio {current_ratio:.3f} já é válido para {content_type}")
                    return image_path
                
                logger.info(f"Corrigindo ratio de {current_ratio:.3f} para {target_ratio:.3f}")
                
                # Calcular novas dimensões com crop centralizado
                if current_ratio < target_ratio:
                    # Imagem muito alta - cortar altura
                    new_height = int(width / target_ratio)
                    new_width = width
                    crop_y = (height - new_height) // 2
                    crop_box = (0, crop_y, width, crop_y + new_height)
                else:
                    # Imagem muito larga - cortar largura
                    new_width = int(height * target_ratio)
                    new_height = height
                    crop_x = (width - new_width) // 2
                    crop_box = (crop_x, 0, crop_x + new_width, height)
                
                # Aplicar crop
                img_cropped = img.crop(crop_box)
                
                # Ajustar tamanho se necessário
                img_final = cls._resize_if_needed(img_cropped, content_type)
                
                # Salvar imagem corrigida com qualidade otimizada
                if img_final.mode == 'RGBA':
                    # Converter RGBA para RGB para JPEG
                    background = Image.new('RGB', img_final.size, (255, 255, 255))
                    background.paste(img_final, mask=img_final.split()[-1])
                    img_final = background
                
                img_final.save(output_path, 'JPEG', quality=90, optimize=True)
                
                final_ratio = img_final.width / img_final.height
                logger.info(f"Imagem corrigida: {img_final.width}x{img_final.height}, ratio: {final_ratio:.3f}")
                
                return output_path
                
        except Exception as e:
            logger.error(f"Erro ao corrigir aspect ratio: {str(e)}")
            return image_path  # Retorna original se falhar
    
    @classmethod
    def _determine_best_ratio(cls, current_ratio, width, height, content_type):
        """Determina o melhor ratio alvo baseado nas características da imagem"""
        
        if content_type in ["story", "reel"]:
            return cls.STORIES_RATIO  # 9:16 para stories/reels
        
        # Para feed posts, escolher o ratio mais próximo que seja válido
        if content_type in ["feed", "carousel"]:
            # Se está próximo do quadrado, usar 1:1 (sempre aceito)
            if 0.9 <= current_ratio <= 1.1:
                return cls.SQUARE_RATIO
            
            # Se é muito vertical, usar 4:5 (portrait padrão)
            elif current_ratio < 0.9:
                return cls.MIN_ASPECT_RATIO  # 4:5
            
            # Se é horizontal, usar 1.91:1 (landscape padrão)
            else:
                return cls.MAX_ASPECT_RATIO  # 1.91:1
        
        # Default para feed quadrado
        return cls.SQUARE_RATIO
    
    @classmethod
    def _is_ratio_valid(cls, ratio, content_type):
        """Verifica se o ratio é válido para o tipo de conteúdo"""
        
        if content_type in ["story", "reel"]:
            # Stories/Reels: aceita próximo de 9:16
            return abs(ratio - cls.STORIES_RATIO) < 0.05
        
        elif content_type in ["feed", "carousel"]:
            # Feed: entre 4:5 e 1.91:1
            return cls.MIN_ASPECT_RATIO <= ratio <= cls.MAX_ASPECT_RATIO
        
        return False
    
    @classmethod 
    def _resize_if_needed(cls, img, content_type):
        """Redimensiona se necessário baseado nos requisitos do tipo de conteúdo"""
        
        width, height = img.size
        
        if content_type in ["story", "reel"]:
            # Stories precisam de mínimo 720x1280
            if width < cls.STORIES_MIN_WIDTH or height < cls.STORIES_MIN_HEIGHT:
                scale_factor = max(
                    cls.STORIES_MIN_WIDTH / width,
                    cls.STORIES_MIN_HEIGHT / height
                )
                new_size = (int(width * scale_factor), int(height * scale_factor))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                logger.info(f"Redimensionado para stories: {new_size}")
        
        else:
            # Feed posts: garantir limites gerais
            if width < cls.MIN_IMG_SIZE or height < cls.MIN_IMG_SIZE:
                scale_factor = max(cls.MIN_IMG_SIZE / width, cls.MIN_IMG_SIZE / height)
                new_size = (int(width * scale_factor), int(height * scale_factor))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                logger.info(f"Redimensionado para tamanho mínimo: {new_size}")
            
            elif width > cls.MAX_IMG_SIZE or height > cls.MAX_IMG_SIZE:
                scale_factor = min(cls.MAX_IMG_SIZE / width, cls.MAX_IMG_SIZE / height)
                new_size = (int(width * scale_factor), int(height * scale_factor))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                logger.info(f"Redimensionado para tamanho máximo: {new_size}")
        
        return img

    @classmethod
    def validate_for_instagram_api(cls, image_path, content_type="feed"):
        """
        Valida se uma imagem atende aos requisitos da API do Instagram.
        Baseado na documentação oficial da Instagram Platform API v23.
        
        Args:
            image_path (str): Caminho para a imagem
            content_type (str): Tipo de conteúdo ("feed", "story", "reel", "carousel")
            
        Returns:
            tuple: (is_valid, issues_list, recommendations)
        """
        issues = []
        recommendations = []
        
        try:
            if not os.path.exists(image_path):
                return False, ["Arquivo não encontrado"], []

            with Image.open(image_path) as img:
                width, height = img.size
                aspect_ratio = width / height
                
                logger.info(f"Validando {content_type}: {width}x{height}, ratio: {aspect_ratio:.3f}")
                
                # Verificar formato (JPEG obrigatório para feed)
                if content_type == "feed" and img.format not in ['JPEG', 'JPG']:
                    issues.append(f"Formato {img.format} não suportado para feed. Use JPEG.")
                    recommendations.append("Converter para JPEG")
                
                # Verificar dimensões mínimas
                if content_type in ["story", "reel"]:
                    if width < cls.STORIES_MIN_WIDTH or height < cls.STORIES_MIN_HEIGHT:
                        issues.append(f"Dimensões muito pequenas para {content_type}: {width}x{height}")
                        recommendations.append(f"Redimensionar para pelo menos {cls.STORIES_MIN_WIDTH}x{cls.STORIES_MIN_HEIGHT}")
                        
                    # Verificar aspect ratio para stories/reels (9:16)
                    if not cls._is_ratio_valid(aspect_ratio, content_type):
                        issues.append(f"Aspect ratio {aspect_ratio:.3f} inválido para {content_type}")
                        recommendations.append("Ajustar para proporção 9:16 (0.563)")
                        
                else:
                    # Feed posts
                    if width < cls.MIN_IMG_SIZE or height < cls.MIN_IMG_SIZE:
                        issues.append(f"Dimensões muito pequenas: {width}x{height}")
                        recommendations.append(f"Redimensionar para pelo menos {cls.MIN_IMG_SIZE}x{cls.MIN_IMG_SIZE}")
                    
                    if width > cls.MAX_IMG_SIZE or height > cls.MAX_IMG_SIZE:
                        issues.append(f"Dimensões muito grandes: {width}x{height}")
                        recommendations.append(f"Redimensionar para máximo {cls.MAX_IMG_SIZE}x{cls.MAX_IMG_SIZE}")
                    
                    # Verificar aspect ratio para feed
                    if not cls._is_ratio_valid(aspect_ratio, content_type):
                        issues.append(f"Aspect ratio {aspect_ratio:.3f} inválido para feed")
                        if aspect_ratio < cls.MIN_ASPECT_RATIO:
                            recommendations.append("Cortar para proporção 4:5 (0.8) ou quadrado 1:1")
                        elif aspect_ratio > cls.MAX_ASPECT_RATIO:
                            recommendations.append("Cortar para proporção 1.91:1 ou quadrado 1:1")
                
                # Verificar qualidade/compressão
                file_size = os.path.getsize(image_path)
                if file_size > 8 * 1024 * 1024:  # 8MB
                    issues.append(f"Arquivo muito grande: {file_size / (1024*1024):.1f}MB")
                    recommendations.append("Comprimir imagem (máximo ~8MB)")
                
                is_valid = len(issues) == 0
                
                if is_valid:
                    logger.info(f"✅ Imagem válida para {content_type}")
                else:
                    logger.warning(f"⚠️ {len(issues)} problemas encontrados para {content_type}")
                    for issue in issues:
                        logger.warning(f"  - {issue}")
                
                return is_valid, issues, recommendations
                
        except Exception as e:
            logger.error(f"Erro na validação: {str(e)}")
            return False, [f"Erro ao processar imagem: {str(e)}"], []
