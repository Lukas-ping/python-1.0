def validar_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

clave = input("ingresa una contraseña: ")

if validar_password(clave):
    print("contraseña valida")
else:
    print("contraseña demasiado corta")
