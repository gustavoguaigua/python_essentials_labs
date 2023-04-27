# -*- coding: utf-8 -*-
"""
Prorama para mostrar el tipo de dato ingresado por consola
Created on Sun Apr 23 22:50:25 2023
@author: Gustavo Guaigua A.
"""
print("################################################################################")
print("Programa que identifica el tipo de dato de un valor ingresado por el usuario")
print("se realizarán cinco interacciones:")
print("################################################################################\n")


for rep in range(1,6):
    if rep==1:
        msg="Primera "
    elif rep==2:
        msg="Segunda "
    elif rep==3:
        msg="Tercera "
    elif rep==4:
        msg="Cuarta "
    else:
        msg="Quinta "

    var01=input(msg+"Interacción, ingrese un valor cualquiera: ")
    longInput=len(var01)
    letras="abcdefghijklmnñopqrstuvwxyz"
    intro="Este tipo de dato en Python es: "
    tipo="Entero"
    resp=intro+tipo
    
    for i in range(0,longInput):
        for j in range(0,len(letras)):
            if var01[i]==letras[j] and i!=longInput: 
                resp=intro+"String"
    
    if tipo=="Entero" and (var01[longInput-1]=="i" or var01[longInput-1]=="j"):
        print(intro+"Número Complejo o Imaginario\n")
    elif tipo=="Entero" and "." in tuple(var01):
        print(intro+"Flotante\n")    
    else:
        print(resp+"\n")
