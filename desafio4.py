'''
Formato de lista
lista_inmubeles=[
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
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
