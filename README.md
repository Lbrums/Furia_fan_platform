# 🐺 FURIA Fan Platform

**FURIA Fan Platform** é um projeto de engajamento com a comunidade de fãs da equipe FURIA Esports. Esta aplicação visa oferecer uma experiência interativa com:

- 🤖 Chatbot de perguntas e respostas sobre o time de CS:GO da FURIA.
- 📊 Coleta e análise de dados dos fãs (Fan Score).
- 🔗 Integração com redes sociais (Twitter/X).
- 🧠 Validação e análise de documentos com inteligência artificial.
- ✅ Verificação se o usuário segue a FURIA no Twitter.

---

## 📌 Objetivo

Oferecer uma plataforma modular que permita conhecer melhor os fãs e oferecer serviços personalizados e exclusivos. Ideal para integrar com a loja oficial, áreas VIP, eventos ou campanhas de fidelidade da FURIA Esports.

---

## ✨ Funcionalidades

### 🔹 1. Chatbot de Fãs (Streamlit + GPT-4 API)
- Informações sobre a line-up atual, stats, jogos, sensibilidade dos players, periféricos, .cfg etc.
- Interface interativa desenvolvida com Streamlit.
- Respostas geradas por modelo fine-tuned do GPT-4 com base em uma base de conhecimento JSON personalizada.

### 🔹 2. Fan Score
- Coleta de dados pessoais e interesses dos fãs.
- Upload de documentos e validação de identidade via IA.
- Leitura de redes sociais e validação de perfis para análise de relevância.
- Possível integração futura com e-commerce da FURIA.

### 🔹 3. Integração com o Redes Sociais (somente X até o momento) (OAuth2)
- Autenticação via OAuth2 (Authorization Code Flow com PKCE).
- Verificação se o usuário segue a conta oficial da FURIA.
- Armazenamento dos dados do usuário para futuras ações promocionais.

---

## 🧰 Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** — Frontend Web Interativo para exibição do chatbot e coleta de dados dos fãs  
- **[FastAPI](https://fastapi.tiangolo.com/)** — Backend leve e de alta performance usado para autenticação e APIs REST  
- **[OpenAI Python SDK](https://pypi.org/project/openai/)** — Integração com o modelo fine-tuned GPT-4o para o chatbot inteligente  
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Gerenciamento de variáveis de ambiente sensíveis através de arquivos `.env`  
- **[Logging](https://docs.python.org/3/library/logging.html)** — Sistema de logging estruturado para registro e auditoria de eventos e falhas  
- **[Uvicorn](https://www.uvicorn.org/)** — Servidor ASGI para execução das rotas do FastAPI com alta performance  
- **[Requests](https://docs.python-requests.org/en/latest/)** — Biblioteca para requisições HTTP, utilizada principalmente na comunicação com a API do Twitter  
- **[face_recognition](https://github.com/ageitgey/face_recognition)** — Verificação de identidade por reconhecimento facial a partir de documentos enviados  
- **[Pillow (PIL)](https://pypi.org/project/Pillow/)** — Processamento de imagens (auxiliar ao face_recognition)  
- **[OAuthlib](https://oauthlib.readthedocs.io/)** — Biblioteca para gerenciamento do fluxo de autenticação OAuth2 com PKCE  
- **[httpx](https://www.python-httpx.org/)** *(alternativa ao Requests)* — Cliente HTTP moderno com suporte assíncrono (possivelmente usado futuramente com FastAPI)  
- **[PostgreSQL](https://www.postgresql.org/)** *(planejado para as próximas etapas)* — Banco de dados relacional robusto para persistência segura e análise dos dados dos fãs  
- **[Pandas](https://pandas.pydata.org/)** — Manipulação e análise de dados estruturados (útil para Fan Score e relatórios futuros)  
- **[Matplotlib](https://matplotlib.org/)** *(opcional/futuro)* — Visualizações gráficas para dashboards e análise de dados dos fãs  
- **[base64](https://docs.python.org/3/library/base64.html)** — Codificação de arquivos e dados binários para transmissão segura em formatos como JSON e URL  

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
│       └── validar_doc.py
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

## 🔧 Dependências de Sistema

Para garantir que todas as bibliotecas funcionem corretamente (especialmente aquelas que envolvem processamento de imagem e autenticação facial), é necessário que o ambiente contenha alguns pré-requisitos instalados no sistema operacional:

- **[CMake](https://cmake.org/)** — Necessário para compilar dependências C/C++ como `dlib`, utilizado por `face_recognition`
- **[Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)** *(Windows)* — Necessário para compilar extensões nativas no ambiente Windows
- **[Poppler](https://github.com/oschwartz10612/poppler-windows)** — Requisito caso seja necessário converter PDF para imagem em módulos futuros
- **`libboost`, `libjpeg`, `libpng`, `libopenblas`** — *(Linux)* Dependências comuns ao instalar `dlib` ou bibliotecas de visão computacional
- **`face_recognition`** também exige o `dlib`, que requer compiladores compatíveis e suporte à arquitetura SIMD

Para instalar no Ubuntu/Debian:

```bash
sudo apt update
sudo apt install cmake build-essential libboost-all-dev libopenblas-dev libjpeg-dev libpng-dev
```
## 🚀 Como executar o projeto
1. Instalação de Dependências

```bash
pip install -r requirements.txt
```
2. Configurar as variáveis de ambiente Crie um arquivo `.env` com o seguinte conteúdo:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
FINE_TUNED_MODEL=ft:gpt-4o-mini-2024-07-18:personal:furia-fan-platform-test-1:BSaIV4bv
TWITTER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx
TWITTER_API_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
3. Rodar o Backend FastAPI

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```
* A API estará disponível em `http://localhost:8800`
* Documentação interativa `http://localhost:8800/docs`
4. Rodar o Frontend Streamlit

```bash
streamlit run Home.py
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

* Envio de notificações personalizadas por e-mail ou redes sociais.
* Dashboard com dados agregados dos fãs.
* Recompensas baseadas no Fan Score.
* Integração com API da loja da FURIA.

---

## 📄 Licença
Este Projeto está licenciado sob os termos da licença MIT.
