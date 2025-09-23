import time

class ConjuntoDeDadosLazy:
    def __init__(self, caminho_do_arquivo):
        self.caminho_do_arquivo = caminho_do_arquivo
        self._dados = None
        print("Objeto criado, mas os dados ainda não foram carregados.")

    def _carregar_dados(self):
        print(f"Carregando dados do arquivo '{self.caminho_do_arquivo}'...")
        time.sleep(2) 
        
        dados_falsos = [
            {"id": 1, "nome": "Alice"}, 
            {"id": 2, "nome": "Bob"}, 
            {"id": 3, "nome": "Charlie"}
        ]
        
        self._dados = dados_falsos
        print("Dados carregados com sucesso!")

    @property
    def dados(self):
        if self._dados is None:
            self._carregar_dados()
        
        return self._dados

if __name__ == "__main__":
    
    print("Iniciando o programa...")
    meus_dados = ConjuntoDeDadosLazy("meu_grande_arquivo.csv")
    print("...O programa está rodando sem consumir a memória dos dados ainda.\n")

    print("Acessando os dados pela primeira vez...")
    dados_carregados = meus_dados.dados
    print(f"Dados obtidos: {dados_carregados}\n")

    print("Acessando os dados pela segunda vez...")
    outros_dados_carregados = meus_dados.dados
    print("Os dados já estavam em memória e foram retornados instantaneamente.")