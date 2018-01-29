from tkinter import *
import matplotlib.pyplot as grafico
import numpy as np

class Application:

    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Sistema GAU")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


    #MOSTRA O GRÁFICO DE BARRAS VERTICAIS COM AS AVALIAÇÕES DA CADEIRA
    def criarGraficoVertical(a):
        def autoLabel(rects):
            for n in rects:
                height = n.get_height()
                ax.text(n.get_x() + n.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center', va='bottom')

        ind = np.arange(len(a[0]))
        width = 0.7

        fig, ax = grafico.subplots()
        notas = ax.bar(ind, a[3], width, color='b')

        ax.set_ylabel('Cotação')
        ax.set_title('Nota das avaliações')
        ax.set_xticks(ind + width)
        ax.set_xticklabels(a[0])
        ax.legend((notas), ('Notas'))

        autoLabel(notas)

        grafico.show()

    #MOSTRA O GRÁFICO DE BARRAS HORIZONTAIS COM AS NOTAS FINAIS DE TODAS AS CADEIRAS DO SEMESTRE
    def criarGraficoHorizontal(dis, a, b, c, d, e):
        grafico.rcdefaults()
        fig, ax = grafico.subplots()

        y_pos = np.arange(len(dis))
        notas = (a[3][len(a[3]) - 1], b[3][len(b[3]) - 1], c[3][len(c[3]) - 1], d[3][len(d[3]) - 1], e[3][len(e[3]) - 1])

        ax.barh(y_pos, notas, align='center', color='b')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(dis)
        ax.invert_yaxis()
        ax.set_xlabel('Cotação')
        ax.set_title('Avaliação geral do semestre')

        grafico.show()