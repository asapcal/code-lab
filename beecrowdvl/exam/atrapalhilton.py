def calcular_quadrado_atrapalhado(matriz):
    # Eleva cada elemento ao quadrado
    return [[x**2 for x in row] for row in matriz]

def formatar_saida(matriz, numero_matriz):
    # Calcula o número de caracteres necessários em cada coluna
    largura_colunas = [
        max(len(str(matriz[i][j])) for i in range(len(matriz)))
        for j in range(len(matriz[0]))
    ]

    # Imprime o cabeçalho
    print(f"Quadrado da matriz #{numero_matriz}:")
    
    # Imprime cada linha da matriz com os números alinhados
    for row in matriz:
        formatted_row = " ".join(f"{num:>{largura_colunas[j]}}" for j, num in enumerate(row))
        print(formatted_row)

def main():
    num_matrizes = int(input())
    numero_matriz = 4  # Começa em 4, como especificado no problema

    for i in range(num_matrizes):
        tamanho = int(input())
        matriz = []
        for _ in range(tamanho):
            linha = list(map(int, input().split()))
            matriz.append(linha)

        # Calcula o "quadrado" da matriz
        quadrado_matriz = calcular_quadrado_atrapalhado(matriz)

        # Formata e imprime a saída
        formatar_saida(quadrado_matriz, numero_matriz)

        # Imprime linha em branco entre matrizes, exceto após a última matriz
        if i < num_matrizes - 1:
            print()

        numero_matriz += 1

if __name__ == "__main__":
    main()
