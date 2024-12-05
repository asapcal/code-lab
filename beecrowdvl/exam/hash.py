def hash_function(key, m):
    # Função de dispersão que retorna o índice com base na chave
    return key % m

def insert(table, key, m):
    # Insere a chave na tabela na posição calculada pela função hash
    index = hash_function(key, m)
    table[index].append(key)

if __name__ == "__main__":
    num_cases = int(input())  # Quantidade de casos de teste

    result = []  # Armazenar o resultado para imprimir tudo de uma vez no final

    for _ in range(num_cases):
        m, n = map(int, input().split())  # Número de endereços e número de chaves
        table = [[] for _ in range(m)]  # Tabela hash com listas vazias
        keys = list(map(int, input().split()))  # Lista das chaves a serem inseridas

        # Inserção das chaves na tabela
        for key in keys:
            insert(table, key, m)

        # Preparar a saída para este caso de teste
        case_result = []
        for i in range(m):
            if table[i]:
                case_result.append(f"{i} -> " + " -> ".join(map(str, table[i])) + " -> \\")
            else:
                case_result.append(f"{i} -> \\")
        
        result.append("\n".join(case_result))  # Armazenar os resultados do caso de teste
    
    # Imprimir todos os resultados, separando os casos por uma linha em branco
    print("\n\n".join(result))
