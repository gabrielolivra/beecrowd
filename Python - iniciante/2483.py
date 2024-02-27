entrada = int(input())
string = 'Feliz natal!'
incremento = 't'
for i in range(entrada):
    incremento+='a'
r = string.replace('ta', incremento)
print(r)