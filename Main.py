from tkinter import *
import pickle
from pathlib import Path
import sys
import Graficos
import datetime
import Textos
import Disciplina
import Avaliacao
import ManipularDados

pasta = "/Users/jailsoncavalcanti/Doc/Projects/Python/GAU/dados/"
nomeF = 'dados.pickles'
avaliacoesArquivo = 'avaliacoes.pickles'
disciplinasArquivo = 'disciplinas.pickles'

def listarDisciplinas():
    for i in range(len(disciplinas)):
        print(disciplinas[i].nome)

def listarAvaliacoesDisciplinas(disciplina):
    for i in range(len(disciplinas)):
        if disciplina == disciplinas[i].nome:
            for j in range(len(disciplinas[i].sistemaAvaliacao)):
                print(disciplinas[i].sistemaAvaliacao[j])

def afixarTabelaAvaliacao(disciplina):
    for i in range(len(disciplinas)):
        if disciplina == disciplinas[i].nome:
            disciplinas[i].afixarTabelaAvaliacao()

def perguntarComRestricao(texto, valor, min, max):
    while(valor < min or valor > max):
        return input(texto)

def afixarTabelaAvaliacaoComResultado(disciplina):
    for i in range(len(disciplinas)):
        if disciplina == disciplinas[i].nome:
            disciplinas[i].verificarEstadoAvaliacao()


avaliacoes = []
#avaliacoes.append(Avaliacao.Avaliacao("Teste1","30","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Teste2","25","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Teste3","30","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Trabalho","10","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Prescença","10","","","p","AP"))
avaliacoes = ManipularDados.abrir(pasta + avaliacoesArquivo)
for i in range(len(avaliacoes)):
    print(avaliacoes[i])
print("---")

disciplinas = []
#disciplinas.append(Disciplina.Disciplina("AP", "Maria"))
#disciplinas.append(Disciplina.Disciplina("SD", "Guerreiro"))
#disciplinas.append(Disciplina.Disciplina("Matemática", "Ana"))
#manipularDados.salvar(disciplinas,pasta + disciplinasArquivo)
disciplinas = ManipularDados.abrir(pasta + disciplinasArquivo)
for i in range(len(disciplinas)):
    print(disciplinas[i])

for i in range(len(disciplinas)):
    for k in range(len(avaliacoes)):
        if avaliacoes[k].disciplina == disciplinas[i].nome:
            disciplinas[i].criarAvaliacao(avaliacoes[k])
#for i in range(len(disciplinas)):
#    print(disciplinas[i].sistemaAvaliacao.nome+"--")
print("---")

afixarTabelaAvaliacao(disciplinas[0].nome)

#for i in range(len(avaliacoes)):
    #disciplinas[0].criarAvaliacao(avaliacoes[i])
#manipularDados.salvar(disciplinas[0], pasta + nomeF)

#disciplinas[0].afixarTabelaAvaliacao()

#print(disciplina)

#grafico.plot( [10,5,3,4,6,8] )

#grafico.title("Muito Fácil")
#grafico.show()

#root = Tk()
#Grafico.Application(root)
#root.mainloop()



#pessoas = abrir(pasta + nomeF)

