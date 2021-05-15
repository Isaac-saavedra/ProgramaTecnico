# Se desea elaborar una calculadora simple, 
# que imprima en pantalla 
# EL OPERADOR ES: [OPERADOR] 
# RESULTADO ES: [RESULTADO]

operador = input("Ingrese el operador: ")
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))

if operador == "+":
    resultado = a + b
elif operador == "-":
    resultado = a - b
elif operador == "*":
    resultado = a * b
elif operador == "/":
    resultado = a / b
else:
    print("No encuentro ese operador")
    exit()

print(f"OPERADOR: {operador}")
print(f"RESULTADO: {resultado}")