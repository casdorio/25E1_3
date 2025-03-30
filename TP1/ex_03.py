class MaxHeap:
    def __init__(self, elementos=None):
        self.heap = elementos or []
        if self.heap:
            for i in range((len(self.heap) - 2) // 2, -1, -1):
                self._ajustar_para_baixo(i)

    def adicionar(self, valor):
        self.heap.append(valor)
        self._ajustar_para_cima(len(self.heap) - 1)

    def _ajustar_para_cima(self, indice):
        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice] > self.heap[pai]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover_maximo(self):
        if not self.heap:
            return None
        maior_valor = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._ajustar_para_baixo(0)
        return maior_valor

    def _ajustar_para_baixo(self, indice):
        tamanho = len(self.heap)
        while indice < tamanho:
            maior = indice
            esquerda, direita = 2 * indice + 1, 2 * indice + 2

            if esquerda < tamanho and self.heap[esquerda] > self.heap[maior]:
                maior = esquerda
            if direita < tamanho and self.heap[direita] > self.heap[maior]:
                maior = direita

            if maior == indice:
                break

            self.heap[indice], self.heap[maior] = self.heap[maior], self.heap[indice]
            indice = maior

if __name__ == "__main__":
    heap_inicial = [50, 30, 40, 10, 20, 35]
    max_heap = MaxHeap(heap_inicial)

    print("Heap inicial:", max_heap.heap)

    max_heap.adicionar(45)
    print("Após adicionar 45:", max_heap.heap)

    maior_removido = max_heap.remover_maximo()
    print("Valor removido (maior):", maior_removido)
    print("Heap após remoção do maior valor:", max_heap.heap)
