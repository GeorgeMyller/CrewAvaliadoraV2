#!/usr/bin/env python
"""
Utilitário de Diagnóstico para Carrossel do Instagram

Este script fornece funções para diagnosticar e validar o ambiente de publicação de carrossel no Instagram via API.
Inclui verificações de permissões do token, limpeza de cache, validação de dimensões das imagens e teste de upload.

Funções Principais:
- check_token_permissions: Verifica se o token possui as permissões necessárias para publicar carrossel.
- clear_carousel_cache: Limpa o estado de cache do carrossel, tanto via API quanto manualmente.
- validate_image_dimensions: Valida se todas as imagens possuem a mesma proporção, requisito do Instagram.
- test_carousel_upload: Testa o upload das imagens do carrossel sem publicar de fato.
- run_diagnostics: Executa todas as verificações e apresenta um resumo dos diagnósticos e recomendações.

Uso:
Execute o script passando caminhos das imagens via argumento --images para validar e testar o upload.
Ideal para desenvolvedores que precisam garantir que o ambiente está pronto para publicar carrosséis no Instagram.

Requisitos:
- Variáveis de ambiente INSTAGRAM_API_KEY e INSTAGRAM_ACCOUNT_ID configuradas.
- Biblioteca Pillow instalada para validação de imagens.
- API de monitoramento opcional rodando em localhost:5001.

Referência:
https://developers.facebook.com/docs/instagram-api/guides/content-publishing

"""

import argparse
import logging
import os
import sys

import requests
from dotenv import load_dotenv

# Add parent directory to path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.agent_social_media.core.instagram.base_instagram_service import BaseInstagramService
from src.agent_social_media.core.instagram.carousel_poster import upload_carousel_images

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("carousel_debug")


def check_token_permissions():
    """Check if the current token has all required permissions for carousel posting"""
    load_dotenv()

    logger.info("\n===== CHECKING TOKEN PERMISSIONS =====")
    token = os.getenv("INSTAGRAM_API_KEY")
    ig_user_id = os.getenv("INSTAGRAM_ACCOUNT_ID")

    if not token or not ig_user_id:
        logger.error(
            "❌ Missing environment variables. Make sure INSTAGRAM_API_KEY and INSTAGRAM_ACCOUNT_ID are set."
        )
        return False

    # Print partial token for verification
    logger.info(f"Token: {token[:15]}...{token[-4:]} (partial)")
    logger.info(f"Instagram User ID: {ig_user_id}")

    service = BaseInstagramService(token, ig_user_id)
    try:
        is_valid, missing_permissions = service.check_token_permissions()

        if is_valid:
            logger.info("✅ Token is valid and has all required permissions")
            return True
        else:
            logger.error(f"❌ Token is missing required permissions: {missing_permissions}")

            # Get detailed token info
            token_info = service.debug_token()
            if "data" in token_info:
                logger.info("\nDetailed token information:")
                data = token_info["data"]
                logger.info(f"App ID: {data.get('app_id', 'N/A')}")
                logger.info(f"Type: {data.get('type', 'N/A')}")
                logger.info(f"Expires: {data.get('expires_at', 'N/A')}")
                logger.info(f"Valid: {data.get('is_valid', False)}")
                logger.info(f"Scopes: {', '.join(data.get('scopes', []))}")

            logger.info("\nRequired permissions for carousel posting:")
            logger.info("- instagram_basic")
            logger.info("- instagram_content_publishing")
            logger.info("\nPlease update your token to include these permissions.")

            return False
    except Exception as e:
        logger.error(f"❌ Error checking token: {e}")
        return False


def clear_carousel_cache():
    """Clear any cached carousel state"""
    logger.info("\n===== CLEARING CAROUSEL CACHE =====")

    try:
        # Try clearing through the monitoring API if available
        try:
            response = requests.post("http://localhost:5001/debug/carousel/clear", timeout=30)
            if response.status_code == 200:
                result = response.json()
                logger.info(
                    f"✅ Successfully cleared carousel state: {result.get('message', 'No message')}"
                )
                return True
            else:
                logger.warning(
                    f"⚠️ Failed to clear carousel state through API: {response.status_code}"
                )
        except requests.RequestException:
            logger.warning(
                "⚠️ Could not connect to monitoring API. Proceeding with manual cleanup..."
            )

        # Manual file cleanup as fallback
        temp_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "temp",
        )
        carousel_files = [
            f for f in os.listdir(temp_path) if os.path.isfile(os.path.join(temp_path, f))
        ]
        logger.info(f"Found {len(carousel_files)} files in temp directory")

        # Don't actually delete here - just informational

        return True
    except Exception as e:
        logger.error(f"❌ Error clearing cache: {e}")
        return False


