# #Creacion de listas
# numeros= [1, 2 , 3, 4, 5]
# Frutas= ["sandia", "manzana", "guayaba", "platano", "melon"]
# datos= ["pedro", 3, 3.8, True]

# print(datos[0])
# print(Frutas[4])
# print(numeros[-1])
# print(Frutas[-1])
# print(datos[-1])

# #para agregar un elemnto a las listas se utiliza append (ejemplo)
# Frutas.append("pera") 
# print(Frutas[-1])
# #para remover algun elemento utilizamos remove (ejemplo)
# Frutas.remove("pera")
# print(Frutas[-1])
# #Para recorrer listas para ver todos sus elementos se utiliza el ciclo for i (ejemplo)
# for i in Frutas:
#     print(i)
# for i in numeros:
#     print(i)

#Tuplas, se representan por parentecis y son inmutables a diferencia de las listas 
colores= ("rojo", "negro", "verde", "azul", "naranja")
numeros= (1, 2, 3, 4, 5,5, 6)
#para saber cuantos elementos existe en una tupla utilizamos la funcion len
print(len(colores))
print(len(numeros))
#la propiedad .count sirve para contar el numero de elementos repetidos en la lista o tupla (ejemplo)
print(numeros.count(5))


# numeros.count(1)
# print(numeros.count(1)) #para saber cuantas veces un elemento esta repetido dentro de la lista

# #Diccionarios llevan llaves 
# d1 = dict[ 
#     ("Alvaro","Aculco")
#     ("Carlos","Bogota")
#     ("Sergio","Guanajuato")
#     ("Josue","Guadalajara")
#     ("Elker","Monterrey")
#     ("Jose","Mexico")
# ]
# print(d1)


