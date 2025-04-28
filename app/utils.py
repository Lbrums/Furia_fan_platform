# app/utils.py
import base64
import requests

# Função para carregar a imagem local e codificar em base64
def get_base64_of_image(image_path):
    """
    Carrega a imagem de um arquivo e a converte para base64.
    :param image_path: Caminho do arquivo de imagem.
    :return: string com a imagem codificada em base64.
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Função para enviar mensagem ao chatbot e receber a resposta
def send_message_to_chatbot(message: str, api_url: str):
    """
    Envia uma mensagem para o chatbot via API e recebe a resposta.
    :param message: Mensagem que será enviada ao chatbot.
    :param api_url: URL da API do chatbot (ex: http://localhost:8000/v1/chat/).
    :return: Resposta do chatbot.
    """
    try:
        response = requests.post(api_url, json={"mensagem": message})
        if response.status_code == 200:
            return response.json().get("resposta", "Erro: resposta não encontrada.")
        else:
            return "Erro: problema ao acessar a API."
    except requests.exceptions.RequestException:
        return "Erro na conexão com a API."
