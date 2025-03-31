
grafo = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [6],
    6: []
}

def dfs(grafo, vertice, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(vertice)
    print(vertice, end=" ")
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

print("DFS a partir do vértice 1:")
dfs(grafo, 1)