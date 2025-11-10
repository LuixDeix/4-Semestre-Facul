class Musica:
    def __init__(self, titulo):
        self.titulo = titulo
        self.anterior = None
        self.proxima = None

class Playlist:
    def __init__(self):
        self.atual = None
        self.inicio = None
        self.fim = None

    def adicionar_nova_musica(self, titulo):
        nova = Musica(titulo)
        if not self.inicio:
            self.inicio = self.fim = self.atual = nova
        else:
            self.fim.proxima = nova
            nova.anterior = self.fim
            self.fim = nova
        print(f"A Música '{titulo}' foi adicionada à playlist com sucesso!")

    def mostrar_atual(self):
        if self.atual:
            print(f"Tocando nesse exato momento: {self.atual.titulo}")
        else:
            print("Nenhuma música na playlist.")

    def avancar(self):
        if self.atual and self.atual.proxima:
            self.atual = self.atual.proxima
            self.mostrar_atual()
        else:
            print("Você já está na última música da playlist.")

    def retroceder(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            self.mostrar_atual()
        else:
            print("Você já está na primeira música da playlist.")

    def listar_musicas(self):
        if not self.inicio:
            print("Playlist vazia.")
            return
        print(" Playlist completa:")
        atual = self.inicio
        while atual:
            marcador = " <- Tocando nesse exato momento" if atual == self.atual else ""
            print(f"- {atual.titulo}{marcador}")
            atual = atual.proxima

playlist = Playlist()
playlist.adicionar_nova_musica("Metralhadora de Jeová")
playlist.adicionar_nova_musica("Jingle Bells")
playlist.adicionar_nova_musica("Teu santo nome")

playlist.mostrar_atual()
playlist.avancar()
playlist.avancar()
playlist.retroceder()
playlist.listar_musicas()
