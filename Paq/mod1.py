def suma12():
    """
    FUNCIÓN QUE NO RECIBE ARGUMENTOS Y NO DEVUELVE DATOS
    SOLO GENERA UN MENSAJE
    Returns
    -------
    None.

    """
    print("Mensaje generado en una funcion...")
    return



def rest1(num1,num2,num3):
    """
    Función que define parámetros, pero no devuelve datos
    """
    resta=num1-num2-num3
    print(f"El resultado de restar num1, num2 y num3 es: {resta}")
    return



def data1():
    """
    Función que no recibe datso, pero si retorna algo
    """
    var1={"A":78,56:1982,"Key3":"Valores"}
    return var1



def func1(var1=1,var2=1):
    """
    Función que recibe datos y devuelve datos
    """
    if var1<=var2:
        print("Multiplicación")
        return var1*var2
    else:
        print("División")
        return var1/var2


#Cantidad variable de parámetros
def funcionv(*var10):
    print(var10)
    return
    

#Promedio de un número variable de datos
def prom1(*val2):
    return sum(val2)/len(val2)














