class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False  

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  
            node = node.children[char]
        node.is_end_of_word = True 

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return [] 
            node = node.children[char]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        palavras = []
        if node.is_end_of_word:
            palavras.append(prefix)

        for char, next_node in node.children.items():
            palavras.extend(self._collect_words(next_node, prefix + char))

        return palavras

trie = Trie()
trie.insert("casa")
trie.insert("carro")
trie.insert("cadeira")
trie.insert("caminhão")
trie.insert("cachorro")

print(trie.search_prefix("ca"))
print(trie.search_prefix("cad"))
print(trie.search_prefix("cam"))
print(trie.search_prefix("xyz"))
