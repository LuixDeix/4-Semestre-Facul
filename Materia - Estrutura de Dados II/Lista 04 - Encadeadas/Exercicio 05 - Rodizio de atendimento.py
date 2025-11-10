class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class RodizioAtendimento:
    def __init__(self):
        self.inicio = None
        self.atual = None

    def adicionar_jogador(self, nome):
        novo = Jogador(nome)
        if not self.inicio:
            self.inicio = novo
            novo.proximo = novo
        else:
            temp = self.inicio
            while temp.proximo != self.inicio:
                temp = temp.proximo
            temp.proximo = novo
            novo.proximo = self.inicio
        print(f" Jogador '{nome}' entrou no rodízio.")

    def mostrar_jogadores(self):
        if not self.inicio:
            print(" Nenhum jogador no rodízio.")
            return
        atual = self.inicio
        print("\n Lista de jogadores no rodízio:")
        while True:
            print(f"- {atual.nome}")
            atual = atual.proximo
            if atual == self.inicio:
                break

    def iniciar_rodizio(self):
        if not self.inicio:
            print("Nenhum jogador para iniciar o rodízio.")
            return
        self.atual = self.inicio
        print(f" Rodízio iniciado! Primeiro a jogar: {self.atual.nome}")

    def proximo_turno(self):
        if not self.atual:
            print("Rodízio ainda não iniciado. Use iniciar_rodizio().")
            return
        self.atual = self.atual.proximo
        print(f" Agora é a vez de: {self.atual.nome}")

    def remover_jogador(self, nome):
        if not self.inicio:
            print("Rodízio vazio.")
            return

        atual = self.inicio
        anterior = None

        while True:
            if atual.nome == nome:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    # Se for o primeiro nó
                    temp = self.inicio
                    while temp.proximo != self.inicio:
                        temp = temp.proximo
                    temp.proximo = atual.proximo
                    self.inicio = atual.proximo
                print(f" Jogador '{nome}' saiu do rodízio.")
                if self.atual == atual:
                    self.atual = self.atual.proximo
                return
            anterior = atual
            atual = atual.proximo
            if atual == self.inicio:
                break
        print(f" Jogador '{nome}' não encontrado.")

rodizio = RodizioAtendimento()

rodizio.adicionar_jogador("Jenifer")
rodizio.adicionar_jogador("Luis")
rodizio.adicionar_jogador("Dudarts")
rodizio.adicionar_jogador("Flamenguista")

rodizio.mostrar_jogadores()

rodizio.iniciar_rodizio()
rodizio.proximo_turno()
rodizio.proximo_turno()

rodizio.remover_jogador("Flamenguista")
rodizio.mostrar_jogadores()
