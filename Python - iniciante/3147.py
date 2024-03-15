guerra = input().split()
humanos = int(guerra[0])
elfos = int(guerra[1])
anoes = int(guerra[2])
orcs = int(guerra[3])
wargs = int(guerra[4])
aguias = int(guerra[5])
bem = humanos + elfos + anoes + aguias
mal = orcs + wargs

if bem >= mal:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')