fruta = ["manzana", "pera", "durazno", 'sandia']
print("Incrementando")
for indice, valor in enumerate(fruta, start=10):
    print(f"[{indice}] -> {valor}")

print("")
print("Disminuyendo")
tamaño = len(fruta)
for indice, valor in enumerate(fruta, start=10):
    print(f"[{indice-tamaño}] -> {valor}")

print("")

print("Mostrando indices pares")
for indice, valor in enumerate(fruta, start=1):
    if indice  % 2 == 0:
        print(f"[{indice}] -> {valor}")
    else:
        continue

print("Mostrando indices impares")
for indice, valor in enumerate(fruta, start=1):
    if indice  % 2 == 0:
        continue
    else:
        print(f"[{indice}] -> {valor}")