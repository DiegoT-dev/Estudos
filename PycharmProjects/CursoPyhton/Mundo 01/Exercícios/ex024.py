n = str(input('Qual a cidade em que você mora? ')).strip()
n = n.upper()
n = n.split()
print('Sua cidade começa com Santo: {}'.format('SANTO' in n[0]))
