# -*- coding: utf-8 -*-
"""

"""
#ejemplo medicion indice de masa corporal IMC

#se ingresan datos de la persona
nombre = 'Camila'
alturaenmetros = 1.57 
pesoenkg = 65

imc = pesoenkg / (alturaenmetros ** 2) #se aplica la formula de medicion de IMC
print 'IMC: '
print imc
if imc < 25: #En caso de que el IMC sea sobre 25 la persona no tiene sobrepeso
    print nombre
    print 'no tiene sobrepeso'
else: #cuando el IMC es mayor a 25 la persona tiene sobrepeso
    print nombre
    print 'tiene sobrepeso'

#en este caso camila tiene sobrepeso


nombre2 = 'Javier'
alturaenmetros2 = 2
pesoenkg2 = 65

imc2 = pesoenkg2 / (alturaenmetros2 ** 2)
print 'IMC: '
print imc2
if imc2 < 25:
    print nombre2
    print 'no tiene sobrepeso'
else:
    print nombre2
    print 'tiene sobrepeso'

#en este caso javier no tiene sobrepeso

