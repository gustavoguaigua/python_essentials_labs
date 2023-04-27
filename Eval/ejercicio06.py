"""
#Mostrar números del 0 al 10
var1=0
while var1<11:
    print(var1)
    var1+=1
"""

"""
#tabla del 7
dato1=1
while dato1<=7:
    print(f"7 * {dato1} = {dato1*7}")
    dato1+=1
"""

"""
#Menu que se mantenga y que salga con el 9
opc = 0
while opc!=3:
    print(' 1. menu opcion 1')
    print(' 2. menu opcion 2')
    print(' 3. Salir')

    opc=int(input("Elija una opción..."))
    
    if (opc==1):
        print(' **** menu opcion 1 ****')
        print("Saludos")
        
    elif (opc==2):
        print(' **** menu opcion 2 ****')
               
    elif (opc==3):
        print(' **** Adios  ****')
    else:
        print('No existe la opcion en el menu')
"""   

        
opcion = '0'
while not(opcion=='9'):
    print(' 1. menu opcion 01')
    print(' 2. menu opcion 02')
    print(' 3. menu opcion 03')
    print(' 4. menu opcion 04')
    print(' 5. menu opcion 05')
    print(' 9. Salir')

    opcion=input('  --- ¿Cuál opcion?: ')
    
    if (opcion=='1'):
        print(' **** menu opcion 01 ****')
        
    elif (opcion=='2'):
        print(' **** menu opcion 02 ****')
        
    elif (opcion=='3'):
        print(' **** menu opcion 03 ****')
        
    elif (opcion=='4'):
        print(' **** menu opcion 04 ****')
        
    elif (opcion=='5'):
        print(' **** menu opcion 05 ****')
                
    elif (opcion=='9'):
        print(' **** Saliendo del menu  ****')
        print(' **** Ejemplo de un menu ****')
    else:
        print('No existe la opcion en el menu')


"""
#Menu con una bandera para salir
while True:
    print("### Menú principal ###")
    var2=int(input("Ingrese su opción: "))
    if var2==1:
        print("Saludos")
        break
    elif var2==2:
        print()
    elif var2==3:
        print("Adios")
        break

"""