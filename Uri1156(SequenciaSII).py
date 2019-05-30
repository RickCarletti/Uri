cont = 20
soma = 0
for cont in range(cont):
    soma = soma + (1 + 2*cont)/(2**cont)
print('{:.2f}'.format(soma))
