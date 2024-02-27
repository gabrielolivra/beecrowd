lista = []
while True:
    valor = int(input())
    if valor < 0:
        break
    else:
        lista.append(valor)
resultado = sum(lista)
media = resultado/len(lista)
print(f'{media:.2f}')