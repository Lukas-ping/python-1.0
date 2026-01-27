#validador de edad / test 1

edad= int (input("¿cual es tu edad?"))

if edad >18:
    print ("sos mayor de edad")
elif edad == 18: 
    print ("sos de la misma edad")
    #en este punto tuve un pequeño error en "else" al no poner :
else:
    print("sos menor de edad")