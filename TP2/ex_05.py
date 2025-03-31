import networkx as nx
import matplotlib.pyplot as plt

logistica = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 7},
    "C": {"A": 10, "E": 8},
    "D": {"B": 7, "E": 6},
    "E": {"C": 8, "D": 6}
}

def vizinhos(centro):
    return logistica.get(centro, {})

def bfs_rota_mais_curta(inicio, destino):
    from collections import deque
    fila = deque([(inicio, [inicio])])
    visitados = set()
    
    while fila:
        atual, caminho = fila.popleft()
        if atual == destino:
            return caminho
        
        visitados.add(atual)
        for vizinho in logistica[atual]:
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))
    
    return None

G = nx.Graph()
for centro, conexoes in logistica.items():
    for vizinho, peso in conexoes.items():
        G.add_edge(centro, vizinho, weight=peso)

pos = nx.spring_layout(G)

plt.figure(figsize=(8, 6))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2500,
    font_size=12,
    edge_color='gray',
    linewidths=1.5
)

edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("Mapa de Centros de Distribuição", fontsize=14, fontweight='bold')
plt.show()

