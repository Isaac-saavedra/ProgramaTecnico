#Booleanos
a = False
b = True
print("La variable a es: ",type(a))
print("La variable b es: ",type(b))
print("")
#Convertir a booleano
c = "False"
print("La variable c fue: ", type(c))
#print("La variable d fue: ", type(d))
c = bool(c)
d = bool(c)
print("")
print("La variable c es: ",type(c))
print("La variable d es: ",type(d))
print("")
e = 1 # Si es 0 arroja False, pero si es 1 arroja True
e = bool(e)
print("La variable e es: ", type(e))
print("La variable e contiene: ", e)
print("")
f = "" #Si la variable está vacía arroja un False, caso contrario arroja un True
f = bool(f)
print("La variable f es: ", type(f))
print("La variable f contiene: ", f)