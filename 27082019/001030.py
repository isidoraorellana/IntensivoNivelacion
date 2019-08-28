# -*- coding: utf-8 -*-
"""


"""
import numpy as np
#se puede probar si los elementos dentro de un array cumple algun criterio, por ejemplo que sean menor o mayor que un valor
z=np.array([1,2,3,4,5])
print z<3 #se obtendra 'true' si cumple el elemento la condicion y 'false' si no

print z[z>3] #see imprimira un array donde el array z es mayor a 3

#esto tambien funciona si se esta trabajando con una foto
