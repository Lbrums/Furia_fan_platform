# app/chatbot_interface.py

import streamlit as st
from utils import get_base64_of_image, send_message_to_chatbot

# Caminho para o arquivo de imagem do ícone (imagem diferente da usada no cabeçalho)
icon_path = "app/icon.png"  # Atualize o caminho se necessário

# Obter a imagem codificada em Base64
icon_base64 = get_base64_of_image(icon_path)

# Configurações iniciais da página
st.set_page_config(page_title="Furia Fan Chat", page_icon=f"data:image/png;base64,{icon_base64}", layout="wide")

# Caminho para a imagem local
image_path = "app/furia_logom.png"  # ajuste se necessário
image_base64 = get_base64_of_image(image_path)

# Estilizar o fundo e o cabeçalho
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #000000;
    }}
    header {{
        background-image: url("data:image/png;base64,{image_base64}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        height: 200px;
        margin-bottom: 30px;
    }}
    .message-bot {{
        background-color: #1f77b4;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        width: fit-content;
        max-width: 70%;
    }}
    .message-user {{
        background-color: #2ca02c;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        width: fit-content;
        max-width: 70%;
        align-self: flex-end;
    }}
    .chat-container {{
        display: flex;
        flex-direction: column;
    }}
    </style>
    <header></header>
    """,
    unsafe_allow_html=True
)

# Inicializar sessão para manter o histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Centralizar conteúdo utilizando 5 colunas
col1, col2, col3, col4, col5 = st.columns([1, 1, 3, 1, 1])  # 5 colunas, sendo col3 centralizada
with col3:
    # Título e descrição dentro da coluna 3
    st.title("Furia Fan Chat")
    st.write("Peça informações sobre a Fúria ou descubra o seu Fan Score!")

    # Mostrar histórico de mensagens
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"<div class='chat-container'><div class='message-user'>{message['content']}</div></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-container'><div class='message-bot'>{message['content']}</div></div>", unsafe_allow_html=True)

    # Campo de entrada do usuário
    user_input = st.text_input("Digite sua mensagem:")

    # Endereço da API FastAPI
    url_api = "http://localhost:8000/v1/chat/"

    # Botões
    col1, col2 = st.columns([4, 2])

    with col1:
        send_button = st.button("Enviar", use_container_width=True)
    with col2:
        clear_button = st.button("Limpar", use_container_width=True)

    # Botão para acesso a aba de fan score.
    fan_score_button = st.button("Furia Fan Score", use_container_width=True)

    # Lógica de envio de mensagem
    if send_button and user_input:
        # Adicionar mensagem do usuário ao histórico
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Enviar mensagem para a API e obter a resposta
        bot_reply = send_message_to_chatbot(user_input, url_api)

        # Adicionar resposta do bot ao histórico
        st.session_state.messages.append({"role": "bot", "content": bot_reply})

        # Limpar o campo de entrada após enviar
        st.rerun()

    # Lógica de limpar a conversa
    if clear_button:
        st.session_state.messages = []
        st.rerun()
