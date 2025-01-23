palabra = input("Introduce una palabra con alguno de los siguientes carácteres: @, #, $, % ")
caracter_especial = ['@', '#', '$', '%']
for caracter in caracter_especial:
    if caracter in palabra:
        print("La palabra contiene el símbolo.", caracter)
        break
else:
    print("La palabra no contiene ninguno de los carácteres especiales.")