nombre_usuario = input('U1>Ingrese un nombre de usuario: ')
contrasena = input('U1>Ingrese una contraseña: ')

nombre_usuario2 = input("U2>Ingrese su nombre de usuario: ")
contrasena2 = input("U2>Ingrese su contraseña: ")
bool1 = True
while bool1:
    if nombre_usuario == nombre_usuario2:
        if contrasena == contrasena2:
            bool1 = False
            print('Usted ingresó correctamente.')
        else:
            print('Ingresó mal la CONTRASEÑA.')
            contrasena2 = input("\nU2>Ingrese su contraseña: ")
    else:
        print('Ingresó mal el USUARIO.')
        nombre_usuario2 = input("\nU2>Ingrese su nombre de usuario: ")
