class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def minimum_spanning_tree_cost(R, C, edges):
    # Ordena as arestas pelo peso
    edges.sort(key=lambda x: x[2])
    disjoint_set = DisjointSet(R)
    
    mst_cost = 0
    mst_edges = 0
    
    for v, w, p in edges:
        # Subtraímos 1 dos nós para usá-los em 0-based indexing
        if disjoint_set.find(v - 1) != disjoint_set.find(w - 1):
            disjoint_set.union(v - 1, w - 1)
            mst_cost += p
            mst_edges += 1
            if mst_edges == R - 1:  # Se já temos R-1 arestas, a MST está completa
                break
    
    return mst_cost

# Leitura de entrada
R, C = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(C)]

# Calculo do custo mínimo da árvore geradora mínima
result = minimum_spanning_tree_cost(R, C, edges)
print(result)
