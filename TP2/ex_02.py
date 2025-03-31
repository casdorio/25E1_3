import networkx as nx
import matplotlib.pyplot as plt

cidade = {
    "Centro": ["Praia da Costa", "Itapuã"],
    "Praia da Costa": ["Centro", "Itaparica", "Coqueiral de Itaparica"],
    "Itapuã": ["Centro", "Coqueiral de Itaparica", "Jaburuna"],
    "Itaparica": ["Praia da Costa", "Vale Encantado"],
    "Coqueiral de Itaparica": ["Praia da Costa", "Itapuã", "Vale Encantado"],
    "Jaburuna": ["Itapuã", "Vale Encantado"],
    "Vale Encantado": ["Itaparica", "Coqueiral de Itaparica", "Jaburuna"]
}

G = nx.Graph()

for bairro, conexoes in cidade.items():
    for conexao in conexoes:
        G.add_edge(bairro, conexao)

pos = nx.spring_layout(G)

plt.figure(figsize=(8, 6))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='orange',
    node_size=2500,
    font_size=12,
    font_color='black',
    edge_color='gray',
    linewidths=1.5
)

plt.title("Mapa de Bairros de Vila Velha - ES", fontsize=14, fontweight='bold')
plt.show()

