# -*- coding: utf-8 -*-
"""

"""
#nivelacion While loops

given_list = [5,4,4,3,1,-2,-3,-5] #sabemos que lista esta en orden descendiente
#se quiere buscar la suma de solo los valores positivos de la lista

total3 = 0 
i = 0 #se define de donde partira la posicion en la lista 
while given_list[i] > 0: #mientras el numero de la lista seleccionado sea positivo correra este while
    total3 += given_list[i] #el numero sera sumado al total
    i+= 1 #se cambiara de posicion en la lista a una mas adelante 

print total3





