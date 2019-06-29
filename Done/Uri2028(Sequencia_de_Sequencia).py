cont = 0
while True:
    cont += 1
    try:
        x = int(input())
        lista = ['0']
        for i in range(1, x+1):
            for j in range(i):
                lista.append(str(i))
        numeros = 'numero' if x == 0 else 'numeros'
        print('Caso {}: {} {}'.format(cont, len(lista), numeros))
        print(' '.join(lista))
        print()
    except EOFError:
        break
