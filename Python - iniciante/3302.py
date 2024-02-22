qtd = int(input())
contador = 0
qtd_resposta = []
lista_resposta = []
while contador < qtd:
    r = input()
    contador +=1
    qtd_resposta.append(contador)
    lista_resposta.append(r)
for i in range(0, len(lista_resposta)):
    print(f'resposta {qtd_resposta[i]}: {lista_resposta[i]}')