#!/usr/bin/env python3

"""
Script auxiliar para obter o token de acesso do Facebook, utilizado para descobrir contas do Instagram vinculadas.
Funcionalidades principais:
- Geração de URL de autorização do Facebook para obtenção do token de acesso, com permissões necessárias para integração com Instagram.
- Validação do token de acesso do usuário, verificando se está válido e exibindo informações básicas do perfil.
- Orientações para adicionar o token obtido ao arquivo .env e executar scripts de descoberta de contas do Instagram.
Requisitos:
- Variáveis de ambiente INSTAGRAM_APP_ID e FACEBOOK_USER_ACCESS_TOKEN configuradas no arquivo .env.
- Permissões solicitadas: instagram_basic, instagram_content_publishing, pages_show_list, pages_read_engagement, business_management.
- Utiliza bibliotecas dotenv, requests e webbrowser.
Como usar:
1. Execute o script para gerar a URL de autorização e obter o token de acesso.
2. Após autorizar, copie o token da URL e adicione ao arquivo .env.
3. Valide o token e, se válido, execute o script de descoberta de contas do Instagram.
Referência:
https://developers.facebook.com/docs/facebook-login/guides/access-tokens/

"""

import os
import webbrowser
from urllib.parse import urlencode
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


def generate_facebook_auth_url():
    """
    Gera URL para obter token de acesso do Facebook
    
    Referência: https://developers.facebook.com/docs/facebook-login/guides/access-tokens/
    """
    
    # Obter configurações do .env
    app_id = os.getenv('INSTAGRAM_APP_ID')
    
    if not app_id:
        print("❌ INSTAGRAM_APP_ID não encontrado no .env!")
        print("Adicione seu App ID do Facebook no arquivo .env")
        return
    
    # Permissões necessárias para descobrir contas do Instagram
    permissions = [
        'instagram_basic',           # Acesso básico ao Instagram
    'instagram_content_publishing', # Publicar conteúdo
        'pages_show_list',          # Listar páginas do Facebook
        'pages_read_engagement',    # Ler engajamento das páginas
        'business_management'       # Gerenciar negócios (opcional)
    ]
    
    # URL de redirecionamento (você pode usar localhost para testes)
    redirect_uri = 'https://localhost/'
    
    # Parâmetros da URL de autorização
    params = {
        'client_id': app_id,
        'redirect_uri': redirect_uri,
        'scope': ','.join(permissions),
        'response_type': 'token',  # Para obter token diretamente na URL
        'display': 'popup'
    }
    
    # Gerar URL completa
    base_url = 'https://www.facebook.com/v23.0/dialog/oauth'
    auth_url = f"{base_url}?{urlencode(params)}"
    
    print("🔐 Token de Acesso do Facebook")
    print("=" * 50)
    print("\n📋 Permissões solicitadas:")
    for permission in permissions:
        print(f"   ✓ {permission}")
    
    print("\n🌐 URL de autorização gerada:")
    print(f"{auth_url}")
    
    print("\n📝 Instruções:")
    print("1. A URL será aberta automaticamente no navegador")
    print("2. Faça login no Facebook se necessário")
    print("3. Autorize as permissões solicitadas")
    print("4. Após autorizar, você será redirecionado para localhost")
    print("5. Copie o token da URL (após #access_token=)")
    print("6. Adicione FACEBOOK_USER_ACCESS_TOKEN=seu_token no .env")
    
    # Abrir URL no navegador
    try:
        webbrowser.open(auth_url)
        print("\n✅ URL aberta no navegador!")
    except Exception as e:
        print(f"\n❌ Erro ao abrir navegador: {e}")
        print("Copie e cole a URL manualmente no navegador.")
    
    return auth_url


def validate_token():
    """
    Valida o token de acesso do Facebook
    """
    access_token = os.getenv('FACEBOOK_USER_ACCESS_TOKEN')
    
    if not access_token:
        print("❌ FACEBOOK_USER_ACCESS_TOKEN não encontrado no .env!")
        return False
    
    import requests
    
    # Verificar validade do token
    url = "https://graph.facebook.com/v23.0/me"
    params = {
        'access_token': access_token,
        'fields': 'id,name,email'
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        user_data = response.json()
        
        print("✅ Token válido!")
        print(f"👤 Usuário: {user_data.get('name')} (ID: {user_data.get('id')})")
        print(f"📧 Email: {user_data.get('email', 'N/A')}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Token inválido ou expirado: {e}")
        return False


def main():
    """Função principal"""
    print("🔐 Facebook Token Generator")
    print("Para descobrir contas do Instagram")
    print("=" * 40)
    
    # Verificar se já existe token
    if os.getenv('FACEBOOK_USER_ACCESS_TOKEN'):
        print("\n🔍 Token encontrado no .env, validando...")
        if validate_token():
            print("\n✅ Token válido! Você pode executar o script de descoberta:")
            print("python discover_instagram_accounts.py")
            return
        else:
            print("\n⚠️  Token inválido ou expirado. Gerando novo...")
    
    # Gerar nova URL de autorização
    print("\n🆕 Gerando nova URL de autorização...")
    generate_facebook_auth_url()
    
    print("\n💡 Dica: Após obter o token, execute:")
    print("python discover_instagram_accounts.py")


if __name__ == "__main__":
    main()
