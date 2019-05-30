n = int(input())
ano = n // 365
mes = (n - ano * 365) // 30
dia = n - ano * 365 - mes * 30
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, mes, dia), end='\n')
