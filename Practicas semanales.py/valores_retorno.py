# # # Valores de retorno sentencia return
# # def area(**dato):
# #     """
# #     calcaula el area de un afigurageométrica y la imprime en la pantalla
# #     """ #Docstring

# #     # Si el diccionario tiene una clave llamda "figura" evalua el valorr de la clave
# #     if dato["figura"]== "Rectangulo":
# #         return(dato["base"]*dato["altura"]) # Su el valor de la clave es "Rectangulo" imprime el valor de la clave "base"
# #     elif dato["figura"]== "Triangulo":
# #         return(dato["base"]*dato["altura"]/2) # Si el valor de la clave es "Triangulo" imprime el valor de la clave "base"
# #     elif dato["figura"]== "Círculo": 
# #         return(3.141593*dato["radio"]**2) # el valor de laclave es "Círculo" imprime el valor de la clave "radio" al cuadrado
# #     else:
# #         return("Figura desconocida") # el valor de la clave no es ninguna de las anteriores, imprime "Fugura desconocida"

# # #Ejemplo de llamda a la funcion
# # Triangulo = area(figura = "Triangulo", base = 10, altura = 5)
# # print(f"El área del triangulo es: {Triangulo}")
# # Círculo = area(figura ="Círculo", radio =10, color = "rojo")
# # print(f"El área del Círculo es: {Círculo}")
# # Dodecagono = area(figura = "Dodecagono", lado = 10)
# # print(f"El área del Dodecagono es: {Dodecagono}")


# # # def promedio(*numeros):
# # #     return sum(numeros) / len(numeros)

# # # x = promedio(4,5,6)
# # # print(x)
# ############################################################
# #Recursividad de funciones en python
# def factorial(numero) :
#     if numero == 0:
#         return 1
#     else:
#         return numero * factorial(numero - 1)
    
# print("El factorial de 0 es (0!):", factorial(0))
# print("El factorial de 1 es (1!):", factorial(1))
# print("El factorial de 3 es (3!):", factorial(3))

###############################################################
#Funciones lambda o funciones anonimas
# suma = lambda x, y : x + y
# print(suma("Hola", "Mundo"))
# print(suma(2,5))

# lista_numeros = [1, 0, -2]
# lista_numeros = sorted(lista_numeros, key = lambda n: abs(n))
# print(lista_numeros)

#############################################################
#funcion zip
paises = ["Kenia","Francia", "México", "Japón"]
capitales = ["Nairobi", "París", "Ciudad de México", "Tokio"]
poblacion = [54, 66, 130]

for i in zip(paises, capitales, poblacion):
    print(i)
    
