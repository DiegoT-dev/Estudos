# Variáveis Compostas:
# _____________ TUPLAS ________________
# Tuplas são Imutáveis
# Variáveis podem comecar de 3 formas: () / [] / {}
# tuplas são representadas por () mas não precisam mais ser inicializadas mais com ()
##########################################################
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
#
# lanche[1] = 'Refrigerante' => não acontece
#
print(lanche[::-1])
#
for c in lanche:
    print(c)
#
for c in range(0, len(lanche)):
    print(lanche[c])
#
#para mostrar em ordem => print(sorted(lanche))
#
