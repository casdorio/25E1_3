class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_da_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no_atual = self.raiz
        for char in palavra:
            if char not in no_atual.filhos:
                no_atual.filhos[char] = NoTrie()
            no_atual = no_atual.filhos[char]
        no_atual.fim_da_palavra = True

    def buscar(self, palavra):
        no_atual = self.raiz
        for char in palavra:
            if char not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[char]
        return no_atual.fim_da_palavra

if __name__ == "__main__":
    trie = Trie()
    trie.inserir("casa")
    trie.inserir("carro")
    
    print("Palavra 'casa' está na Trie?", trie.buscar("casa"))
    print("Palavra 'carro' está na Trie?", trie.buscar("carro"))
    print("Palavra 'caminho' está na Trie?", trie.buscar("caminho"))
