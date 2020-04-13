altura = float(input('Qual a sua altura: '))
peso = float(input('Qual é o seu peso: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Você está ABAIXO DO PESO. Seu IMC = {:.1f}'.format(imc))
elif imc <= 25:
    print('Você está no seu PESO IDEAL. Seu IMC = {:.1f}'.format(imc))
elif imc <= 30:
    print('Você está com SOBREPESO. Seu IMC = {:.1f}'.format(imc))
elif imc <= 40:
    print('Você está com OBESIDADE. Seu IMC = {:.1f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA. Seu IMC = {:.1f}'.format(imc))
