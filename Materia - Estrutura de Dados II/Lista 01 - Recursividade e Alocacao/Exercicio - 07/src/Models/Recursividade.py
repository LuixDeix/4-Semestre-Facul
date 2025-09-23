NUM_FILAS = 5
NUM_ASSENTOS_POR_FILA = 10

assentos = [[0 for _ in range(NUM_ASSENTOS_POR_FILA)] for _ in range(NUM_FILAS)]

def Exibir_Assentos():
    print("\n=-= Mapa de Assentos =-=")
    print("  ", end="")
    for i in range(NUM_ASSENTOS_POR_FILA):
        print(f" {i+1} ", end="")
    print("\n" + "---" * (NUM_ASSENTOS_POR_FILA + 1))
    
    for i, fila in enumerate(assentos):
        print(f"F{i+1}|", end="")
        for assento in fila:
            if assento == 0:
                print(" O ", end="")
            else:
                print(" X ", end="")
        print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=\n")

def Reservar_Assento(fila, assento):
    fila_idx = fila - 1
    assento_idx = assento - 1

    if not (0 <= fila_idx < NUM_FILAS and 0 <= assento_idx < NUM_ASSENTOS_POR_FILA):
        print("Erro: A fila ou o assento não existe.")
        return False
        
    if assentos[fila_idx][assento_idx] == 0:
        assentos[fila_idx][assento_idx] = 1
        print(f"Assento Fila {fila}, Assento {assento} reservado com sucesso!")
        return True
    else:
        print(f"Erro: Assento Fila {fila}, Assento {assento} já está ocupado.")
        return False

def Cancelar_Reserva(fila, assento):
    fila_idx = fila - 1
    assento_idx = assento - 1

    if not (0 <= fila_idx < NUM_FILAS and 0 <= assento_idx < NUM_ASSENTOS_POR_FILA):
        print("Erro: A fila ou o assento não existe.")
        return False

    if assentos[fila_idx][assento_idx] == 1:
        assentos[fila_idx][assento_idx] = 0
        print(f"Reserva do assento Fila {fila}, Assento {assento} cancelada com sucesso!")
        return True
    else:
        print(f"Erro: Assento Fila {fila}, Assento {assento} não estava ocupado.")
        return False

if __name__ == "__main__":
    Exibir_Assentos()

    print("--- Tentando reservar assentos ---")
    Reservar_Assento(fila=2, assento=5)
    Reservar_Assento(fila=3, assento=8)
    Reservar_Assento(fila=2, assento=5)
    
    Exibir_Assentos()

    print("--- Tentando cancelar uma reserva ---")
    Cancelar_Reserva(fila=2, assento=5)
    Cancelar_Reserva(fila=4, assento=1) 
    
    Exibir_Assentos()