class HeapArray:
    def __init__(self, elementos=None):
        self.heap = elementos if elementos else []

    def obter_pai(self, i):
        return (i - 1) // 2 if i > 0 else None

    def obter_filho_esquerdo(self, i):
        return 2 * i + 1 if 2 * i + 1 < len(self.heap) else None

    def obter_filho_direito(self, i):
        return 2 * i + 2 if 2 * i + 2 < len(self.heap) else None

if __name__ == "__main__":
    heap = HeapArray([10, 20, 30, 40, 50, 60, 70])
    
    indice = 2 
    print(f"Elemento no índice {indice}: {heap.heap[indice]}")
    
    pai = heap.obter_pai(indice)
    print(f"Índice do pai: {pai}, Valor: {heap.heap[pai] if pai is not None else 'Não existe'}")
    
    filho_esq = heap.obter_filho_esquerdo(indice)
    print(f"Índice do filho esquerdo: {filho_esq}, Valor: {heap.heap[filho_esq] if filho_esq is not None else 'Não existe'}")
    
    filho_dir = heap.obter_filho_direito(indice)
    print(f"Índice do filho direito: {filho_dir}, Valor: {heap.heap[filho_dir] if filho_dir is not None else 'Não existe'}")
