# Furia_fan_platform

Sistema de engajamento de fãs da FURIA Esports, composto por:
- Interface de Chatbot para interação com usuários
- Backend API para processamento inteligente de mensagens
- Integração com modelo fine-tuned baseado em GPT-4o
- Arquitetura modular e escalável para expansão futura (Fan Score, rede sociais, base de conhecimento etc.)

---

## 📚 Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** — Frontend Web Interativo
- **[FastAPI](https://fastapi.tiangolo.com/)** — Backend leve e de alta performance
- **[OpenAI Python SDK](https://pypi.org/project/openai/)** — Integração com modelo fine-tuned GPT-4o
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Carregamento de variáveis sensíveis a partir de `.env`
- **[Logging](https://docs.python.org/3/library/logging.html)** — Logging estruturado para diagnóstico e auditoria
- **[Uvicorn](https://www.uvicorn.org/)** — Servidor ASGI para execução do FastAPI
- **[PostgreSQL](https://www.postgresql.org/)** *(planejado para as próximas etapas)*
- **[Requests](https://docs.python-requests.org/en/latest/)** — Biblioteca HTTP para interações com a API no frontend (Streamlit)

---

## 🗂️ Estrutura de Diretórios

```bash
fan-engagement/
│
├── app/
│   ├── furia_logom.png             # Imagem do cabeçalho da pagina
│   ├── icon.png                    # Icone da pagina
│   ├── utils.py                    # Funções utilitárias (como gerenciar interações)
│   ├── __init__
│   └── fan_score/
│       ├── __init__.py
│       ├── auth_twitter.py
│       ├── form_info_pessoal.py
│       ├── integrar_redes.py
│       ├── upload_documentos.py
│       └── validar_links.py
│       
├── Home.py 
├── pages/
│   └── Fan_Score.py
│
├── backend/
│   ├── main.py                     # Inicialização do FastAPI
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── chatbot.py       # Endpoint de Chatbot
│   ├── core/
│   │   └── config.py                # Configurações globais
│   ├── models/
│   │   └── chatbot.py               # Modelos Pydantic
│   └── services/
│       └── chatbot_service.py       # Lógica de geração de respostas
│
├── .env                             # Variáveis de ambiente (não versionado)
├── requirements.txt                 # Dependências do projeto
├── README.md                        # Documentação
├── .gitignore                       # Arquivos a serem ignorados
└── .streamlit/
    └── config.toml                  # Configurações opcionais do Streamlit
```

---

## 🚀 Como executar o projeto
1. Instalação de Dependências

```bash
pip install -r requirements.txt
```
2. Configurar as variáveis de ambiente Crie um arquivo `.env` com o seguinte conteúdo:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
FINE_TUNED_MODEL=ft:gpt-4o-mini-2024-07-18:personal:furia-fan-platform-test-1:BSaIV4bv
```
3. Rodar o Backend FastAPI

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```
* A API estará disponível em `http://localhost:8800`
* Documentação interativa `http://localhost:8800/docs`
4. Rodar o Frontend Streamlit

```bash
streamlit run app/Home.py
```
* A aplicação Web estará disponível no endereço informado pelo terminal

---

## 🧩 Funcionalidades Atuais

* Chatbot funcional com interface web (Streamlit)
* Integração com modelo fine-tuned GPT-4o via OpenAI AP
* Interface estilizada, com logo da empresa como cabeçalho e fundo personalizado.
* Uso de logs estruturados para monitoramento e depuração
* Variáveis sensíveis isoladas com `.env`
* Estrutura modular preparada para:
    * Criação de Fan Score;
    * Integração com redes sociais;
    * Armazenamento de interações no banco de dados;
    * Expansão com novos módulos de processamento e inteligência.

---

## 📈 Próximos Passos

* Implementar sistema de Fan Score baseado em interações
* Criar interface dedicada para exibir o Fan Score
* Integrar APIs de redes sociais

---

## 📄 Licença
Este Projeto está licenciado sob os termos da licença MIT.
