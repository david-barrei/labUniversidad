


class Estudiante():

    def __init__(self, carnet, carrera):
        self.carnet = carnet
        self.carrera = carrera

    def estudiante(self):

        return (f"El carnet es {self.carnet} la carrera es {self.carrera}")
    
class Curso():

    def __init__(self,nombre,codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def curso(self):

        return (f"El nombre es {self.nombre} el codigo es {self.codigo} y el profesor es {self.profesor}") 