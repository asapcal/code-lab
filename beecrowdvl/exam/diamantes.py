def contar_diamantes(linha):
    pilha = 0
    diamantes = 0

    for char in linha:
        if char == '<':
            pilha += 1
        elif char == '>' and pilha > 0:
            pilha -= 1
            diamantes += 1

    return diamantes

# Leitura do número de casos de teste
n = int(input().strip())
resultados = []

# Processa cada caso de teste e armazena os resultados
for _ in range(n):
    linha = input().strip()
    resultados.append(contar_diamantes(linha))

# Imprime todos os resultados ao final
print(*resultados, sep='\n')
