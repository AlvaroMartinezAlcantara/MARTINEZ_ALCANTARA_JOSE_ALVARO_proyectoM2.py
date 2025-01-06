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
