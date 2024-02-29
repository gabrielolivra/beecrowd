nomes = input().split()
maior = max(nomes)
menor = min(nomes)
for n in nomes:
    if n not in maior and  n not in menor:
        resultado = nomes.index(n)
        if resultado == 0:
            print('huguinho')
        elif resultado == 1:
            print('zezinho')
        else:
            print('luisinho')
            