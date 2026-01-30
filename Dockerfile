FROM python:3.10-slim

# Instala dependências do sistema para o psycopg2 e leitura de Excel
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]

