valores = input().split()
inicio, fim = map(int, valores)
if inicio < fim:
    print('O JOGO DUROU',fim - inicio,'HORA(S)')  
elif inicio == fim:
    print('O JOGO DUROU',24,'HORA(S)')
elif inicio < 24 and fim < inicio:
    print('O JOGO DUROU',(24 - inicio) + fim,'HORA(S)')