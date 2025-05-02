# Furia_fan_platform
Sistema de engajamento de fãs, composto por:
- Interface de Chatbot para interação com usuários
- Backend API para processamento das mensagens
- Estrutura modular e escalável para futuras expansões como: pontuação de fãs (Fan Score), integração com redes sociais e armazenamento de dados.

---

## 📚 Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** — Frontend Web Interativo
- **[FastAPI](https://fastapi.tiangolo.com/)** — Backend leve e de alta performance
- **[httpx](https://www.python-httpx.org/)** — Cliente HTTP assíncrono para comunicação entre frontend e backend
- **[Uvicorn](https://www.uvicorn.org/)** — Servidor ASGI para execução do FastAPI
- **[PostgreSQL](https://www.postgresql.org/)** *(planejado para as próximas etapas)*
- **[Requests](https://docs.python-requests.org/en/latest/)** — Biblioteca HTTP para interações com a API no frontend (Streamlit)

---

## 🗂️ Estrutura de Diretórios

```bash
fan-engagement/
│
├── app/
│   ├── furia_logom.png            # Imagem do cabeçalho da pagina
│   ├── icon.png                   # Icone da pagina
│   ├── utils.py                   # Funções utilitárias (como gerenciar interações)
│   └── chatbot_interface.py       # Frontend Streamlit
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
├── requirements.txt                # Dependências do projeto
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
2. Rodar o Backend FastAPI

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```
* A API estará disponível em `http://localhost:8800`
* Documentação interativa `http://localhost:8800/docs`
3. Rodar o Frontend Streamlit

```bash
streamlit run app/chatbot_interface.py
```
* A aplicação Web estará disponível no endereço informado pelo terminal

---

## 🧩 Funcionalidades Atuais

* Chatbot web para interação com usuários
* Comunicação entre Frontend (Streamlit) e Backend (FastAPI) via API REST.
* Interface estilizada, com logo da empresa como cabeçalho e fundo personalizado.
* Estrutura modular preparada para:
    * Criação de Fan Score;
    * Integração com redes sociais;
    * Armazenamento de interações no banco de dados;
    * Expansão com novos módulos de processamento e inteligência.

---

## 📈 Próximos Passos

* Implementar persistência de dados em PostgreSQL.
* Desenvolver sistema de pontuação de fãs (Fan Score).
* Implementar autenticação e autorização para usuários.
* Integrar com APIs de redes sociais para enriquecimento do perfil dos fãs.

---

## 📄 Licença
Este Projeto está licenciado sob os termos da licença MIT.
