# Solicitud de datos personales
print("Para determinar su IMC, favor de completar el siguiente formulario :")
nombre=input("Introduce tu nombre: ")
apellido_paterno=input("Introduce tu apellido Paterno: ")
apellido_materno=input("Introduce tu apellido Materno: ")

# Solicitud de datos numéricos con validación
peso=float(input("Introduce tu peso en Kilogramos: "))
edad=int(input("Introduce tu edad: "))
estatura=float(input("Introduce tu estatura en metros: "))

# Cálculo del IMC
IMC = peso / estatura**2

# Impresión de los resultados
print("Nombre: " + nombre)
print("Apellido Paterno: " + apellido_paterno)
print("Apellido Materno: "+ apellido_materno)
print("Peso: "+ str(peso) + "kilogramos")
print("Estatura: "+ str(estatura) + "metros")
print("Edad: " + str(edad) + "años")
print("IMC: " + str(IMC) )

if IMC >= 0 and IMC <= 15.99:
    print("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
    print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
    print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
    print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
    print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
    print ("obesidad media")
elif IMC >= 40.00:
    print ("obesidad morbida")