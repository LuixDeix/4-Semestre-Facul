def Inverter_String(string):
    if len(string) == 0:
        return string
    else:
        return Inverter_String(string[1:]) + string[0]

minha_string = "Dudarts é um cara bacana"
string_invertida = Inverter_String(minha_string)
print(f"   • String original: '{minha_string}'")
print(f"   • String invertida: '{string_invertida}'")