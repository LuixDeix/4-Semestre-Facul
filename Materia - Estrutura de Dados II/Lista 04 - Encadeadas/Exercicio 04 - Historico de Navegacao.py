class Pagina:
    def __init__(self, url):
        self.url = url
        self.anterior = None
        self.proxima = None

class HistoricoNavegacao:
    def __init__(self):
        self.atual = None
        self.inicio = None
        self.fim = None

    def visitar(self, url):
        nova = Pagina(url)
        if self.atual is None:
            self.inicio = self.fim = self.atual = nova
        else:
            self.atual.proxima = None
            nova.anterior = self.atual
            self.atual.proxima = nova
            self.atual = nova
            self.fim = nova
        print(f"Visitando: {url}")

    def voltar(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print(f"Voltou para: {self.atual.url}")
        else:
            print("Não há página anterior.")

    def avancar(self):
        if self.atual and self.atual.proxima:
            self.atual = self.atual.proxima
            print(f"Avançou para: {self.atual.url}")
        else:
            print("Não há próxima página.")

    def pagina_atual(self):
        if self.atual:
            print(f"Página atual: {self.atual.url}")
        else:
            print("Histórico vazio.")

    def mostrar_historico(self):
        if not self.inicio:
            print("Nenhum histórico disponível.")
            return
        print("\nHistórico de Navegação:")
        atual = self.inicio
        while atual:
            marcador = " <- (Atual)" if atual == self.atual else ""
            print(f"- {atual.url}{marcador}")
            atual = atual.proxima

historico = HistoricoNavegacao()

historico.visitar("www.github.com")
historico.visitar("www.dotnet.com")
historico.visitar("www.amazon.com")

historico.voltar()
historico.pagina_atual()

historico.visitar("www.mercadolivre.com")
historico.mostrar_historico()

historico.voltar()
historico.avancar()