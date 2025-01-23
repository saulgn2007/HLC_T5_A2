contraseña = "sercreta123"
intentos = 0
limite = 3

while intentos < limite:
    c = input("Introduce la contraseña: ")
    if c == contraseña:
        print("bienvendio a tu cuenta.")
        break
    else:
        intentos += 1
        print ("contraseña incorrecta, te quedan", limite - intentos, "intentos.")
        if intentos == limite:
            print("cuenta bloqueada.")
        