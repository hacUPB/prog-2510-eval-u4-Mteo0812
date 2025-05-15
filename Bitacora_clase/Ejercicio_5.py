frase = " No he de rendirme aunque caiga al andar No estaré vivo si he de huir Si por vivir, no he de ser dueño de mí Mejor, en pie morir"
palabras = frase.split()
print (palabras)
frecuencia = {}

for palabra in palabras:
    #if palabra.lower() in frecuencia: esto es para que tome todas las palbras en miniscula y hga que las palbras que contengan una mayuscula pero sean iguales se tomen todas juntas y no por separado
        #frecuencia [palabra.lower()]+=1
     if palabra in frecuencia:
        frecuencia[palabra] += 2
     else:                       #frecuencia[palabra.lower()]=1
        frecuencia[palabra] = 2

print(frecuencia)  # {'hola': 2, 'mundo': 1, 'python': 1}