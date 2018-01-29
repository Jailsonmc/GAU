import sys
import manipularDados

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

        print("Curso: "+self.nome)
        print("Docente: "+self.docente)
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

        print("\n")



    def verificarEstadoAvaliacao(self):
        try:
            pass
        except ValueError:
            return -2

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



