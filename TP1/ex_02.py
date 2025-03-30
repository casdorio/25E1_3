class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _pai(self, indice):
        return (indice - 1) // 2
    
    def _filho_esquerdo(self, indice):
        return 2 * indice + 1
    
    def _filho_direito(self, indice):
        return 2 * indice + 2
    
    def _ajustar_para_cima(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[self._pai(indice)]:
            self.heap[indice], self.heap[self._pai(indice)] = self.heap[self._pai(indice)], self.heap[indice]
            indice = self._pai(indice)
    
    def _ajustar_para_baixo(self, indice):
        menor = indice
        esquerdo = self._filho_esquerdo(indice)
        direito = self._filho_direito(indice)
        
        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[menor]:
            menor = esquerdo
        if direito < len(self.heap) and self.heap[direito] < self.heap[menor]:
            menor = direito
        
        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._ajustar_para_baixo(menor)
    
    def inserir(self, valor):
        self.heap.append(valor)
        self._ajustar_para_cima(len(self.heap) - 1)
    
    def remover_minimo(self):
        if not self.heap:
            raise IndexError("Heap está vazio")
        
        minimo = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._ajustar_para_baixo(0)
        
        return minimo
    
    def ver_minimo(self):
        if not self.heap:
            raise IndexError("Heap está vazio")
        return self.heap[0]
    
    def esta_vazio(self):
        return len(self.heap) == 0
    
    def __str__(self):
        return str(self.heap)

heap = MinHeap()
heap.inserir(10)
heap.inserir(5)
heap.inserir(15)
heap.inserir(3)

print(heap)
print(heap.remover_minimo())
print(heap)
