import math
a = float(input('Digite um angulo qualquer: '))
b = math.radians(a)
cos = math.cos(b)
sen = math.sin(b)
tan = math.tan(b)
print('Para o ângulo de {}° temos:\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(a, sen, cos, tan))
