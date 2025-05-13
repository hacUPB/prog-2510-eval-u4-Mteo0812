import os
import csv
import matplotlib.pyplot as plt

def listar_archivos():
    ruta = input("Ingrese la ruta (o presione Enter para usar la ruta actual): ").strip()
    if not ruta:
        ruta = os.getcwd()  
    if not os.path.isdir(ruta):
        print("La ruta no existe.")
        return
    print("\nArchivos en la ruta:", ruta)
    for archivo in os.listdir(ruta):
        print("- " + archivo)

# ======================
# Funciones para .TXT
# ======================

def contar_palabras_y_caracteres(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            palabras = texto.split()
            total_caracteres = len(texto)
            sin_espacios = len(texto.replace(" ", "").replace("\n", ""))
            print("Número de palabras:", len(palabras))
            print("Número de caracteres (incluyendo espacios):", total_caracteres)
            print("Número de caracteres (sin espacios):", sin_espacios)
    except FileNotFoundError:
        print("Archivo no encontrado.")

def reemplazar_palabra(nombre_archivo):
    palabra_antigua = input("Palabra a buscar: ")
    palabra_nueva = input("Palabra por la que se reemplazará: ")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        contenido = contenido.replace(palabra_antigua, palabra_nueva)
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        print("Reemplazo realizado con éxito.")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def histograma_vocales(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read().lower()
        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for letra in texto:
            if letra in vocales:
                vocales[letra] += 1
        print("Ocurrencia de vocales:", vocales)

        plt.bar(vocales.keys(), vocales.values(), color='orange')
        plt.title("Histograma de Vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Frecuencia")
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("Archivo no encontrado.")

# ======================
# Funciones para .CSV
# ======================

def mostrar_15_filas(nombre_archivo):
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            contador = 0
            for fila in lector:
                print(fila)
                contador += 1
                if contador >= 15:
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.")

def calcular_estadisticas_csv(nombre_archivo):
    columna_nombre = input("Nombre de la columna a analizar: ")
    datos = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                valor = fila.get(columna_nombre)
                if valor is not None and valor.replace(".", "", 1).replace("-", "", 1).isdigit():
                    datos.append(float(valor))

        if len(datos) == 0:
            print("No se encontraron datos numéricos en esa columna.")
            return

        total = len(datos)
        promedio = sum(datos) / total
        datos_ordenados = sorted(datos)
        mediana = datos_ordenados[total // 2] if total % 2 != 0 else (datos_ordenados[total // 2 - 1] + datos_ordenados[total // 2]) / 2
        print("Número de datos:", total)
        print("Promedio:", promedio)
        print("Mediana:", mediana)
        print("Máximo:", max(datos))
        print("Mínimo:", min(datos))

    except FileNotFoundError:
        print("Archivo no encontrado.")

def graficar_columna_csv(nombre_archivo):
    columna_nombre = input("Nombre de la columna numérica a graficar: ")
    datos = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                valor = fila.get(columna_nombre)
                if valor is not None and valor.replace(".", "", 1).replace("-", "", 1).isdigit():
                    datos.append(float(valor))

        if not datos:
            print("No se encontraron datos numéricos.")
            return

        plt.plot(datos, marker='o', linestyle='-', color='blue')
        plt.title("Gráfico de la columna: " + columna_nombre)
        plt.xlabel("Índice")
        plt.ylabel(columna_nombre)
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("Archivo no encontrado.")

# ======================
# Menús
# ======================

def submenu_txt():
    archivo = input("Ingrese el nombre del archivo .txt: ")
    while True:
        print("\n--- Submenú TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            contar_palabras_y_caracteres(archivo)
        elif opcion == "2":
            reemplazar_palabra(archivo)
        elif opcion == "3":
            histograma_vocales(archivo)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def submenu_csv():
    archivo = input("Ingrese el nombre del archivo .csv: ")
    while True:
        print("\n--- Submenú CSV ---")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas")
        print("3. Graficar una columna")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_15_filas(archivo)
        elif opcion == "2":
            calcular_estadisticas_csv(archivo)
        elif opcion == "3":
            graficar_columna_csv(archivo)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# ======================
# Función principal
# ======================

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Listar archivos en ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
