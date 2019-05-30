ponto = list(map(float, input().split()))
x = ponto[0]
y = ponto[1]
if x == y == 0:
    print('Origem', end='\n')
elif x == 0 and y != 0:
    print('Eixo Y', end='\n')
elif x != 0 and y == 0:
    print('Eixo X', end='\n')
elif x > 0 and y > 0:
    print('Q1', end='\n')
elif x < 0 and y > 0:
    print('Q2', end='\n')
elif x < 0 and y < 0:
    print('Q3', end='\n')
elif x > 0 and y < 0:
    print('Q4', end='\n')
