'''
Formato de lista
lista_inmubeles=[
{'año': 2010, 'metros': 150, 'habitaciones': 4,
    'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2,
    'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4,
    'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3,
    'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2,
    'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
--------------------------------------------------------------------------------------------
- Agregar un inmueble
- Editar un inmueble
- Eliminar un inmueble
- Cambiar el estado del inmueble
- Buscar un inmueble segun mi presupuesto (buscar dpto <= al precio mio)
    >def search(lista_inmuebles, mipresupuesto):
    >   return nueva_lista
    >La nueva_lista debe contener los inmubeles con precio menor o igual a mi presupuesto.
    >
--------------------------------------------------------------------------------------------
Reglas de validación
 Inmuebles solo de zona: A, B o C.
 Inmuebles con estado: Disponible, Reservado o Vendido.
 No opera con inmuebles:
 Anteriores al año 2000.
 Menores de 60 metros cuadrados.
 Menores de 2 habitaciones.
--------------------------------------------------------------------------------------------
Reglas de precio
 Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
 Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
 Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2





(EJEMPLO)
claro, yo lo hice asi:

print("*** Bienvenidos a tu Software de Gestion Inmobiliaria ***")
while menu != 9:
print("MENU:")
print('1 - Ver propiedades')
print('2 - Agregar propiedad')
print('3 - Editar propiedad')
print('4 - Borrar propiedad')
print('5 - Buscar propiedades segun presupuesto')
print('9 - Salir\n')
menu = int(input('Ingrese una opcion: '))

'''


# LISTA PRE CARGADA
lista_inmubeles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4,
     'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2,
     'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4,
     'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3,
     'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2,
     'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
# ================DEFINICION DE FUNCIONES================


# Funcion para Agregar un inmueble.
def agregar(lista_inmuebles, nuevo_inmueble):
    lista_inmuebles.append(nuevo_inmueble)


# prueba
agregar(lista_inmubeles, {'año': 2010, 'metros': 56, 'habitaciones': 4,
        'garaje': True, 'zona': 'C', 'estado': 'Disponible'})
print(f'Se agrgo:\n{lista_inmubeles[5]}')


# Funcion para Editar un inmubele.


def modificar(lista_inmuebles, indice, inmueble_editado):
    if indice < len(lista_inmuebles):
        lista_inmuebles[indice] = inmueble_editado

    else:
        print(
            f"No es posible editar, por que el índice [{indice}], no existe.")


# prueba
modificar(lista_inmubeles, 5, {'año': 2011, 'metros': 56,
          'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'})
print(f'Se editó:\n{lista_inmubeles[5]}')

# Funcion para Eliminar un inmueble.


def eliminar(lista_inmuebles, indice):
    if indice < len(lista_inmuebles):
        del lista_inmuebles[indice]

    else:
        print("El índice está fuera de rango.")


# Funcion Cambiar Estado del inmueble.


def estado(lista_inmuebles, indice, nuevo_estado):
    if indice < len(lista_inmuebles):
        lista_inmuebles[indice]['estado'] = nuevo_estado
    else:
        print("El índice está fuera de rango.")


# prueba
estado(lista_inmubeles, 5, 'Reservado')
print(f'Se cambio el estado del inmueble:\n{lista_inmubeles[5]}')

# FUNCION CALCULO DE PREICOS
#  Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
#  Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
#  Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2


def calculo_precio(lista_inmuebles, indice):
    antiguedad = 2023 - lista_inmubeles[indice]['año']
    if lista_inmubeles[indice]['zona'] == 'A':
        if lista_inmubeles[indice]['garaje']:
            precio = (lista_inmuebles[indice]['metros']*100 + lista_inmuebles[indice]
                      ['habitaciones']*500 + 1500) * (1 - antiguedad/100)
        else:
            precio = (lista_inmuebles[indice]['metros']*100 +
                      lista_inmuebles[indice]['habitaciones']*500) * (1 - antiguedad/100)

    if lista_inmubeles[indice]['zona'] == 'B':
        if lista_inmubeles[indice]['garaje']:
            precio = (lista_inmuebles[indice]['metros']*100 + lista_inmuebles[indice]
                      ['habitaciones']*500 + 1500) * (1 - antiguedad/100) * 1.5
            print(f"ESTAMOS ACA")
        else:
            precio = (lista_inmuebles[indice]['metros']*100 + lista_inmuebles[indice]
                      ['habitaciones']*500) * (1 - antiguedad/100) * 1.5

    if lista_inmubeles[indice]['zona'] == 'C':
        if lista_inmubeles[indice]['garaje']:
            precio = (lista_inmuebles[indice]['metros']*100 + lista_inmuebles[indice]
                      ['habitaciones']*500 + 1500) * (1 - antiguedad/100) * 2
        else:
            precio = (lista_inmuebles[indice]['metros']*100 + lista_inmuebles[indice]
                      ['habitaciones']*500) * (1 - antiguedad/100) * 2
    return precio


# prueba calculo precio
print(calculo_precio(lista_inmubeles, 0))
