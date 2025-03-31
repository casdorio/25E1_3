import heapq

def dijkstra(graph, start, end):
    dist = {airport: float('infinity') for airport in graph}
    dist[start] = 0  
    
    priority_queue = [(0, start)] 
    
    while priority_queue:
        current_distance, current_airport = heapq.heappop(priority_queue)
        
        if current_airport == end:
            break
        
        if current_distance > dist[current_airport]:
            continue
        
        for neighbor, weight in graph[current_airport].items():
            distance = current_distance + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist[end] if dist[end] != float('infinity') else None

graph = {
    'Aeroporto1': {'Aeroporto2': 300, 'Aeroporto3': 500},
    'Aeroporto2': {'Aeroporto1': 300, 'Aeroporto3': 200, 'Aeroporto4': 600},
    'Aeroporto3': {'Aeroporto1': 500, 'Aeroporto2': 200, 'Aeroporto4': 100},
    'Aeroporto4': {'Aeroporto2': 600, 'Aeroporto3': 100}
}

start = 'Aeroporto1'
end = 'Aeroporto4'

shortest_distance = dijkstra(graph, start, end)

if shortest_distance is not None:
    print(f"A distância mais curta entre {start} e {end} é {shortest_distance} km.")
else:
    print(f"Não há caminho disponível entre {start} e {end}.")
