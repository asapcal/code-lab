def ponteiros_iguais(H, M, S):
    resultados = []
    # Iteramos sobre horas, minutos e segundos.
    for h in range(H):
        for m in range(M):
            for s in range(S):
                # Verificamos se horas, minutos e segundos são iguais.
                if h == m == s:
                    resultados.append((h, m, s))
    
    # Imprimimos a quantidade de horários encontrados com ponteiros iguais.
    print(len(resultados))
    # Imprimimos cada horário em que ocorre "ponteiros iguais".
    for h, m, s in resultados:
        print(h, m, s)

# Exemplo de uso:
# Valores de entrada para o teste: 10 horas, 10 minutos, 10 segundos.
H, M, S = 10, 10, 10
ponteiros_iguais(H, M, S)
