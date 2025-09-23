from .Impressora import Impressora

def Menu():
    simulador = Impressora()

    while True:
        print("\n--- Menu da Impressora ---")
        print("1. Adicionar Documento à Fila")
        print("2. Imprimir Próximo Documento")
        print("3. Verificar Status da Fila")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do documento: ")
            try:
                paginas = int(input("Digite o número de páginas: "))
                simulador.adicionar_documento(nome, paginas)
            except ValueError:
                print("Entrada inválida. Digite um número para as páginas.")
        elif escolha == '2':
            simulador.imprimir_proximo_documento()
        elif escolha == '3':
            simulador.mostrar_status()
        elif escolha == '0':
            print("Saindo da simulação. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")