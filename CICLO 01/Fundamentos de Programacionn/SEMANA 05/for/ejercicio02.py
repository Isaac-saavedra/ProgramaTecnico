# Realizar la tabla de verdad
booleanos = [False, True]

print("="*22)
print("Tabla de verdad de and")
print("="*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep="\t")

print("="*22)
print("Tabla de verdad de or")
print("="*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep="\t")

print("="*22)
print("Tabla de verdad de not")
print("="*22)
for x in booleanos:
    print(x, not x, sep="\t")