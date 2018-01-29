class Avaliacao():

    def __init__(self, nome, percentagem, data, nota, tipo, disciplina):
        self.nome = nome
        self.percentagem = percentagem
        self.data = data
        self.nota = nota
        self.tipo = tipo
        self.disciplina = disciplina

    def __str__(self):
        return self.nome
