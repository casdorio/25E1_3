import networkx as nx
import matplotlib.pyplot as plt

rede_social = {
    "Alice": ["Bob", "Carlos"],
    "Bob": ["Alice", "Diana"],
    "Carlos": ["Alice", "Diana", "Eduardo"],
    "Diana": ["Bob", "Carlos"],
    "Eduardo": ["Carlos"]
}

G = nx.Graph()

for pessoa, conexoes in rede_social.items():
    for conexao in conexoes:
        G.add_edge(pessoa, conexao)

pos = nx.kamada_kawai_layout(G)  

plt.figure(figsize=(8, 6))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=2500, 
    font_size=12,  
    font_color='darkblue', 
    edge_color='black',
    linewidths=1.5
)

plt.title("Rede Social Simples", fontsize=14, fontweight='bold')
plt.show()
