import time
from PySide2.QtWidgets import QWidget
from views.ConfirmDelte import Ui_Form
from PySide2.QtCore import Qt


class ConfirmDeletec(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.setWindowFlag(Qt.Window)
        self.btnEliminarRegistro.clicked.connect(self.eliminarRegistro)
        self.btnCancelarEliminar.clicked.connect(self.close)

    def eliminarRegistro(self):
        idReg = self.lblIdRegAeliminar.text()
        table = self.lblTablaaEliminar.text()
        self.opcionEliminar(idReg, table)

    def opcionEliminar(self, id, tabla):
        if tabla == 'grado':
            from dao.Congrado import ConGrado
            cong = ConGrado()
            if cong.eliminar(id):
                self.lblIdRegAeliminar.setText("1")
                self.close()
        if tabla == 'materia':
            from dao.ConMateria import ConMateria
            conm = ConMateria()
            if conm.eliminar(id):
                self.close()
        if tabla == 'estudiante':
            from dao.ConEstudiante import ConEstudiante
            conest = ConEstudiante()
            if conest.eliminar(id):
                self.close()
        if tabla == 'nota':
            from dao.ConNotas import ConNotas
            connots = ConNotas()
            if connots.eliminar(id):
                self.close()
        if tabla == 'borrarall':
            from dao.ConMateria import ConMateria
            conm = ConMateria()
            if conm.eliminar_base_datos():
                print("DATOS BORRADOS")
                self.close()

