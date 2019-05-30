x = int(input())
y = x + 12
while x < y:
    if x % 2 == 0:
        x = x + 1
    print(x, end='\n')
    x = x + 2
