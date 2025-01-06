#utilizamos la funcion "evaluar_longitud_palabra()" para determinar el numero de caracteres en una palabra
def evaluar_longitud_palabra():
#solicitamos a la persona que ingrese una palabra 
    palabra = input("Ingresa una palabra: ")
#medimos la longitud de la palabra ingresada
    longitud = len(palabra)
#si la palabra tiene de 4 a 8 caracteres, es correcta y se imprime el mensaje " La palabra es correcta"
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
#si la palabra tiene menos de 4 caracteres, es incorrecta y se imprime el mensaje "Hacen falta letras"
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
#si la palabra tiene mas de 8 caracteres, es incorrecta y se imprime el mensaje "Sobran letras "
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

#Volvemos a escribir la funcion, para ejecutar lo que se enuentra entre "evaluar_longitud_palabra()"
evaluar_longitud_palabra()