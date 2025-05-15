# Lista global para almacenar los diccionarios de personas
personas = []

def agregar_persona(nombre: str, edad: int, ciudad:str): #str: letras int:numero entero
    persona = {
        'nombre': nombre,
        'edad': edad,
        'ciudad': ciudad
    }
    personas.append(persona)

def main():
    name = input("Ingrese el nombre: ")
    age = int(input("ingresa la edad: "))
    city = input("Ingrese la ciudad: ")

    agregar_persona(name, age,  city)
    agregar_persona("Juan", 18, "Medellin")
    print(f"Dccionario: {personas[0]}")
    print(f"Persona: {personas[1]["nombre"]}")


    for usuario in personas:
        if usuario["edad"] > 18:
            print(usuario["nombre"])
    
    for usuario in personas:
        if usuario ["ciudad"] == "Medellin":
            print(usuario ["nombre"])

if __name__ == "__main__ ":
    main()