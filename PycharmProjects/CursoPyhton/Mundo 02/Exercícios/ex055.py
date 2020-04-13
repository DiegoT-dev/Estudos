maiorpeso = float()
menorpeso = float()
for c in range(0, 5):
    peso = float(input('Digite o peso da pessoa: '))
    if c == 0:
        maiorpeso = peso
        menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print('O maior peso digitado foi {:.1f}kg e o menor {:.1f}kg'.format(maiorpeso, menorpeso))
