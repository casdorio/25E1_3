import heapq

def prim_algorithm(graph, start):
    visited = {start}
    mst = []
    total_cost = 0

    edges = []
    for neighbor, cost in graph[start]:
        heapq.heappush(edges, (cost, start, neighbor))

    while edges and len(visited) < len(graph):
        cost, source, target = heapq.heappop(edges)
        if target in visited:
            continue

        visited.add(target)
        mst.append((source, target, cost))
        total_cost += cost

        for neighbor, neighbor_cost in graph[target]:
            if neighbor not in visited:
                heapq.heappush(edges, (neighbor_cost, target, neighbor))

    return mst, total_cost

graph_example = {
    'Bairro A': [
        ('Bairro B', 50),
        ('Bairro C', 80)
    ],
    'Bairro B': [
        ('Bairro A', 50),
        ('Bairro D', 30),
        ('Bairro C', 70)
    ],
    'Bairro D': [
        ('Bairro B', 30),
        ('Bairro E', 40)
    ],
    'Bairro C': [
        ('Bairro A', 80),
        ('Bairro B', 70),
        ('Bairro F', 90)
    ],
    'Bairro E': [
        ('Bairro D', 40),
        ('Bairro F', 60)
    ],
    'Bairro F': [
        ('Bairro C', 90),
        ('Bairro E', 60)
    ]
}

mst, total_cost = prim_algorithm(graph_example, 'Bairro A')

print("Conexões recomendadas para expansão da rede:")
for source, target, cost in mst:
    print(f"Conectar {source} a {target} com custo de R$ {cost}")
print(f"\nCusto total de expansão: R$ {total_cost}")
