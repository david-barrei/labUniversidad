

class Persona():

    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def __str__(self):

        return (f"El nombre es {self.nombre} su edad {self.edad} y el genero {self.sexo}")
       

