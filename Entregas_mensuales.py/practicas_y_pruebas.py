# def verificar_longitud_palabra():
#     palabra = input("Ingresa una palabra: ").strip()  # Elimina espacios adicionales
#     longitud = len(palabra)

#     if 4 <= longitud <= 8:
#         print("La palabra es correcta.")
#     elif longitud < 4:
#         print(f"Hacen falta letras. Solo tiene {longitud} letras.")
#     else:
#         print(f"Sobran letras. Tiene {longitud} letras.")

# # Ejecutar la función
# verificar_longitud_palabra()

def verificar_longitud_palabra_con_estructuras():
    # Lista de mensajes predeterminados
    mensajes = [
        "La palabra es correcta.",
        "Hacen falta letras. Solo tiene {longitud} letras.",
        "Sobran letras. Tiene {longitud} letras."
    ]
    
    # Diccionario que mapea condiciones a índices de mensajes
    condiciones = {
        "correcta": 0,  # Mensaje para longitud correcta
        "corta": 1,    # Mensaje para longitud corta
        "larga": 2     # Mensaje para longitud larga
    }

    # Solicitar palabra al usuario
    palabra = input("Ingresa una palabra: ").strip()  # Elimina espacios adicionales
    longitud = len(palabra)  # Calcula la longitud de la palabra

    # Determinar el tipo de longitud usando una tupla
    tipo_longitud = (
        "correcta" if 4 <= longitud <= 8 else
        "corta" if longitud < 4 else
        "larga"
    )

    # Obtener el mensaje adecuado del diccionario y la lista
    mensaje = mensajes[condiciones[tipo_longitud]]
    
    # Imprimir el mensaje con la longitud si es necesario
    print(mensaje.format(longitud=longitud))

# Ejecutar la función
verificar_longitud_palabra_con_estructuras()