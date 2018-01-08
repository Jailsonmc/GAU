import datetime

import methods
import textos


continuar = True
print("Bem-vindo Aluno")
while continuar:
    for i,j in enumerate (textos.opcoes):
        print(textos.opcoes[i])

    valor = input("Digite o valor correspondente")
















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
