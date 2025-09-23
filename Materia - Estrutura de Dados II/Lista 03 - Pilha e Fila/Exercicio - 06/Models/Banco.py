import random
from Models.Cliente import Cliente
from src.Fila.Fila import Fila

class Banco:
    def __init__(self, tempo_total_simulacao, tempo_medio_chegada, tempo_medio_atendimento):
        self.fila = Fila()
        self.tempo_total_simulacao = tempo_total_simulacao
        self.tempo_medio_chegada = tempo_medio_chegada
        self.tempo_medio_atendimento = tempo_medio_atendimento
        
        self.clientes_atendidos = 0
        self.tempo_total_espera = 0
        self.tempo_servidor_livre = True
        self.cliente_id_counter = 0

    def rodar_simulacao(self):
        tempo_servico_restante = 0

        print("--- Simulacão de Atendimento de Clientes Iniciada ---")
        
        for tempo_atual in range(self.tempo_total_simulacao):
            if random.random() < 1/self.tempo_medio_chegada:
                self.cliente_id_counter += 1
                novo_cliente = Cliente(self.cliente_id_counter, tempo_atual)
                self.fila.enfileirar(novo_cliente)
                print(f"Tempo {tempo_atual}: Cliente {novo_cliente.id} chegou. Fila: {self.fila.tamanho()} clientes")

            if self.tempo_servidor_livre and not self.fila.taVazio():
                cliente_a_atender = self.fila.desenfileirar().dado
                self.tempo_servidor_livre = False
                
                tempo_espera = tempo_atual - cliente_a_atender.tempo_chegada
                self.tempo_total_espera += tempo_espera
                
                tempo_servico_restante = random.expovariate(1/self.tempo_medio_atendimento)
                tempo_servico_restante = max(1, int(tempo_servico_restante))
                
                print(f"Tempo {tempo_atual}: Atendimento do Cliente {cliente_a_atender.id} começou. Tempo de espera: {tempo_espera} min")
            
            if not self.tempo_servidor_livre:
                tempo_servico_restante -= 1
                if tempo_servico_restante <= 0:
                    self.tempo_servidor_livre = True
                    self.clientes_atendidos += 1
                    print(f"Tempo {tempo_atual}: Atendimento finalizado.")

        print("\n--- Simulação Concluída ---")

    def mostrar_resultados(self):
        print("\n=== Resultados Finais ===")
        print(f"Clientes atendidos: {self.clientes_atendidos}")
        
        if self.clientes_atendidos > 0:
            tempo_medio_espera = self.tempo_total_espera / self.clientes_atendidos
            print(f"Tempo médio de espera: {tempo_medio_espera:.2f} minutos")
        else:
            print("Nenhum cliente foi atendido.")

        print(f"Clientes restantes na fila: {self.fila.tamanho()}")
        if self.fila.tamanho() > 0:
            clientes_restantes = [c.dado.id for c in self.fila.listar()]
            print(f"IDs dos clientes restantes: {clientes_restantes}")