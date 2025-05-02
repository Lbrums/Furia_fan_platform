import streamlit as st
import re

def validar_link(rede, link):
    """Valida o link com base no padrão da rede."""
    padroes = {
        'Twitter': r'^https?://(www\.)?twitter\.com/[\w_]+$',
        'Instagram': r'^https?://(www\.)?instagram\.com/[\w_.]+$',
        'Twitch': r'^https?://(www\.)?twitch\.tv/[\w_]+$'
    }
    if rede in padroes:
        return re.match(padroes[rede], link) is not None
    return False

def render_social_integration():
    """Renderiza formulário para entrada de redes sociais."""
    st.markdown("Informe os links das suas redes sociais associadas ao universo gamer/FURIA:")

    redes = {
        "Twitter": "",
        "Instagram": "",
        "Twitch": ""
    }

    for rede in redes:
        link = st.text_input(f"Link do {rede}", key=rede.lower())
        if link:
            if validar_link(rede, link):
                st.success(f"{rede} validado com sucesso!")
            else:
                st.error(f"O link informado para o {rede} não parece válido.")

    # Simula envio para base de dados ou API
    if st.button("Salvar Redes Sociais"):
        st.success("Redes sociais salvas com sucesso! (simulação)")
