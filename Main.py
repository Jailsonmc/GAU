from tkinter import *
import pickle
from pathlib import Path
import sys
import Grafico
import datetime
import methods
import textos
import Disciplina
import Avaliacao
import manipularDados

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



avaliacoes = []
#avaliacoes.append(Avaliacao.Avaliacao("Teste1","30","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Teste2","25","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Teste3","30","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Trabalho","10","20170802","","n","AP"))
#avaliacoes.append(Avaliacao.Avaliacao("Prescença","10","","","p","AP"))
avaliacoes = manipularDados.abrir(pasta + avaliacoesArquivo)
for i in range(len(avaliacoes)):
    print(avaliacoes[i])
print("---")

disciplinas = []
#disciplinas.append(Disciplina.Disciplina("AP", "Maria"))
#disciplinas.append(Disciplina.Disciplina("SD", "Guerreiro"))
#disciplinas.append(Disciplina.Disciplina("Matemática", "Ana"))
#manipularDados.salvar(disciplinas,pasta + disciplinasArquivo)
disciplinas = manipularDados.abrir(pasta + disciplinasArquivo)
for i in range(len(disciplinas)):
    print(disciplinas[i])

for i in range(len(disciplinas)):
    for k in range(len(avaliacoes)):
        if avaliacoes[k].disciplina == disciplinas[i].nome:
            disciplinas[i].criarAvaliacao(avaliacoes[k])
#for i in range(len(disciplinas)):
#    print(disciplinas[i].sistemaAvaliacao.nome+"--")
print("---")

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

    for i,j in enumerate(textos.opcoes):
        print(textos.opcoes[i])

    valor = int(input(textoPadrao))

    #Caso queira criar disciplina ou avaliação
    if valor == 1:


        nome = input("Digite o nome da disciplina")
        docente = input("Digite o nome do docente")
        disciplinas.append(Disciplina.Disciplina(nome, docente))
        try:
            manipularDados.salvar(disciplinas, pasta + disciplinasArquivo)
            print("Disciplina criada com sucesso.")
        except ValueError:
            print("Erro ao gravar arquivo")

    elif valor == 2:
        for i,j in enumerate(textos.opcoes122):
            print(textos.opcoes122[i])
        valor = int(input(textoPadrao))
        if valor == 1:
            print("Lista de disciplinas:")
            if len(disciplinas) == 0:
                print("Não há disciplinas")
            else:
                listarDisciplinas()
                valor = 2
        if valor == 2:
            nomeDisciplina = input("Digite o nome da disciplina")
            for i in range(len(disciplinas)):
                if nomeDisciplina == disciplinas[i].nome:
                    tipo = input("Selecione o tipo da avaliação(n para normal ou p presença):")
                    nome = input("Digite o nome da avaliação:")
                    percentagem = input("Digite a percentagem da avaliação:")
                    data = input("Digite a data da avaliação:")
                    avaliacoes.append(Avaliacao.Avaliacao(nome,percentagem,data,"",tipo,nomeDisciplina))
                    disciplinas[i].afixarTabelaAvaliacao()
                    try:
                        manipularDados.salvar(avaliacoes, pasta + avaliacoesArquivo)
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
                for k in range(len(disciplinas[i])):
                    print(disciplinas[i])

        for i,j in enumerate(textos.opcoes22):
            print(textos.opcoes22[i])
            valor = int(input(textoPadrao))

    #Caso queira verificar o estado de avaliação
    elif valor == 4:
        listarDisciplinas()
        disciplina = input("Digite a disciplina")
        afixarTabelaAvaliacao(disciplina)

    #Caso queira gráficos informativos
    elif valor == 5:
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