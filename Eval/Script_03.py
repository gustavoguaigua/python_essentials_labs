# -*- coding: utf-8 -*-
"""
Considerando la siguiente tupla codifique un programa que permita separar los números pares
e impares. Identifique también los posibles valores que considere atípicos a ese arreglo.

Created on Mon Apr 24 08:36:04 2023
@author: Gustavo Guaigua A.
"""
Datos_2021 = [1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
t1=tuple(sorted(set(Datos_2021)))       
par,inpar="",""
for i in range(0,len(t1)):
    num=t1[i]%2
    if num==0:
        if par!="":
            par=par+","+str(t1[i])
        else:
            par=str(t1[i])
    else:
        if inpar!="":
            inpar=inpar+","+str(t1[i])
        else:
            inpar=str(t1[i])

print("\n\nSin duplicados:")
print(f"Los números pares son: {par}")
print(f"Los números impares son: {inpar}")
