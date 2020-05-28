s = c = int()
t = '-'
print(f'{t*20}Digite 999 para parar{t*20}')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c:02} números e a soma entre eles é {s:02}.')
