class Pedidos:
    def __init__(self):
        self.pedidos = []
        print("Sistema de pedidos da lanchonete inicializado.")
    
    def fazer_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")
        
    def processar_proximo_pedido(self):
        if not self.pedidos:
            print("Nenhum pedido na fila para processar.")
            return None
        
        pedido_processado = self.pedidos.pop(0)
        print(f"Processando pedido: '{pedido_processado}'... Concluído!")
        return pedido_processado
    
    def mostrar_fila(self):
        print("\n--- Fila de Pedidos ---")
        if not self.pedidos:
            print("A fila está vazia.")
        else:
            for i, pedido in enumerate(self.pedidos):
                print(f"{i+1}. {pedido}")