# calculadora basica / test 2

numero1 = float(input("ingresa el primer numero: "))
numero2 = float(input("ingresa el segundo numero: "))

operacion = input("elige una operacion ( + , - , * , / ): ")

#me di cuenta que me codigo tenia un error , el porblema se debia principalmente a un problema de indentación (espacios al principio de la línea).
if operacion == "+":
    resultado = numero1 + numero2
    print("el resultado es", resultado)

elif operacion == "-":
    resultado = numero1 - numero2
    print("el resultado es", resultado)

elif operacion == "*":
    resultado = numero1 - numero2
    print("el resultado es", resultado)

elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("el resultado es:", resultado)
    else:
        print("no se puede dividir por cero")

else:
    print("operacion no valida")