def calcularNotas(matrixNotas):

    notasParciais = []
    for i in range(len(matrixNotas)-2):
        if matrixNotas[i][3] != "":
            notasParciais.append((matrixNotas[i][1] * matrixNotas[i][3])/100)
        print(notasParciais)

    if len(notasParciais) == len(matrixNotas)-2:
        print("ok")
    else:
        notaParapassar = 0
        if (len(matrixNotas)-2) - len(notasParciais) == 1:
            for i in range(len(notasParciais)):
                notaParapassar += notasParciais[i]
            print(notaParapassar)
            print(matrixNotas[len(matrixNotas)-2][3])
            valor = 10 / ( notaParapassar + (matrixNotas[len(matrixNotas)-2][3]*matrixNotas[len(matrixNotas) - 2][3]/100) )
            valor = valor/matrixNotas[len(matrixNotas) - 2][1]*100
            valor = round(valor,2)
            print("Falta ",valor)