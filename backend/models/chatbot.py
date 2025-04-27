# backend/models/chatbot.py

from pydantic import BaseModel

class MensagemUsuario(BaseModel):
    mensagem: str

class RespostaBot(BaseModel):
    resposta: str
