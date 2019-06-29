while True:
    try:
        h1, m1 = map(int, input().split(':'))
        atraso = 0
        m1 += h1 * 60
        mmax = 8 * 60
        if m1 + 60 > mmax:
            atraso = m1 + 60 - mmax
        print('Atraso maximo: {}'.format(atraso))
    except EOFError:
        break
