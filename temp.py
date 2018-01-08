import datetime

curso = "Engenharia Informática"

disciplinas = ["Estruturas Discretas de Computação","Algoritmia e Programação","Matemática I",
               "Modelação e Bases de Dados","Sistemas Digitais"]

docentes = ["Professor de EDC","Professor de AP","Professor de Matemática I","Professor de BD","Professor de SD"]

avaliacaoEDC = [ [ "Trabalho 1",10, 20171010, 15] , [ "Teste 1", 10, 20180115, 8] , ["Trabalho 2", 35, 20171120, 14],
                 ["Teste 2", 35, 20171216,13], ["Presenças",10,"",2] , ["Final","","",14] ]

t = datetime.time(9,30,45,100000)
#print(t.hour)
#print(t)

t1Date = str(avaliacaoEDC[1][2])
print("Tamanho",len(t1Date))

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

"""for i in range(len(avaliacaoEDC)):
    for j in range(len(avaliacaoEDC)-2):
        if (i == len(avaliacaoEDC)):
            #print(avaliacaoEDC[j][i],end="")
        else:
            #print(avaliacaoEDC[i][j])
            #print(avaliacaoEDC[j][i],end="\ sn")
            #print(avaliacaoEDC[i][j])

#print(avaliacaoEDC[][])"""