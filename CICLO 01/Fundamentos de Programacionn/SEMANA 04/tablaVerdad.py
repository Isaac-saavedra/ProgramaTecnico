a, b = True, False
#a = True
#b = False

print("Tabla de verdad de and")
print("-"*22)
print(b, b, b and b, sep = " \t ")
print(b, a, b and a, sep = " \t ")
print(a, b, a and b, sep = " \t ")
print(a, a, a and a, sep = " \t ")
print("")
print("Tabla de verdad de or")
print("-"*22)
print(b, b, b or b, sep = " \t ")
print(b, a, b or a, sep = " \t ")
print(a, b, a or b, sep = " \t ")
print(a, a, a or a, sep = " \t ")
print("")
print("Tabla de verdad de not")
print("-"*22)
print(b, not b, sep = " \t ")
print(a, not a, sep = " \t ")