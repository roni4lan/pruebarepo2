# import random
# print(random.randint(1, 33))

print("===============================\nFactorial Numero")


def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


print(factorial(2))


print("===============================\nInvertir Lista")


def invertir_lista(lista):
    nueva_lista = []
    for elemento in reversed(lista):
        nueva_lista.append(elemento)
    return nueva_lista


print(invertir_lista(['a', 'b', 'c', 0, 1, 2]))


print("===============================\nBuscar Palabra")

var = ''


def buscar_palabra(lista, objetivo):
    var = objetivo
    for palabra in lista:
        if palabra == objetivo:
            return True
    return False


buscar_palabra(['hola', 'chau', 'bienvenido'], 'chau')
print('>>>>>', var)
# print(f'Se encontró la palabra {} en la lista.')
