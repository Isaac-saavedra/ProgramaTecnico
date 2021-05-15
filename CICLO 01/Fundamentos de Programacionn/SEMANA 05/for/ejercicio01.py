#  Escribir un programa que pida al usuario una palabra y la muestre 10 veces por pantalla.

palabra = input("Ingrese una palabra: ")

for x in range(1,11):
    print("[",x,"] ", palabra)