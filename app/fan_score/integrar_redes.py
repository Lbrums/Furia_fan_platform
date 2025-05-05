import streamlit as st
import re
import json
from pathlib import Path

def validar_link(rede, link):
    """Valida o link com base no padrão da rede."""
    padroes = {
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
        "Instagram": "",
        "Twitch": ""
    }

    redes_validadas = {}

    for rede in redes:
        link = st.text_input(f"Link do {rede}", key=rede.lower())
        if link:
            if validar_link(rede, link):
                redes_validadas[rede] = link
                st.success(f"{rede} validado com sucesso!")
            else:
                st.error(f"O link informado para o {rede} não parece válido, copie o link da barra de endereços ou compartilhe através do 3 pontinhos e cole no campo correspondente.")

    def salvar_redes_sociais(cpf: str, redes_validadas: dict):
        """Salva as redes sociais validadas no arquivo JSON associado ao CPF do usuário."""
        nome_arquivo = cpf.replace(".", "").replace("-", "") + ".json"
        caminho = Path("dados_fan") / nome_arquivo

        # Se o arquivo já existir, carrega os dados existentes
        if caminho.exists():
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
        else:
            dados = {}

        # Atualiza ou cria a chave para as redes sociais
        dados["redes_sociais"] = redes_validadas

        # Cria o diretório "dados_fan" se não existir
        Path("dados_fan").mkdir(parents=True, exist_ok=True)

        # Salva os dados no arquivo JSON
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    cpf = st.text_input("Digite novamente seu CPF para vincular:", key="cpf_verificacao")

    # Quando o botão for pressionado, o envio real é realizado
    if st.button("Salvar Redes Sociais"):
        if cpf:
            if redes_validadas:
                salvar_redes_sociais(cpf, redes_validadas)
                st.success("Redes sociais salvas com sucesso!")
            else:
                st.warning("Nenhuma rede social válida foi inserida.")
        else:
            st.warning("Informe o CPF para associar essas redes ao usuário.")
