import heapq

def prim(graph):
    n = len(graph)
    
    min_cost = [float('inf')] * n  
    min_cost[0] = 0  
    visited = [False] * n  
    prev = [None] * n

    pq = [(0, 0)]  
    mst_edges = []  
    
    while pq:
        cost, u = heapq.heappop(pq)  
        
        if visited[u]:
            continue  
        
        visited[u] = True  
        
        if u != 0: 
            mst_edges.append((prev[u], u, cost))
        
        for v in range(n):
            if not visited[v] and graph[u][v] < min_cost[v]:
                min_cost[v] = graph[u][v]
                prev[v] = u  
                heapq.heappush(pq, (graph[u][v], v))  
    
    return mst_edges

graph = [
    [0, 10, 20, 0, 0], 
    [10, 0, 5, 15, 0], 
    [20, 5, 0, 10, 30],
    [0, 15, 10, 0, 50], 
    [0, 0, 30, 50, 0]  
]

mst_edges = prim(graph)

print("Arestas da Árvore Geradora Mínima:")
for u, v, cost in mst_edges:
    print(f"De cidade {u} para cidade {v} com custo {cost}")
