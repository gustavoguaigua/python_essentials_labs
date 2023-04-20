#ed1, tit1=int(input("Ingrese su edad: ")),input("Tiene tÃ­tulo de bachiller: ").lower()
ed1=int(input("Ingrese su edad: "))

if ed1 >= 18:
    print("Usted es mayor de edad...")
    tit1=input("Tiene tí­tulo de bachiller: ").lower()
    if tit1=="si":
        print("Si puede sacar la licencia")
    else:
        print("No tiene tí­tulo de bachiller")
else:
    print("Usted NO es mayor de edad")
    if ed1>=16:
        print("Existe la posibilidad de permiso de aprendizaje")
    else:
        print("No es posible sacar una licencia")
    