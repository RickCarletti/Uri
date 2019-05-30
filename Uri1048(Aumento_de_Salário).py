def final(Porcentagem_de_aumento):
    ajuste = S * (Porcentagem_de_aumento/100)
    NovoS = S + ajuste
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'
          .format(NovoS, ajuste, Porcentagem_de_aumento), end='\n')


S = float(input())
if S <= 400.00:
    final(15)
elif S <= 800.00:
    final(12)
elif S <= 1200.00:
    final(10)
elif S <= 2000.00:
    final(7)
else:
    final(4)
