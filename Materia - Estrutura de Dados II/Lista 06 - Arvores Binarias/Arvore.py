class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None 
        self.direita = None  

class EstruturaArvore:
    def __init__(self):
        self.root = None 


    def _adicionar_recursivo(self, elemento_atual, valor):
        if elemento_atual is None:
            return Elemento(valor)
        if valor < elemento_atual.valor:
            elemento_atual.esquerda = self._adicionar_recursivo(elemento_atual.esquerda, valor)
        elif valor > elemento_atual.valor:
            elemento_atual.direita = self._adicionar_recursivo(elemento_atual.direita, valor)
        return elemento_atual

    def _procurar_recursivo(self, elemento_atual, valor):
        if elemento_atual is None:
            return None
        if valor == elemento_atual.valor:
            return elemento_atual
        if valor < elemento_atual.valor:
            return self._procurar_recursivo(elemento_atual.esquerda, valor)
        else:
            return self._procurar_recursivo(elemento_atual.direita, valor)

    def _encontrar_menor(self, elemento_atual):
        cursor = elemento_atual
        while cursor.esquerda is not None:
            cursor = cursor.esquerda
        return cursor

    def _excluir_recursivo(self, elemento_atual, valor):
        if elemento_atual is None:
            return elemento_atual
        
        if valor < elemento_atual.valor:
            elemento_atual.esquerda = self._excluir_recursivo(elemento_atual.esquerda, valor)
        elif valor > elemento_atual.valor:
            elemento_atual.direita = self._excluir_recursivo(elemento_atual.direita, valor)
        else:
            if elemento_atual.esquerda is None:
                return elemento_atual.direita
            elif elemento_atual.direita is None:
                return elemento_atual.esquerda
            
            substituto = self._encontrar_menor(elemento_atual.direita)
            elemento_atual.valor = substituto.valor
            elemento_atual.direita = self._excluir_recursivo(elemento_atual.direita, substituto.valor)
        return elemento_atual

    def _percorrer_pre_ordem(self, elemento_atual):
        if elemento_atual:
            print(elemento_atual.valor, end=" -> ") 
            self._percorrer_pre_ordem(elemento_atual.esquerda)
            self._percorrer_pre_ordem(elemento_atual.direita)

    def _percorrer_in_ordem(self, elemento_atual):
        if elemento_atual:
            self._percorrer_in_ordem(elemento_atual.esquerda)
            print(elemento_atual.valor, end=" -> ") 
            self._percorrer_in_ordem(elemento_atual.direita)

    def _percorrer_pos_ordem(self, elemento_atual):
        if elemento_atual:
            self._percorrer_pos_ordem(elemento_atual.esquerda)
            self._percorrer_pos_ordem(elemento_atual.direita)
            print(elemento_atual.valor, end=" -> ") 

    def _contar_recursivo(self, elemento_atual):
        if elemento_atual is None:
            return 0
        return 1 + self._contar_recursivo(elemento_atual.esquerda) + self._contar_recursivo(elemento_atual.direita)

    def _buscar_sugestoes(self, elemento_atual, termo, lista_sugestoes):
        if elemento_atual:
            if elemento_atual.valor.lower().startswith(termo):
                lista_sugestoes.append(elemento_atual.valor)
            self._buscar_sugestoes(elemento_atual.esquerda, termo, lista_sugestoes)
            self._buscar_sugestoes(elemento_atual.direita, termo, lista_sugestoes)


    def adicionar(self, valor):
        self.root = self._adicionar_recursivo(self.root, valor)

    def procurar(self, valor): 
        return self._procurar_recursivo(self.root, valor)

    def excluir(self, valor): 
        self.root = self._excluir_recursivo(self.root, valor)

    def mostrar_pre_ordem(self):
        self._percorrer_pre_ordem(self.root)
        print("FIM") 

    def mostrar_in_ordem(self):
        self._percorrer_in_ordem(self.root)
        print("FIM")

    def mostrar_pos_ordem(self):
        self._percorrer_pos_ordem(self.root)
        print("FIM")

    def total_elementos(self): 
        return self._contar_recursivo(self.root)

    def autocompletar(self, termo): 
        sugestoes = []
        self._buscar_sugestoes(self.root, termo.lower(), sugestoes)
        return sugestoes


minha_arvore = EstruturaArvore()
lista_cidades = ["São Paulo", "Santos", "Campinas", "Sorocaba", "Suzano", "Carapicuíba", "Santo André", "São Roque"]

for item in lista_cidades:
    minha_arvore.adicionar(item)

print("--- Exibindo em Pré-Ordem ---")
minha_arvore.mostrar_pre_ordem()

print("\n--- Exibindo em In-Ordem (Ordenado) ---")
minha_arvore.mostrar_in_ordem()

print("\n--- Exibindo em Pós-Ordem ---")
minha_arvore.mostrar_pos_ordem()

print(f"\n>> Quantidade total de itens: {minha_arvore.total_elementos()}")

item_procurado = "Santos"
resultado = "Item localizado" if minha_arvore.procurar(item_procurado) else "Item não existe"
print(f"\n>> Verificando por '{item_procurado}': {resultado}")

item_procurado = "Franca"
resultado = "Item localizado" if minha_arvore.procurar(item_procurado) else "Item não existe"
print(f">> Verificando por '{item_procurado}': {resultado}")

minha_arvore.excluir("Suzano") 
print("\n>> Estrutura após excluir 'Suzano' (In-Ordem):")
minha_arvore.mostrar_in_ordem()

prefixo = "Sa"
print(f"\n>> Sugestões de autocompletar para '{prefixo}': {minha_arvore.autocompletar(prefixo)}")