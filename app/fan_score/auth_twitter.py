# app/fan_score/auth_twitter.py

import streamlit as st
from requests_oauthlib import OAuth1Session
from pathlib import Path
import os
import json
from datetime import datetime
import requests
from urllib.parse import parse_qs

# Carregar variáveis de ambiente
from dotenv import load_dotenv

load_dotenv()

# Credenciais OAuth 1.0a
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")

# URLs do Twitter
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate"
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
FURIA_USER_ID = "894704535037513729"


def get_oauth_session(token=None, secret=None):
    return OAuth1Session(
        API_KEY,
        client_secret=API_SECRET,
        resource_owner_key=token,
        resource_owner_secret=secret,
        callback_uri="oob"
    )


def salvar_dados_twitter(cpf: str, user_data: dict, follows_furia: bool):
    """Salva os dados automaticamente na pasta dados_fan"""
    try:
        cpf_limpo = cpf.replace(".", "").replace("-", "")
        if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
            raise ValueError("CPF inválido")

        dados = {
            "twitter": {
                "username": user_data.get("screen_name"),
                "id": user_data.get("id_str"),
                "segue_furia": follows_furia,
                "data_verificacao": datetime.now().isoformat()
            },
            "dados_pessoais": {
                "cpf": cpf_limpo
            }
        }

        pasta = Path("dados_fan")
        pasta.mkdir(exist_ok=True)
        caminho = pasta / f"{cpf_limpo}.json"

        if caminho.exists():
            with open(caminho, "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
            dados_existentes.update(dados)
            dados = dados_existentes

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        return True
    except Exception as e:
        st.error(f"Erro ao salvar dados: {str(e)}")
        return False


def render_twitter_auth():
    """Fluxo principal de autenticação com gestão completa de estados"""
    # Verificação inicial de segurança
    required_keys = [
        'cpf_validado',
        'twitter_access_token',
        'twitter_access_token_secret'
    ]

    # Etapa 1: Validação do CPF
    if "cpf_validado" not in st.session_state:
        with st.container(border=True):
            st.subheader("🔐 Validação Inicial")
            cpf = st.text_input(
                "Digite seu CPF para iniciar:",
                placeholder="000.000.000-00",
                key="cpf_input"
            )

            if st.button("Validar CPF"):
                cpf_limpo = cpf.replace(".", "").replace("-", "")
                if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
                    st.session_state.cpf_validado = cpf_limpo
                    st.rerun()
                else:
                    st.error("CPF inválido! Digite 11 dígitos")
        return None

    # Etapa 2: Geração do link de autenticação
    if "twitter_auth_url" not in st.session_state:
        try:
            oauth = OAuth1Session(API_KEY, client_secret=API_SECRET, callback_uri="oob")
            fetch_response = oauth.fetch_request_token(REQUEST_TOKEN_URL)

            st.session_state.update({
                "oauth_token": fetch_response.get("oauth_token"),
                "oauth_token_secret": fetch_response.get("oauth_token_secret"),
                "twitter_auth_url": oauth.authorization_url(AUTHENTICATE_URL),
                "token_timestamp": datetime.now().timestamp()
            })

        except Exception as e:
            st.error(f"Erro na conexão inicial: {str(e)}")
            return None

    # Etapa 3: Interface de autenticação integrada
    with st.container(border=True):
        st.subheader("📱 Autenticação no Twitter")

        # Parte 3.1: Link e campo do PIN
        st.markdown(f"""
            ### Siga estes passos:
            1. [Clique para autenticar]({st.session_state.twitter_auth_url})
            2. Autorize o aplicativo
            3. Copie o PIN de 7 dígitos
            4. Cole abaixo (válido por 2 minutos)
        """)

        pin = st.text_input(
            "PIN do Twitter:",
            key="twitter_pin",
            max_chars=7,
            placeholder="1234567"
        )

        # Parte 3.2: Processamento do PIN
        if pin:
            try:
                # Validação básica do PIN
                if not pin.isdigit() or len(pin) != 7:
                    raise ValueError("PIN deve conter 7 dígitos numéricos")

                # Verificar expiração
                if (datetime.now().timestamp() - st.session_state.token_timestamp) > 120:
                    raise PermissionError("PIN expirado! Reinicie o processo")

                # Obter tokens de acesso
                oauth = OAuth1Session(
                    API_KEY,
                    client_secret=API_SECRET,
                    resource_owner_key=st.session_state.oauth_token,
                    resource_owner_secret=st.session_state.oauth_token_secret
                )

                access_tokens = oauth.fetch_access_token(
                    ACCESS_TOKEN_URL,
                    verifier=pin
                )

                # Armazenar tokens de forma segura
                st.session_state.update({
                    "twitter_access_token": access_tokens["oauth_token"],
                    "twitter_access_token_secret": access_tokens["oauth_token_secret"]
                })

                # Obter dados do usuário
                user_oauth = OAuth1Session(
                    API_KEY,
                    client_secret=API_SECRET,
                    resource_owner_key=st.session_state.twitter_access_token,
                    resource_owner_secret=st.session_state.twitter_access_token_secret
                )

                user_data = user_oauth.get(
                    "https://api.twitter.com/1.1/account/verify_credentials.json"
                ).json()

                # Verificação de seguimento
                follows_furia = usuario_segue_furia(user_data["id_str"], st.session_state.twitter_access_token)
                st.session_state.update({
                    "twitter_access_token": st.session_state.twitter_access_token,
                    "twitter_access_token_secret": st.session_state.twitter_access_token_secret,
                    "twitter_user_id": user_data["id_str"],
                    "twitter_username": user_data["screen_name"],
                    "twitter_follows_furia": follows_furia
                })

                # Salvamento automático
                if salvar_dados_twitter(st.session_state.cpf_validado, user_data, follows_furia):
                    # Limpeza controlada de estados
                    keys_to_purge = [
                        'oauth_token', 'oauth_token_secret',
                        'twitter_auth_url', 'token_timestamp',
                        'cpf_validado', 'twitter_pin'
                    ]
                    for key in keys_to_purge:
                        if key in st.session_state:
                            del st.session_state[key]

                    return user_data

            except Exception as e:
                st.error(f"Erro crítico: {str(e)}")
                # Reset seguro para nova tentativa
                st.session_state.clear()
                return None

    return None


def usuario_segue_furia(user_id: str, access_token: str) -> bool:
    furia_id = "1521179323"  # ID da conta da FURIA
    url = f"https://api.twitter.com/2/users/{user_id}/following"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "max_results": 1000  # limite máximo permitido
    }

    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print("Erro:", response.status_code, response.text)
            return False

        data = response.json()
        for followed_user in data.get("data", []):
            if followed_user.get("id") == furia_id:
                return True

        # Paginação (caso siga mais de 1000 usuários)
        url = data.get("meta", {}).get("next_token")
        if url:
            url = f"https://api.twitter.com/2/users/{user_id}/following?pagination_token={url}"
        else:
            break

    return False