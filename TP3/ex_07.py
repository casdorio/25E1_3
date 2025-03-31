import heapq

def prim(graph, start):
    total_cost = 0
    min_cost = {start: 0}
    priority_queue = [(0, start)] 
    visited = set()
    
    while priority_queue:
        current_cost, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        total_cost += current_cost
        
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited:
                if neighbor not in min_cost or weight < min_cost[neighbor]:
                    min_cost[neighbor] = weight
                    heapq.heappush(priority_queue, (weight, neighbor))
    
    return total_cost

graph = {
    'A': {'B': 10, 'C': 20, 'D': 30},
    'B': {'A': 10, 'C': 15, 'E': 50},
    'C': {'A': 20, 'B': 15, 'D': 25, 'E': 10},
    'D': {'A': 30, 'C': 25, 'E': 20},
    'E': {'B': 50, 'C': 10, 'D': 20}
}

start_bairro = 'A'
min_cost = prim(graph, start_bairro)

print(f"Custo total da instalação da fibra óptica: {min_cost}")
