# numeros_certo = [('one', 1), ('two', 2), ('three', 3)]

# contador_numeros = 0
# texto = ''
# qtd = int(input())
# while contador < qtd:
#     text = input()
#     for i in text:
#         for chave, valor in numeros_certo:
#             print(chave)
#     contador+=1


# contador = 0
# contador1 = 0
# contador2 = 0
# contador3 = 0
# one = 'one'
# two = 'two'
# three = 'three'
# qtd = int(input())
# while contador < qtd:
#     text = input()
#     for t in range(0, len(text)):
#         if len(text) == 3:
#             if text[t] == one[t]:
#                 contador1+=1
#             elif text[t] == two[t]:
#                 contador2 +=1
#         else:     
#             if text[t] == three[t]:
#                 contador3+=1
# if contador1+1 == len(one):
#     print('1')
# elif contador2+1 == len(two):
#     print('2')
# elif contador3+1 == len(three):
#     print('3')
#     contador1 = 0
#     contador2 = 0
#     contador3 = 0
#     contador+=1
qte = int(input())

for i in range(qte):
    texto = input()
    
    if(len(texto)>3):
        print(3)
    else:
        soma = 0
        if (texto[0:1]=='o'):
            soma += 1
        if (texto[1:2]=='n'):
            soma += 1
        if (texto[2:3]=='e'):
            soma += 1
        
        if(soma>=2):
            print(1)
        else:
            print(2)