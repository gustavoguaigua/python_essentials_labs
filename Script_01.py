"""
Ejercicio - 1
Parte - 1
Script_01
Created on Thu Apr 20 17:39:10 2023
@author: Gustavo Guaigua A.

"""
print("Empezando a trabajar con Python")
print("Realizado por: Gustavo Guaigua A.\n")
print("Consultando los tipos de valores:\n")

#Consultando el tipo de dato de 875
num01=875
print(f"El tipo de dato de {num01} es:\n{str(type(num01)).upper()}\n")

#Consultando el tipo de dato de 4.89 
num02=4.89
print(f"El tipo de dato de {num02} es:\n{str(type(num02)).upper()}\n")

#Consultando el tipo de dato de la cadena de texto "Now is better than never."
txt01="Now is better than never."
print(f"El tipo de dato del texto: {txt01} es:\n{str(type(txt01)).upper()}\n")

#Consultando el tipo de dato de 1.32
num03=1.32
print(f"El tipo de dato de: {num03} es:\n{str(type(num03)).upper()}\n")

#Consultando si el valor 5+8i corresponde a un número entero?
#Se reemplaza la letra j por la i de número imaginario para visualizar 
num04=5+8j
str01=str(num04).replace("j", "i")
print(f"¿El valor {str01[1:5]} corresponde a un valor entero? ")
print(str(isinstance(num04, int)).upper()+"\n")

#Consultando si el valor 8.2 corresponde a un valor entero?
num05=8.2
print(f"¿El valor {num05} corresponde a un valor entero? ")
print(str(isinstance(num05, int)).upper()+"\n")

#Consultando si una cadena de texto corresponde a un tipo de dato string?
txt02="Readability counts."
print(f"¿El texto: {txt02} corresponde a un string? ")
print(str(isinstance(txt02, str)).upper()+"\n")
