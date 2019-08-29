# -*- coding: utf-8 -*-
"""

"""

import numpy as np 

a = np.linspace(1,12,6)

#se puede averiguar el tipo de data del array
b = a.dtype
print b #imprimira el valor del tipo de data, en esta caso float64 que es el default que da numpy en python

#se puede saber cuanta memoria en bytes toma el array
c = a.itemsize
print c 

#se puede hacer una comparacion de los elementos del array con alguna afirmacion, si sale false no cumple la afirmacion, si sale true si la cumple. El array puede ser multidimensional

a = a.reshape(3,2) #se transforman las dimensiones
print a
print a > 3  # mostrara true or false dependiendo si los elementos cumplen que sean mayor a 3
#todo lo anterior mencionado tambien se puede hacer para arrays multidimensionales (shape, size, dtype)