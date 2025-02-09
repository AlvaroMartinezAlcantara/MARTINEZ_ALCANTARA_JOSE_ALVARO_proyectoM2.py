# Parámetros de tipo tupla, *args

# def promedio(*numeros):
#     """
#     Recibe una cantidad variable de valores numéricos como argumentos
#     y calcula e imprime su promedio.
#     """
#     promedio = sum(numeros) / len(numeros)
#     print("El promedio es:", promedio)

# # Llamadas de ejemplo
# promedio(4)
# promedio(4, 5, 6)
# promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)

# def es_numero(titulo, *serie) :
#     """
#     Imprime un titulo
#     verifica si el caracter en el parametro de tipo tupla es un numero o no
#     """
#     print(titulo)
#     for i in serie:
#         if type(i) == int or i.isdigit():
#             print (f"{i} es numero")
#         else:
#             print(F"{i} no es numero")

# # es_numero("Numero", "1", "2", "3")
# # es_numero("Letras", "a", "b", "c")

# nombre = "Mezcla"
# lista_varios = ["a", "2", 3, "f", 5]
# es_numero(nombre, *lista_varios)

#Parámetros tipo diccionario **kwargs
def area(**dato):
    """
    calcaula el area de un afigurageométrica y la imprime en la pantalla
    """ #Docstring

    # Si el diccionario tiene una clave llamda "figura" evalua el valorr de la clave
    if dato["figura"]== "Rectangulo":
        print(dato["base"]*dato["altura"]) # Su el valor de la clave es "Rectangulo" imprime el valor de la clave "base"
    elif dato["figura"]== "Triangulo":
        print(dato["base"]*dato["altura"]/2) # Si el valor de la clave es "Triangulo" imprime el valor de la clave "base"
    elif dato["figura"]== "Círculo": 
        print(3.141593*dato["radio"]**2) # el valor de laclave es "Círculo" imprime el valor de la clave "radio" al cuadrado
    else:
        print("Figura desconocida") # el valor de la clave no es ninguna de las anteriores, imprime "Fugura desconocida"

area(figura = "Triangulo", base = 10, altura = 5)
area(figura ="Círculo", radio =10, color = "rojo")
area(figura = "Dodecagono", lado = 10)

