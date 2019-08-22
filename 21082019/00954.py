# -*- coding: utf-8 -*-
"""

"""
#en este tutorial se aprendio como crear una lista, agregarle elementos, eliminar elementos de est y, reemplazaras los elementos existentes.


lista = [1, 2, 'tres', 'cuatro', 5] #lista con numeros y strings
lista.append(6) #se agrega un 6

print lista 

lista.pop() #se le quita el 6
print lista

lista['tres'] = 3 #se cambia el string tres por un numero 3
lista['cuatro'] = 4 #se cambia string cuatro por un 4

print lista #ahora la lista será solo se numeros