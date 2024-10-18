# Pin specific version for stability
# Use debian for easier build utilities
FROM golang:1.19-alpine AS build

WORKDIR /app

COPY . .

#RUN go mod download

EXPOSE 8000

CMD ["go", "run", "./server.go"]
