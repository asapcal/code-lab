# Etapa de contrução
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Imagem final
FROM gcr.io/distroless/python3

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY script.py .

CMD ["script.py"]