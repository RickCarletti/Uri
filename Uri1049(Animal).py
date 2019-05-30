def final(animal):
    print(animal, end='\n')


t1 = str(input())
t2 = str(input())
t3 = str(input())
if t1 == 'vertebrado':
    if t2 == 'ave':
        if t3 == 'carnivoro':
            final('aguia')
        elif t3 == 'onivoro':
            final('pomba')
    elif t2 == 'mamifero':
        if t3 == 'onivoro':
            final('homem')
        elif t3 == 'herbivoro':
            final('vaca')
elif t1 == 'invertebrado':
    if t2 == 'inseto':
        if t3 == 'hematofago':
            final('pulga')
        elif t3 == 'herbivoro':
            final('lagarta')
    elif t2 == 'anelideo':
        if t3 == 'hematofago':
            final('sanguessuga')
        elif t3 == 'onivoro':
            final('minhoca')
