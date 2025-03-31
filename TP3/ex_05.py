import heapq

def dijkstra_city_smart(graph, start, end, max_battery_range):
    dist = {city: float('infinity') for city in graph}
    time = {city: float('infinity') for city in graph}
    dist[start] = 0
    time[start] = 0
    
    priority_queue = [(0, 0, start)]
    
    while priority_queue:
        current_time, current_dist, current_city = heapq.heappop(priority_queue)
        
        if current_city == end:
            return current_time, current_dist
        
        if current_dist > max_battery_range:
            continue 
        
        for neighbor, (time_cost, dist_cost, has_station) in graph[current_city].items():
            new_dist = current_dist + dist_cost
            if new_dist > max_battery_range and not has_station:
                continue  
            
            new_time = current_time + time_cost
            
            if new_time < time[neighbor] or (new_time == time[neighbor] and new_dist < dist[neighbor]):
                dist[neighbor] = new_dist
                time[neighbor] = new_time
                heapq.heappush(priority_queue, (new_time, new_dist, neighbor))
    
    return None, None 

graph = {
    'A': {'B': (5, 10, False), 'C': (3, 7, True)},  
    'B': {'A': (5, 10, False), 'C': (2, 5, False), 'D': (4, 8, True)},
    'C': {'A': (3, 7, True), 'B': (2, 5, False), 'D': (1, 2, False)},
    'D': {'B': (4, 8, True), 'C': (1, 2, False)}
}

start = 'A'
end = 'D'
max_battery_range = 15  

travel_time, travel_distance = dijkstra_city_smart(graph, start, end, max_battery_range)

if travel_time is not None:
    print(f"O tempo mais rápido para ir de {start} a {end} é {travel_time} minutos, percorrendo {travel_distance} km.")
else:
    print(f"Não há caminho disponível de {start} a {end} com a autonomia de {max_battery_range} km.")
