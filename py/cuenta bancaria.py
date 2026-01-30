#cuenta bancaria = titular , saldo ,  metodos .

contraseña = input("ingresa la contraseña de tu cuenta bancaria: ")


#decidi agregar un elif para el caso de que la contraseña sea incorrecta como en las apps de bancos

contraseña_correcta = "abc123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    contraseña = input("Ingresa la contraseña de tu cuenta bancaria: ")

    if contraseña == contraseña_correcta:
        print("Acceso concedido")
        print("entraste a tu cuenta bancaria")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta, intenta de nuevo")

if intentos == max_intentos:
    print("Demasiados intentos fallidos, tu cuenta ha sido bloqueada")


operaciones_disponibles = (input("¿Qué operación deseas realizar? (mostrar saldo, depositar, retirar): "))

class CuentaBancaria:
    def __init__(self, titular , saldo , numero_de_cuenta , contreseña):
        self.titular = titular
        self.saldo = saldo
        self.numero_de_cuenta =  numero_de_cuenta
        self.contreseña = contreseña

CuentaBancaria = CuentaBancaria("luis" , 1000 , "123456789" , "abc123")

if operaciones_disponibles == "mostrar saldo":
        print("el saldo de la cuenta es de:", CuentaBancaria.saldo)

elif operaciones_disponibles == "depositar":
     monto_a_depositar = float(input("ingresa el monto a depositar: "))
     CuentaBancaria.saldo += monto_a_depositar
     print("deposito exitoso. nuevo saldo:", CuentaBancaria.saldo)

elif operaciones_disponibles == "retirar":
        monto_a_retirar = float(input("ingresa el monto a retirar: "))
        if monto_a_retirar <= CuentaBancaria.saldo:
            CuentaBancaria.saldo -= monto_a_retirar
            print("retiro exitoso. nuevo saldo:", CuentaBancaria.saldo)
        else:
            print("fondos insuficientes para realizar el retiro.")
     
        