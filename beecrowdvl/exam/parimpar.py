#Função de ordenação
def ordenar_numeros(numeros):
    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    pares.sort()
    impares.sort(reverse=True)

    return pares + impares

# Leitura da entrada
N = int(input())
numeros = []
for _ in range(N):
    numeros.append(int(input()))

# Ordenação e impressão
resultado = ordenar_numeros(numeros)
for num in resultado:
    print(num)