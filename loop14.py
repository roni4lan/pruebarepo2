numero = int(input("Ingresar un valor>"))
# for i in range(1, numero+1):
#     print(f"{str(i)*i}")

for i in range(1, numero+1):
    for j in range(i):
        print(i, end=" ")
    print("")
