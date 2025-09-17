# FastAPI Template

Este é um template modular e escalável para criação de APIs RESTful usando FastAPI, SQLAlchemy, e Pydantic. Ideal para iniciar projetos rapidamente com boas práticas de arquitetura, segurança e documentação automática.

## 🚀 Recursos

- FastAPI — Alta performance, fácil de usar, documentação automática (Swagger UI e ReDoc)

- SQLAlchemy — ORM para interação com banco de dados (PostgreSQL, MySQL, SQLite, etc.)

- Pydantic — Validação e serialização de dados

- JWT Auth — Autenticação via tokens JWT

- Docker & Docker Compose — Ambiente de desenvolvimento containerizado

- .env — Gerenciamento de variáveis de ambiente com python-dotenv

### 📂 Estrutura do projeto
```
fastapi-template/
   ├── v1/                    # Rotas da API
   │   ├── api.py
   │   └── endpoints/
   │       ├── artigo.py
   │       └── usuario.py
   ├── core/                   # Configurações e segurança
   │   ├── auth.py
   │   ├── configa.py
   │   ├── database.py
   │   ├── deps.py
   │   └── security.py
   ├── models/                 # Modelos do banco de dados (SQLAlchemy)
   ├── schemas/                # Modelos de dados (Pydantic)
   ├── database/               # Conexão e sessão do banco
   ├── schemas/                # Migrações do banco
.gitignore
 requirements.txt
 Dockerfile
 docker-compose.yml
 README.md
 main.py
```
 
### 📋 Pré-requisitos

Python 3.10.x, pip, Docker e Docker Compose

```
$ pip install -r requirements.txt
```

## 📄 Licença

Este projeto está livre para uso.
