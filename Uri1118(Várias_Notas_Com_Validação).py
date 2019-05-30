rept = 1
while rept != 2:
    if rept == 1:
        cont = 0
        while cont < 2:
            nota = float(input())
            if cont == 0 and 0 <= nota <= 10:
                nota1 = nota
                cont = cont + 1
            elif cont == 1 and 0 <= nota <= 10:
                nota2 = nota
                cont = cont + 1
            else:
                print('nota invalida')
        print('media = {:.2f}'.format((nota1 + nota2) / 2), end='\n')
    rept = int(input('novo calculo (1-sim 2-nao)'))
    print()
