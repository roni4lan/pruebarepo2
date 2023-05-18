import random

usuario = input("Ingrese un nombre de usuario.\n>")
num_ganador = random.randint(1, 100)
print(f"<=======  ¡Bienvenido {usuario}! =======>")

aux = 9
while aux > 0:
    num_usuario = input("Por favor, ingrese un número entero.\n>")
    if num_usuario.isdigit():
        num_usuario = int(num_usuario)
        aux -= 1
        print(f"Muy bien {usuario}. Este es tu intento Nº{aux}")
        if num_usuario > num_ganador:
            print("Pista: El numero ganador es más pequeño.")
        else:
            if num_usuario < num_ganador:
                print("Pista: El número ganador es mayor.")
            else:
                print("¡Felicitaciones, GANASTE!")
                print(
                    f"El número gandaor fué <{num_ganador}>, y {usuario} escogió el número <{num_usuario}>")
                break

    else:
        print("El numero que ingresó es invalido.")
