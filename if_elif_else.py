# segun el clima voy a salir a correr o me voy a quedar en casa

clima = input(
    'Ingrese como se encuentra el clima.\nEscriba si está "Soleado" o si está "Lluvioso".\n>')
if (clima.lower() == 'soleado'):
    print('Puedes salir a correr.')
elif (clima.lower() == 'lluvioso'):
    print('Esta lloviendo!')
else:
    print('quedate en casaaa')
