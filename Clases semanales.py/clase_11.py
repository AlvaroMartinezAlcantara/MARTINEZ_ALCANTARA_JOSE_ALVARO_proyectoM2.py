# # 
# # Python code for 1-D random walk.
# import random
# import numpy as np
# import matplotlib.pyplot as plt

# # Probability to move up or down
# prob = [0.05, 0.95] 

# # statically defining the starting position
# start = 2
# positions = [start]

# # creating the random points
# rr = np.random.random(1000)
# downp = rr < prob[0]
# upp = rr > prob[1]


# for idownp, iupp in zip(downp, upp):
# 	down = idownp and positions[-1] > 1
# 	up = iupp and positions[-1] < 4
# 	positions.append(positions[-1] - down + up)

# # plotting down the graph of the random walk in 1D
# plt.plot(positions)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

def simular_galton(n_canicas=3000, n_niveles=12):
    """Simula la caída de las canicas en una máquina de Galton."""
    contenedores = np.zeros(n_niveles + 1, dtype=int)
    
    for _ in range(n_canicas):
        posicion = sum(np.random.choice([0, 1], size=n_niveles))  # 0 = izquierda, 1 = derecha
        contenedores[posicion] += 1
    
    return contenedores

def graficar_histograma(contenedores):
    """Grafica el histograma de distribución de las canicas en los contenedores."""
    plt.bar(range(len(contenedores)), contenedores, color='blue', edgecolor='black')
    plt.xlabel('Posición del Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de Máquina de Galton')
    plt.show()

# Ejecutar simulación y graficar resultados
contenedores = simular_galton()
graficar_histograma(contenedores)
