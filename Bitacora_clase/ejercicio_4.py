
# from random import randit 

# lista = []
# for i range (100):
#     lista.append(randit(50,90))
# conjunto  = set(lista)

# no_repetidos = list(conjunto)

# print(no_repetidos)



from random import randint

lista1 = []
lista2 = []

for i in range(100):
    lista1.append(randint(0,100))
    lista2.append(randint(50,150))
 
#Encntrar elementos comunes 
conjunto1 = set(lista1)
conjunto2 = set(lista2)
comunes = conjunto1.intersection(conjunto2)
lista_comunes = list(comunes)

