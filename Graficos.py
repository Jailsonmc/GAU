from tkinter import *
import matplotlib.pyplot as grafico
import numpy as np


def graficoVertical(listaNotas, listaNomes, disciplina):
    # Variáveis para o Bar Chart
    y_axis = [20,50,30]

    x_axis = range(len(listaNotas))
    width_n = 0.4
    bar_color = 'yellow'

    grafico.bar(listaNomes, listaNotas, width=width_n, color=bar_color)
    grafico.show()

#MOSTRA O GRÁFICO DE BARRAS HORIZONTAIS COM AS NOTAS FINAIS DE TODAS AS CADEIRAS DO SEMESTRE
def graficoHorizontal(disciplinas, listaNotasFinais):
    grafico.rcdefaults()
    fig, ax = grafico.subplots()

    y_pos = np.arange(len(disciplinas))

    ax.barh(y_pos, listaNotasFinais, align='center', color='b')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(disciplinas)
    ax.invert_yaxis()
    ax.set_xlabel('Cotação')
    ax.set_title('Avaliação geral do semestre')

    grafico.show()

