import heapq

def dijkstra(graph, start, end):
    dist = {city: float('infinity') for city in graph}
    dist[start] = 0  
    
    priority_queue = [(0, start)] 
    
    while priority_queue:
        current_cost, current_city = heapq.heappop(priority_queue)
        
        if current_city == end:
            break
        
        if current_cost > dist[current_city]:
            continue
        
        for neighbor, cost in graph[current_city].items():
            total_cost = current_cost + cost
            
            if total_cost < dist[neighbor]:
                dist[neighbor] = total_cost
                heapq.heappush(priority_queue, (total_cost, neighbor))
    
    return dist[end] if dist[end] != float('infinity') else None

graph = {
    'CidadeA': {'CidadeB': 50, 'CidadeC': 70},
    'CidadeB': {'CidadeA': 50, 'CidadeC': 60, 'CidadeD': 90},
    'CidadeC': {'CidadeA': 70, 'CidadeB': 60, 'CidadeD': 40},
    'CidadeD': {'CidadeB': 90, 'CidadeC': 40}
}

start = 'CidadeA'
end = 'CidadeD'

lowest_cost = dijkstra(graph, start, end)

if lowest_cost is not None:
    print(f"O custo mais barato para ir de {start} a {end} é R${lowest_cost}.")
else:
    print(f"Não há caminho disponível entre {start} e {end}.")
