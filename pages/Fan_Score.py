import os
import base64
import streamlit as st
from app.fan_score import form_info_pessoal, upload_documentos, integrar_redes, auth_twitter

def get_base64_of_image(image_path):
    """
    Carrega a imagem de um arquivo e a converte para base64.
    :param image_path: Caminho do arquivo de imagem.
    :return: string com a imagem codificada em base64.
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

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
        height: 150px; /* reduzido */
        background-size: contain;
        margin-bottom: 30px;
    }}
    @media (max-width: 768px) {{
    header {{
        height: 100px;
        }}
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

# Etapa 3: Redes Sociais
st.header("3. Redes Sociais")
integrar_redes.render_social_integration()

# Etapa 4: Conectar com o Twitter (OAuth2)
st.header("4. Conectar com o Twitter")
auth_twitter.iniciar_login_twitter()

# Rodapé
st.markdown("---")
st.caption("Seus dados são protegidos e utilizados apenas para fins de análise interna da FURIA Esports.")