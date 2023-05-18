nombre_usuario = input('Ingrese su usuario: ')
v1 = float(input("ingrese v1: "))
v2 = float(input("ingrese v2: "))
v3 = float(input("ingrese v3: "))
sumatoria = v1+v2+v3
comision = sumatoria * 0.1
print(f'El usuario "{nombre_usuario}", posee una sumatoria de ${sumatoria}, con una comision de: ${round(comision,2)}')
