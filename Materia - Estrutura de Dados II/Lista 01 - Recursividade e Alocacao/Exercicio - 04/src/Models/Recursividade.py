def Insira_o_Numero():
    print(" =-=-=-=-=- Insira números inteiros e positivos -=-=-=-=-= ")
    numero_a = int(input("   • Insira o primeiro número: "))
    numero_b = int(input("   • Insira o segundo número: "))
    return print(Multiplicador(numero_a, numero_b))

def Multiplicador(numero_a, numero_b):
    if numero_a > numero_b:
        return Multiplicador(numero_b, numero_a)
    if numero_a == 0 or numero_b == 0:
        return 0
    if numero_a == 1:
        return numero_b
    
    total = 0
    contador = 1
    while contador <= numero_a:
        total += numero_b
        contador += 1
    return total