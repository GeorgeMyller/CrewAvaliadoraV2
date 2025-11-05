#!/usr/bin/env python3

"""

Script integrado para descobrir IDs das contas do Instagram
Usa as configurações existentes no group_configs.json

Classes:
    InstagramIDDiscovery:
        Classe para descobrir IDs das contas do Instagram usando tokens existentes.
        Métodos:
            __init__():
                Inicializa o descobridor usando configurações existentes.
            _load_existing_configs() -> Dict:
                Carrega configurações existentes dos grupos a partir do arquivo group_configs.json.
            discover_user_info(access_token: str) -> Dict:
                Descobre informações do usuário usando o token de acesso do Instagram/Facebook.
            analyze_current_configs():
                Analisa as configurações atuais e descobre mais informações sobre as contas vinculadas.
            discover_from_facebook_user_token(user_token: str):
                Descobre todas as contas do Instagram vinculadas a um usuário do Facebook usando seu token.
            _show_config_summary(accounts: List[Dict]):
                Mostra um resumo das configurações para adicionar ao group_configs.json.
Funções:
    main():
        Função principal do script. Analisa configurações existentes e permite descobrir novas contas do Instagram
        usando um token de usuário do Facebook.
        
Baseado na Instagram Graph API v23
Referência: https://developers.facebook.com/docs/instagram-platform/reference
"""

import json
import requests
from pathlib import Path
from typing import Dict, List


