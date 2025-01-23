def cuadrados():
    num_entero = int(input("Ingrese un número entero: "))
    if num_entero < 0:
        print("El número ingresado no es válido")
    else:
        cuadrado = [i**2 for i in range(1 , num_entero+1)]
        print(cuadrado)
cuadrados()
