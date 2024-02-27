contador = 0
frase_final = []
encremento = ''
qtd = int(input())
while contador < qtd:
    text = input()
    text1 = text.replace('·', ' ')
    lista_nome = text1.split()
    for l in lista_nome:
        encremento+=l[0]
    contador+=1
    print(encremento)
    encremento = ''
