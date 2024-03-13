qtd = int(input())
contador_m = 0
contador_f = 0
for i in range(qtd):
    entrada = input().split()
    if entrada[1] == 'F':
        contador_f+=1
    elif entrada[1] == 'M':
        contador_m+=1
print(contador_m, 'carrinhos')
print(contador_f, 'bonecas')
    