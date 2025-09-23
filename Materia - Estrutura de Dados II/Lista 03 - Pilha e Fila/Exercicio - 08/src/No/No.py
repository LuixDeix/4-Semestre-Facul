class No():
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __str__(self):
        return str(self.valor)
    
    def imprimir(self):
        print(self.valor)
    
    def temProximo(self):
        return self.proximo is not None