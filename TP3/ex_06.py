import heapq

def dijkstra_air_transport(graph, start, end, max_connection_time, required_scales):
    cost = {airport: float('infinity') for airport in graph}
    cost[start] = 0
    
    priority_queue = [(0, start, 0)]  
    
    while priority_queue:
        current_cost, current_airport, current_connection_time = heapq.heappop(priority_queue)
        
        if current_airport == end:
            return current_cost
        
        for neighbor, (flight_cost, connection_time, has_scale) in graph[current_airport].items():
            if has_scale and (current_airport, neighbor) in required_scales:
                flight_cost += required_scales[(current_airport, neighbor)]
            
            if current_connection_time + connection_time > max_connection_time:
                continue
            
            new_cost = current_cost + flight_cost
            new_connection_time = current_connection_time + connection_time
            
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor, new_connection_time))
    
    return None  

graph = {
    'JFK': {'LHR': (500, 2, False), 'CDG': (600, 3, True)},  
    'LHR': {'JFK': (500, 2, False), 'CDG': (450, 2, True)},
    'CDG': {'JFK': (600, 3, True), 'LHR': (450, 2, True)}
}

required_scales = {
    ('JFK', 'CDG'): 100,  
    ('LHR', 'CDG'): 80   
}

max_connection_time = 4

start = 'JFK'
end = 'CDG'

min_cost = dijkstra_air_transport(graph, start, end, max_connection_time, required_scales)

if min_cost is not None:
    print(f"O custo mais baixo para viajar de {start} a {end} é ${min_cost}.")
else:
    print(f"Não há um caminho viável entre {start} e {end} com as restrições de tempo de conexão.")
