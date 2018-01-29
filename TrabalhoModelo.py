#BIBLIOTECAS NECESSÁRIAS PARA O PROGRAMA FUNCIONAR
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import pickle




#IMPRIME AS LISTAS DE CADEIRAS E PROFESSORES
def printCadeiras(a, b):
    print("Disciplinas:\n")
    for i in range(0, len(a)):
        print(i + 1, a[i], "-", b[i])
    print("\n")

#IMPRIME OS QUADROS DE AVALIAÇÃO DA CADEIRA
def printAvaliacao(a):
    saida = ""
    for i in a[0]:
        saida += "| " + str(i) + " "
    saida += "\n_____________________________________________"
    for i in a[1:]:
        saida += "\n"
        for j in i:
            if j != "a":
                saida += "|" + str(j)
        saida += "\n__________________________________________"
    return saida

#IMPRIME AS OPÇÕES DENTRO DO MENU DA CADEIRA
def printOpcoes(a):
    print("\nO que quer fazer agora? (0 - recuar no programa)\n")
    for i in range(0, len(a)):
        print(i + 1, a[i])
    print("\n")

#CALCULA A NOTA FINAL DA CADEIRA
def calcFinal(a):
    total = 0
    for i in range(0, len(a[1]) - 1):
        total = total + float(a[1][i]) * a[3][i]
    a[3][len(a[3]) - 1] = total

#CALCULA A NOTA MÍNIMA PARA PASSAR NA CADEIRA E DETETA SE É NECESSÁRIO PREENCHER O CAMPO DA NOTA FINAL
def detectParaMedia(a):


#sempre que um dos campos tem o valor 0.0, ele associa como um campo vazio

    if a == avalMat1 or a == avalAP:
        if a[3][0] and a[3][1] and a[3][2] and a[3][3] and a[3][4] == '':
            calcFinal(a)
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))



            if a[3][4] != '':
                if a[3][4] >= 9.5:
                    print("\nAPROVADO")
                else:
                    print("\nREPROVADO")
        elif a[3][0] and a[3][1] and a[3][2] and a[3][3] == '' and a[3][4] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))


            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*a[3][1] + a[1][2]*a[3][2] + a[1][3]*i
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][3] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] and a[3][2] == '' and a[3][3] and a[3][4] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*a[3][1] + a[1][2]*i + a[1][3]*a[3][3]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][2] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] == '' and a[3][2] and a[3][3] and a[3][4] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*i + a[1][2]*a[3][2] + a[1][3]*a[3][3]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][1] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] == '' and a[3][1] and a[3][2] and a[3][3] and a[3][4] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))
            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0] * i + a[1][1] * a[3][1] + a[1][2] * a[3][2] + a[1][3] * a[3][3]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][0] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] and a[3][2] and a[3][3] and a[3][4]:
            calcFinal(a)
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            if a[3][4] >= 9.5:
                print("\nAPROVADO")
            else:
                print("\nREPROVADO")
        else:
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))
    elif a == avalEDC:
        if a[3][0] and a[3][1] and a[3][2] and a[3][3] and a[3][4] and a[3][5] == '':
            calcFinal(a)
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            if a[3][5] != '':
                if a[3][5] >= 9.5:
                    print("\nAPROVADO")
                else:
                    print("\nREPROVADO")
        elif a[3][0] and a[3][1] and a[3][2] and a[3][3] and a[3][4] == '' and a[3][5] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*a[3][1] + a[1][2]*a[3][2] + a[1][3]*a[3][3] + a[1][4]*i
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][4] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] and a[3][2] and a[3][3] == '' and a[3][4] and a[3][5] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*a[3][1] + a[1][2]*a[3][2] + a[1][3]*i + a[1][4]*a[3][4]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][3] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] and a[3][2] == '' and a[3][3] and a[3][4] and a[3][5] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*a[3][1] + a[1][2]*i + a[1][3]*a[3][3] + a[1][4]*a[3][4]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][2] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] == '' and a[3][2] and a[3][3] and a[3][4] and a[3][5] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))
            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*i + a[1][2]*a[3][2] + a[1][3]*a[3][3] + a[1][4]*a[3][4]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][1] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] == '' and a[3][1] and a[3][2] and a[3][3] and a[3][4] and a[3][5] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*i + a[1][1]*a[3][1] + a[1][2]*a[3][2] + a[1][3]*a[3][3] + a[1][4]*a[3][4]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][0] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] and a[3][2] and a[3][3] and a[3][4] and a[3][5]:
            calcFinal(a)
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            if a[3][5] >= 9.5:
                print("\nAPROVADO")
            else:
                print("\nREPROVADO")
        else:
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))
    else:
        if a[3][0] and a[3][1] and a[3][2] and a[3][3] == '':
            calcFinal(a)
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            file.readlines()

            if a[3][3] != '':
                if a[3][3] >= 9.5:
                    print("\nAPROVADO")
                else:
                    print("\nREPROVADO")
        elif a[3][0] and a[3][1] and a[3][2] == '' and a[3][3] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*a[3][1] + a[1][2]*i
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][2] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] == '' and a[3][2] and a[3][3] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*a[3][0] + a[1][1]*i + a[1][2]*a[3][2]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][1] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] == '' and a[3][1] and a[3][2] and a[3][3] == '':
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            for i in np.arange(0.0, 20.1, 0.1):
                nota = a[1][0]*i + a[1][1]*a[3][1] + a[1][2]*a[3][2]
                if nota >= 9.5:
                    print("\nPrecisa de conseguir um " + str(i) + " na avaliação '" + a[0][0] + "' para tirar positiva no final da cadeira")
                    break
        elif a[3][0] and a[3][1] and a[3][2] and a[3][3]:
            calcFinal(a)
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

            if a[3][3] >= 9.5:
                print("\nAPROVADO")
            else:
                print("\nREPROVADO")
        else:
            print(printAvaliacao(a))
            file = open('teste.pck', 'wb')
            pickle.dump(printAvaliacao(a), file)
            file = open('teste.pck', 'rb')
            x = pickle.load(file)
            print(str(x))

