x = 0
positiv = 0
while x < 6:
    y = float(input())
    if y > 0:
        positiv = positiv + 1
    x = x + 1
print('{} valores positivos'.format(positiv))
