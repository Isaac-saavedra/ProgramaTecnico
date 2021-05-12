palabra: chr =""
producto = ""
monto: float = 0
total: float = 0
descuento = 0


while palabra.upper() != 'N':
    producto = input('ingrese nombre producto : ')
    monto = int(input('ingrese precio venta : '))
    total += monto
    palabra = input('Desea continuar (S/N ) ')

    print('Monto total de la compra: ', total)

    if total > 500:
        descuento = total * 0.20
        print('Descuento generado 20 : ', descuento)
    else:
        descuento = total * 0.05
        print('Descuento generado 5% : ', descuento)

    print('Total a pagar : ', total - descuento)  