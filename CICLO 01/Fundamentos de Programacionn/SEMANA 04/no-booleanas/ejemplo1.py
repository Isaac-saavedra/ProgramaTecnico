numero = int(input("Escriba un número: "))

print("Primera comparación")
print(f"Valor es: {numero % 2}")
print("")
if numero % 2 != 0:
    print(f"{numero} es impar")
else:
    print(f"{numero} es par")

print("")
print("Segunda comparación")
print(f"Valor es: {bool(numero % 2)}")
print("")

if numero % 2:
    print(f"{numero} es impar")
else:
    print(f"{numero} es par")