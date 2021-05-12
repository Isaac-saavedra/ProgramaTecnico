num = int(input("Numero: "))
#cifras = num
if num > 99:
    print ("El numero supera las 2 cifras")
    
elif num < 10:
    print("Le falta ", 10-num, "para 2 cifras")
     
else:
    print("Le falta ", 100-num, "para 3 cifras")
        

