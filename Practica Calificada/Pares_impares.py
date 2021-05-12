tot_par = 0
tot_impar = 0
i = 1

while i <= 100:
    if (i % 2 == 1):  
        tot_impar += i

    else:
        tot_par += i
        i += 1
        
        print('Suma total  numeros pares: ', tot_par)
        #print('Suma total numeros impares: ', tot_impar)
        #print('Suma total numeros pares e impares: ', tot_impar + tot_par)