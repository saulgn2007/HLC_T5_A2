num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
num3 = input("Introduce el tercer número: ")

if num1 > num2 and num1 > num3:
    print("El número mayor es: ", num1)
elif num2 > num1 and num2 > num3:
    print("El número mayor es: ", num2)
elif num3 > num1 and num3 > num2:
    print("El número mayor es: ", num3)
else:
    print("Hay números que son iguales")