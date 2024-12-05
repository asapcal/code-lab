import math

def simplificar(numerador, denominador):
    # Calcula o Máximo Divisor Comum (MDC) entre numerador e denominador
    divisor_comum = math.gcd(numerador, denominador)
    # Retorna o numerador e denominador simplificados
    return numerador // divisor_comum, denominador // divisor_comum

def calcular_operacao(N1, D1, operacao, N2, D2):
    # Realiza a operação conforme o tipo
    if operacao == '+':
        # Soma: (N1 * D2 + N2 * D1) / (D1 * D2)
        num = N1 * D2 + N2 * D1
        den = D1 * D2
    elif operacao == '-':
        # Subtração: (N1 * D2 - N2 * D1) / (D1 * D2)
        num = N1 * D2 - N2 * D1
        den = D1 * D2
    elif operacao == '*':
        # Multiplicação: (N1 * N2) / (D1 * D2)
        num = N1 * N2
        den = D1 * D2
    elif operacao == '/':
        # Divisão: (N1 * D2) / (N2 * D1)
        num = N1 * D2
        den = N2 * D1
    return num, den

def main():
    # Lê o número de casos de teste
    n = int(input())
    
    for _ in range(n):
        # Lê a expressão
        N1, _, D1, operacao, N2, _, D2 = input().split()
        # Converte as frações de string para inteiros
        N1, D1, N2, D2 = int(N1), int(D1), int(N2), int(D2)
        
        # Calcula o numerador e denominador após a operação
        num, den = calcular_operacao(N1, D1, operacao, N2, D2)
        
        # Simplifica a fração resultante
        num_simplificado, den_simplificado = simplificar(num, den)
        
        # Exibe a saída no formato requerido
        print(f"{num}/{den} = {num_simplificado}/{den_simplificado}")

# Executa a função principal
main()
