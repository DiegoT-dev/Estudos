pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    print(pa, end=', ')
    pa += r
    c += 1
print('...\nAcabou!')