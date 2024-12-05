def decodificar_matring(matriz):
    # Determina F (primeiro valor da primeira coluna) e L (último valor da última coluna)
    F = int("".join(str(matriz[i][0]) for i in range(4)))  # Constrói o número F a partir da primeira coluna
    L = int("".join(str(matriz[i][-1]) for i in range(4))) # Constrói o número L a partir da última coluna
    
    print(f"F: {F}, L: {L}")  # Debug: imprime F e L para conferência

    # Determina N com base no número de colunas - 2 (excluindo F e L)
    N = len(matriz[0]) - 2
    
    # Lista para armazenar os números decodificados da matriz
    mensagem_codificada = []
    
    # Extrai os valores intermediários da matriz e forma os números de 4 dígitos
    for i in range(1, N + 1):  # Colunas de 1 até N (indexadas a partir de 1)
        # Constrói um número de 4 dígitos a partir dos valores das quatro linhas na coluna i
        numero_str = ''.join(str(matriz[j][i]) for j in range(4))
        #mensagem_codificada.append(int(numero_str))
        Mj = int(numero_str)
        mensagem_codificada.append(Mj)
        print(f"Mj (coluna {i}): {Mj}")  # Debug: imprime cada número codificado da mensagem

    # Decodifica cada número para caracteres ASCII usando a fórmula fornecida
    #mensagem_decodificada = ''.join(
    #    chr((F * Mj + L) % 257) for Mj in mensagem_codificada
    #)

    mensagem_decodificada = ''
    for Mj in mensagem_codificada:
        Ci = (F * Mj + L) % 257
        # Confere se Ci está no intervalo ASCII imprimível
        if 32 <= Ci <= 126:  # Limita ao intervalo imprimível
            mensagem_decodificada += chr(Ci)
        else:
            print(f"Valor Ci fora do intervalo imprimível: {Ci}")
            mensagem_decodificada += '?'  # Usa '?' como substituto para debug
    
        print(f"Ci (valor ASCII): {Ci}, caractere: {chr(Ci) if 32 <= Ci <= 126 else '?'}")  # Debug
    
    return mensagem_decodificada

# Exemplo de entrada (matriz 4x(N+2))
matriz = [
    [4, 1, 8, 0, 5],
    [9, 9, 9, 3, 4],
    [3, 9, 1, 2, 7],
    [2, 3, 6, 5, 9]
]  

# Executa o algoritmo e exibe o resultado
resultado = decodificar_matring(matriz)
print(resultado)  # Saída esperada: "OBI" para o exemplo fornecido
