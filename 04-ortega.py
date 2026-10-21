def main():
    # 1. Crear numeros.txt con los números del 1 al 10 (uno por línea)
    with open("numeros.txt", "w") as archivo:
        for n in range(1, 11):
            archivo.write(f"{n}\n")

    # 2. Leer el archivo
    with open("numeros.txt", "r") as archivo:
        lineas = archivo.readlines()

    # 3. Calcular el promedio
    suma = 0
    for linea in lineas:
        suma = suma + int(linea)

    promedio = suma / len(lineas)

    # 4. Guardar el resultado en resultado.txt
    with open("resultado.txt", "w") as archivo:
        archivo.write(f"El promedio es: {promedio}\n")

    print(f"El promedio es: {promedio}")


if __name__ == "__main__":
    main()