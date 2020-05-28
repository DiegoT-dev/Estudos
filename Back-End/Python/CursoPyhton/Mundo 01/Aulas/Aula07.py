# ____________________Operadores Aritméticos_____________________
#
# + -> Adição                     / _________Precedências_______
# - -> Subtração                  /         1. ()
# * -> Multiplicação              /          2. **
# / -> Divisão                    /           3. * / // %
# ** -> Potência                  /            4. + -
# // -> Divisão Inteira           /
# % -> Módulo (resto da divisão)  /
#
# Alguns testes....
#print('='*21)
#print(' '*10,'Oi',' '*10)
#print('='*21)
#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:-^20}'.format(nome))
# para quebrar linha no meio \n e para não quebrar no final , end=""
n1 = int(input('Digite um número: '))
n2 = int(input('Agora outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {} o produto é {} e a divisão é {:.3f}!'.format(s, m, d))
print('Já a divisão inteira é {0} e a potenciação de {2} elevado a {3} é igual a {2}!'.format(di, e, n1, n2))
