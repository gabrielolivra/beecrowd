valor_inicial = int(input())
contador = 0
lista_dados = []
while contador < valor_inicial:
    valores = int(input())
    lista_dados.append(valores)
    contador +=1
for i in lista_dados:
    if i == 0:
        print('NULL')
    elif i%2 == 0 and i > 0:
        print("EVEN POSITIVE")
    elif i%2 == 0 and i < 0:
        print("EVEN NEGATIVE")
    elif i%2 !=0 and i > 0:
        print("ODD POSITIVE")
    elif i%2 !=0 and i < 0:
        print("ODD NEGATIVE")
