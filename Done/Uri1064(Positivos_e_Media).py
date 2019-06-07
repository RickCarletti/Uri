x = 0
positiv = 0
todosp = 0
while x < 6:
    y = float(input())
    if y > 0:
        positiv = positiv + 1
        todosp = todosp + y
    x = x + 1
print('{} valores positivos\n{:.1f}'.format(positiv, todosp/positiv), end='\n')
