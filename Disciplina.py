import sys

class Disciplina:
    def __init__(self, nome, docente):
        self.nome = nome
        self.sistemaAvaliacao = []
        self.docente = docente

    def __str__(self):
        return self.nome

    def escreverLabelTabela(self, texto, tamanho):
        return (tamanho - len(texto))*" "

    def criarAvaliacao(self, avaliacao):
        try:

            if len(self.sistemaAvaliacao) > 0:
                for i in range(len(self.sistemaAvaliacao)):
                    if avaliacao.nome == self.sistemaAvaliacao[i].nome:
                        #return "Já existe uma avaliação com este nome."
                        return -1
                        #break
                    else:
                        self.sistemaAvaliacao.append(avaliacao)
                        #return "Avaliação adicionada com sucesso"
                        return 1
                        #break
            else:
                self.sistemaAvaliacao.append(avaliacao)
                #return "Avaliação adicionada com sucesso"
                return 1
        except ValueError:
            #return "Ocorreu um erro ao adicionar a avaliação"
            return -2

    def removerAvaliacao(self, nome):
        try:
            for i in range(len(self.sistemaAvaliacao)):
                if nome == self.sistemaAvaliacao[i].nome:
                    self.sistemaAvaliacao.pop(i)
                    return 1
                    break
                else:
                    return -1
                    break
        except ValueError:
            return -2

    def afixarTabelaAvaliacao(self):

        print("Avaliação contínua 1° ano/1° semestre - Curso: "+self.nome)
        print("Docente: "+self.docente)
        listaNotas = []
        resultado = 0
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].nome + self.escreverLabelTabela(self.sistemaAvaliacao[i].nome,10) )
        print("Final")
        print("\n")
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].percentagem +"% "+ self.escreverLabelTabela(self.sistemaAvaliacao[i].percentagem,9) )
        print("\n")
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].data + self.escreverLabelTabela(self.sistemaAvaliacao[i].data,10) )
        print("\n")
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].nota + self.escreverLabelTabela(self.sistemaAvaliacao[i].nota,10) )
            if self.sistemaAvaliacao[i].nota != "":
                listaNotas.append(self.sistemaAvaliacao[i].nota)
            print(listaNotas)
            if len(listaNotas) == len(self.sistemaAvaliacao):
                print("Entrou")
                for i in range(len(self.sistemaAvaliacao)):
                    resultado = resultado + self.sistemaAvaliacao[i].nota*(self.sistemaAvaliacao[i].percentagem/100)
                print(resultado)
        print("\n")


    def retornarClassificacoes(self):
        listaNotas = []
        for i in range(len(self.sistemaAvaliacao)):
            listaNotas.append(self.sistemaAvaliacao[i].nota)
        return listaNotas

    def retornarNomesAvaliacoes(self):
        listaNomes = []
        for i in range(len(self.sistemaAvaliacao)):
            listaNomes.append(self.sistemaAvaliacao[i].nome)
        return listaNomes

    def retornarNotaFinal(self):
        listaNotas = []
        resultadoParcial = 0
        for i in range(len(self.sistemaAvaliacao)):
            if self.sistemaAvaliacao[i].nota != "":
                listaNotas.append(self.sistemaAvaliacao[i].nota)
        if len(listaNotas) == len(self.sistemaAvaliacao):
            for k in range(len(self.sistemaAvaliacao)):
                resultadoParcial = resultadoParcial + (self.sistemaAvaliacao[k].nota * (self.sistemaAvaliacao[k].percentagem/100))
            if len(self.sistemaAvaliacao) == 0:
                #return "Não Definida"
                return 0
            else:
                return resultadoParcial/len(self.sistemaAvaliacao)
        else:
            return 0
            #return "Não Definida"

        print(self.sistemaAvaliacao)

    def verificarEstadoAvaliacao(self):
        print("Curso: "+self.nome)
        print("Docente: "+self.docente)
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].nome + self.escreverLabelTabela(self.sistemaAvaliacao[i].nome,10) )
        #print("Final")
        print("\n")
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].percentagem +"% "+ self.escreverLabelTabela(self.sistemaAvaliacao[i].percentagem,9) )
        print("\n")
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].data + self.escreverLabelTabela(self.sistemaAvaliacao[i].data,10) )
        print("\n")
        for i in range(len(self.sistemaAvaliacao)):
            sys.stdout.write(self.sistemaAvaliacao[i].nota + self.escreverLabelTabela(self.sistemaAvaliacao[i].nota,10) )

        print("\n")
        listaNotas = []
        listaNotasPercentagem = []
        temPrescenca = False
        listaNotasVazias = []
        listaNotasVaziasPercentagem = []
        for i in range(len(self.sistemaAvaliacao)):
            if self.sistemaAvaliacao[i].nota != "":
                listaNotas.append(float(self.sistemaAvaliacao[i].nota))
                listaNotasPercentagem.append(float(self.sistemaAvaliacao[i].percentagem))
            if self.sistemaAvaliacao[i].tipo == "p":
                temPrescenca = True
                percentagemPrecenca = self.sistemaAvaliacao[i].percentagem
            if self.sistemaAvaliacao[i].nota == "" and self.sistemaAvaliacao[i].tipo != "p":
                listaNotasVazias.append(self.sistemaAvaliacao[i].nota)
                listaNotasVaziasPercentagem.append(self.sistemaAvaliacao[i].percentagem)
        somatioPercentagem = sum(listaNotasPercentagem)
        nota = 0

        if temPrescenca and len(listaNotas) == (len(self.sistemaAvaliacao) - 2 ) and len(listaNotasVazias) == 1:

            for i in range(len(listaNotas)):
                nota = float(nota) + float(listaNotas[i])*(float(listaNotasPercentagem[i])/100)
                nota = float(nota) + float(20)*(float(percentagemPrecenca[i])/100)

            notaNecessaria = (10 - float(nota))/float(str(listaNotasVaziasPercentagem[0]))
            notaNecessaria = round(notaNecessaria,2)
            print("Nota Necessária para passar: "+str(notaNecessaria))
        elif temPrescenca and len(listaNotas) == (len(self.sistemaAvaliacao) - 1) and len(listaNotasVazias) == 0:
            nota = 0
            #print(listaNotas)
            #print(listaNotasPercentagem)
            #print(percentagemPrecenca)
            for i in range(len(listaNotas)):
                nota = float(nota) + float(listaNotas[i])*(float(listaNotasPercentagem[i])/100)
                nota = float(nota) + float(20)*(float(percentagemPrecenca[0])/100)
            print("Nota Final : " + str(round(nota,2)))
            print("")
        else:
            print("Há mais de 1 item faltando, no entando não pode ser calculado a nota para passar.\n")
            print("")

    def regitarClassificacao(self, nome, nota):
        try:
            for i in range(len(self.sistemaAvaliacao)):
                if nome == self.sistemaAvaliacao[i].nome:
                    self.sistemaAvaliacao[i].nota = nota
                    return 1
                    break
                else:
                    return -1
                    break
        except ValueError:
            return -2



