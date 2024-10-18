# Usa a imagem base do Ubuntu
FROM python:3.12-slim

# Atualiza os pacotes do sistema e instala as ferramentas
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    git \
    vim \
    nano \
    build-essential \ 
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia os arquivos
COPY app.py  /app/app.py
COPY requirements.txt  /app/requirements.txt

#Define o diretório de trabalho
WORKDIR /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando para rodar o script
CMD ["python3", "app.py"]
