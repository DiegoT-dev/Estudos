# ----------- Cores no Terminal -----------
# ANSI (escape sequence) ---- \033[_X_:_Y_:_Z_m
# onde X é o STYLE, Y é o TEXT e Z é o BACK
#STYLE: 0-(none) / 1-(bold) / 4-(underline) / 7-(negative)
#TEXT: 30-branco / 31- vermelho / 32-verde / 33-amarelo / 34- azul / 35-magenta / 36-ciano / 37-cinza
#BACK: 40-branco / 41- vermelho / 42-verde / 43-amarelo / 44- azul / 45-magenta / 46-ciano / 47-cinza
print('\033[1:31:40mOlá Mundo!\033[m')
