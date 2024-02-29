qtd = int(input())
lista = []
lista_par = []
lista_impar = []
for i in range(qtd):
    valor = int(input())
    lista.append(valor)
for l in lista:
    if l % 2 == 0:
        lista_par.append(l)
    else:
        lista_impar.append(l)
lista_par.sort()
lista_impar.sort(reverse=True)
for lp in lista_par:
    print(lp)
for li in lista_impar:
    print(li)
