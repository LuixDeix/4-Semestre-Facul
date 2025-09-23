def Insira_a_Palavra():
    palavra = input(" • Insira palavra que quer reverter aqui: ")
    return print(Inverter_Palavra(palavra))

def Inverter_Palavra(palavra):
    if len(palavra) == 0:
        return palavra
    else: 
        return Inverter_Palavra(palavra[1:])+palavra[0]