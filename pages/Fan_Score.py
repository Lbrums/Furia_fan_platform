# app/pages/fan_score.py

import os
import json
import base64
from pathlib import Path
import streamlit as st

from app.fan_score import (
    form_info_pessoal,
    upload_documentos,
    integrar_redes,
    auth_twitter,
    validar_doc
)
from app.fan_score.integrar_redes import render_social_integration


# === Funções auxiliares ===
def get_image_base64_if_exists(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# === Configurações da página ===
ICON_PATH = "app/icon.png"
IMAGE_PATH = "app/furia_logom.png"

st.set_page_config(
    page_title="Furia Fan Score",
    page_icon=f"data:image/png;base64,{get_image_base64_if_exists(ICON_PATH)}"
)

STYLES = f"""
<style>
    .stApp {{ background-color: #000000; }}
    header {{
        background-image: url("data:image/png;base64,{get_image_base64_if_exists(IMAGE_PATH)}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        height: 150px;
        margin-bottom: 30px;
    }}
    @media (max-width: 768px) {{
        header {{ height: 100px; }}
    }}
    .message-bot {{
        background-color: #1f77b4;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        max-width: 70%;
    }}
    .message-user {{
        background-color: #2ca02c;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        max-width: 70%;
        align-self: flex-end;
    }}
</style>
<header></header>
"""
st.markdown(STYLES, unsafe_allow_html=True)

# === Fluxo principal ===
st.title("FURIA Fan Score - Conheça seu Perfil de Fã")
st.markdown("""Preencha os campos abaixo para validar seu perfil de fã da FURIA:""")

# 1. Dados Pessoais
with st.expander("1. Dados Pessoais", expanded=True):
    form_info_pessoal.render_form()

# 2. Upload de Documentos
with st.expander("2. Verificação de Identidade", expanded=False):
    upload_documentos.render_upload()
    cpf_verificacao = st.text_input("Digite seu CPF para verificação:", key="doc_cpf")
    if st.button("Validar Documentos"):
        path_verificacao = Path("documentos_fan") / cpf_verificacao
        resultado = validar_doc.verificar_identidade(path_verificacao)
        if resultado:
            st.success("✅ Identidade verificada com sucesso!")
        else:
            st.error("❌ Não foi possível verificar a identidade. Verifique os arquivos enviados.")

# 3. Conexão com Twitter
with st.expander("3. Conexão Twitter", expanded=False):
    user_data = auth_twitter.render_twitter_auth()
    if user_data:
        st.success("Conexão Concluída!")
        st.write(f"""
        **Dados do Twitter:**
        - Nome: {user_data.get('name')}
        - Usuário: @{user_data.get('screen_name')}
        - Segue a FURIA: {'Sim' if st.session_state.get('twitter_follows_furia') else 'Não'}
        """)

# 4. Outras Redes
with st.expander("4. Outras Redes", expanded=False):
    render_social_integration()

# === Rodapé ===
st.markdown("---")
st.caption("© 2024 FURIA Esports - Todos os direitos reservados")