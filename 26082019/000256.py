# -*- coding: utf-8 -*-
"""

"""

#se aprendera a usar diccionarios en python
#cada key tiene un valor asociado

d = {} #se crea un nuevo diccionario asignado a la variable d

#
e = {"George": 24, "Tom": 32} #esta es otra manera de definir un diccionario 
#

d["George"] = 24 #se le agrega una key 'george' asociado a un valor 24
d["Tom"] = 32 #key tom valor 32
d["Jenny"] = 16 #key jenny valor 16 

print (d["George"]) #esto imprimira el valor asociado a la key George

d["Jenny"]= 20 #se le puede cambiar el valor asociado a la key 
print (d["Jenny"])