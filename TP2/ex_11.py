grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

def dfs_recursivo(grafo, inicio, visitados=None, ordem=None):

    if visitados is None:
        visitados = set()
    if ordem is None:
        ordem = []

    visitados.add(inicio)
    ordem.append(inicio)

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados, ordem)

    return ordem

ordem_dfs = dfs_recursivo(grafo, "A")
print("Ordem de visitação (DFS) a partir de A:", ordem_dfs)