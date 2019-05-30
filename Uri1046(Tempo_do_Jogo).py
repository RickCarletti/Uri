h = list(map(int, input().split()))
if h[0] >= h[1]:
    print('O JOGO DUROU {} HORA(S)'.format(h[1] + 24 - h[0]), end='\n')
else:
    print('O JOGO DUROU {} HORA(S)'.format(h[1] - h[0]), end='\n')
