pago_diario = 50

total_horas = int(input('Ingrese total horas: '))
    

if total_horas >= 8:
    if total_horas == 8:
        print("Tu pago es:  S/. ", pago_diario)
    elif total_horas == 9:  # 1 HORA
        print("Tu pago es:  S/. ", pago_diario + (pago_diario * 0.1))
    elif total_horas == 10:  # 2 HORAS
        print("Tu pago es:  S/. ", pago_diario + (pago_diario * 0.3))
    elif total_horas == 11:  # 3 HORAS
        print("Tu pago es:  S/. ", pago_diario + (pago_diario * 0.4))
    elif total_horas == 12:  # 4 HORAS
        print("Tu pago es:  S/. ", pago_diario + (pago_diario * 0.6))
    elif total_horas == 13:  # 5 HORAS
        print("Tu pago es:  S/. ", pago_diario + (pago_diario * 0.8))
else:        
    if total_horas >= 3:
        print("Tu pago es:  S/. ", pago_diario - (pago_diario * 0.25))
    elif total_horas >= -2:
        print("Tu pago es:  S/. ", pago_diario - (pago_diario * 0.75))