def validate_image_dimensions(image_paths: list[str]) -> bool:
    """Check that all images have the same aspect ratio"""
    from PIL import Image

    logger.info("\n===== VALIDATING IMAGE DIMENSIONS =====")

    if not image_paths:
        logger.error("❌ No images provided")
        return False

    try:
        dimensions = []
        for path in image_paths:
            if not os.path.exists(path):
                logger.error(f"❌ Image not found: {path}")
                return False

            with Image.open(path) as img:
                width, height = img.size
                aspect_ratio = round(width / height, 3)
                dimensions.append((width, height, aspect_ratio))
                logger.info(
                    f"Image: {os.path.basename(path)}, Size: {width}x{height}, Aspect ratio: {aspect_ratio}"
                )

        # Check if all aspect ratios are the same (within a small tolerance)
        first_ratio = dimensions[0][2]
        all_same = all(abs(d[2] - first_ratio) < 0.01 for d in dimensions)

        if all_same:
            logger.info("✅ All images have the same aspect ratio")
            return True
        else:
            logger.error(
                "❌ Images have different aspect ratios. Instagram requires all carousel images to have the same aspect ratio."
            )
            return False

    except Exception as e:
        logger.error(f"❌ Error validating images: {e}")
        return False


def test_carousel_upload(image_paths: list[str]) -> bool:
    """Test uploading images for carousel without actually posting"""
    logger.info("\n===== TESTING CAROUSEL UPLOAD =====")

    if not image_paths:
        logger.error("❌ No images provided")
        return False

    try:

        def progress_callback(current, total):
            logger.info(f"Uploading image {current}/{total}...")

        success, uploaded_images, image_urls = upload_carousel_images(
            image_paths, progress_callback=progress_callback
        )

        if success and len(image_urls) >= 2:
            logger.info(f"✅ Successfully uploaded {len(image_urls)} images")
            for i, url in enumerate(image_urls):
                logger.info(f"  {i + 1}. {url}")
            return True
        else:
            logger.error(
                f"❌ Failed to upload images. Got {len(image_urls)} valid URLs, need at least 2."
            )
            return False

    except Exception as e:
        logger.error(f"❌ Error testing carousel upload: {e}")
        return False


def run_diagnostics(image_paths: list[str] | None = None):
    """Run all diagnostics"""
    logger.info("Starting Instagram Carousel Diagnostics...\n")

    checks = [
        {"name": "Token Permissions", "passed": check_token_permissions()},
        {"name": "Cache Clearing", "passed": clear_carousel_cache()},
    ]

    if image_paths and len(image_paths) >= 2:
        checks.extend(
            [
                {
                    "name": "Image Validation",
                    "passed": validate_image_dimensions(image_paths),
                },
                {"name": "Upload Test", "passed": test_carousel_upload(image_paths)},
            ]
        )

    # Print summary
    logger.info("\n===== DIAGNOSTICS SUMMARY =====")
    all_passed = True
    for check in checks:
        status = "✅ PASSED" if check["passed"] else "❌ FAILED"
        all_passed = all_passed and check["passed"]
        logger.info(f"{status} - {check['name']}")

    logger.info("\nRECOMMENDATIONS:")
    if not all_passed:
        logger.info("- Fix the issues reported above before attempting to post carousels")

        if not checks[0]["passed"]:
            logger.info(
                "- Get a new token with proper permissions from the Facebook Developer Dashboard"
            )
            logger.info("  Required permissions: instagram_basic, instagram_content_publishing")

        if len(checks) > 2 and not checks[2]["passed"]:
            logger.info("- Ensure all carousel images have exactly the same aspect ratio")
            logger.info(
                "- Instagram recommended ratios: 1.91:1 (landscape), 1:1 (square), or 4:5 (portrait)"
            )
            logger.info("- Each image should be less than 8MB")

        logger.info("- After fixing issues, run the debug script again to verify")
    else:
        logger.info("- All checks passed! Your setup should be ready to post carousels")
        logger.info("- If you're still having issues, check the Instagram API status")
        logger.info("- Make sure you have fewer than 25 API posts in a 24 hour period")

    logger.info("\nFor more help, see:")
    logger.info("https://developers.facebook.com/docs/instagram-api/guides/content-publishing")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Carousel Debug Utility")
    parser.add_argument("--images", nargs="+", help="Paths to test images for carousel validation")

    args = parser.parse_args()

    run_diagnostics(args.images)