textoPadrao = "Digite o valor correspondente"
continuar = True
print("Bem-vindo Aluno")
while continuar:

    for i,j in enumerate(Textos.opcoes):
        print(Textos.opcoes[i])

    valor = int(input(textoPadrao))

    #Caso queira criar disciplina ou avaliação
    if valor == 1:

        nome = input("Digite o nome da disciplina")
        docente = input("Digite o nome do docente")
        disciplinas.append(Disciplina.Disciplina(nome, docente))
        try:
            ManipularDados.salvar(disciplinas, pasta + disciplinasArquivo)
            print("Disciplina criada com sucesso.")
        except ValueError:
            print("Erro ao gravar arquivo")

    elif valor == 2:

        listarDisciplinas()

        #for i,j in enumerate(Textos.opcoes122):
            #print(Textos.opcoes122[i])
        #valor = int(input(textoPadrao))
        #if valor == 1:
            #print("Lista de disciplinas:")
            #if len(disciplinas) == 0:
                #print("Não há disciplinas")
            #else:
                #listarDisciplinas()
                #valor = 2
        #if valor == 2:
        nomeDisciplina = input("Digite o nome da disciplina")
        for i in range(len(disciplinas)):
            if nomeDisciplina == disciplinas[i].nome:
                tipo = input("Selecione o tipo da avaliação(n para normal ou p presença):")
                nome = input("Digite o nome da avaliação:")

                while True:
                    percentagem = input("Digite a percentagem da avaliação:")
                    if int(percentagem) > 0 and int(percentagem) < 100:
                        break

                data = input("Digite a data da avaliação:")
                avaliacoes.append(Avaliacao.Avaliacao(nome,percentagem,data,"",tipo,nomeDisciplina))
                disciplinas[i].afixarTabelaAvaliacao()
                try:
                    ManipularDados.salvar(avaliacoes, pasta + avaliacoesArquivo)
                    print("Avaliação criada com sucesso.")
                except ValueError:
                    print("Erro ao gravar arquivo")
        print("Não existe a disciplina")

    #Caso queira registar classificação
    elif valor == 3:
        listarDisciplinas()
        disciplina = input("Digite a disciplina")

        listarAvaliacoesDisciplinas(disciplina)
        avaliacao = input("Digite a avaliação")

        for i in range(len(disciplinas)):
            if disciplina == disciplinas[i].nome:
                print(disciplinas[i])
                for k in range(len(disciplinas[i].sistemaAvaliacao)):
                    if avaliacao == disciplinas[i].sistemaAvaliacao[k].nome:
                        nota = input("Digite a classificação:")
                        for j in range(len(avaliacoes)):
                            if avaliacoes[j].disciplina == disciplina and avaliacoes[j].nome == avaliacao:
                                if float(nota) > 20 or float(nota) < 0:
                                    print("Nota inválida")
                                else:
                                    avaliacoes[j].nota = nota
                try:
                    ManipularDados.salvar(avaliacoes, pasta + avaliacoesArquivo)
                    print("Avaliação criada com sucesso.")
                except ValueError:
                    print("Erro ao gravar arquivo")
        afixarTabelaAvaliacao(disciplina)

        #var = input("EE")

        #for i,j in enumerate(Textos.opcoes22):
        #    print(Textos.opcoes22[i])
        #    valor = int(input(textoPadrao))

    #Caso queira verificar o estado de avaliação
    elif valor == 4:
        listarDisciplinas()
        disciplina = input("Digite a disciplina")
        afixarTabelaAvaliacaoComResultado(disciplina)

    #Caso queira gráficos informativos(Vertical)
    elif valor == 5:
        listarDisciplinas()
        listaNotas = []
        listaNomes = []
        disciplina = input("Digite a disciplina")
        for i in range(len(disciplinas)):
            if disciplina == disciplinas[i].nome:
                listaNotas = disciplinas[i].retornarClassificacoes()
                listaNomes = disciplinas[i].retornarNomesAvaliacoes()
                Graficos.graficoVertical(listaNotas, listaNomes, disciplinas[i].nome)

    #Caso queira gráficos informativos(Horizontal)
    elif valor == 6:
        listaNotasFinais = []
        listaNomesDisciplinas = []
        listarDisciplinas()
        #listaN = [2, 15, 3, 9, 14]
        for i in range(len(disciplinas)):
           #for j in range(len(disciplinas[i].sistemaAvaliacao)):
                #print(disciplinas[i].sistemaAvaliacao[j])
            listaNotasFinais.append(disciplinas[i].retornarNotaFinal())
            listaNomesDisciplinas.append(disciplinas[i].nome)

        Graficos.graficoHorizontal(listaNomesDisciplinas, listaNotasFinais)


    elif valor == 7:
        pass

    elif valor == 8:
        pass

    else:
        continuar = False

"""

t = datetime.time(9,30,45,100000)

t1Date = str(textos.avaliacaoEDC[1][2])



aux = methods.calcularNotas(textos.avaliacaoEDC)

print("Teste: ",aux)

ano = t1Date[0:4]
mes = t1Date[4:6]
dia = t1Date[6:8]

print(ano)
print(mes)
print(dia)

d = datetime.datetime(int(ano), int(mes), int(dia), 23, 59, 59)
print(d)

td = datetime.datetime.today()

tdt = datetime.timedelta(7)

print("Faltam:",d - td)

#2print("Faltam:>", tdt)

x = datetime.datetime.today()
y = datetime.datetime.now()
z = datetime.datetime.utcnow()

print(x)
print(y)
print(z)
"""