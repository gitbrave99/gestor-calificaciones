class Grado:
    def __init__(self) -> None:
        self._idGrado=0
        self._grado=""
        self._seccion=""
    
    @property
    def idGrado(self):
        return self._idGrado
    
    @idGrado.setter
    def idGrado(self, idGrado):
        self._idGrado=idGrado

    @property
    def grado(self):
        return self._grado
    
    @grado.setter
    def grado(self,grado):
        self._grado=grado

    @property
    def seccion(self):
        return self._seccion
    
    @seccion.setter
    def seccion(self,seccion):
        self._seccion=seccion

