#Utilizar al menos dos funciones
#Preguntar cuantos alumnos se registraran, en caso de ingresar una cantidad, se asume que se registraran 3 alumnos
# Preguntar el nombre y dos calificaciones.
# Mostrar el nombre en pantalla con inicial mayuscula y proimedio
# Al finalizar el programa se mostrara una lista con el nombre de cada alumno y sus calificaciones

def captura_alumnos(numero = 3) :
    """
    Registra alumnos y dos calificaciones
    Recibe como parámetro la cantidad de alumnos a registrar
    Si no se especificael numero de alumnos, se registraran 3
    """
    lista_alumos = []
    for i in range(numero) :
        nombre = input(f'{i +1}. -Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificacion de {nombre} : "))
        calificacion2 = int(input(f"Ingrese la segunda calificacion de {nombre} : "))
        lista_alumos.append([nombre, calificacion1, calificacion2])
    print("Las calificaciones de los alumnos son:", lista_alumos)

def promedio(nombre, calificacion1, calificacion2) :
    """
    calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recibe como parámetros el nombre y dos calificaciones del alumno
    """

numero_alumnos = input("cuantos alumnos desea registar")

if numero_alumnos.isdigit() :
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else :
    captura_alumnos()


