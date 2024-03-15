valores = input().split()
qtd_anoes = int(valores[0])
val_fixo = 2
km = int(valores[1])
total_pessoas = qtd_anoes+ val_fixo
resultado = km/total_pessoas
print(f'{resultado:.2f}')