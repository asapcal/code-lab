def criptografar(texto):
    # Primeira etapa: desloca caracteres alfabéticos 3 posições para a direita
    primeira_etapa = ""
    for char in texto:
        if char.isalpha():  # Só aplica o deslocamento se for letra
            primeira_etapa += chr(ord(char) + 3)
        else:
            primeira_etapa += char

    # Segunda etapa: inverte a string
    segunda_etapa = primeira_etapa[::-1]

    # Terceira etapa: desloca a segunda metade uma posição para a esquerda
    metade = len(segunda_etapa) // 2
    terceira_etapa = (
        segunda_etapa[:metade] + 
        ''.join(chr(ord(char) - 1) for char in segunda_etapa[metade:])
    )

    return terceira_etapa

if __name__ == "__main__":
    # Lê o número de linhas a serem criptografadas
    n = int(input().strip())
    
    # Processa cada linha de entrada e imprime o resultado criptografado
    for _ in range(n):
        linha = input().strip()
        resultado = criptografar(linha)
        print(resultado)
