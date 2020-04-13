import random
n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A sequência de alunos para apresentação é a seguinte:\n', lista)
