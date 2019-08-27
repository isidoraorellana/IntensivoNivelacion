# -*- coding: utf-8 -*-
"""
"""

e = {"George": 24, "Tom": 32} #se crea diccionario
#valores pueden ser de cualquier tipo 
#las keys generalmente son strings o numeros
e[10] = 100 #se agrega una key que es un numero asociado a un valor que tambien es un numero
print e 

#iterar en pares key-valor
for key, value in e.items(): #ciclo for imprimira cada key con su valor asignado
    print ("key:")
    print(key)
    print("value:")
    print (value)
    print("")


 
