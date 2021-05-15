#En una discoteca, se permite el acceso a ingresos de mayores de edad, 
#ayuda a la persona de SEGURIDAD para validar dicho acceso, 
#en caso de que no sea mayor, lo mandas para su casa.

consulta = int(input("¿Que edad tienes?: "))
if consulta >= 18:
    print(f"Bienvenido, tienes permitido el acceso")
else:
    print(f"Vete a tu casa menor de edad.")