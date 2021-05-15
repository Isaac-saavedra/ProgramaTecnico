# Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
# Considerar el caso en que ambos son iguales.

a = int(input("Ingresa un número: "))
b = int(input("Ingresa un número: "))

if a<b:
    print(f"El número {a} es menor")
elif a == b:
    print(f"El número {a} y {b} son iguales")
else:
    print(f"El número {b} es menor")