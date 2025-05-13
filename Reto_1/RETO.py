import os               
import csv              
import matplotlib 

def listar_archivos():
    ruta = input("Ingresa la reuta del archivo a utlizar (Presione enter si desea quedarse en esta ruta): ").strip()
    if not ruta:
        ruta = os.getcwd() #REcordar que se pone el not para verificar que si este vacio y solo asi se utiliza los soguiente de la linea 
    if not os.path.isdir(ruta):
        
