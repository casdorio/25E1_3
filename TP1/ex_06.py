import heapq

class FilaDePrioridade:
    def __init__(self):
        self.fila = []

    def adicionar_tarefa(self, prioridade, tarefa):
        heapq.heappush(self.fila, (prioridade, tarefa))

    def proxima_tarefa(self):
        return heapq.heappop(self.fila)[1] if self.fila else None

    def visualizar_tarefas(self):
        return sorted(self.fila)

if __name__ == "__main__":
    agenda = FilaDePrioridade()
    
    agenda.adicionar_tarefa(3, "Enviar relatório")
    agenda.adicionar_tarefa(1, "Atender cliente urgente")
    agenda.adicionar_tarefa(2, "Reunião com equipe")

    print("Tarefas na fila:", agenda.visualizar_tarefas())
    print("Próxima tarefa a ser executada:", agenda.proxima_tarefa())
    print("Tarefas restantes:", agenda.visualizar_tarefas())
