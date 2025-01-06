#EJERCICIO PARA CALMAR LA ANSIEDAD
#Mensaje de bienvenida
print("Bienvenido a tu acompañamiento durante este proceso de ansiedad")
print("Vamos a enumerar cosas que pueden percibir tus sentidos")
#Creacion de listas, para que ahi se almacenen los elementos
#5 cosas que se puedan ver
#4 cosas que puedas escuhar
#3 cosas que puedas saborear
#2 cosas que puedas oler 
#1 cosa que puedas tocar
vista =[]
oido =[]
gusto =[]
olfato =[]
tacto =[]

#pedir al usuario las cosas para cada sentido
print("piensa en 5 cosas que puedes ver")
for i in range(5):
    item = input(f"elemento{i+1}:")
    vista.append(item)

print("\nPiensa en 4 cosas que puedas oir")
for i in range(4):
    item = input(f"elemento {i+1}:")
    oido.append(item)

print("\nPiensa en 3 cosas que puedas saborear")
for i in range(3):
    item = input(f"elemento {i+1}:")
    gusto.append(item)

print("\nPiensa en 2 cosas que puedas oler")
for i in range(2):
    item = input(f"elemento {i+1}:")
    olfato.append(item)

print("\nPiensa en 2 cosas que puedas tocar")
for i in range(1):
    item = input(f"elemento {i+1}:")
    tacto.append(item)