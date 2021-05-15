# Se tiene dos variables A y B, dichas variables se inicializan 
# de la siguiente manera 32 y 24. 
# Se desea hacer una comparación de, que variable es mayor. 
# Imprimir en pantalla: La variable A o B es mayor, La variable A o B es menor.

A, B = 24, 32

if A > B or B > A:
    print(f"La variable A o B es mayor")
else:
    print("La variable B o A es menor")