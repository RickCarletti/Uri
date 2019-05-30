n = list(map(float, input().split()))
n = sorted(n)
a = n[2]
b = n[1]
c = n[0]
if a >= b + c:
    print('NAO FORMA TRIANGULO', end='\n')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO', end='\n')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO', end='\n')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO', end='\n')
    if a == b == c:
        print('TRIANGULO EQUILATERO', end='\n')
    if a == b != c or a == c != b or b == c != a:
        print('TRIANGULO ISOSCELES', end='\n')
