Impar = []
Par = []
impar = 0
par = 0
for i in range(15):
    X = int(input())
    if X % 2 == 0:
        Par.append(X)
        par = par + 1
        if par == 5:
            for j in range(5):
                print('par[{}] = {}'.format(j, Par[j]))
            Par = []
            par = 0
    else:
        Impar.append(X)
        impar = impar + 1
        if impar == 5:
            for j in range(5):
                print('impar[{}] = {}'.format(j, Impar[j]))
            Impar = []
            impar = 0
for impar in range(impar):
    print('impar[{}] = {}'.format(impar, Impar[impar]))
for par in range(par):
    print('par[{}] = {}'.format(par, Par[par]))
