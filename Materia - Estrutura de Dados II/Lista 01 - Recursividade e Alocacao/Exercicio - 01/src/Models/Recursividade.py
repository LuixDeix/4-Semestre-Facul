import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def Insira_o_Diretorio():
    diretorio = input("• Coloque aqui o path do diretório que deseja que seja lido:")
    return Leitura_Diretorios(diretorio, 0)

def Leitura_Diretorios(diretorio, nivel):
    a = os.scandir(diretorio)
    for item in a:
        Exibir(item.name, nivel, "📁" if item.is_dir() else "📄")
        if item.is_dir():
            Leitura_Diretorios(os.path.join(diretorio, item.name), nivel + 1)

def Exibir(nome, nivel, icone):
    print(f"{" "*(4*nivel)}{icone} {nome}")