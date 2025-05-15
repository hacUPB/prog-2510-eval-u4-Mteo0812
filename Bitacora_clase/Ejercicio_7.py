base_datos = { # variable global y lo que garnatiza es que se puede utlizar el todas las funciones 
    "usuario1": "contrasena1",
    "usuario2": "contrasena2",
    "usuario3": "contrasena3",
    "usuario4": "contrasena4",
    "usuario5": "contrasena5"
}

def login(usuario:str, contrasena: str): #si se creace una varible local en una funcion esa variable se destruye apenas se sale de la funcion 
    if usuario in base_datos:
        if contrasena == base_datos[usuario]:
            print("Ingreso exitoso")
            return True
        else:
           print("contraseña incorrecta")
           return False
    else:
        print("Usuario no registrado")
        return False


def main():
    contador = 0
    while contador < 3:
        user = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        if login(user,password):
            print("Acceso concedido")
            break
        else:
            contador += 1 
            if contador == 3:
                print("Muchos intentos fallidos ")
                break
    




if __name__ == "__main__":
    main()
