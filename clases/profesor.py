from .persona import Persona
class Profesor(Persona):

    def __init__(self,nombre,edad,sexo,codigo, especialidad):
        super().__init__(nombre,sexo,edad)
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):

        return f"{super().__str__()}, codigo: {self.nombre}, especialidad {self.especialidad}"
        


