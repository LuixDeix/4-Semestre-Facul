from src.Validador.Validador import Validador

print("--- Testes de Expressões ---")

expressao1 = "(1 + (2 * 3))"
print(f"'{expressao1}' é válida? {Validador(expressao1)}")

expressao2 = "((a + b) / (c - d))"
print(f"'{expressao2}' é válida? {Validador(expressao2)}")

expressao3 = "5 * (x + (y / z)) - 10"
print(f"'{expressao3}' é válida? {Validador(expressao3)}")

print("\n--- Testes de Expressões Inválidas ---")

expressao4 = "((1 + 2)"
print(f"'{expressao4}' é válida? {Validador(expressao4)}")

expressao5 = "(3 * 4))"
print(f"'{expressao5}' é válida? {Validador(expressao5)}")

expressao6 = "())("
print(f"'{expressao6}' é válida? {Validador(expressao6)}")

expressao7 = ")a + b("
print(f"'{expressao7}' é válida? {Validador(expressao7)}")