class ciudadanoec():
    def __init__(self,cedula,nombre,apellido,edad):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def genlista(self):
        try:
            print("Lista construida")
            return [self.nombre,self.apellido,self.edad,self.cedula]
        except:
             print("ha ocurrido un error")
    def gendic(self,trabajo):
        self.trabajo=trabajo
        return {"1":self.cedula,"2":self.trabajo}