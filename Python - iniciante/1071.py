soma = 0
x = int(input())
y = int(input())

if x > y:
    x -= 1
    while x > y:
        if x % 2 != 0:
            soma += x
        x -= 1
if y > x:
    y -= 1
    while y > x:
        if y % 2 != 0:
            soma += y
        y -= 1
print(soma)