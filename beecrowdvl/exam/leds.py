def contar_leds(numero):
    """
    Conta a quantidade de LEDs necessários para representar um número.

    Args:
        numero: O número a ser analisado.

    Returns:
        O número de LEDs necessários.
    """
    # Dicionário com a quantidade de LEDs para cada dígito
    leds_por_digito = {
        '1': 2, '2': 5, '3': 5, '4': 4, '5': 5,
        '6': 6, '7': 3, '8': 7, '9': 6, '0': 6
    }

    # Soma a quantidade de LEDs para cada dígito no número
    return sum(leds_por_digito[digito] for digito in numero)

if __name__ == "__main__":
    # Lê o número de casos de teste
    num_casos = int(input().strip())

    # Processa cada caso de teste e imprime o resultado
    for _ in range(num_casos):
        numero = input().strip()
        resultado = contar_leds(numero)
        print(f"{resultado} leds")
