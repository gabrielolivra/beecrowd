contador = 0
lista_valores = []
while contador < 100:
    try:
        valor = int(input())
        lista_valores.append(valor)
        contador+=1
    except EOFError:
        break
print(max(lista_valores))
print((lista_valores.index(max(lista_valores)))+1)