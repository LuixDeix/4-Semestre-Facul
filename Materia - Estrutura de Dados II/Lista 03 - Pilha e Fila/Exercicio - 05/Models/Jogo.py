from src.Pilha.Pilha import Pilha

class Jogo:
    def __init__(self, limite_historico=5):
        self.estado_atual = 0
        self.pilha_historico = Pilha()
        self.limite_historico = limite_historico
        print("Jogo iniciado. Estado inicial: 0")

    def fazer_jogada(self, novo_estado):
        if self.pilha_historico.tamanho() == self.limite_historico:
            self.pilha_historico.itens.pop(0)
            
        self.pilha_historico.empilhar(self.estado_atual)
        self.estado_atual = novo_estado
        print(f"Jogada realizada. Novo estado: {self.estado_atual}")

    def voltar_no_tempo(self):
        estado_anterior = self.pilha_historico.desempilhar()
        if estado_anterior is not None:
            self.estado_atual = estado_anterior
            print(f"Voltando no tempo... Estado restaurado: {self.estado_atual}")
        else:
            print("Não é possível voltar no tempo. Você está no estado inicial.")

    def mostrar_estado(self):
        print("\n--- Estado Atual do Jogo ---")
        print(f"Estado: {self.estado_atual}")
        print(f"Histórico ({self.pilha_historico.tamanho()} jogadas): {self.pilha_historico.listar()}")
        print("----------------------------")