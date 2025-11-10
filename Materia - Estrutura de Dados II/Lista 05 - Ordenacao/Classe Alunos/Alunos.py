import random
import string
import time

class Aluno:
    def __init__(self, nome, media):
        self.nome = nome
        self.media = media
    def __repr__(self):
        return f"{self.nome} - Média: {self.media:.2f}"

def gerar_nome():
    return ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 10)))

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista)//2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista)//2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def quicksort_alunos(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista)//2].media
    menores = [x for x in lista if x.media < pivo]
    iguais = [x for x in lista if x.media == pivo]
    maiores = [x for x in lista if x.media > pivo]
    return quicksort_alunos(menores) + iguais + quicksort_alunos(maiores)

nomes = [gerar_nome() for _ in range(10000)]

inicio_qs = time.time()
qs_resultado = quicksort(nomes[:])
tempo_qs = time.time() - inicio_qs

inicio_ms = time.time()
ms_resultado = mergesort(nomes[:])
tempo_ms = time.time() - inicio_ms

alunos = [Aluno(gerar_nome(), random.uniform(0, 10)) for _ in range(10000)]
inicio_qs_alunos = time.time()
qs_alunos = quicksort_alunos(alunos[:])
tempo_qs_alunos = time.time() - inicio_qs_alunos


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-         Relatório de Performance:         -=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"QuickSort (nomes): {tempo_qs:.6f}s")
print(f"MergeSort (nomes): {tempo_ms:.6f}s")
print(f"QuickSort (alunos por média): {tempo_qs_alunos:.6f}s")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\nTop 5 alunos com maiores médias:")
for a in sorted(alunos, key=lambda x: x.media, reverse=True)[:5]:
    print(a)