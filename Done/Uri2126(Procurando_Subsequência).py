cont = 1
while True:
    try:
        N1 = input()
        N2 = input()
        quant, last = 0, -1
        for i in range(len(N2)):
            if N2[i:].count(N1) != 0:
                quant += 1 if N2[i:].index(N1) == 0 else 0
                last = i+1
        print('Caso #{}:'.format(cont))
        print('Qtd.Subsequencias: {}\nPos: {}'.format(quant, last)) if last != -1 else print('Nao existe subsequencia')
        cont += 1
        print()
    except EOFError:
        break
