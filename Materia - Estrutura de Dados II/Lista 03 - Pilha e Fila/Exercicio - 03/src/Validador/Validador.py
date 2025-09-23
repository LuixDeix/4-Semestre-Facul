def Validador(expressao):
    pilha = [] 

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            else:
                pilha.pop()

    return len(pilha) == 0