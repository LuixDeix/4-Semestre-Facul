agenda = {}

def Adicionar_Contato(nome, telefone):
    if nome in agenda:
        print(f"O contato '{nome}' já existe. Número atualizado para {telefone}.")
    else:
        print(f"Contato '{nome}' adicionado com sucesso.")
    agenda[nome] = telefone

def Buscar_Contato(nome):
    if nome in agenda:
        print(f"Nome: {nome} | Telefone: {agenda[nome]}")
        return agenda[nome]
    else:
        print(f"Erro: Contato '{nome}' não encontrado na agenda.")
        return None
    
def Remover_Contato(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso.")
    else:
        print(f"Erro: Contato '{nome}' não encontrado na agenda.")

def Listar_Contatos():
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("\n--- Lista de Contatos ---")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome} | Telefone: {telefone}")
        print("-------------------------\n")

def Menu():
    while True:
        print("\n=-= Menu da Agenda Telefônica =-=")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Listar Contatos")
        print("5. Sair")
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone: ")
            Adicionar_Contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            Remover_Contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato a ser buscado: ")
            Buscar_Contato(nome)
        elif escolha == '4':
            Listar_Contatos()
        elif escolha == '5':
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    Menu()