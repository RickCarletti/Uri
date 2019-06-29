while True:
    lista31 = [1, 3, 5, 7, 8, 10]
    lista30 = [4, 6, 9, 11]
    try:
        mes, dia = map(int, input().split())
        if dia == 24 and mes == 12:
            print('E vespera de natal!')
        elif mes == 12 and dia > 25:
            print('Ja passou!')
        elif mes == 12 and dia == 25:
            print('E natal!')
        else:
            diastot = 0
            for i in range(mes, 12):
                if i in lista30:
                    diastot += 30
                elif i in lista31:
                    diastot += 31
                elif i == 2:
                    diastot += 29
            diastot = diastot + 25 - dia
            print('Faltam {} dias para o natal!'.format(diastot))
    except EOFError:
        break
