# app/chatbot_interface.py

import streamlit as st
import httpx

# Função que consulta a API FastAPI para obter a resposta do bot
def obter_resposta(mensagem_usuario):
    try:
        # Endereço local da API FastAPI
        url_api = "http://localhost:8000/v1/chat/"

        # Payload enviado para a API
        payload = {"mensagem": mensagem_usuario}

        # Envio da requisição POST
        response = httpx.post(url_api, json=payload, timeout=5.0)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            resposta_bot = response.json().get("resposta", "Sem resposta")
            return resposta_bot
        else:
            return "Erro ao se comunicar com o servidor do chatbot."

    except httpx.RequestError:
        return "Servidor do chatbot indisponível no momento."
    
# Configurações da página
st.set_page_config(page_title="Furia Fan Chat", page_icon="🐆", layout="centered")

# Título
st.title("🐆O que você quer saber da Furia?")

# Histórico de conversas na sessão
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Campo de entrada do usuário
with st.form(key="formulario_chat"):
    mensagem_usuario = st.text_input("Digite sua mensagem:", "")
    enviar = st.form_submit_button("Enviar")

# Processamento da mensagem
if enviar and mensagem_usuario:
    resposta = obter_resposta(mensagem_usuario)
    st.session_state.mensagens.append(("Você", mensagem_usuario))
    st.session_state.mensagens.append(("Bot", resposta))

# Exibição do histórico de mensagens
for remetente, mensagem in st.session_state.mensagens:
    if remetente == "Você":
        st.markdown(f"**🧑 {remetente}:** {mensagem}")
    else:
        st.markdown(f"**🤖 {remetente}:** {mensagem}")