#FUNÇÃO PARA INTRODUZIR A COTAÇÃO NA AVALIAÇÃO INDICADA
def introCota(a):
    avaliacao = int(input("\nQual é avaliação que pretende dar uma cotação? (1 - Teste 1; 2 - Teste 2; ...)"))
    nota = float(input("\nQual é o valor da avaliação? "))
    if nota > 0.0 and nota <= 20.0:
        a[3][avaliacao - 1] = nota
    elif nota == 0:
        a[3][avaliacao - 1] = 0.0
    else:
        print("INPUT INVÁLIDO")

#MOSTRA QUANTO TEMPO FALTA PARA UMA CERTA AVALIAÇÃO
def showData(a):
    dataHoje = dt.datetime.today()
    aval = int(input("\nQual é avaliação que pretende saber quanto tempo falta? (1 - Teste 1; 2 - Teste 2; ...)"))
    ano = int(a[2][aval - 1][0:4])
    mes = int(a[2][aval - 1][4:6])
    dia = int(a[2][aval - 1][6:8])
    dataTeste = dt.datetime(ano, mes, dia, 00, 00, 00)
    dataRest = dataTeste - dataHoje
    print("\nFaltam", dataRest, "para a avaliação", a[0][aval - 1], "\n")

#MOSTRA O GRÁFICO DE BARRAS VERTICAIS COM AS AVALIAÇÕES DA CADEIRA
def criarGraficoVertical(a):
    def autoLabel(rects):
        for n in rects:
            height = n.get_height()
            ax.text(n.get_x() + n.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center', va='bottom')

    ind = np.arange(len(a[0]))
    width = 0.7

    fig, ax = plt.subplots()
    notas = ax.bar(ind, a[3], width, color='b')

    ax.set_ylabel('Cotação')
    ax.set_title('Nota das avaliações')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(a[0])
    ax.legend((notas), ('Notas'))

    autoLabel(notas)

    plt.show()

#MOSTRA O GRÁFICO DE BARRAS HORIZONTAIS COM AS NOTAS FINAIS DE TODAS AS CADEIRAS DO SEMESTRE
def criarGraficoHorizontal(dis, a, b, c, d, e):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    y_pos = np.arange(len(dis))
    notas = (a[3][len(a[3]) - 1], b[3][len(b[3]) - 1], c[3][len(c[3]) - 1], d[3][len(d[3]) - 1], e[3][len(e[3]) - 1])

    ax.barh(y_pos, notas, align='center', color='b')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dis)
    ax.invert_yaxis()
    ax.set_xlabel('Cotação')
    ax.set_title('Avaliação geral do semestre')

    plt.show()

#------COMEÇO DO PROGRAMA------
print("Seja bem-vindo(a) ao GAU - Gestão de Avaliação na Universidade\n")

#CADEIRAS DO CURSO DE ENGENHARIA DE INFORMÁTICA NO 1º SEMESTRE
cadeiras = ["Mat 1", "EDC", "AP", "MBD", "SD"]
professores = ["Patricia Ferreira", "Rui Neves", "Paulo Enes da Silveira", "Marco Costa", "João Guerreiro/Daniel Silvestre"]

#QUADROS DE AVALIAÇÕES DE CADA CADEIRA
avalMat1 = [["Teste 1", "Teste 2", "Mini-Testes", "Presenças", "Final"], [0.4, 0.4, 0.15, 0.05, "*"], ["20171127", "20180122", "*", "*", "*"], ['', '', '', '', '']]
avalEDC = [["Teste 1", "Teste 2", "Trabalho 1", "Trabalho 2", "Presenças", "Final"], [0.35, 0.35, 0.1, 0.1, 0.1, "*"], ["20171206", "20180117", "20180112", "20180126", "*", "*"], ['', '', '', '', '', '']]
avalAP = [["Teste 1", "Teste 2", "Trabalho", "Presenças", "Final"], [0.3, 0.3, 0.35, 0.05, "*"], ["20171205", "20180119", "20180115", "*", "*"], ['', '', '', '', '']]
avalMBD = [["Teste 1", "Teste 2", "Presenças", "Final"], [0.45, 0.45, 0.1, "*"], ["20171129", "20180124", "*", "*"], ['', '', '', '']]
avalSD = [["Teste 1", "Teste 2", "Média dos Laboratórios", "Final"], [0.3, 0.3, 0.4, "*"], ["20171123", "20180118", "*", "*"], ['', '', '', '']]





