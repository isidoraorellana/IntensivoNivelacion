# -*- coding: utf-8 -*-
"""

"""
#se aprende de true statements y break 

given_list2 = [5,4,4,3,1,-2,-3,-5]

total = 0 
i = 0
while True: #se define una verdad que mientras se mantenga seguira corriendo el loop
    total  += given_list2[i]
    i += 1
    if given_list2[i] <= 0: #cuando haya un numero menor a 0 se saldra del loop
        break

print total