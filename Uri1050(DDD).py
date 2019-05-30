lista = {'61': 'Brasilia', '71': 'Salvador', '11': 'Sao Paulo', '21': 'Rio de Janeiro', '32': 'Juiz de Fora',
         '19': 'Campinas', '27': 'Vitoria', '31': 'Belo Horizonte'}
ddd = str(input())
if ddd != 61 and ddd != '71' and ddd != '11' and ddd != '21' and ddd != '32' and ddd != '19' and ddd != '27' and ddd != '31':
    print('DDD nao cadastrado', end='\n')
else:
    position = lista.get(ddd)
    print(position, end='\n')
