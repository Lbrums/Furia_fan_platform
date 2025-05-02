# backend/services/chatbot_service.py

from dotenv import load_dotenv
import os
import logging
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Configuração de logging estruturado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("chatbot_service")

# Inicialização da API OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
FINE_TUNED_MODEL = os.getenv("FINE_TUNED_MODEL")  # Ex: ft:gpt-4o-mini-...

def gerar_resposta_chatgpt(mensagem_usuario: str) -> str:
    """
    Gera resposta usando modelo fine-tuned da OpenAI.

    Args:
        mensagem_usuario: Texto enviado pelo usuário

    Returns:
        Texto de resposta gerado pelo modelo
    """
    try:
        if not FINE_TUNED_MODEL or not FINE_TUNED_MODEL.startswith("ft:"):
            logger.error("Modelo fine-tuned não está configurado corretamente: %s", FINE_TUNED_MODEL)
            return "Erro: Modelo fine-tuned não configurado corretamente."

        response = client.chat.completions.create(
            model=FINE_TUNED_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "O chatbot da FURIA Esports é especializado em fornecer informações factuais "
                        "sobre o time de CS:GO/CS2 da FURIA, incluindo elenco, patrocínios, conquistas e setup técnico."
                    )
                },
                {"role": "user", "content": mensagem_usuario}
            ],
            temperature=1,
            max_tokens=2048
        )

        logger.info("Resposta gerada com sucesso")
        logger.info("Modelo usado: %s", FINE_TUNED_MODEL)
        logger.info("Tokens usados: %d", response.usage.total_tokens)

        return response.choices[0].message.content

    except Exception as e:
        logger.exception("Erro ao gerar resposta com OpenAI")
        return "Desculpe, ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde."
