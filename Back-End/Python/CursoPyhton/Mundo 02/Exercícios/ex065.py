c = 0
s = 0
resp = 'S'
while resp != 'N':
    n = int(input('Digite um número: '))
    resp = str(input('\033[1:30mQuer continuar?[S/N]\033[m ')).strip().upper()[:1]
    c += 1
    if c == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    s += n
print('Analisando os dados digitados, informo:\nA média dos valores digitados é {:.2f}\nO maior número digitado foi {}\nE o menor número digitado foi o {}'.format(s / c, maior, menor))
