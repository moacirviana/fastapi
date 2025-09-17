# Fase 1: Construção
FROM python:3.11-slim AS builder

WORKDIR /app

# Copia apenas o requirements.txt primeiro para aproveitar cache
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Fase 2: Runtime (mais leve e seguro)
FROM python:3.11-slim

# OpenShift roda containers como usuário não-root por padrão
# Criamos um usuário não-root
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser /app

WORKDIR /app

# Copia as dependências instaladas da fase de build
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação
COPY . .

# Define o usuário não-root (recomendado no OpenShift)
USER appuser

# Expõe a porta que o FastAPI vai usar (normalmente 8000)
EXPOSE 8000

# Comando para rodar a aplicação
# Substitua "main:app" pelo seu módulo:app (ex: app/main.py → main:app)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
