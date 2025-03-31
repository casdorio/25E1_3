import random
import time
import heapq

def create_random_network(n, edge_probability=0.1):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < edge_probability:
                weight = random.randint(1, 10)
                graph[i].append((j, weight))
    return graph

def dijkstra_algorithm(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    return distances

def floyd_warshall_algorithm(n, graph):
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0

    for u in range(n):
        for v, weight in graph[u]:
            distances[u][v] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances

def evaluate_algorithm_performance(n, edge_probability):
    graph = create_random_network(n, edge_probability)

    start_time = time.time()
    dijkstra_algorithm(graph, 0)
    dijkstra_duration = time.time() - start_time

    start_time = time.time()
    floyd_warshall_algorithm(n, graph)
    floyd_duration = time.time() - start_time

    return dijkstra_duration, floyd_duration

graph_sizes = [50, 100, 150, 500, 600]
edge_probability = 0.1

print("Análise de tempos de execução:")
print("Nº de Vértices | Tempo Dijkstra (seg) | Tempo Floyd-Warshall (seg)")
for n in graph_sizes:
    d_time, f_time = evaluate_algorithm_performance(n, edge_probability)
    print(f"{n:>15} | {d_time:>21.5f} | {f_time:>25.5f}")
