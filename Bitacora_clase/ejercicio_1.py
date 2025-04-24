Matriz = [[1,4,6,8,3],[8,9,12,54,47],[98,45,78,3,10]]
print(Matriz)

fil = len(Matriz)
col = len(Matriz[0])

for i in range(fil): #Indice de las filas  generado los numero 0 1 y 2 
    for j in range(col): # Indice de las columnas genera los indices 
        print(f"{Matriz[i][j]:3}", end='    ')
    print()
    

