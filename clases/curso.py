from .profesor import Profesor

class Curso():
    def __init__(self, nombre, codigo, profesor) :
        #Atributos basicos del curo
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def __str__(self):
        return f"Curso: {self.nombre}, Codigo: {self.codigo}, Profesor: {self.profesor}"
