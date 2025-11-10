import random
import time

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __repr__(self):
        return f"{self.nome} - R${self.preco:.2f}"

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].preco > lista[j + 1].preco:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j].preco > chave.preco:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

produtos = [Produto(f"Produto {i+1}", random.uniform(1, 1000)) for i in range(1000)]

inicio_bubble = time.time()
bubble_sort(produtos[:])
tempo_bubble = time.time() - inicio_bubble

inicio_insertion = time.time()
insertion_sort(produtos[:])
tempo_insertion = time.time() - inicio_insertion

ranking = sorted(produtos, key=lambda p: p.preco, reverse=True)[:10]

print(f"Tempo Bubble Sort: {tempo_bubble:.6f}s")
print(f"Tempo Insertion Sort: {tempo_insertion:.6f}s\n")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("           Top 10 produtos mais caros:         ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
for i, p in enumerate(ranking, 1):
    print(f"{i}º - {p}")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")