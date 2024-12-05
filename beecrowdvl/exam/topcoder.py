import re

def calcular_dificuldade(enunciado):
    # Dividir o enunciado em palavras, separadas por espaços
    palavras = enunciado.split()
    
    # Filtrar palavras válidas (somente letras e opcionalmente um ponto no final)
    palavras_validas = []
    for palavra in palavras:
        # Verificar se a palavra é válida: somente letras e no máximo um ponto no final
        if re.fullmatch(r'[a-zA-Z]+\.?', palavra):
            # Remover o ponto final, se existir
            if palavra.endswith('.'):
                palavra = palavra[:-1]
            palavras_validas.append(palavra)
    
    # Calcular o comprimento médio das palavras
    num_palavras = len(palavras_validas)
    if num_palavras == 0:
        comprimento_medio = 0
    else:
        comprimento_medio = sum(len(palavra) for palavra in palavras_validas) // num_palavras
    
    # Atribuir a dificuldade com base no comprimento médio
    if comprimento_medio <= 3:
        return 250
    elif comprimento_medio <= 5:
        return 500
    else:
        return 1000

# Leitura dos casos de teste
import sys
for line in sys.stdin:
    line = line.strip()
    if line:  # Ignorar linhas vazias
        print(calcular_dificuldade(line))
