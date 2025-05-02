# app/fan_score/form_info_pessoal.py

import streamlit as st
import json
from pathlib import Path

def render_form():
    with st.form(key="form_info_pessoal"):
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome completo")
            cpf = st.text_input("CPF")
            data_nascimento = st.date_input("Data de nascimento")
            genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro", "Prefiro não dizer"])

        with col2:
            cep = st.text_input("CEP")
            cidade = st.text_input("Cidade")
            estado = st.text_input("Estado")

        st.markdown("---")
        st.subheader("Interesses e Atividades em e-sports")

        interesses = st.multiselect("Quais áreas você mais acompanha?", [
            "CS:GO/CS2", "Valorant", "LoL", "FIFA", "Dota 2", "Outros"
        ])

        eventos = st.text_area("Quais eventos presenciais ou online de e-sports você participou no último ano?")
        compras = st.text_area("Quais produtos/licenciados da FURIA você adquiriu no último ano?")

        submit = st.form_submit_button("Salvar informações")

        if submit:
            dados = {
                "nome": nome,
                "cpf": cpf,
                "data_nascimento": str(data_nascimento),
                "genero": genero,
                "cep": cep,
                "cidade": cidade,
                "estado": estado,
                "interesses": interesses,
                "eventos": eventos,
                "compras": compras
            }

            salvar_dados_localmente(dados)
            st.success("Informações salvas com sucesso!")


def salvar_dados_localmente(dados: dict):
    Path("dados_fan").mkdir(exist_ok=True)
    nome_arquivo = dados['cpf'].replace(".", "").replace("-", "") + ".json"
    caminho = Path("dados_fan") / nome_arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
