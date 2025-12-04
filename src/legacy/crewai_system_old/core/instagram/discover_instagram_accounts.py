#!/usr/bin/env python3

"""
Script para descobrir múltiplas contas do Instagram vinculadas ao Facebook
Segue as instruções da Instagram Graph API v23 para descoberta de contas

Funcionalidades:
- Obtém todas as páginas do Facebook gerenciadas pelo usuário.
- Verifica se cada página possui uma conta profissional do Instagram vinculada.
- Recupera detalhes das contas do Instagram vinculadas (nome de usuário, nome, foto de perfil, número de seguidores, número de posts, tipo de conta).
- Exporta as informações das contas descobertas em formato .env para configuração.
- Salva os dados das contas em um arquivo JSON.
Requisitos:
- Token de acesso de usuário do Facebook com permissões: instagram_basic, pages_show_list, pages_read_engagement.
- Variável de ambiente FACEBOOK_USER_ACCESS_TOKEN definida no arquivo .env.

Referência: https://developers.facebook.com/docs/instagram-platform/reference
"""

import json
import os

import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


class InstagramAccountDiscovery:
    """Classe para descobrir contas do Instagram vinculadas ao Facebook"""

    def __init__(self, access_token: str):
        """
        Inicializa o descobridor de contas

        Args:
            access_token: Token de acesso de usuário do Facebook
        """
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v23.0"

    def get_facebook_pages(self) -> list[dict]:
        """
        Obtém todas as Páginas do Facebook que o usuário gerencia

        Endpoint: /me/accounts
        Permissões necessárias: pages_show_list, pages_read_engagement

        Returns:
            Lista de páginas do Facebook
        """
        url = f"{self.base_url}/me/accounts"
        params = {
            "access_token": self.access_token,
            "fields": "id,name,access_token,instagram_business_account",
        }

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()
            pages = data.get("data", [])

            print(f"✅ Encontradas {len(pages)} páginas do Facebook")

            for page in pages:
                print(f"📄 Página: {page.get('name')} (ID: {page.get('id')})")
                if page.get("instagram_business_account"):
                    print(f"   📱 Instagram vinculado: {page['instagram_business_account']['id']}")
                else:
                    print("   ❌ Nenhuma conta do Instagram vinculada")

            return pages

        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao obter páginas do Facebook: {e}")
            return []

    def get_instagram_account_details(
        self, instagram_account_id: str, page_access_token: str
    ) -> dict:
        """
        Obtém detalhes de uma conta específica do Instagram

        Args:
            instagram_account_id: ID da conta do Instagram
            page_access_token: Token de acesso da página

        Returns:
            Detalhes da conta do Instagram
        """
        url = f"{self.base_url}/{instagram_account_id}"
        params = {
            "access_token": page_access_token,
            "fields": "id,username,name,profile_picture_url,followers_count,media_count,account_type",
        }

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao obter detalhes da conta {instagram_account_id}: {e}")
            return {}

    def discover_all_accounts(self) -> list[dict]:
        """
        Descobre todas as contas do Instagram vinculadas às páginas do Facebook

        Returns:
            Lista de contas do Instagram descobertas
        """
        print("🔍 Iniciando descoberta de contas do Instagram...")
        print("=" * 60)

        # Obter páginas do Facebook
        pages = self.get_facebook_pages()

        instagram_accounts = []

        for page in pages:
            page_id = page.get("id")
            page_name = page.get("name")
            page_access_token = page.get("access_token")

            print(f"\n📄 Analisando página: {page_name}")

            # Verificar se há conta do Instagram vinculada
            instagram_business_account = page.get("instagram_business_account")

            if instagram_business_account and page_access_token:
                instagram_account_id = instagram_business_account["id"]

                # Obter detalhes da conta do Instagram
                details = self.get_instagram_account_details(
                    instagram_account_id, page_access_token
                )

                if details:
                    account_info = {
                        "instagram_account_id": instagram_account_id,
                        "facebook_page_id": page_id,
                        "facebook_page_name": page_name,
                        "page_access_token": page_access_token,
                        "instagram_username": details.get("username"),
                        "instagram_name": details.get("name"),
                        "followers_count": details.get("followers_count"),
                        "media_count": details.get("media_count"),
                        "account_type": details.get("account_type"),
                        "profile_picture_url": details.get("profile_picture_url"),
                    }

                    instagram_accounts.append(account_info)

                    print(f"   ✅ Instagram encontrado: @{details.get('username')}")
                    print(f"   📊 Seguidores: {details.get('followers_count', 'N/A')}")
                    print(f"   📸 Posts: {details.get('media_count', 'N/A')}")
                    print(f"   🏷️  Tipo: {details.get('account_type', 'N/A')}")
            else:
                print("   ❌ Nenhuma conta do Instagram vinculada")

        return instagram_accounts

    def export_to_env_format(self, accounts: list[dict]) -> None:
        """
        Exporta as contas descobertas no formato .env

        Args:
            accounts: Lista de contas descobertas
        """
        print("\n" + "=" * 60)
        print("📝 CONFIGURAÇÕES PARA .ENV")
        print("=" * 60)

        for i, account in enumerate(accounts, 1):
            print(f"\n# Conta {i}: @{account['instagram_username']} ({account['instagram_name']})")
            print(f"# Facebook Page: {account['facebook_page_name']}")
            print(f"# Seguidores: {account.get('followers_count', 'N/A')}")
            print(f"INSTAGRAM_ACCOUNT_ID_{i}={account['instagram_account_id']}")
            print(f"INSTAGRAM_USERNAME_{i}={account['instagram_username']}")
            print(f"FACEBOOK_PAGE_ID_{i}={account['facebook_page_id']}")
            print(f"PAGE_ACCESS_TOKEN_{i}={account['page_access_token']}")

    def save_to_json(
        self, accounts: list[dict], filename: str = "discovered_accounts.json"
    ) -> None:
        """
        Salva as contas descobertas em um arquivo JSON

        Args:
            accounts: Lista de contas descobertas
            filename: Nome do arquivo para salvar
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(accounts, f, indent=2, ensure_ascii=False)

            print(f"\n💾 Contas salvas em: {filename}")

        except Exception as e:
            print(f"❌ Erro ao salvar arquivo: {e}")


def main():
    """Função principal"""
    print("🔍 Instagram Account Discovery Tool")
    print("Descobrindo contas do Instagram vinculadas ao Facebook...")
    print("=" * 60)

    # Obter token de acesso do usuário do Facebook
    access_token = os.getenv("FACEBOOK_USER_ACCESS_TOKEN")

    if not access_token:
        print("❌ Token de acesso não encontrado!")
        print("\nPara obter o token:")
        print("1. Vá para: https://developers.facebook.com/tools/explorer/")
        print("2. Selecione seu app")
        print("3. Adicione as permissões: instagram_basic, pages_show_list, pages_read_engagement")
        print("4. Gere o token de usuário")
        print("5. Adicione FACEBOOK_USER_ACCESS_TOKEN=seu_token no arquivo .env")
        return

    # Criar instância do descobridor
    discovery = InstagramAccountDiscovery(access_token)

    # Descobrir contas
    accounts = discovery.discover_all_accounts()

    if accounts:
        print(f"\n🎉 Descobertas {len(accounts)} contas do Instagram!")

        # Exportar configurações
        discovery.export_to_env_format(accounts)

        # Salvar em JSON
        discovery.save_to_json(accounts)

    else:
        print("\n❌ Nenhuma conta do Instagram encontrada.")
        print("\nVerifique se:")
        print("- Você tem páginas do Facebook configuradas")
        print("- As páginas estão vinculadas a contas profissionais do Instagram")
        print("- Você tem as permissões necessárias")


if __name__ == "__main__":
    main()
