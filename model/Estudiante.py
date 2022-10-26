class Estudiante:
    def __init__(self) -> None:
        self._nombre = ""
        self._nie = ""

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nie(self):
        return self._nie

    @nie.setter
    def nie(self, nie):
        self._nie = nie
