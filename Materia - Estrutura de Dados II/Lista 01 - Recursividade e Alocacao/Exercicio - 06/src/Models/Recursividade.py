def Torres_de_Hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    Torres_de_Hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    Torres_de_Hanoi(n - 1, auxiliar, destino, origem)

n_discos = 5
Torres_de_Hanoi(n_discos, 'Torre A (Origem)', 'Torre C (Destino)', 'Torre B (Auxiliar)')

print(f"\n---")
print(f"   • A solução para {n_discos} discos requer 2^{n_discos} - 1 = {2**n_discos - 1} movimentos.")