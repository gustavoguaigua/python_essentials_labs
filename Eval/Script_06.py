# -*- coding: utf-8 -*-
"""
Convertir cada programa realizado en el aula virtual en un módulo independiente y 
Crear un nuevo programa que disponga de un menú que esté activo
Created on Wed Apr 26 15:19:45 2023
@author: Gustavo Guaigua A.
"""

try:
    
    def menu():
        print("\n############################# MENÚ PRINCIPAL #################################")
        print("Digite el número del programa que desea ejecutar: ")
        print("1.  Ejercicio01.py - \"Hola Mundo\"")
        print("2.  Ejercicio02.py - \"Tabs y saltos de línea\"")
        print("3.  Ejercicio03.py - \"Strings e interpolación de variables\"")
        print("4.  Ejercicio04.py - \"Funciones upper() y lower()\"")
        print("5.  Ejercicio05.py - \"Estructura de decisión IF\"")
        print("6.  Ejercicio06.py - \"Creando menús\"")
        print("7.  Ejercicio07.py - \"Instrucción continue\"")
        print("8.  Ejercicio08.py - \"Instrucción break\"")
        print("9.  Ejercicio09.py - \"Funciones\"")
        print("10. Ejercicio10.py - \"Función que suma un número variable de enteros\"")
        print("0.  Salir")

    while True:
        menu()
        var01=int(input("\nDigite el número del módulo que desea ejecutar...: "))
        if var01==1:
            import ejercicio01 as m1
            print("\n################### RESULTADO ###############################")
            m1.fun02()
            input("\npresione <enter> para continuar...:")
        elif var01==2:
            import ejercicio02 as m2
            print("\n################### RESULTADO ###############################")
            m2.fun02()
            print(m2.var01)
            input("\npresione <enter> para continuar...:")
        elif var01==3:
            import ejercicio03 as m3
            print("\n################### RESULTADO ###############################")
            m3.strcom
            input("\npresione <enter> para continuar...:")
        elif var01==4:
            import ejercicio04 as m4
            print("\n################### RESULTADO ###############################")
            m4.ed1
            input("\npresione <enter> para continuar...:")
        elif var01==5:
            import ejercicio05 as m5
            print("\n################### RESULTADO ###############################")
            m5.ed1
            input("\npresione <enter> para continuar...:")
        elif var01==6:
            import ejercicio06 as m6
            print("\n################### RESULTADO ###############################")
            m6.opcion
            input("\npresione <enter> para continuar...:")
        elif var01==7:
            import ejercicio07 as m7
            print("\n################### RESULTADO ###############################")
            m7.num
            input("\npresione <enter> para continuar...:")
        elif var01==8:
            import ejercicio08 as m8
            print("\n################### RESULTADO ###############################")
            m8.i
            input("\npresione <enter> para continuar...:")
        elif var01==9:
            import ejercicio09 as m9
            print("\n################### RESULTADO ###############################")
            m9.saludo()
            print(m9.suma12(23,6))
            input("\npresione <enter> para continuar...:")
        elif var01==10:
            import suma_enteros as s
            print("\n################### RESULTADO ###############################")
            print(s.suma_enteros(3,4,5,2,5,5))
            input("\npresione <enter> para continuar...:")
        else:
            break
except:
    print("Ha ocurrido una excepción")