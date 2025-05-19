import os
import csv
import matplotlib.pyplot as plt

def listar_archivos():
    ruta = input("Ingresa la ruta del archivo  (Presione enter para utilizar la ruta actual): ").strip()
    if not ruta:
        ruta = os.getcwd()
    if os.path.isdir(ruta):
        print("Archivos pertenecientes a la ruta: ")
        archivos = os.listdir(ruta)
        for archivo in archivos:
            print(archivo)
    else:
        print("Ruta no existente")

# FUNCIONES PARA ARCHIVOS .TXT

def num_caracteres(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            palabras = texto.split()
            total_caracteres = len(texto)
            sin_espacios = len(texto.replace(" ", "").replace("\n", ""))
            print(f"Número de palabras: {len(palabras)}")
            print(f"Número de caracteres (incluyendo espacios): {total_caracteres}")
            print(f"Número de caracteres (sin espacios): {sin_espacios}")
    except:
        print("El archivo no se ha encontrado.")

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
    except:
        print("Archivo no encontrado.")


def histograma_vocales(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read().lower()
            vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

            for letra in texto:
                if letra in vocales:
                    vocales[letra] += 1

            print("Número de ocurrencias de vocales:")
            for vocal, frecuencia in vocales.items():
                print(f"{vocal.upper()}: {frecuencia}")

            # Creamos una lista expandida para plt.hist
            datos_histograma = []
            for vocal, cantidad in vocales.items():
                datos_histograma.extend([vocal] * cantidad)

            # Graficar histograma
            plt.hist(datos_histograma, bins=len(vocales), edgecolor='black')
            plt.title('Histograma de ocurrencias de vocales')
            plt.xlabel('Vocales')
            plt.ylabel('Frecuencia')
            plt.show()

    except:
        print(f"El archivo '{nombre_archivo}' no se encontró.")

def submenu_txt():
    nombre_archivo = input("Nombre del archivo de texto (.txt): ")
    while True:
        print("\n--- Submenú para archivos .txt ---")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de las vocales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            num_caracteres(nombre_archivo)
        elif opcion == "2":
            reemplazar_palabra(nombre_archivo)
        elif opcion == "3":
            histograma_vocales(nombre_archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# FUNCIONES PARA ARCHIVOS .CSV

def mostrar_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            contador = 0
            for fila in lector:
                print(fila)
                contador += 1
                if contador == 15:
                    break
    except:
        print("Archivo no encontrado.")

def calcular_estadisticas(nombre_archivo):
    columna = input("Nombre de la columna numérica a analizar: ")
    try:
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = []
            for fila in lector:
                if fila[columna].replace('.', '', 1).isdigit():
                    datos.append(float(fila[columna]))
        if datos:
            datos.sort()
            total = len(datos)
            promedio = sum(datos) / total
            mediana = datos[total // 2] if total % 2 != 0 else (datos[total // 2 - 1] + datos[total // 2]) / 2
            print(f"Total de datos: {total}")
            print(f"Promedio: {promedio}")
            print(f"Mediana: {mediana}")
            print(f"Valor máximo: {max(datos)}")
            print(f"Valor mínimo: {min(datos)}")
        else:
            print("No se encontraron datos numéricos válidos.")
    except:
        print("Archivo no encontrado o columna inválida.")

def graficar_columna(nombre_archivo):
    columna = input("Nombre de la columna numérica a graficar: ")
    try:
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = []
            for fila in lector:
                if fila[columna].replace('.', '', 1).isdigit():
                    datos.append(float(fila[columna]))
        if datos:
            plt.plot(datos, marker='o')
            plt.title(f"Gráfica de la columna '{columna}'")
            plt.xlabel("Índice")
            plt.ylabel(columna)
            plt.grid(True)
            plt.show()
        else:
            print("No se encontraron datos numéricos válidos.")
    except:
        print("Archivo no encontrado o columna inválida.")

def submenu_csv():
    nombre_archivo = input("Nombre del archivo .csv: ")
    while True:
        print("\n--- Submenú para archivos .csv ---")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_csv(nombre_archivo)
        elif opcion == "2":
            calcular_estadisticas(nombre_archivo)
        elif opcion == "3":
            graficar_columna(nombre_archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# MENÚ PRINCIPAL

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Listar archivos en un directorio")
        print("2. Trabajar con archivo .txt")
        print("3. Trabajar con archivo .csv")
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
            print("Opción no válida.")

main()

#Notas:
# - se utilizo la inteligencia arcitificial para la correcion de errores en las funciones calcular estaidisticas en la linea 123 ya que no se estaba validando si el valor era un numero o no
# - tambien se utilizo la inteligencia artificial para validar si el uso del if era correcto y nos corrijio que era mejor utilizar el if not en la primera funcion
# - Por motivos de un error en la configuracion del pip.py no se pudo instalar la libreria matplotlib, por lo que no se pudo probar la funcion de graficar, pero se dejo el codigo para que funcione al momento de instalar la libreria
# y por medio de la intelegencia artifical se verifico que el codigo funcioana acarde a lo solicitado en la actividad
# - Se adjuntaron tambien los archivos csv y txt para que se pueda probar el funcionamiento del programa, pero por motivos de el error no se pudo verificar la funcionalidad de forma local 
