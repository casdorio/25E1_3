import heapq

def dijkstra(graph, start, end):
    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0  
    
    priority_queue = [(0, start)] 
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex == end:
            break
        
        if current_distance > dist[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist[end] if dist[end] != float('infinity') else None

graph = {
    'Centro': {'A': 10, 'B': 5, 'C': 15},
    'A': {'Centro': 10, 'B': 4, 'D': 12},
    'B': {'Centro': 5, 'A': 4, 'D': 6},
    'C': {'Centro': 15, 'D': 8},
    'D': {'A': 12, 'B': 6, 'C': 8}
}

start = 'Centro'
end = 'D'

shortest_time = dijkstra(graph, start, end)

if shortest_time is not None:
    print(f"O tempo mais rápido para ir de {start} a {end} é {shortest_time} minutos.")
else:
    print(f"Não há caminho disponível entre {start} e {end}.")
