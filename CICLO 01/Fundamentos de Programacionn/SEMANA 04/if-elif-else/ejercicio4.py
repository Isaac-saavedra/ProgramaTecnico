# Requerir al usuario que ingrese un día de la semana 
# e imprimir un mensaje si: 
# Está escrito en minus, MAYUS, Capitalize
# Caso contrario, imprimir: ESCRITO DE MALA MANERA

dia = input("Ingrese un día de la semana: ")

#print("Minúscula")
#print(dia.lower())
#print("Mayúscula")
#print(dia.upper())
#print("Primera MAYUS, resto minus")
#print(dia.capitalize())

if dia == dia.lower():
    print(f"Día {dia} escrito en minúscula.")
elif dia == dia.upper():
    print(f"Día {dia} escrito en mayúscula.")
elif dia == dia.capitalize():
    print(f"Día {dia} escrito en primera MAYUS y resto minus.")
else:
    print(f"Día {dia} escrito en mala manera.")