#COISAS QUE SE PODE FAZER DENTRO DA TABELA DE AVALIAÇÕES
opcoes = ["Introduzir cotação a uma das avaliações", "Mostrar o tempo restante para uma avaliação", "Mostrar gráfico das avaliações"]

selecOP = 999


#O PROGRAMA VAI CORRER ATÉ O USER DAR O INPUT '0' NO selecCadeira
while selecOP != 0:

    print("O que quer fazer agora? \n1 - abrir uma disciplina \n2 - mostrar gráfico vertical com as notas (só pode ser mostrado se todas as cadeiras tiverem nota final) \n0 - sair do programa\n")

    selecOP = int(input())

    if selecOP == 1:
        selecCadeira = 999

        while selecCadeira != 0:
            printCadeiras(cadeiras, professores)

            selecCadeira = int(input("Qual disciplina quer selecionar? (0 - Recuar no programa) "))

            print("\n")

            if (selecCadeira == 1):
                selecOpcao = 999

                while selecOpcao != 0:
                    print(cadeiras[selecCadeira - 1])

                    detectParaMedia(avalMat1)

                    printOpcoes(opcoes)
                    selecOpcao = int(input())

                    if selecOpcao == 1:
                        introCota(avalMat1)
                    elif selecOpcao == 2:
                        criarGraficoVertical(avalMat1)
                    elif selecOpcao == 3:
                        showData(avalMat1)
                    elif selecOpcao == 0:
                        print("\nA sair da disciplina.")
                    else:
                        print("OPÇÃO INVÁLIDA!")

            elif (selecCadeira == 2):
                selecOpcao = 999

                while selecOpcao != 0:
                    print(cadeiras[selecCadeira - 1])

                    detectParaMedia(avalEDC)

                    printOpcoes(opcoes)
                    selecOpcao = int(input())

                    if selecOpcao == 1:
                        introCota(avalEDC)
                    elif selecOpcao == 2:
                        criarGraficoVertical(avalEDC)
                    elif selecOpcao == 3:
                        showData(avalEDC)
                    elif selecOpcao == 0:
                        print("\nA sair da disciplina.")
                    else:
                        print("OPÇÃO INVÁLIDA!")

            elif (selecCadeira == 3):
                selecOpcao = 999

                while selecOpcao != 0:
                    print(cadeiras[selecCadeira - 1])

                    detectParaMedia(avalAP)

                    printOpcoes(opcoes)
                    selecOpcao = int(input())

                    if selecOpcao == 1:
                        introCota(avalAP)
                    elif selecOpcao == 2:
                        criarGraficoVertical(avalAP)
                    elif selecOpcao == 3:
                        showData(avalAP)
                    elif selecOpcao == 0:
                        print("\nA sair da disciplina.")
                    else:
                        print("OPÇÃO INVÁLIDA!")

            elif (selecCadeira == 4):
                selecOpcao = 999

                while selecOpcao != 0:
                    print(cadeiras[selecCadeira - 1])

                    detectParaMedia(avalMBD)

                    printOpcoes(opcoes)
                    selecOpcao = int(input())

                    if selecOpcao == 1:
                        introCota(avalMBD)
                    elif selecOpcao == 2:
                        criarGraficoVertical(avalMBD)
                    elif selecOpcao == 3:
                        showData(avalMBD)
                    elif selecOpcao == 0:
                        print("\nA sair da disciplina.")
                    else:
                        print("OPÇÃO INVÁLIDA!")

            elif (selecCadeira == 5):
                selecOpcao = 999

                while selecOpcao != 0:
                    print(cadeiras[selecCadeira - 1])

                    detectParaMedia(avalSD)

                    printOpcoes(opcoes)
                    selecOpcao = int(input())

                    if selecOpcao == 1:
                        introCota(avalSD)
                    elif selecOpcao == 2:
                        criarGraficoVertical(avalSD)
                    elif selecOpcao == 3:
                        showData(avalSD)
                    elif selecOpcao == 0:
                        print("\nA sair da disciplina.")
                    else:
                        print("OPÇÃO INVÁLIDA!")

            elif (selecCadeira == 0):
                print("\nA recuar no programa")

            else:
                print("OPÇÃO INVÁLIDA!\n")

    elif selecOP == 2:
        criarGraficoHorizontal(cadeiras, avalMat1, avalEDC, avalAP, avalMBD, avalSD)
    elif selecOP == 0:
        print("Até sempre!!! ;)")
    else:
        print("OPÇÃO INVÁLIDA!")