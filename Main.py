import Graficos
#import datetime
import Textos
import Disciplina
import Avaliacao
import ManipularDados
import Curso

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

curso = Curso.Curso("Engenharia Informática")

avaliacoes = []
avaliacoes = ManipularDados.abrir(pasta + avaliacoesArquivo)
#for i in range(len(avaliacoes)):
#    print(str(avaliacoes[i]) + " - - " + str(avaliacoes[i].disciplina))
#print("---")

disciplinas = []
disciplinas = ManipularDados.abrir(pasta + disciplinasArquivo)
#for i in range(len(disciplinas)):
#    print(disciplinas[i])

curso.disciplinas = disciplinas

for i in range(len(disciplinas)):
    for k in range(len(avaliacoes)):
        if avaliacoes[k].disciplina == disciplinas[i].nome:
            disciplinas[i].criarAvaliacao(avaliacoes[k])
#print("---")

#afixarTabelaAvaliacao(disciplinas[0].nome)

textoPadrao = "Digite o valor correspondente"
continuar = True
print("Bem-vindo")
print("AVALIAÇÃO CONTÍNUA 1.º ANO/1.º SEM - " + curso.nome)
while continuar:

    for i,j in enumerate(Textos.opcoes):
        print(Textos.opcoes[i])

    valor = input(textoPadrao)

    try:
        valor = int(valor)
    except ValueError:
        break

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
                        verificar = True
                        while verificar == True:
                            try:
                                nota = float(input("Digite a classificação:"))
                                verificar = False
                            except ValueError:
                                print("Valor não é um número")

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
        afixarTabelaAvaliacaoComResultado(disciplina)

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
        for i in range(len(disciplinas)):
            listaNotasFinais.append(disciplinas[i].retornarNotaFinal())
            listaNomesDisciplinas.append(disciplinas[i].nome)

        Graficos.graficoHorizontal(listaNomesDisciplinas, listaNotasFinais)


    elif valor == 7:
        listarDisciplinas()
        disciplina = input("Digite a disciplina")
        listaIndice = []
        for i in range(len(disciplinas)):
            if disciplina == disciplinas[i].nome:
                for k in range(len(avaliacoes)):
                    print(str(len(avaliacoes)) + "~~" + avaliacoes[k].disciplina+"--")
                    if avaliacoes[k].disciplina == disciplina:
                        listaIndice.append(k)
                for k in range(len(avaliacoes)):
                    print(avaliacoes[k])
                #for k in range(len(listaIndice)):
                #    print(listaIndice[k])
                #    avaliacoes.pop(listaIndice[k])
                try:
                    ManipularDados.salvar(avaliacoes, pasta + avaliacoesArquivo)
                    disciplinas.pop(i)
                    ManipularDados.salvar(disciplinas, pasta + disciplinasArquivo)
                    print("Disciplina removida com sucesso.")
                except ValueError:
                    print("Erro ao remover disciplina")

    elif valor == 8:
        listarDisciplinas()
        disciplina = input("Digite a disciplina")

        listarAvaliacoesDisciplinas(disciplina)
        avaliacao = input("Digite a avaliação")

        for i in range(len(disciplinas)):
            if disciplina == disciplinas[i].nome:
                for k in range(len(disciplinas[i].sistemaAvaliacao)):
                    if avaliacao == disciplinas[i].sistemaAvaliacao[k].nome:
                        avaliacoes.pop(k)
                        try:
                            ManipularDados.salvar(avaliacoes, pasta + avaliacoesArquivo)
                            print("Avaliação removida com sucesso.")
                        except ValueError:
                            print("Erro ao remover avaliação")

    elif valor == 9 :

        print("Disciplinas: ")
        for i in range(len(disciplinas)):
            print(str(disciplinas[i]) + " - ", end="")
        print("")
        print("Avaliações: ")
        #for i in range(len(avaliacoes)):
        #    print(str(avaliacoes[i]) + " - " , end="")
        #print("")
        for i in range(len(avaliacoes)):
            print(str(avaliacoes[i]) + " "* (15 - len(avaliacoes[i].nome)) + " - (" + str(avaliacoes[i].disciplina)+")" + " "* (15 - len(avaliacoes[i].disciplina))+ " Nota:" + str(avaliacoes[i].nota) + " "* (15 - len(str(avaliacoes[i].nota))) + " Data:" + str(avaliacoes[i].data) + " "* (15 - len(avaliacoes[i].data))   + " Tipo:" + str(avaliacoes[i].tipo))
        print("---")

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