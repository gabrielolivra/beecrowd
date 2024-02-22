values = [int(x) for x in input().split()]
maior = values[0]
for valor in values:
    if  valor > maior:
        maior = valor
print(maior,"eh o maior")