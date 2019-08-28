# -*- coding: utf-8 -*-
"""

"""

import numpy as np

#se puede aplicar una suma, resto u otro entre arrays, esto hara que los elementos que estan en la misma posicion en los dos arrays hagan esta operacion, por ejemplo ambos elementos de la posicion 0 se  sumaran 
a_array = np.array([1,2,3,4,5])
b_array = np.array([6,7,8,9,10])

print a_array + b_array #se suman ambos array
print a_array * 30 #cada elemento se multiplicara por 30

#se pueden transponer los elementos de los array, osea se cambian las filas por columnas
#plt.imshow(photo[:,:,0], T) #la T es la que crea la transposicion

