# app/fan_score/upload_documentos.py

import streamlit as st
from pathlib import Path
import shutil

def render_upload():
    st.write("Faça o upload dos seguintes documentos em formato PDF ou imagem:")

    doc_id_frente = st.file_uploader("Documento de identidade (frente)", type=["png", "jpg", "jpeg", "pdf"], key="doc_frente")
    doc_id_verso = st.file_uploader("Documento de identidade (verso)", type=["png", "jpg", "jpeg", "pdf"], key="doc_verso")
    comprovante = st.file_uploader("Comprovante de residência", type=["png", "jpg", "jpeg", "pdf"], key="comprovante")

    cpf_input = st.text_input("Digite novamente seu CPF para associar os arquivos:")

    if st.button("Enviar documentos"):
        if not cpf_input:
            st.error("Por favor, digite o CPF para associar os arquivos.")
            return

        pasta_destino = Path("documentos_fan") / cpf_input.replace(".", "").replace("-", "")
        pasta_destino.mkdir(parents=True, exist_ok=True)

        salvar_arquivo(doc_id_frente, pasta_destino, "documento_frente")
        salvar_arquivo(doc_id_verso, pasta_destino, "documento_verso")
        salvar_arquivo(comprovante, pasta_destino, "comprovante_residencia")

        st.success("Documentos enviados com sucesso!")


def salvar_arquivo(arquivo, pasta_destino, nome_base):
    if arquivo is not None:
        extensao = Path(arquivo.name).suffix
        caminho = pasta_destino / f"{nome_base}{extensao}"
        with open(caminho, "wb") as f:
            shutil.copyfileobj(arquivo, f)