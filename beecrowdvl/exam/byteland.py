class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def max_economy(m, n, roads):
    if m == 0 and n == 0:
        return None
    
    # Calcular o custo total
    total_cost = sum(z for _, _, z in roads)
    
    # Ordenar as estradas pelo comprimento
    roads.sort(key=lambda x: x[2])
    
    # Encontrar a MST usando o algoritmo de Kruskal
    uf = UnionFind(m)
    mst_cost = 0
    edges_used = 0
    
    for x, y, z in roads:
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            mst_cost += z
            edges_used += 1
            if edges_used == m - 1:  # Terminamos a MST
                break
    
    # Calcular a economia máxima
    return total_cost - mst_cost

# Leitura da entrada
import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    idx = 0
    results = []
    
    while True:
        m, n = map(int, data[idx].split())
        idx += 1
        if m == 0 and n == 0:
            break
        
        roads = []
        for _ in range(n):
            x, y, z = map(int, data[idx].split())
            roads.append((x, y, z))
            idx += 1
        
        result = max_economy(m, n, roads)
        if result is not None:
            results.append(result)
    
    # Saída dos resultados
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
