class Aluno:
    def __init__(self, nome, ra, idade):
        self.nome = nome
        self.ra = ra
        self.idade = idade
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def cadastrar_aluno(self, nome, ra, idade):
        novo = Aluno(nome, ra, idade)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        print(f"Aluno {nome} cadastrado com sucesso!")

    def listar_alunos(self):
        if self.inicio is None:
            print("Nenhum aluno cadastrado.")
            return
        atual = self.inicio
        print("\n Lista de alunos cadastrados:")
        while atual:
            print(f"Nome: {atual.nome}, RA: {atual.ra}, Idade: {atual.idade}")
            atual = atual.proximo

    def buscar_aluno(self, ra):
        atual = self.inicio
        while atual:
            if atual.ra == ra:
                print(f"\n Aluno encontrado:")
                print(f"Nome: {atual.nome}, RA: {atual.ra}, Idade: {atual.idade}")
                return atual
            atual = atual.proximo
        print(f"\n Aluno com RA {ra} não encontrado.")
        return None

    def remover_aluno(self, ra):
        if self.inicio is None:
            print("Lista vazia. Nenhum aluno para remover.")
            return

        if self.inicio.ra == ra:
            print(f"Aluno {self.inicio.nome} removido.")
            self.inicio = self.inicio.proximo
            return

        anterior = None
        atual = self.inicio
        while atual and atual.ra != ra:
            anterior = atual
            atual = atual.proximo

        if atual:
            anterior.proximo = atual.proximo
            print(f"Aluno {atual.nome} removido com sucesso.")
        else:
            print(f"Aluno com RA {ra} não encontrado.")

    def contar_alunos(self):
        contador = 0
        atual = self.inicio
        while atual:
            contador += 1
            atual = atual.proximo
        print(f"\nTotal de alunos cadastrados: {contador}")
        return contador

lista = ListaEncadeada()

lista.cadastrar_aluno("Jenifer", "5148762", 19)
lista.cadastrar_aluno("Luis", "5458872", 19)

lista.listar_alunos()

lista.buscar_aluno("5148762")
lista.remover_aluno("5458872")
lista.listar_alunos()

lista.contar_alunos()