# -*- coding: utf-8 -*-
"""
Title: Desarrollar un programa que permita validar la contraseña introducida por un usuario con validaciones.
Created on Mon Apr 24 23:04:01 2023
@author: Gustavo Guaigua A.
"""

minus="abcdefghij"
mayus="KLMNOPQRST"
nume="1234567890"
espe="$%*@"
longMin=5
longMax=15
cont=0
msgOk="\n############# Bienvenido al sistema... acceso exitoso..!!! ###########################"
msgErr="\nSu contraseña no cumple con los requisitos de seguridad:\n"
msgErr1="* Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.\n"
msgErr2="* Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.\n"
msgErr3="* Debe contener al menos un número entre 0 y 9.\n"
msgErr4="* Debe contener un símbolo especial entre: $,%,*,@.\n"
msgErr5="* Debe tener un tamaño mínimo de 5 caracteres y máximo de 15.\n"
print("\n\n##########################################################################################")
print("CONTRASEÑA DE USUARIO.")
print("Recuerde que para que una contraseña sea segura:...")
print(msgErr1+msgErr2+msgErr3+msgErr4+msgErr5)
print("##########################################################################################\n")

key=input("Ingrese la contraseña: ")

for i in key:
    if i in minus:
        msgErr1=""
        cont+=1
        break

for i in key:
    if i in mayus:
        msgErr2=""
        cont+=1
        break

for i in key:
    if i in nume:
        msgErr3=""
        cont+=1
        break

for i in key:
    if i in espe:
        msgErr4=""
        cont+=1
        break

if len(key)>=5 and len(key)<=15:
    msgErr5=""
    cont+=1


if cont==5:
    print(msgOk)
else:
    print(msgErr+msgErr1+msgErr2+msgErr3+msgErr4+msgErr5)



