lista_pessoas =[]
n1 = int(input())
for i in range(n1):
    qtd_pessoas = int(input())
    lista = []
    for k in range(qtd_pessoas):
        pessoa = input()
        lista.append(pessoa)
    lista_pessoas.append(lista)
for i in lista_pessoas:
    chines = 0
    portugues = 0
    espanhol = 0
    for l in i:
        if l == 'portugues':
            portugues+=1
        if l == 'chines':
            chines+=1
        if l == 'espanhol':
            espanhol+=1
    if chines == 0 and portugues == 0:
        print('espanhol')
    elif portugues == 0 and espanhol == 0:
        print('chines')
    elif chines == 0 and espanhol == 0:
        print('portugues')
    else:
        print('ingles')