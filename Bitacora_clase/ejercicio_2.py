

filas = 2
columnas = 3
lista = []

for i in range (filas):
    lista.append([]) 
    for j in range(columnas):
        n = int(input("ingrese un valor: "))
        lista[i].append(n) 
print (lista)