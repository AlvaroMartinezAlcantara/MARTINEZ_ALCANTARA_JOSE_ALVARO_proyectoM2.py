# # Programa que genera una contraseña de 8 caracteres a partir de 3 palabras dadas por el usuario

# palabra1 = input("Introduce la primera palabra: ")
# palabra2 = input("Introduce la segunda palabra: ")
# palabra3 = input("Introduce la tercera palabra: ")
# #Si la palabra es de menos de 2 caracteres, se rellena con X  
# if len(palabra1) < 2:
#     palabra1 = "X" + palabra1
# if len(palabra2) < 2:
#     palabra2 = "X" + palabra2
# if len(palabra3) < 2:
#     palabra3 = "X" + palabra3
# #Se genera la contraseña
# contraseña = palabra1[0] + palabra2[0] + palabra3[0] + palabra1[1] + palabra2[1] + palabra3[1]
# print("La contraseña es:", contraseña)

# # Se solicita contraseña al usuario
# # Si la contraseña es de menos caracteres informa cuántos faltan
# # Si la contraseña es de más caracteres informa cuántos sobran
# # Si la contraseña es correcta, informa que es correcta

# contraseña_usuario = input("Introduce la contraseña: ") # Se solicita contraseña al usuario
# if len(contraseña_usuario) < len(contraseña):
#     print("Faltan", len(contraseña) - len(contraseña_usuario), "caracteres")
# elif len(contraseña_usuario) > len(contraseña):
#     print("Sobran", len(contraseña_usuario) - len(contraseña), "caracteres")
# elif contraseña_usuario == contraseña:
#     print("Contraseña correcta")
# else:
#     print("Contraseña incorrecta")


#Proporciona funciones para interactuar con el sistema operativo y en este caso para pausar la ejecucion del programa al final.
import os 
#Se solicita a la persona que ingrese un valor para "x" convirtiendose en  valor entero
x = int (input ('Ingresa el valor de x: '))
#Se solicita a la persona que ingrese un valor para "y" convirtiendose en  valor entero
y = int (input ('Ingresa el valor de y: '))
#verificamos con condicional if si "x" e "y" son iguales a cero, entonces imprimimos como "Error" ya que los valores no deben ser 0
if x == 0 or y == 0:
    print("Error: Ninguna coordenada puede ser 0.")
#Con la condicional if determinamos si "X" e "Y" son  mayores que 0, pertenecen al cuadrante 1
if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
# Una vez que el programa no cumple el condicional if, sigue con elif donde si "x" es menor que 0, e "Y" es mayor que 0,pertenecen al cuadrante 2
elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
# Una vez mas que no se cumple la condicional elif, se sigue con otro elif, donde si "X" e "Y" son menores que 0, pertenecen al cuadrante 3
elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
# Una vez mas no se cumple la condicional elif, seguimos con otro elif, donde si "X" es mayor que 0, e "Y" menos que 0, pertenecen al cuadrante 4
elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")
# Pausa el programa para que la persona presione cualquier tecla antes de cerarr el programa.
os.system('pause')


