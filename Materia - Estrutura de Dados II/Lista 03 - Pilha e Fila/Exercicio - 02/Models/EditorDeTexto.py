from src.Pilha.Pilha import Pilha
from src.No.No import No

class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.pilha_undo = Pilha()
        self.pilha_redo = Pilha()
        self.pilha_undo.inserir(No(self.texto))

    def _imprimir_estado(self, operacao):
        print(f"\n--- {operacao} ---")
        print(f"Texto atual: '{self.texto}'")
        print(f"Tamanho da pilha UNDO: {self.pilha_undo.tamanho()}")
        print(f"Tamanho da pilha REDO: {self.pilha_redo.tamanho()}")
        print("--------------------")

    def digitar(self, entrada):
        self.texto += entrada
        self.pilha_undo.inserir(No(self.texto))
        self.pilha_redo = Pilha()
        self._imprimir_estado("Ação: Digitando")

    def apagar(self, num_caracteres=1):
        self.texto = self.texto[:-num_caracteres]
        self.pilha_undo.inserir(No(self.texto))
        self.pilha_redo = Pilha()
        self._imprimir_estado("Ação: Apagando")

    def desfazer(self):
        if self.pilha_undo.tamanho() > 1:
            estado_desfeito = self.pilha_undo.remover()
            self.pilha_redo.inserir(estado_desfeito)
            
            self.texto = self.pilha_undo.obterTopo().dado
            self._imprimir_estado("Ação: Desfazendo")
        else:
            print("\nNão há mais ações para desfazer.")

    def refazer(self):
        if not self.pilha_redo.taVazio():
            estado_refeito = self.pilha_redo.remover()
            self.pilha_undo.inserir(estado_refeito)
            
            self.texto = self.pilha_undo.obterTopo().dado
            self._imprimir_estado("Ação: Refazendo")
        else:
            print("\nNão há mais ações para refazer.")