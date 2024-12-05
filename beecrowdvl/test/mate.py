def codificar_palavra(palavra):
    pilha = []
    resultado = []

    # Itera sobre cada letra e aplica a lógica alternada
    for i, letra in enumerate(palavra):
        if i % 2 == 0:  # Índice par: coloca na pilha
            pilha.append(letra)
        else:  # Índice ímpar: anota diretamente no resultado
            resultado.append(letra)

    # Após o fim, esvaziamos a pilha e adicionamos ao resultado
    while pilha:
        resultado.append(pilha.pop())

    # Junta o resultado em uma string
    return ''.join(resultado)

# Testes com os exemplos fornecidos
print(codificar_palavra("MANTEIGA"))  # Deve imprimir ATJAGENM
print(codificar_palavra("MUITO"))     # Deve imprimir UTOIM
