def result(quant, valor):
    print('Total: R$ {:.2f}'.format(quant * valor), end='\n')


n = list(map(int, input().split()))
if n[0] == 1:
    result(n[1], 4.00)
elif n[0] == 2:
    result(n[1], 4.50)
elif n[0] == 3:
    result(n[1], 5.00)
elif n[0] == 4:
    result(n[1], 2.00)
elif n[0] == 5:
    result(n[1], 1.50)
else:
    print('Deu ruim')
