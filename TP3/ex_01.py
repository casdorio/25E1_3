import heapq

def dijkstra(graph, start):
    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0  
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > dist[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist

graph = {
    'Centro': {'A': 4, 'B': 2},
    'A': {'Centro': 4, 'B': 5, 'C': 10},
    'B': {'Centro': 2, 'A': 5, 'C': 3},
    'C': {'A': 10, 'B': 3}
}

start = 'Centro'

distances = dijkstra(graph, start)

print("Menores distâncias a partir do Centro de Distribuição:")
for bairro, distance in distances.items():
    print(f"Distância até {bairro}: {distance}")
