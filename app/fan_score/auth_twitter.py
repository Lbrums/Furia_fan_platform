import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from urllib.parse import urlencode
import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8501"  # Altere em produção
SCOPES = ["tweet.read", "users.read", "like.read", "follows.read"]
AUTH_URL = "https://twitter.com/i/oauth2/authorize"
TOKEN_URL = "https://api.twitter.com/2/oauth2/token"
USER_URL = "https://api.twitter.com/2/users/me"

def iniciar_login_twitter():
    st.subheader("Conectar com Twitter (X)")

    if not CLIENT_ID or not CLIENT_SECRET:
        st.error("CLIENT_ID ou CLIENT_SECRET não encontrados nas variáveis de ambiente.")
        return

    oauth = OAuth2Session(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPES,
    )

    if "twitter_token" not in st.session_state:
        # Passo 1: Gera URL de autorização
        auth_url, state = oauth.create_authorization_url(AUTH_URL)
        st.session_state["oauth_state"] = state
        st.markdown(f"[Clique aqui para conectar com o Twitter]({auth_url})")

        # Passo 2: Verifica se há retorno com código de autorização
        query_params = st.query_params  # substituído aqui
        if "code" in query_params:
            code = query_params["code"][0]
            state = query_params.get("state", [None])[0]
            auth_response_url = f"{REDIRECT_URI}?{urlencode({'code': code, 'state': state})}"

            try:
                token = oauth.fetch_token(
                    TOKEN_URL,
                    code=code,
                    authorization_response=auth_response_url
                )
                st.session_state["twitter_token"] = token
                st.success("Autenticado com sucesso no Twitter!")

                # Recupera dados do usuário
                headers = {"Authorization": f"Bearer {token['access_token']}"}
                user_info = requests.get(USER_URL, headers=headers).json()

                if "data" in user_info:
                    st.session_state["twitter_user"] = user_info["data"]
                    st.json(user_info["data"])
                else:
                    st.error("Erro ao obter dados do perfil do Twitter.")

            except Exception as e:
                st.error(f"Erro durante autenticação: {e}")
    else:
        st.success("Você já está autenticado com o Twitter")
        if "twitter_user" in st.session_state:
            st.json(st.session_state["twitter_user"])

        if st.button("Desconectar do Twitter"):
            del st.session_state["twitter_token"]
            st.experimental_rerun()
