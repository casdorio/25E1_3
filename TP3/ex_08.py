def floyd_warshall(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    
    for u in vertices:
        dist[u][u] = 0  
        for v, weight in graph[u].items():
            dist[u][v] = weight  
    
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = {
    'A': {'B': 10, 'C': 30, 'D': 50},
    'B': {'A': 10, 'C': 20, 'E': 60},
    'C': {'A': 30, 'B': 20, 'D': 10, 'E': 40},
    'D': {'A': 50, 'C': 10, 'E': 30},
    'E': {'B': 60, 'C': 40, 'D': 30}
}

distances = floyd_warshall(graph)

for u in distances:
    for v in distances[u]:
        print(f"Distância mínima de {u} para {v}: {distances[u][v]} minutos")
