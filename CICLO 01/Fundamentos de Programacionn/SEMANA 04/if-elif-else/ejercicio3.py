# Se desea saber si el alumno, Aprobó, Pasó a las justas o Reprobó, 
# donde mayores de 18 es APROBADO, 
# mayores de 12 es PASÓ A LAS JUSTAS 
# y mayores de 0 REPROBÓ

nota = int(input("Ingrese un nota: "))

if nota > 0 and nota < 12 :
    print(f"La nota del alumno es {nota} y REPROBÓ el curso.")
elif nota >= 12 and nota < 18:
    print(f"La nota del alumno es {nota} y PASÓ A LAS JUSTAS el curso.")
else:
    print(f"La nota del alumno es {nota} y APROBÓ el curso.")