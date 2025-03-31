from collections import deque

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"],
}

def busca_em_largura(grafo, inicio):
    visitadas = set([inicio]) 
    fila = deque([inicio])  
    
    ordem_visitados = []
    
    while fila:
        atual = fila.popleft() 
        ordem_visitados.append(atual)
        for vizinho in grafo[atual]:
            if vizinho not in visitadas:
                visitadas.add(vizinho)
                fila.append(vizinho)

    return ordem_visitados

ordem = busca_em_largura(grafo, "A")
print("Ordem dos vértices visitados pela BFS:", ordem)
