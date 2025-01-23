def adivinanzas():
    import random
    numero = random.randint(1, 50)

    while True:
            intento = int(input("Adivina el número: "))
            if intento == numero:
                print("¡Correcto!")
                break
            elif intento < numero:
                print("Demasiado bajo")
            else:
                print("Demasiado alto")
adivinanzas()