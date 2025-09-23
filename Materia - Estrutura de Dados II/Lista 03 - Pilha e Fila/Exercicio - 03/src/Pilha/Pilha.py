from src.No.No import No

class Pilha():
    def __init__(self):
        self.base: No = None
        self.tamanho = 0

    def inserir(self, no:No):
        if self.taVazio():
            self.base = no
        else:
            self.obterTopo().proximo = no
        self.tamanho += 1

    def _listarTodos(self, no:No):
        if no.temProximo():
            self._listarTodos(no.proximo)
        no.imprimir()

    def listar(self):
        self._listarTodos(self.base)

    def obterTopo(self):
        atual = self.base
        
        if not atual:
            return None
            
        while atual.temProximo():
            atual = atual.proximo
        return atual

    def tamanho(self):
        return self.tamanho

    def taVazio(self):
        return self.tamanho == 0
    
    def remover(self) -> No:
        if self.tamanho == 1:
            ultimo = self.base
            self.base = None
            self.tamanho = 0
            return ultimo
            
        atual = self.base
        
        if not atual:
            return None

        while atual.proximo.temProximo(): 
            atual = atual.proximo

        ultimo = atual.proximo
        atual.proximo = None
        self.tamanho -= 1
        return ultimo