# Se desea saber si el número ingresado por el usuario, 
# está en el rango de 10 a 100. 
# En caso de que se encuentre en el rango, 
# imprimir en pantalla "El número si existe", caso contrario, "El número no existe"

numero = int(input("Ingrese un número: "))

if numero > 9 and numero <= 99:
    print(f"El número {numero} si existe")
else:
    print(f"El número {numero} no existe")