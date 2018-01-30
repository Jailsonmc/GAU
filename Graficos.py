from tkinter import *
import matplotlib.pyplot as grafico
import numpy as np

#MOSTRA O GRÁFICO DE BARRAS VERTICAIS COM AS AVALIAÇÕES DA CADEIRA
def graficoVertical(listaNotas, listaNomes, disciplina):

    def autoLabel(rects):
        for n in rects:
            height = n.get_height()
            ax.text(n.get_x() + n.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center', va='bottom')

    indices = np.arange(len(listaNotas))
    width = 0.8

    fig, ax = grafico.subplots()
    notas = ax.bar(indices, listaNotas, width, color='b')

    ax.set_ylabel("Cotação")
    ax.set_title("Notas da disciplina: " + disciplina)
    ax.set_xticks(indices + width)
    ax.set_xticklabels(listaNomes)
    ax.legend((notas), ('Notas'))

    autoLabel(notas)

    grafico.show()

def graficoVertical2(listaNotas, listaNomes, disciplina):
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

