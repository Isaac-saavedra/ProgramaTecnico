# Se desea saber si el número ingresado es múltiplo de 3 y 10, 
# caso contrario que imprima en pantalla, no encuentro múltiplos de 3 y 10

numero = int(input("Ingrese un número: "))

if numero % 3 == 0:
    print(f"El número {numero} es múltiplo de 3")
elif numero % 10 == 0:
    print(f"El número {numero} es múltiplo de 10")
else:
    print("No encuentro múltiplos de 3 y 10")    