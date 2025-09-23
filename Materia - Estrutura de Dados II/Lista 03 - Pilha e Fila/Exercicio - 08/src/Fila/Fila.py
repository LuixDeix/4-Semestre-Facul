from src.No.No import No

class Fila:
    def __init__(self):
        self.base = None
        self.cauda = None
        self.tamanho = 0

    def taVazio(self):
        return self.tamanho == 0

    def enfileirar(self, no: No):
        if self.taVazio():
            self.base = no
            self.cauda = no
        else:
            self.cauda.proximo = no
            self.cauda = no
        self.tamanho += 1

    def desenfileirar(self):
        if self.taVazio():
            return None
        
        no_removido = self.base
        self.base = self.base.proximo
        
        if self.base is None:
            self.cauda = None
            
        self.tamanho -= 1
        return no_removido.valor
    
    def ver_inicio(self):
        if self.taVazio():
            return None
        return self.base.valor
    
    def tamanho(self):
        return self.tamanho

    def listar(self):
        elementos = []
        atual = self.base
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos