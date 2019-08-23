# -*- coding: utf-8 -*-
"""

"""

#se hara un ciclo while que sume todos los numeros negativos de la lista
given_list = [7,5,4,4,3,1,-2,-3,-5,-7]

total = 0 
i = 0
while i < len(given_list): #mientras se este dentro del rango de la lista
    if given_list[i]<0:
        total += given_list[i] #si el numero es negativo se le sumara al total
    i+= 1 #se cambiara de posicion en la lista a una mas adelante 

print total
