# backend/main.py

from fastapi import FastAPI
from backend.api.v1.endpoints import chatbot

app = FastAPI(
    title="Fan Engagement API",
    version="1.0.0",
)

# Inclui as rotas do chatbot
app.include_router(chatbot.router, prefix="/v1/chat", tags=["Chatbot"])
