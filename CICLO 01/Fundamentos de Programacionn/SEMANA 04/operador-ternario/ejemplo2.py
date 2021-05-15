a, b = 100, 0
c = (a/b if b!=0 else -1)
print("Primer método")
print(f"Mensaje: {c}")
print("")

print("Segundo método")
if b!=0:
    print(a/b)
else:
    print(f"Mensaje: -1")