def dibuja ():
    num_estrellas = int(input("Introduce el número de estrellas: "))
    contador = 1
    estrellas = "★"
    for index in range(num_estrellas):
        print(estrellas + contador)
        contador += 1