segundos=int(input())
horas = segundos // 3600
segs_restantes = segundos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60


print("{}:{}:{}".format(horas,minutos,segs_restantes_final))