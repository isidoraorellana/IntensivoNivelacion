# -*- coding: utf-8 -*-
"""

"""


import numpy as np 

a = np.linspace(1,12,6)
#se puede cambiar la forma del array
a = a.reshape(3,2) #se cambiara a un array de dos dimensiones, 3 filas 2 columnas
print a 


#se puede cambiar el tamaño del array
b = a.size
print b #mmostrara el tamaño del array (cantidad elementos)

#se puede averiguar la forma
c = a.shape #mostrara la forma del array (filas,columnas)