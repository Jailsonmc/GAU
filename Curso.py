class Curso:

    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def __str__(self):
        return self.nome

    def adicionarDisciplina(self, disciplina):
        try:
            for i in range(len(self.disciplinas)):
                if disciplina.nome == self.disciplinas[i].nome:
                    return -1
                    break
                else:
                    self.disciplinas.append(disciplina)
                    return 1
                    break
        except ValueError:
            return -2

    def removerDisciplina(self, nome):
        try:
            for i in range(len(self.disciplinas)):
                if nome == self.disciplinas[i].nome:
                    self.disciplinas.pop(i)
                    return 1
                    break
                else:
                    return -1
                    break
        except ValueError:
            return -2

    def editarDisciplina(self, nome):
        try:
            for i in range(len(self.disciplinas)):
                if nome == self.disciplinas[i].nome:
                    self.disciplinas.nome[i] == nome
                    return 1
                    break
                else:
                    return -1
                    break
        except ValueError:
            return -2


