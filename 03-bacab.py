archivo = open("nombres.txt", "r")

nombres = archivo.readlines()

archivo.close()

print("Lista de nombres:")

for nombre in nombres:
    print(nombre.strip())

print("Total de nombres:", len(nombres))