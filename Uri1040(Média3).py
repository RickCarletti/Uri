n = list(map(float, input().split()))
media = (n[0] * 2 + n[1] * 3 + n[2] * 4 + n[3] * 1) / 10
print('Media: {:.1f}'.format(media), end='\n')
if media >= 7:
    print('Aluno aprovado.', end='\n')
elif 5 <= media < 7:
    print('Aluno em exame.', end='\n')
    n1 = float(input())
    print('Nota do exame: {:.1f}'.format(n1))
    media = (media + n1)/2
    if media >= 5:
        print('Aluno aprovado.', end='\n')
    else:
        print('Aluno reprovado', end='\n')
    print('Media final: {:.1f}'.format(media), end='\n')
else:
    print('Aluno reprovado.', end='\n')
