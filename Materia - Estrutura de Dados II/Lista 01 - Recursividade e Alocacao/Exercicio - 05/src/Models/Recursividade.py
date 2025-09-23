mapa = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

caminho_minimo = None

def Encontrar_caminho_minimo_recursivo(mapa, pos_atual, destino, caminho_percorrido, visitados):
    global caminho_minimo
    
    linha, coluna = pos_atual
    num_linhas = len(mapa)
    num_colunas = len(mapa[0])
    
    if (linha < 0 or linha >= num_linhas or
        coluna < 0 or coluna >= num_colunas or
        mapa[linha][coluna] == 1 or
        pos_atual in visitados):
        return
    caminho_percorrido.append(pos_atual)
    visitados.add(pos_atual)

    if pos_atual == destino:
        if caminho_minimo is None or len(caminho_percorrido) < len(caminho_minimo):
            caminho_minimo = list(caminho_percorrido)
        return
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for d_linha, d_coluna in direcoes:
        proxima_posicao = (linha + d_linha, coluna + d_coluna)
        Encontrar_caminho_minimo_recursivo(mapa, proxima_posicao, destino, caminho_percorrido, visitados)
    caminho_percorrido.pop()
    visitados.remove(pos_atual)

ponto_inicial = (0, 0)
ponto_final = (4, 4)
Encontrar_caminho_minimo_recursivo(mapa, ponto_inicial, ponto_final, [], set())

if caminho_minimo:
    print("Caminho mínimo encontrado:")
    for pos in caminho_minimo:
        print(pos, end=" -> ")
    print("Fim")
    print(f"\nComprimento do caminho: {len(caminho_minimo)} passos")
else:
    print("Não foi possível encontrar um caminho.")