def voto(x):
    from datetime import datetime
    a = datetime.today().year - x
    if a < 16:
        return (f'Com {a} anos o Voto não é Permitido')
    elif 16 <= a < 18 or a >= 65:
        return (f'Com {a} anos o Voto é Opcional')
    else:
        return (f'Com {a} anos o Voto é Obrigatório')


ano = int(input("Qual o seu ano de nascimento? "))
print(voto(ano))
