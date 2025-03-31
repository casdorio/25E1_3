from collections import deque

grafo = {
    "A": ["B", "C"],  
    "B": ["A", "D", "E"],  
    "C": ["A", "F"],  
    "D": ["B"],  
    "E": ["B", "F"], 
    "F": ["C", "E"]  
}

def bfs_caminho_curto(grafo, inicio, destino):
    visitados = set([inicio])
    fila = deque([[inicio]])  
    
    while fila:
        caminho_atual = fila.popleft()  
        ultimo_vertice = caminho_atual[-1] 
        
        if ultimo_vertice == destino:
            return caminho_atual
        
        for vizinho in grafo[ultimo_vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho_atual + [vizinho])  

    return None  

def bfs_com_ordem(grafo, inicio, destino):
    visitados = set([inicio])
    fila = deque([[inicio]])  
    ordem_visita = [] 
    
    while fila:
        caminho_atual = fila.popleft()  
        ultimo_vertice = caminho_atual[-1] 
        
        if ultimo_vertice == destino:
            return caminho_atual, ordem_visita
        
        for vizinho in grafo[ultimo_vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho_atual + [vizinho]) 
                ordem_visita.append(vizinho)  

    return None, ordem_visita  

caminho = bfs_caminho_curto(grafo, "A", "F")
print("Caminho mais curto de A a F:", caminho)

caminho, ordem = bfs_com_ordem(grafo, "A", "F")
print("Caminho mais curto de A a F:", caminho)
print("Ordem dos bairros visitados:", ordem)
