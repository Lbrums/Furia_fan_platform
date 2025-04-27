# app/chatbot_interface.py

import streamlit as st

# Função simulada de resposta do chatbot
def obter_resposta(mensagem_usuario):
    # Aqui futuramente haverá chamada à API FastAPI
    return f"Resposta do bot para: {mensagem_usuario}"

# Configurações da página
st.set_page_config(page_title="Chatbot - Fan Engagement", page_icon="🤖", layout="centered")

# Título
st.title("🤖 Chatbot do Time - Fan Engagement")

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
