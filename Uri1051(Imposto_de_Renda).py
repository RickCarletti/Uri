def final(Imposto_final):
    print('R$ {:.2f}'.format(Imposto_final), end='\n')


renda = float(input())
if renda <= 2000.00:
    print('Isento', end='\n')
else:
    renda = renda - 2000.00
    if renda > 1000.00:
        Imposto = 1000.00 * 0.08
        renda = renda - 1000.00
        if renda > 1500:
            Imposto = Imposto + 1500.00 * 0.18
            renda = renda - 1500.00
            Imposto = Imposto + renda * 0.28
            final(Imposto)
        else:
            Imposto = Imposto + renda * 0.18
            final(Imposto)

    else:
        Imposto = renda * 0.08
        final(Imposto)
