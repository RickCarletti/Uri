rept = 0
maior = 0
posicao = 0
while rept < 100:
    rept = rept + 1
    N = int(input())
    if N > maior:
        maior = N
        posicao = rept
print('{}\n{}'.format(maior, posicao), end='\n')
