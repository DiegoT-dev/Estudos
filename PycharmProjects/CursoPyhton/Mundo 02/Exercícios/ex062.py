pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    print(pa, end=', ')
    pa += r
    c += 1
print('...\nEsse foram os 10 primeiros termos da PA. ', end='')
c2 = int(input('Gostaria de ver mais quantos termos? '))
while c2 != 0:
    c = 0
    while c < c2:
        print(pa, end=', ')
        pa += r
        c += 1
    c2 = int(input('...\nGostaria de ver mais quantos termos? '))
print('Acabou!')