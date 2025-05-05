# Home.py

import streamlit as st
import re
from app.utils import get_base64_of_image, send_message_to_chatbot

# Caminho para o arquivo de imagem do ícone
icon_path = "app/icon.png"
icon_base64 = get_base64_of_image(icon_path)

# Configurações da página
st.set_page_config(page_title="Furia Fan Chat", page_icon=f"data:image/png;base64,{icon_base64}", layout="wide")

# Caminho para a imagem do cabeçalho
image_path = "app/furia_logom.png"
image_base64 = get_base64_of_image(image_path)

# Estilização da página
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


# Função para mapear palavras-chave e links da HLTV
def detectar_link_relevante(texto: str):
    texto = texto.lower()
    mapa_links = {
        "Partidas": (["partida", "partidas", "jogo", "jogos"], "#tab-matchesBox"),
        "line-up": (["elenco", "jogadores", "lineup", "roster"], "#tab-rosterBox"),
        "Informações": (["informação", "info", "detalhes"], "#tab-infoBox"),
        "Torneios": (["campeonato", "eventos", "torneios"], "#tab-eventsBox"),
        "Conquistas": (["conquista", "título", "troféu"], "#tab-achievementsBox"),
        "Noticias": (["notícia", "notícias", "news"], "#tab-newsBox"),
        "Estatísticas": (["estatística", "stats", "desempenho"], "#tab-statsBox"),
    }

    base_url = "https://www.hltv.org/team/8297/furia"

    for categoria, (palavras, sufixo) in mapa_links.items():
        if any(re.search(rf"\b{re.escape(p)}\b", texto) for p in palavras):
            return (
                f"<div class='chat-container'>"
                f"<div class='message-bot'>Confira mais sobre <strong>{categoria}</strong> da FURIA em: "
                f"<a href='{base_url + sufixo}' target='_blank' style='color: #FFD700;'>"
                f"HLTV - {categoria}</a></div></div>"
            )

    return None


# Inicialização da sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Layout centralizado
col1, col2, col3, col4, col5 = st.columns([1, 1, 3, 1, 1])
with col3:
    st.title("Furia Fan Chat")
    st.write("Peça informações sobre a Fúria ou descubra o seu Fan Score!")

    # Exibir histórico de mensagens
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"<div class='chat-container'><div class='message-user'>{message['content']}</div></div>",
                        unsafe_allow_html=True)
        else:
            if message['content'].startswith("<div"):
                st.markdown(message['content'], unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-container'><div class='message-bot'>{message['content']}</div></div>",
                            unsafe_allow_html=True)

    # Campo de entrada
    user_input = st.text_input("Digite sua mensagem:")

    # Endereço da API
    url_api = "http://localhost:8000/v1/chat/"

    # Botões
    col1, col2 = st.columns([4, 2])
    with col1:
        send_button = st.button("Enviar", use_container_width=True)
    with col2:
        clear_button = st.button("Limpar", use_container_width=True)

    # Botão para fan score
    fan_score_button = st.button("Furia Fan Score", use_container_width=True)

    if fan_score_button:
        st.switch_page("pages/Fan_Score.py")

    # Lógica de envio de mensagem
    if send_button and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        bot_reply = send_message_to_chatbot(user_input, url_api)
        st.session_state.messages.append({"role": "bot", "content": bot_reply})

        # Segunda resposta com link relevante
        link_mensagem = detectar_link_relevante(user_input)
        if link_mensagem:
            st.session_state.messages.append({"role": "bot", "content": link_mensagem})

        st.rerun()

    # Lógica de limpeza
    if clear_button:
        st.session_state.messages = []
        st.rerun()
