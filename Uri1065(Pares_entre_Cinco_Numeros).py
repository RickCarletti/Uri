x = 0
pares = 0
while x < 5:
    y = float(input())
    if y % 2 == 0:
        pares = pares + 1
    x = x + 1
print('{} valores pares'.format(pares), end='\n')
