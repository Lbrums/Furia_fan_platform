# backend/api/v1/endpoints/chatbot.py

from fastapi import APIRouter
from backend.models.chatbot import MensagemUsuario, RespostaBot
from backend.services.chatbot_service import gerar_resposta_chatgpt

router = APIRouter()

@router.post("/", response_model=RespostaBot)
def chat(mensagem: MensagemUsuario):
    resposta_texto = gerar_resposta_chatgpt(mensagem.mensagem)
    return RespostaBot(resposta=resposta_texto)
