num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El número mayor es: ", num1)
elif num2 > num1 and num2 > num3:
    print("El número mayor es: ", num2)
else:
    print("El número mayor es: ", num3)

if num1==num2:
    print("El número 1 y el número 2 son iguales")
elif num1==num3:
    print("El número 1 y el número 3 son iguales")
elif num2==num3:
    print("El número 2 y el número 3 son iguales")
else:
    print("Todos los números son iguales")