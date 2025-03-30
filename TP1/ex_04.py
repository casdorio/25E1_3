class MinHeap:
    def __init__(self, arr=None):
        self.heap = arr or []
        if self.heap:
            for i in range((len(self.heap) - 2) // 2, -1, -1):
                self._heapify_down(i)

    def pop(self):
        if not self.heap:
            return None
        
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self._heapify_down(0)
        
        return raiz

    def _heapify_down(self, index):
        tamanho = len(self.heap)
        while index < tamanho:
            menor = index
            esquerda, direita = 2 * index + 1, 2 * index + 2

            if esquerda < tamanho and self.heap[esquerda] < self.heap[menor]:
                menor = esquerda
            if direita < tamanho and self.heap[direita] < self.heap[menor]:
                menor = direita

            if menor == index:
                break

            self.heap[index], self.heap[menor] = self.heap[menor], self.heap[index]
            index = menor

if __name__ == "__main__":
    heap_inicial = [10, 20, 30, 40, 50]
    min_heap = MinHeap(heap_inicial)

    print("Heap inicial:", min_heap.heap)

    removido = min_heap.pop()
    print("Elemento removido (raiz):", removido)
    print("Heap após remoção da raiz:", min_heap.heap)
