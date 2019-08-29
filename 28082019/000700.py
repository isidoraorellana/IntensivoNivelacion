# -*- coding: utf-8 -*-
"""

"""

#los arreglos numpy logran acortar el tiempo en comparacion con las listas
#se ejecutan mucho mas rapido porque usa menos tiempo data
#el tiempo de ejecucion de un array numpy es mas rapido que iterar una lista 
#se puede cambiar el data type dependiendo del array 

import numpy as np 

#se mostraran maneras de crar arrays
a = np.array([2,3,4]) #se crea un array 
print a

a = np.arange (1,12,2) #crea una array con valores desde 1 hasta 12 de dos en dos
print a 

a = np.linspace(1,12,6) #crea array floatingpoint desde 1 hasta 12 con 6 elementos espaciados igualmente
print a

#se puede cambiar la forma del array

