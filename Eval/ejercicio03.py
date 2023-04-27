"""
String e interpolación de variables
"""

# Mi nombre es y mi apellido es y 
# mi edad es:
#nombre,apellido,edad="Gustavo","Guaigua",53    
#print("Mi nombre es: ,\nMi apellido es: ,\nMi edad es: ,\n\nMucho gusto...!!!!")

#print("Mi nombre es:\t"+nombre+"\nMi apellido es:\t"+apellido+"\nMi edad es:\t\t"+str(edad))

#strgg="Mi nombre es:\t"+nombre+"\nMi apellido es:\t"+apellido+"\nMi edad es:\t\t"+str(edad)"

#print(strgg)

#print("Mi nombre es \t",nombre,"\nMi apellido es'\t",apellido,"\nMi edad es\t",edad)


#método FORMAT
#strcom="Mi nombre es {nombre}, mi apellido es {apellido}, mi edad es {edad} años, mucho gusto".format(nombre="Gus",apellido="Guaigua",edad=44)


#String tipo f
#strcom=f"Mi nombre es: {nombre},\nMi apellido es: {apellido.upper()},\nMi edad es: {edad*10},\n\nMucho gusto...!!!!"
#print(strcom)


#Múltimples imput en una sola línea
#var1,var2=input("Valor1: "),input("valor2: ")



strcom="Mi nombre es {nombre}, mi apellido es {apellido}, \
    mi edad es {edad} años, mucho gusto".format(nombre=input("Ingrese el nombre:"), apellido="Guaigua", edad=44)
print(strcom)
