from src.Pilha.Pilha import Pilha

class HistoricoAcoes:
    def __init__(self):
        self.acoes_pilha = Pilha()
        print("Histórico de ações inicializado.")

    def registrar_acao(self, acao):
        self.acoes_pilha.empilhar(acao)
        print(f"Ação registrada: '{acao}'")

    def desfazer(self):
        try:
            ultima_acao = self.acoes_pilha.desempilhar()
            print(f"Ação desfeita: '{ultima_acao}'")
            return ultima_acao
        except IndexError:
            print("Não há mais ações para desfazer.")
            return None

    def mostrar_historico(self):
        print("\n--- Histórico de Ações (mais recente para mais antiga) ---")
        if self.acoes_pilha.taVazio():
            print("O histórico está vazio.")
        else:
            historico = self.acoes_pilha.listar()
            for i, acao in enumerate(historico):
                print(f"{i+1}. {acao}")
        print("----------------------------------------------------------")