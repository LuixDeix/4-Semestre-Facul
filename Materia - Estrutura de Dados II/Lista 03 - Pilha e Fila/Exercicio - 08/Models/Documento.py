class Documento:
    def __init__(self, nome, paginas, pagina_atual=0):
        self.nome = nome
        self.paginas = paginas
        self.pagina_atual = pagina_atual
        
    def __repr__(self):
        return f"'{self.nome}' ({self.paginas} páginas)"