class InstagramIDDiscovery:
    """Classe para descobrir IDs das contas do Instagram usando tokens existentes"""
    
    def __init__(self):
        """Inicializa o descobridor usando configurações existentes"""
        self.base_url = "https://graph.facebook.com/v23.0"
        self.config_file = Path("config/environments/group_configs.json")
        self.groups = self._load_existing_configs()
    
    def _load_existing_configs(self) -> Dict:
        """Carrega configurações existentes dos grupos"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"❌ Erro ao carregar configurações: {e}")
            return {}
    
    def discover_user_info(self, access_token: str) -> Dict:
        """
        Descobre informações do usuário usando o token de acesso
        
        Args:
            access_token: Token de acesso do Instagram/Facebook
            
        Returns:
            Informações do usuário
        """
        # Primeiro, tentar como token de usuário do Facebook
        url = f"{self.base_url}/me"
        params = {
            'access_token': access_token,
            'fields': 'id,name,accounts{id,name,instagram_business_account{id,username,name}}'
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 200:
                data = response.json()
                print("✅ Token de usuário do Facebook válido")
                print(f"👤 Usuário: {data.get('name')} (ID: {data.get('id')})")
                
                # Processar páginas e contas do Instagram
                accounts = data.get('accounts', {}).get('data', [])
                instagram_accounts = []
                
                for account in accounts:
                    instagram_business = account.get('instagram_business_account')
                    if instagram_business:
                        instagram_accounts.append({
                            'facebook_page_id': account['id'],
                            'facebook_page_name': account['name'],
                            'instagram_account_id': instagram_business['id'],
                            'instagram_username': instagram_business.get('username'),
                            'instagram_name': instagram_business.get('name')
                        })
                
                return {
                    'type': 'facebook_user',
                    'user_info': data,
                    'instagram_accounts': instagram_accounts
                }
        except Exception as e:
            print(f"❌ Não é token de usuário do Facebook: {e}")
        
        # Se não funcionou como token de usuário, tentar como token de página
        url = f"{self.base_url}/me"
        params = {
            'access_token': access_token,
            'fields': 'id,name,instagram_business_account{id,username,name,followers_count,media_count}'
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 200:
                data = response.json()
                instagram_account = data.get('instagram_business_account')
                
                if instagram_account:
                    print("✅ Token de página do Facebook válido")
                    print(f"📄 Página: {data.get('name')} (ID: {data.get('id')})")
                    
                    return {
                        'type': 'facebook_page',
                        'page_info': data,
                        'instagram_account': instagram_account
                    }
        except Exception as e:
            print(f"❌ Não é token de página do Facebook: {e}")
        
        # Tentar como token direto do Instagram
        # Nota: Instagram Basic Display API tem endpoints diferentes
        print("🔍 Tentando como token do Instagram...")
        
        return {'type': 'unknown', 'error': 'Token não reconhecido'}
    
    def analyze_current_configs(self):
        """Analisa as configurações atuais e descobre mais informações"""
        print("🔍 Analisando configurações atuais...")
        print("=" * 60)
        
        if not self.groups:
            print("❌ Nenhuma configuração encontrada")
            print("📋 Para criar o arquivo de configuração:")
            print("   cp config/environments/group_configs.json.example config/environments/group_configs.json")
            print("📖 Consulte CONFIG_SETUP.md para mais informações")
            return
        
        for group_id, config in self.groups.items():
            print(f"\n📱 Grupo: {config.get('group_name', 'N/A')} (ID: {group_id})")
            print(f"   Instagram Account ID: {config.get('instagram_account_id')}")
            
            # Tentar descobrir mais informações usando o token
            access_token = config.get('instagram_access_token')
            if access_token:
                print("   🔍 Descobrindo informações adicionais...")
                info = self.discover_user_info(access_token)
                
                if info['type'] == 'facebook_user':
                    print("   ✅ Token de usuário do Facebook")
                    for ig_account in info['instagram_accounts']:
                        print(f"      📄 Página: {ig_account['facebook_page_name']}")
                        print(f"      📱 Instagram: @{ig_account['instagram_username']} (ID: {ig_account['instagram_account_id']})")
                
                elif info['type'] == 'facebook_page':
                    ig_account = info['instagram_account']
                    print("   ✅ Token de página do Facebook")
                    print(f"      📱 Instagram: @{ig_account.get('username')} (ID: {ig_account['id']})")
                    print(f"      👥 Seguidores: {ig_account.get('followers_count', 'N/A')}")
                    print(f"      📸 Posts: {ig_account.get('media_count', 'N/A')}")
                
                else:
                    print(f"   ❌ {info.get('error', 'Token não reconhecido')}")
            else:
                print("   ⚠️  Nenhum access_token encontrado")
    
    def discover_from_facebook_user_token(self, user_token: str):
        """
        Descobre todas as contas usando um token de usuário do Facebook
        
        Args:
            user_token: Token de acesso de usuário do Facebook
        """
        print("\n🔍 Descobrindo contas com token de usuário do Facebook...")
        print("=" * 60)
        
        # Obter páginas do usuário
        url = f"{self.base_url}/me/accounts"
        params = {
            'access_token': user_token,
            'fields': 'id,name,access_token,instagram_business_account{id,username,name,followers_count,media_count,account_type}'
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            pages = data.get('data', [])
            
            print(f"✅ Encontradas {len(pages)} páginas do Facebook")
            
            discovered_accounts = []
            
            for page in pages:
                page_id = page['id']
                page_name = page['name']
                page_token = page.get('access_token')
                
                print(f"\n📄 Página: {page_name} (ID: {page_id})")
                
                instagram_account = page.get('instagram_business_account')
                if instagram_account:
                    account_info = {
                        'facebook_page_id': page_id,
                        'facebook_page_name': page_name,
                        'page_access_token': page_token,
                        'instagram_account_id': instagram_account['id'],
                        'instagram_username': instagram_account.get('username'),
                        'instagram_name': instagram_account.get('name'),
                        'followers_count': instagram_account.get('followers_count'),
                        'media_count': instagram_account.get('media_count'),
                        'account_type': instagram_account.get('account_type')
                    }
                    
                    discovered_accounts.append(account_info)
                    
                    print(f"   ✅ Instagram: @{instagram_account.get('username')}")
                    print(f"   📊 ID: {instagram_account['id']}")
                    print(f"   👥 Seguidores: {instagram_account.get('followers_count', 'N/A')}")
                    print(f"   📸 Posts: {instagram_account.get('media_count', 'N/A')}")
                    print(f"   🏷️  Tipo: {instagram_account.get('account_type', 'N/A')}")
                else:
                    print("   ❌ Nenhuma conta do Instagram vinculada")
            
            # Mostrar resumo para adicionar ao group_configs.json
            if discovered_accounts:
                self._show_config_summary(discovered_accounts)
            
            return discovered_accounts
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao descobrir contas: {e}")
            return []
    
    def _show_config_summary(self, accounts: List[Dict]):
        """Mostra resumo das configurações para adicionar ao group_configs.json"""
        print("\n" + "=" * 60)
        print("📝 CONFIGURAÇÕES PARA ADICIONAR AO group_configs.json")
        print("=" * 60)
        
        for account in accounts:
            group_id = f"group_{account['instagram_account_id']}"  # Ou use o ID do grupo do WhatsApp
            
            print(f'\n  "{group_id}": {{')
            print(f'    "group_id": "{group_id}",')
            print(f'    "group_name": "Grupo {account["instagram_username"]}",')
            print('    "instagram_api_key": "SEU_APP_ACCESS_TOKEN",')
            print(f'    "instagram_account_id": "{account["instagram_account_id"]}",')
            print(f'    "instagram_access_token": "{account.get("page_access_token", "TOKEN_DA_PAGINA")}",')
            print('    "imgur_client_id": "SEU_IMGUR_CLIENT_ID",')
            print('    "imgur_client_secret": "SEU_IMGUR_CLIENT_SECRET",')
            print('    "gemini_api_key": "SUA_GEMINI_API_KEY",')
            print('    "active": true')
            print('  },')


def main():
    """Função principal"""
    print("🔍 Instagram ID Discovery Tool")
    print("Descobrindo IDs das suas contas do Instagram")
    print("=" * 50)
    
    discovery = InstagramIDDiscovery()
    
    # Primeiro, analisar configurações existentes
    discovery.analyze_current_configs()
    
    # Perguntar se o usuário tem um token de usuário do Facebook
    print("\n" + "=" * 50)
    print("🆕 DESCOBRIR NOVAS CONTAS")
    print("=" * 50)
    print("\nPara descobrir TODAS as suas contas do Instagram:")
    print("1. Vá para: https://developers.facebook.com/tools/explorer/")
    print("2. Selecione seu app")
    print("3. Adicione as permissões: pages_show_list, pages_read_engagement, instagram_basic")
    print("4. Gere um 'User Token' (não Page Token)")
    print("5. Cole o token quando solicitado")
    
    user_token = input("\n🔑 Cole seu token de usuário do Facebook (ou Enter para pular): ").strip()
    
    if user_token:
        discovery.discover_from_facebook_user_token(user_token)
    else:
        print("\n✅ Análise concluída com configurações existentes.")
    
    print("\n💡 Dica: Para adicionar novos grupos, use:")
    print("python -m src.config.group_manager_cli add GROUP_ID 'Nome do Grupo' --instagram-account-id ID_DESCOBERTO")


if __name__ == "__main__":
    main()
