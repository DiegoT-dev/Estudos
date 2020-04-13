#import random
from random import randint
#pc = random.randint(0,5)
pc = randint(0, 5)
us = int(input('Acabo de escolher um número de 0 a 5. Que número foi esse? '))
if us == pc:
    print('Céussss.....você acertou!')
else:
    print('HahaHa.....você errou!')
print('Porque o número que eu escolhi foi o {}.'.format(pc))
# Rara fazer esperar
# Biblioteca time / método sleep()
