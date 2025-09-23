from Models.Pedidos import Pedidos

lanchonete = Pedidos()

lanchonete.fazer_pedido("X-Burger e Fritas")
lanchonete.fazer_pedido("Suco de Laranja")
lanchonete.fazer_pedido("Combo Família")

lanchonete.mostrar_fila()

lanchonete.processar_proximo_pedido()
lanchonete.processar_proximo_pedido()

lanchonete.fazer_pedido("Milkshake de Chocolate")

lanchonete.mostrar_fila()

lanchonete.processar_proximo_pedido()
lanchonete.processar_proximo_pedido()

lanchonete.processar_proximo_pedido()