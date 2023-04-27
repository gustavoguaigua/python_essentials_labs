# -*- coding: utf-8 -*-
"""
Desarrollar un programa que permita encontrar los valores más altos y bajos dentro de los
valores de un diccionario
Created on Tue Apr 25 22:16:13 2023
@author: Gustavo Guaigua A.
"""
 
def menu1():
	print("\nElija una opción:\n")
	print("\t1) Demostración del cálculo de valores, altos y bajos en diccionarios.")
	print("\t2) Salir")

def menu2():
    print("\nElija un diccionario para la demostración:\n")
    print("1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}")
    print("2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}")
    print("3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}")
    print("4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}")
    print("9) Regresar al menú principal")


def calcula(dict01, var01, var02):
    lista01=list(dict01.values())
    lista01.sort()
    print(lista01)
    lista01.sort(reverse=True)
    listaFinal01,listaFinal02=[],[]
    for i in range(0,var01):
        listaFinal01.append(lista01[i])
    print("\n##################### RESULTADO #########################")
    print("Valores ALTOS calculados en formato LISTA: "+str(listaFinal01))    
    print("Valores ALTOS calculados en formato TUPLA: "+str(tuple(listaFinal01)))
    lista01.sort()
    for i in range(0,var02):
        listaFinal02.append(lista01[i])
    print("*************************************")
    print("Valores BAJOS calculados en formato LISTA: "+str(listaFinal02))    
    print("Valores BAJOS calculados en formato TUPLA: "+str(tuple(listaFinal02)))
    input("Presione <enter> para continuar...")





while True:
    menu1()
    opt=input("\nDigite 1 o 2 según la opción deseada: ")
    if opt=="1":
        #break
        while True:
            menu2()
            opt1=input("\nDigite del 1 al 4, según la opción deseada: ")

            if opt1=="1":
                dict01={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
                print("\nEligió la: Opción 1")
                while True:
                    var01=int(input("Digite el número de valores ALTOS que desea mostrar: "))
                    var02=int(input("Digite el número de valores BAJOS que desea mostrar: "))
                    if var01 > len(dict01) or var02 > len(dict01):
                        print("El número solicitado excede el tamaño del arreglo........ vuelva a ingresar:\n ")
                    else:
                        calcula(dict01, var01, var02)
                        break                    
            if opt1=="2":
                dict01={"tplA1":4,"tplA2":-12,"tplA3":56,"tplA4":-34,"tplA5":98,"tplA6":102,
                        "tplB1":9,"tplB2":0,"tlpB3":1,"tplB4":10,"tplB5":-3,"tplB6":14,
                        "tlpC1":87,"tlpC2":12,"tlpC3":56,"tlpC4":987,"tlpC5":-61}
                print("\nEligió la: Opción 2")
                while True:
                    var01=int(input("Digite el número de valores ALTOS que desea mostrar: "))
                    var02=int(input("Digite el número de valores BAJOS que desea mostrar: "))
                    if var01 > len(dict01) or var02 > len(dict01):
                        print("El número solicitado excede el tamaño del arreglo........ vuelva a ingresar:\n ")
                    else:
                        calcula(dict01, var01, var02)
                        break
            if opt1=="3":
                dict01={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
                print("\nEligió la: Opción 3")
                while True:
                    var01=int(input("Digite el número de valores ALTOS que desea mostrar: "))
                    var02=int(input("Digite el número de valores BAJOS que desea mostrar: "))
                    if var01 > len(dict01) or var02 > len(dict01):
                        print("El número solicitado excede el tamaño del arreglo........ vuelva a ingresar:\n ")
                    else:
                        calcula(dict01, var01, var02)
                        break
            if opt1=="4":
                dict01={"lst11":4,"lst12":6,"lst13":-12,"lst14":56,"lst15":-9,"lst16":5.7,"lst17":33,"lst18":100,
                        "lst21":9,"lst22":0,"lst23":81,"lst24":-2,"lst25":-56,
                        "lst31":12,"lst32":31,"lst33":87,"lst34":1,"lst35":0,"lst36":4,"lst37":-11}
                print("\nEligió la: Opción 4")
                while True:
                    var01=int(input("Digite el número de valores ALTOS que desea mostrar: "))
                    var02=int(input("Digite el número de valores BAJOS que desea mostrar: "))
                    if var01 > len(dict01) or var02 > len(dict01):
                        print("El número solicitado excede el tamaño del arreglo........ vuelva a ingresar:\n ")
                    else:
                        calcula(dict01, var01, var02)
                        break
            if opt1=="9":
                break
            else:
                print("\n\n#######################################################")
                print("ERROR.....Elija una opción del 1 al 4.....!!!")
                print("#######################################################")
    elif opt=="2":
        break
    else:
        print("\n\n#######################################################")
        print("ERROR.....Solo puede elegir entre el 1 y el 2.....!!!")
        print("#######################################################")





