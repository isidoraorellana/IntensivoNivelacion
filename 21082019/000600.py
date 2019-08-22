# -*- coding: utf-8 -*-
"""

"""

a = [3,10,-1] #se define una lista con elementos 3, 10 y -1 y se le asigna esta lista a la variable a
print a
a.append(1) #se le agrega el item '1' a la lista 'a'

print a #aqui se imprime con el 1 incluido

a.append('hello') #a la lista tambien se le pueden agregar strings

print a

#una lista tambien puede incluir otras listas
a.append([1,2]) #se le agrega a la lista 'a' otra lista que contiene los elementos 1 y 2

print a

a.pop() #esto eliminara el ultimo elemento de la lista
print a #ya no tendra [1,2]

a.pop()
print a #se le elimino 'hello'

print a[0] #se puede referir a un elemento especifico de la lista, llamandolo por su ubicacion en ella, el primer elemento es 0 y de ahi en adelante

print a[3]

a[0] = 100 #se le puede asignar un nuevo valor a un elemento de la lista

print a #aqui se habra reemplazado el 3 por un 100