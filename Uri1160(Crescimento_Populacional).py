T = int(input())
for T in range(T):
    PA, PB, G1, G2 = map(float, input().split())
    anos = 0
    while anos <= 101 and PA <= PB:
        anos = anos + 1
        PA = PA + int(PA * (G1/100))
        PB = PB + int(PB * (G2/100))
    if anos <= 100:
        print('{} anos.'.format(anos), end='\n')
    else:
        print('Mais de 1 seculo.', end='\n')
