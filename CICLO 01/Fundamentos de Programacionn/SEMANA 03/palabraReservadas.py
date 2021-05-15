import keyword

print("En caso exista la palabra reservada, arroja True")
print(keyword.iskeyword('as'))
print("En caso no exista la palabra reservada, arroja False")
print(keyword.iskeyword('x'))
print("Mostrar todas las palabras reservadas:")
print(keyword.kwlist)