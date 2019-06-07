N = float(input())
if 0 <= N <= 25:
    print('Intervalo [0,25]', end='\n')
elif 25 < N <= 50:
    print('Intervalo (25,50]', end='\n')
elif 50 < N <= 75:
    print('Intervalo (50,75]', end='\n')
elif 75 < N <= 100:
    print('Intervalo (75,100]', end='\n')
else:
    print('Fora de intervalo', end='\n')
