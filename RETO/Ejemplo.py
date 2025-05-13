#solicitamos al ususario el nombre del archivo a crea 
nombre_archivo = input("Ingrese el nombre del archivo: ")
nombre_archivo += ",txt"
print(nombre_archivo)


#usamos with para crear el contetxto y escribir datos en le archivo 
with open(nombre_archivo,'w') as archivo:
    #solicitamos al usuario los datos a escribir en el archivo 
    datos = input("Ingrese su nombre: ")
    try:
        edad = int(input("Ingrese su edad: "))  
        archivo.write(str(edad)+ "\n")
        archivo.write("\n")
    except ValueError:
        print ("Tipo de dato equivocado ")
        
    try:
        estatura = float(input("Ingrese su estatura: "))
        archivo.write(str(estatura)+ "\n")
    except ValueError:
        print ("Tipo de dato equivicado")
    archivo.write(datos)
    
  
    
