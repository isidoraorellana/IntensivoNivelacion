# -*- coding: utf-8 -*-
"""

"""

#se puede crear una variable que sea la suma de todos los numeros solo multiplos de otro numero

total13=0
for i in range(1,8):
    if i %3 == 0:  #modulo operador da el resto de una division, asi sabemos, si da 0, que sera multiplo del numero
        total13 += i #si el numero es multiplo (osea i%3=0 entonces se sumará al total
print total13