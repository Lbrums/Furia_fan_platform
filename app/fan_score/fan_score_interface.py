import os
import streamlit as st
from app.utils import get_base64_of_image
from app.fan_score import form_info_pessoal, upload_documentos

# Variáveis para caminhos de imagens
ICON_PATH = "app/icon.png"
IMAGE_PATH = "app/furia_logom.png"

def load_image_base64(path):
    """Carrega uma imagem e a converte para Base64."""
    if os.path.exists(path):
        return get_base64_of_image(path)
    return ""

# Codificação das imagens em Base64
icon_base64 = load_image_base64(ICON_PATH)
image_base64 = load_image_base64(IMAGE_PATH)

# Configurações da página
st.set_page_config(
    page_title="Furia Fan Score",
    page_icon=f"data:image/png;base64,{icon_base64}"
)

# Estilos CSS
STYLES = f"""
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
"""

# Aplicar estilos
st.markdown(STYLES, unsafe_allow_html=True)

# Conteúdo da página
st.title("FURIA Fan Score - Conheça seu Perfil de Fã")
st.markdown("""
    Este questionário tem como objetivo coletar informações para entendermos
    melhor o seu perfil como fã de e-sports e da FURIA. Preencha os campos abaixo
    e envie seus documentos para análise.
""")

# Etapa 1: Dados Pessoais e Interesses
st.header("1. Dados Pessoais e Interesses")
form_info_pessoal.render_form()

# Etapa 2: Upload de Documentos
st.header("2. Envie seus Documentos")
upload_documentos.render_upload()

# Rodapé
st.markdown("---")
st.caption("Seus dados são protegidos e utilizados apenas para fins de análise interna da FURIA Esports.")