from Models.Banco import Banco

simulacao = Banco(tempo_total_simulacao=1000,
                           tempo_medio_chegada=3,
                           tempo_medio_atendimento=5)

simulacao.rodar_simulacao()
simulacao.mostrar_resultados()