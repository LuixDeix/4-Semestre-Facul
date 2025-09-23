from src.Pilha.Pilha import Pilha

class CalculadoraRPN:
    def __init__(self):
        self.pilha = Pilha()
        self.operadores = ['+', '-', '*', '/']

    def calcular(self, expressao):
        tokens = expressao.split()

        for token in tokens:
            if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
                numero = float(token)
                self.pilha.inserir(numero)
            
            elif token in self.operadores:
                if self.pilha.tamanho() < 2:
                    raise ValueError("Expressão inválida: faltam operandos para o operador.")

                operando2 = self.pilha.remover()
                operando1 = self.pilha.remover()
                
                resultado = 0
                if token == '+':
                    resultado = operando1 + operando2
                elif token == '-':
                    resultado = operando1 - operando2
                elif token == '*':
                    resultado = operando1 * operando2
                elif token == '/':
                    if operando2 == 0:
                        raise ZeroDivisionError("Erro: divisão por zero.")
                    resultado = operando1 / operando2
                
                self.pilha.inserir(resultado)
            else:
                raise ValueError(f"Token inválido na expressão: {token}")

        if self.pilha.tamanho() == 1:
            return self.pilha.remover()
        else:
            raise ValueError("Expressão inválida: número de operandos e operadores não corresponde.")