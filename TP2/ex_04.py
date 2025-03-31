class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}
    
    def adicionar_bairro(self, bairro):
        if bairro not in self.lista_adjacencia:
            self.lista_adjacencia[bairro] = []
    
    def adicionar_conexao(self, bairro1, bairro2):
        if bairro1 in self.lista_adjacencia and bairro2 in self.lista_adjacencia:
            self.lista_adjacencia[bairro1].append(bairro2)
            self.lista_adjacencia[bairro2].append(bairro1) 
    
    def vizinhos(self, bairro):
        return self.lista_adjacencia.get(bairro, [])
    
    def mostrar_grafo(self):
        for bairro, vizinhos in self.lista_adjacencia.items():
            print(f"{bairro} -> {', '.join(vizinhos)}")

grafo = Grafo()

grafo.adicionar_bairro("Centro")
grafo.adicionar_bairro("Bairro A")
grafo.adicionar_bairro("Bairro B")
grafo.adicionar_bairro("Bairro C")
grafo.adicionar_bairro("Bairro D")

grafo.adicionar_conexao("Centro", "Bairro A")
grafo.adicionar_conexao("Centro", "Bairro B")
grafo.adicionar_conexao("Bairro A", "Bairro C")
grafo.adicionar_conexao("Bairro B", "Bairro C")
grafo.adicionar_conexao("Bairro C", "Bairro D")

grafo.mostrar_grafo()

bairro = "Bairro C"
print(f"Vizinhos de {bairro}: {grafo.vizinhos(bairro)}")
