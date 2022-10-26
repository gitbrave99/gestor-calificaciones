class Materia:
    def __init__(self) -> None:
        self._materia=""
        self._idGrado=0
    
    @property
    def idGrado(self):
        return self._idGrado
    
    @idGrado.setter
    def idGrado(self,idGrado):
        self.idGrado=idGrado

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self,materia):
        self._materia=materia