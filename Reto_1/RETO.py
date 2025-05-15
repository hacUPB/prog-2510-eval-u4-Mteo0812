import os               
import csv              
import matplotlib


def listar_archivos():
    ruta = input("Ingresa la ruta del archivo  (Presione enter para utlizar la ruta actual): ").strip()
    if not ruta: #Con la ayuda de la inteligencia artificial corregir errores de coherencia en este caso el if ruta==" " por un if not ruta:
    
        ruta = os.getcwd()
    if os.path.isdir(ruta):
        print("Archivos pertenecientes a la ruta: ")
        archivos= os .listdir(ruta)
        for archivo in archivos:
            print(archivo)
    else:
        print("Ruta no existente")
        
# Archivos .txt
def num_caracteres (nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo: #UTF-8 para caracteres especiales 
            texto = archivo.read() #Leer el archivo 
            palabras = texto.split()  # Se divide el texto en palabras
            total_caracteres = len(texto)
            sin_espacios = len(texto.replace(" ", "").replace("\n", "")) #Elimino todos los espacios 
            print(f"Número de palabras: {len(palabras)}")
            print(f"Número de caracteres (incluyendo espacios): {total_caracteres}") 
            print(f"Número de caracteres (sin espacios): {sin_espacios}")
    except:
        print("El archivo no se a encontrado")

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

def historigrama_vocales (nombre_archivo):
    try:
        with open(nombre_archivo,'r', encoding='utf-8') as archivo:
            texto = archivo.read().lower() #para leer y convertir todo en minuscula 
            vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
           

            for letra in texto:
                if letra in texto:
                    vocales[letra]= +1
            print ("Numero de ocurrecias de vocales: ")

            vol_hist = list(vocales.values())
            for vocal, frecuencia in vocales.items():
                print(f"{vocal.upper()}:{frecuencia}") #convertimos los caracteres en mayusculas para que muestre como se repiten


# creamos el histograma 
        plt.hist(vol_hist, bins=5,)
        plt.title('Histograma de ocurrencias de vocales')
        plt.xlabel('Vocales')
        plt.ylabel('Número de ocurrencias')
        plt.show()

    except :
        print(f"El archivo '{nombre_archivo}' no se encontró.")

