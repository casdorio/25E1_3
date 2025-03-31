transacoes = {
    "Conta A": ["Conta B"],
    "Conta B": ["Conta C"],
    "Conta C": ["Conta D"],
    "Conta D": ["Conta A"],
    "Conta E": ["Conta F"],
    "Conta F": ["Conta G"],
    "Conta G": ["Conta H"],
    "Conta H": []
}

def detectar_ciclo(grafo):
    visitados = set() 
    pilha_recursiva = set()

    def dfs(v):
        if v in pilha_recursiva:
            return True
        if v in visitados:
            return False
        
        visitados.add(v)
        pilha_recursiva.add(v)
        
        for vizinho in grafo[v]:
            if dfs(vizinho):
                return True
        
        pilha_recursiva.remove(v)
        return False

    for vertice in grafo:
        if vertice not in visitados:
            if dfs(vertice):
                return True
    return False

if detectar_ciclo(transacoes):
    print("Ciclo detectado: possível fraude financeira!")
else:
    print("Nenhum ciclo detectado.")
