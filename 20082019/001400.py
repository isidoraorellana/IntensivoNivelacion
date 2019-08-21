# -*- coding: utf-8 -*-
"""

"""

#se le otorgara una funcion a la ecuacion del IMC

def calcula_imc(nombre, alturam, pesokg): 
    imc = pesokg / (alturam**2) #la funcion tiene la formula para calcular el IMC con sus respectivas variables
    print 'imc: '
    print imc
    if imc < 25: #empiece un if else que determinara si la persona tiene o no sobrepeso de acuerdo al valor de su IMC
        return nombre + ' no tiene sobrepeso'
    else:
        return nombre + ' tiene sobrepeso'

#se definen los sujetos y caracteristicas variables a evaluar en la funcion
nombre1 = 'carlos'
altura1= 2
peso1= 90

nombre2 = 'sofi'
altura2 = 1.8
peso2 = 70 

#se llama a la funcion y se le otorgan las variables definidas para los sujetos

resultado1 = calcula_imc(nombre1, altura1, peso1)
print resultado1

resultado2 = calcula_imc(nombre2, altura2, peso2)
print resultado2

#finalmente se imprime si la persona tiene o no sobrepeso de acuerdo a los resultados de su imc