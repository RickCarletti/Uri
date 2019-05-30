X = 1
while X != 0:
    X = int(input())
    if X != 0:
        keep = 5
        soma = 0
        x = X
        for keep in range(keep):
            if x % 2 != 0:
                x = x + 1
            soma = soma + x
            x = x + 2
        print(soma)
