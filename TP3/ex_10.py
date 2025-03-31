import heapq

def prim(graph, bairros):
    n = len(graph)
    min_cost = [float('inf')] * n
    min_cost[0] = 0
    visited = [False] * n
    prev = [None] * n
    pq = [(0, 0)]
    
    while pq:
        cost, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        for v, weight in enumerate(graph[u]):
            if not visited[v] and weight < min_cost[v]:
                min_cost[v] = weight
                prev[v] = u
                heapq.heappush(pq, (weight, v))
    
    mst_edges = []
    for v in range(1, n):
        if prev[v] is not None:
            mst_edges.append((bairros[prev[v]], bairros[v], graph[v][prev[v]]))
    
    return mst_edges

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

bairros = ["Bairro A", "Bairro B", "Bairro C", "Bairro D", "Bairro E"]

mst_edges = prim(graph, bairros)
print(mst_edges)
