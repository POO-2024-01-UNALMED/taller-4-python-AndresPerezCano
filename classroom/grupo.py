from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if asignaturas is None:
           self._asignaturas = []
           return self._asignaturas
        elif estudiantes is None:
           self.listadoAlumnos = []
           return self.listadoAlumnos

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
           lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
     
    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"
    # def __str__(self):
    #     pass

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
