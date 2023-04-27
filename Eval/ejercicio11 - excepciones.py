try: 
    var1,var2=80,90
    print(var2/var1)
except ZeroDivisionError:
    print("Ocurre una excepción div/0")
except (TypeError, ModuleNotFoundError):
    print("Error de tipo")
else:
    print("Está ejecutándose un bloque else")
finally:
    print("Está ejecutándose FINALLY")