# #Random es un modulo de python que genera números aleatorios
# import random

# def tiro_dado(num_tiros) :
#     for dado in range(num_tiros) :
#         print("El dado " + str(dado + 1) + " dio : " + str(random.randint(1, 6))) 
# tiro_dado(5)
#######################################################################
# # biblioteca Numpy, la cual está especializada en cálculos numéricos y análisis de datos
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(0)
# numeros = np.random.rand(10)
# print(numeros)
# plt.plot(numeros)
# plt.show()

####################################################################################
# Las graficas de datos nos ofrecen una representacion de datos visual del compaortamiento de la informacion
# import numpy as np
# import matplotlib.pyplot as plt
# datos = np.random.normal(0, 1.0, 1000)
# plt.hist(datos)
# plt.show()

import random
import matplotlib.pyplot as plt
eje_x = [random.randint(1 , 100) for n in range (100)]
eje_y = [random.randint(1 , 100) for n in range (100)]
plt.scatter(eje_x, eje_y)
plt.title("Gráfica de dispercion")
plt.show()

