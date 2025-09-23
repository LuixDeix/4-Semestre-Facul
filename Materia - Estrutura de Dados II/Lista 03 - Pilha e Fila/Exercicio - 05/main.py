from Models.Jogo import Jogo

meu_jogo = Jogo(limite_historico=5)

meu_jogo.fazer_jogada(10)
meu_jogo.fazer_jogada(25)
meu_jogo.fazer_jogada(7)

meu_jogo.mostrar_estado()

print("\nFazendo mais jogadas para exceder o limite do histórico...")
meu_jogo.fazer_jogada(42)
meu_jogo.fazer_jogada(13)
meu_jogo.fazer_jogada(99)

meu_jogo.mostrar_estado()

print("\nVoltando no tempo 3 vezes...")
meu_jogo.voltar_no_tempo()
meu_jogo.voltar_no_tempo()
meu_jogo.voltar_no_tempo()

meu_jogo.mostrar_estado()

print("\nVoltando no tempo novamente...")
meu_jogo.voltar_no_tempo()
meu_jogo.voltar_no_tempo()

meu_jogo.voltar_no_tempo()