def main():
    # Crear numeros.txt con 10 numeros
    with open("numeros.txt","w") as archivo:
        archivo.write("10\n")
        archivo.write("20\n")
        archivo.write("15\n")
        archivo.write("30\n")
        archivo.write("25\n")
        archivo.write("8\n")
        archivo.write("12\n")
        archivo.write("18\n")
        archivo.write("22\n")
        archivo.write("14\n")

    # Leer y calcular promedio
    with open("numeros.txt","r") as archivo:
        lineas = archivo.readlines()

    suma = 0
    for num in lineas:
        suma = suma + int(num)

    promedio = suma / 10

    # Guardar resultado
    with open("resultado.txt","w") as archivo:
        archivo.write(f"El promedio es: {promedio}\n")

    print(f"El promedio es: {promedio}")

if __name__ == "__main__":
    main()