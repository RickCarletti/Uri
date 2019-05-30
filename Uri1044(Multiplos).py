x = list(map(int, input().split()))
if x[0] % x[1] == 0 or x[1] % x[0] == 0:
    print('Sao Multiplos', end='\n')
else:
    print('Nao sao Multiplos', end='\n')
