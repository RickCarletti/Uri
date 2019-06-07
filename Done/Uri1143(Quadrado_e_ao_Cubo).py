rept = int(input())
x = 0
while rept > 0:
    x = x + 1
    print('{} {} {}'.format(x, x**2, x**3), end='\n')
    rept = rept - 1
