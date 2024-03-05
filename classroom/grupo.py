from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if asignaturas is None and estudiantes is None:
           self._asignaturas = []
           self.listadoAlumnos = []
        elif estudiantes is None and asignaturas is not None:
           self.listadoAlumnos = []
           self._asignaturas = asignaturas
        elif estudiantes is not None and asignaturas is  None:
            self.listadoAlumnos = estudiantes
            self._asignaturas = []
        else:
           self._asignaturas = asignaturas
           self.listadoAlumnos = estudiantes
           

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
