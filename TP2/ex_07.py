
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"],
}

print("Conexões entre as Cidades (Estradas):")
for cidade, estradas in grafo.items():
    print(f"{cidade}: {estradas}")

def busca_em_profundidade(cidades, inicio, visitadas=None):
    if visitadas is None:
        visitadas = set()
    visitadas.add(inicio)
    print(inicio, end=" ")
    for cidade_vizinha in cidades[inicio]:
        if cidade_vizinha not in visitadas:
            busca_em_profundidade(cidades, cidade_vizinha, visitadas)

from collections import deque
def busca_em_largura(cidades, inicio):
    visitadas = set([inicio])
    fila = deque([inicio])
    while fila:
        atual = fila.popleft()
        print(atual, end=" ")
        for cidade_vizinha in cidades[atual]:
            if cidade_vizinha not in visitadas:
                visitadas.add(cidade_vizinha)
                fila.append(cidade_vizinha)

print("\nTravessia em Profundidade (DFS) começando pela Cidade A:")
busca_em_profundidade(grafo, "A")

print("\nTravessia em Largura (BFS) começando pela Cidade A:")
busca_em_largura(grafo, "A")
