# Variáveis Compostas:
# _____________ Listas ________________
# Listas podem ser mutáveis
# Variáveis podem comecar de 3 formas: () / [] / {}
# Listas são representadas por []
# podem ser feitas com variavel = list()
##########################################################
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
#adicionar
num.append(7)
print(num)
num.insert(2, 10)
print(num)
#ordenar
num.sort()
print(num)
num.sort(reverse=True)
print(num)
#remoção de elementos
num.pop()#pode ser vazio o indice e eliminara o ultimo elemento ou indicar qual indice quer ser eliminado'''
print(num)
num.remove(5)#para remover a ocorrência do elemento'''
print(num)
del num[1]#deleta o indice desejado'''
print(num)
###############################################
valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Final da lista')