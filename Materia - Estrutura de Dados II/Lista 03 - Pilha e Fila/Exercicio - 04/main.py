from Models.HistoricoAcoes import HistoricoAcoes

historico = HistoricoAcoes()

historico.registrar_acao("digitou 'Olá'")
historico.registrar_acao("digitou ' mundo'")
historico.registrar_acao("inseriu uma imagem")
historico.registrar_acao("formatou o texto")

historico.mostrar_historico()

historico.desfazer() 
historico.desfazer() 
historico.desfazer()

historico.mostrar_historico()

historico.desfazer()

historico.desfazer()