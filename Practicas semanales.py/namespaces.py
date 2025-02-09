#  Un namespaces es el espacio abstracto en el que viven los identificadores
# El ambito global es aquel en el que trabajamos desde que abrimos el interprete de Python
# El ambito local corresponde al espacio que se crea durante la ejecucion de una funcion.

#probando Ambitos

titulo = "Probando Ambitos"
suma = 10.5

def sumar() :
    suma -2 + 2
    print(titulo)
    print("Suma en ambito local",suma,id(suma))

print("Antes de llamar a la funcion")
print("Suma en ambito global",suma,id(suma))
sumar()
print("Despues de llamar a la funcion sumar")
print("Suma en ambito global",suma,id(suma))

