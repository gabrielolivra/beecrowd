valores = input().split()
a, b, c, d = map(float, valores)
media = (a*2 + b*3 + c*4 + d*1)/10
if media >= 7.0:
    print("Media:", f'{media:.1f}')
    print("Aluno aprovado.")
elif media >=5.0 and media <= 6.9:
    print("Media:",f'{media:.1f}')
    print("Aluno em exame.")
    exame = float(input())
    resultado = (media + exame) / 2
    print("Nota do exame:",f'{exame:.1f}')
    if resultado >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", f'{resultado:.1f}')
    else:
        print("Aluno aprovado.")
        print("Media final:",f'{resultado:.1f}')
else:
    print("Media:", f'{media:.1f}')
    print("Aluno reprovado.")