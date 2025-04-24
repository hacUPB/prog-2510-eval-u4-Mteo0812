usuarios = {
    "user1": {"nombre": "Ana", "edad": 25},
    "user2": {"nombre": "Luis", "edad": 30}
}

print(usuarios["user1"]["edad"])
#Crear nombre y edad del usuario y agregarlo al diccionario 
usuario_nuevo = {
"user3" : {"Nombre": "edad"}
}
nombre  = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

usuario_nuevo["nombre"] = nombre
usuario_nuevo["edad"] = edad

usuarios["user3"] = usuario_nuevo
print(usuarios)