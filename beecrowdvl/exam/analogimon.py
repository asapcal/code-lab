#import sys
#import bisect
#
#def process_gym(IP, attempts):
#    gym = []  # Lista de Poderes de Combate dos analógimôns no ginásio (ordenada)
#    
#    for pc, na in attempts:
#        # Definindo o intervalo de combate permitido [pc - IP, pc + IP]
#        lower_bound = pc - IP
#        upper_bound = pc + IP
#        
#        # Encontrar a posição do primeiro valor maior ou igual a lower_bound
#        left = bisect.bisect_left(gym, lower_bound)
#        # Encontrar a posição do primeiro valor maior que upper_bound
#        right = bisect.bisect_right(gym, upper_bound)
#        
#        # Contando analógimôns dentro do intervalo
#        num_in_range = right - left
#        
#        # Verificar se pode inserir o novo analógimôn
#        if num_in_range <= na:
#            # Inserindo o novo analógimôn mantendo a lista ordenada
#            bisect.insort(gym, pc)
#    
#    return len(gym)
#
#def main():
#    input = sys.stdin.read
#    data = input().strip().splitlines()
#    
#    index = 0
#    results = []
#    
#    while index < len(data):
#        # Lendo IP e M para cada caso de teste
#        ip, m = map(int, data[index].split())
#        index += 1
#        
#        attempts = []
#        for _ in range(m):
#            pc, na = map(int, data[index].split())
#            attempts.append((pc, na))
#            index += 1
#        
#        # Processa o ginásio e armazena o resultado
#        results.append(process_gym(ip, attempts))
#    
#    # Imprime todos os resultados
#    print("\n".join(map(str, results)))
#
#if __name__ == "__main__":
#    main()
#

#from sortedcontainers import SortedList
#
#def process_gym(IP, attempts):
#    gym = SortedList()  # Usa SortedList para manter a lista ordenada
#    
#    for pc, na in attempts:
#        # Definindo o intervalo de combate permitido [pc - IP, pc + IP]
#        lower_bound = pc - IP
#        upper_bound = pc + IP
#        
#        # Encontrar quantos analógimôns estão no intervalo [lower_bound, upper_bound]
#        num_in_range = gym.bisect_right(upper_bound) - gym.bisect_left(lower_bound)
#        
#        # Verificar se pode inserir o novo analógimôn
#        if num_in_range <= na:
#            gym.add(pc)  # Inserir o novo analógimôn mantendo a lista ordenada
#    
#    return len(gym)
#
#def main():
#    results = []
#    
#    while True:
#        try:
#            ip, m = map(int, input().split())
#            attempts = []
#            for _ in range(m):
#                pc, na = map(int, input().split())
#                attempts.append((pc, na))
#            results.append(process_gym(ip, attempts))
#        except EOFError:
#            break
#    
#    print("\n".join(map(str, results)))
#
#if __name__ == "__main__":
#    main()
#
#
#class FenwickTree:
#    def __init__(self, size):
#        self.size = size
#        self.tree = [0] * (size + 1)
#
#    def update(self, index, value):
#        while index <= self.size:
#            self.tree[index] += value
#            index += index & -index
#
#    def query(self, index):
#        result = 0
#        while index > 0:
#            result += self.tree[index]
#            index -= index & -index
#        return result
#
#    def range_query(self, left, right):
#        return self.query(right) - self.query(left - 1)
#
#
#def process_gym(IP, attempts, max_pc):
#    fenwick = FenwickTree(max_pc)
#    gym = set()  # Usamos um set para garantir que não haja repetição de PC
#    
#    for pc, na in attempts:
#        # Verificar quantos analógimôns estão no intervalo [pc - IP, pc + IP]
#        lower_bound = max(1, pc - IP)
#        upper_bound = min(max_pc, pc + IP)
#        
#        num_in_range = fenwick.range_query(lower_bound, upper_bound)
#        
#        # Verificar se pode inserir o novo analógimôn
#        if num_in_range <= na and pc not in gym:
#            # Inserir no ginásio
#            gym.add(pc)
#            fenwick.update(pc, 1)  # Atualiza o Fenwick Tree para contar esse PC
#    
#    return len(gym)
#
#
#def main():
#    results = []
#    max_pc = 100000  # O maior valor possível para o PC
#
#    while True:
#        try:
#            ip, m = map(int, input().split())
#            attempts = []
#            for _ in range(m):
#                pc, na = map(int, input().split())
#                attempts.append((pc, na))
#            results.append(process_gym(ip, attempts, max_pc))
#        except EOFError:
#            break
#    
#    print("\n".join(map(str, results)))
#
#
#if __name__ == "__main__":
#    main()
#
import sys
from sortedcontainers import SortedList

def process_gym(IP, attempts):
    gym = SortedList()  # Manter os PCs ordenados
    
    for pc, na in attempts:
        # Verificar quantos analógimôns estão no intervalo [pc - IP, pc + IP]
        lower_bound = pc - IP
        upper_bound = pc + IP
        
        # Obter o número de analógimôns no intervalo usando a SortedList
        num_in_range = gym.bisect_right(upper_bound) - gym.bisect_left(lower_bound)
        
        # Se o número de analógimôns no intervalo for menor ou igual ao NA, insere no ginásio
        if num_in_range <= na:
            gym.add(pc)  # Adiciona o novo analógimôn na posição correta
    
    return len(gym)

def main():
    input_data = sys.stdin.read().strip().splitlines()  # Lê toda a entrada de uma vez
    idx = 0
    results = []
    
    while idx < len(input_data):
        ip, m = map(int, input_data[idx].split())
        attempts = []
        for i in range(m):
            pc, na = map(int, input_data[idx + 1 + i].split())
            attempts.append((pc, na))
        results.append(process_gym(ip, attempts))
        idx += m + 1
    
    # Exibe todos os resultados de uma vez
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
