

from random import randint

fila = 5
columnas = 12 
ventas_anio = [] # Para guardar las ventas por año
lista = []
for i in range(fila):
    for j in range(columnas):
        lista.append([])
        n = randint(0,30)
        lista[i].append(n)

for i in range(fila):
    for j in range(columnas):
        print(f"{lista[i][j]:4}", end=' ')
    print()
# generamos los indices de las filas 
#con lo que esta acontinuacion lo utlizamos para que vaya fila por fila, los sume, los guarde en una variable y lo agregue en una lista vacia
for f in range(fila):
    total_anio = (sum(lista[f]))
    ventas_anio.append(total_anio)
# impirmo, calculo el mayor, luego utlizampos el valor y calculamos el indice ( ubicacion) y lo imprimimos con un condiconal, en este caso apartir del año 2020 en adelante
print(ventas_anio)
mayor = max(ventas_anio)
print(mayor)
indice = ventas_anio.index(mayor)
print(f"El año de mayor ventas fue: ! {2020+indice} ¡")

    

