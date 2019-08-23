# -*- coding: utf-8 -*-
"""

"""

#se calcularan la suma de todos los numeros multiplos de 3 y 5 menores a 100

total =0 #se crea variable que se le ira sumando los numeros seleccionados
for i in range(1, 100): #ciclo for de valores entre 1 y 99
    if i%3==0 or i%5==0: #condicion para que se le sume a la variable total
        total += i #si pasan la condicion se le suma a la variable
print total
    
