# -*- coding: utf-8 -*-
"""

"""

b = ['banana', 'manzana', 'durazno' ]

#se invertira el nombre del primer y ultimo elemento de la lista

temp = b[0] #se define variable temporal nueva
b[0]=b[2]
b[2]=temp

print b 

#atajo de lo mismo
b[0], b[2]=b[2], b[0]
print b