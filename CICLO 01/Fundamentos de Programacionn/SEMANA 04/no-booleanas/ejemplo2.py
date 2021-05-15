numero = int(input("Escriba un número: "))
print("Primera comparación")
print(f"Valor es: {numero % 2}")
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
print("")
print("Segunda comparación")
print(f"Valor es: not {bool(numero % 2)}")
print(f"Valor es: {not numero % 2}")


if not numero % 2:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")