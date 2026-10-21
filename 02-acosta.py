archivo = open("nombres.txt", "w")

for i in range(5):
    nombre = input("Ingresa un nombre: ")
    archivo.write(nombre + "\n")

archivo.close()