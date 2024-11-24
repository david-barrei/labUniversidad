from clases.universidad import Universidad
from clases.profesor import Profesor
from clases.estudiante import Estudiante
from clases.curso import Curso


universidad = Universidad("Universidad del Salvador")

#crear profesor

profesor_juan = Profesor("Juan Perez",30, "Masculino",[521553], "Matematicas")
profesor_samanta = Profesor("Samanta Calderon",21, "Femenino",[551235], "Fisica")
profesor_carlos = Profesor("Carlos Juca",39, "Masculino",[5562335], "Quimica")


#Crear los cursos con los profesores respectivos

curso_matematicas = Curso("Matematicas","MAT101", profesor_juan)
curso_fisica = Curso("Fisica","FIS101", profesor_samanta)
curso_quimica = Curso("Quimica","QUI101", profesor_carlos)

#Agregar los cursos a la universidad

universidad.agregar_curso(curso_matematicas)
universidad.agregar_curso(curso_fisica)
universidad.agregar_curso(curso_quimica)

#Crear un estudiante

estudiante_carlos = Estudiante("Carlos Perez",20, "Masculino",1545151, "Ingenieria")


print(universidad)
print("-----------")
print(estudiante_carlos)
print("------------")
print(profesor_juan)
print("-------------")
print(curso_fisica)

curso_nuevo_fisica = Curso("Fisica", "FIS102", profesor_samanta)
universidad.agregar_curso(curso_nuevo_fisica)

print(universidad)