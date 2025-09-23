from src.Fila.Fila import Fila
from src.No.No import No
from .Documento import Documento
import time 
import random

class Impressora:
    def __init__(self, capacidade_fila=5):
        self.fila_documentos = Fila()
        self.capacidade_fila = capacidade_fila
        self.impressora_com_erro = False
        print("Simulador de impressora iniciado.")
        print(f"Capacidade da fila: {self.capacidade_fila} documentos.")
        print("Chances de erro por página: 1 em 10.\n")

    def adicionar_documento(self, nome, paginas):
        if paginas <= 0:
            print("Número de páginas inválido. Documento não adicionado.")
            return

        if self.fila_documentos.tamanho >= self.capacidade_fila:
            print("Erro: Fila da impressora cheia. O documento não pode ser adicionado.")
            return

        novo_documento = Documento(nome, paginas)
        
        novo_no = No(novo_documento)
        
        self.fila_documentos.enfileirar(novo_no)
        print(f"Documento '{novo_documento.nome}' ({novo_documento.paginas} páginas) adicionado à fila.")

    def bater_na_impressora(self):
        if self.impressora_com_erro:
            resposta = input("Deseja tentar bater na impressora para consertar? (s/n): ")
            if resposta.lower() == 's':
                print("Você bateu na impressora... e parece que ela voltou a funcionar!")
                self.impressora_com_erro = False
                return True
            else:
                print("Impressora permanece com erro. Não é possível imprimir.")
                return False
        else:
            print("Não há necessidade de bater na impressora, ela está funcionando (por enquanto!).")
            return True

    def imprimir_proximo_documento(self):
        if self.fila_documentos.taVazio():
            print("Nenhum documento na fila para imprimir.")
            return

        if self.impressora_com_erro:
            print("Impressora com erro! Não é possível imprimir. Tente consertar.")
            return

        doc_a_imprimir = self.fila_documentos.ver_inicio()
        
        print(f"\n--- Imprimindo Documento: '{doc_a_imprimir.nome}' ({doc_a_imprimir.paginas} páginas) ---")

        for i in range(doc_a_imprimir.pagina_atual + 1, doc_a_imprimir.paginas + 1):
            if self.impressora_com_erro:
                print(f"Impressão de '{doc_a_imprimir.nome}' interrompida na página {i - 1} (erro persistente).")
                if not self.bater_na_impressora():
                    return
            
            if random.randint(1, 10) == 1:
                print(f"### ERRO DE IMPRESSÃO! Impressora travou na página {i} de '{doc_a_imprimir.nome}'.")
                self.impressora_com_erro = True
                doc_a_imprimir.pagina_atual = i - 1
                if not self.bater_na_impressora():
                    return
            
            print(f"Imprimindo '{doc_a_imprimir.nome}' - Página {i} de {doc_a_imprimir.paginas}")
            doc_a_imprimir.pagina_atual = i
            time.sleep(0.05)
        
        self.fila_documentos.desenfileirar()
        print(f"\nDocumento '{doc_a_imprimir.nome}' impresso com sucesso!")

    def mostrar_status(self):
        print("\n--- Status da Fila ---")
        if self.fila_documentos.taVazio():
            print("Fila de impressão está vazia.")
        else:
            print(f"Documentos na fila: {self.fila_documentos.tamanho()}")
            proximo = self.fila_documentos.ver_inicio()
            print(f"Próximo a ser impresso: '{proximo.nome}' ({proximo.paginas} páginas totais, próxima página: {proximo.pagina_atual + 1})")
        print(f"Status da Impressora: {'COM ERRO' if self.impressora_com_erro else 'Funcionando'}")
        print("------------------------")