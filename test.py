entrada = 3
lista = []
for i in range(1,10):
    lista.append(i)
    if len(lista) == 4:
        lista.append(i)
print(lista)
    