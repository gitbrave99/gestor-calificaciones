from PySide2.QtWidgets import QWidget,QTableWidgetItem
from views.VerNotasView import Ui_VerNotas
from PySide2.QtCore import Qt


class VerNotasc(QWidget, Ui_VerNotas):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.setWindowFlag(Qt.Window)
        
        self.headerBach=("Materia","Trimestre I","Trimestre II","Trimestre III","Trimestre IV","Final")
        self.header3C=("Materia","Periodo I","Periodo II","Periodo III","Final")
        self.tblNotasGlobales.setColumnCount(6)
        self.tblNotasGlobales.setHorizontalHeaderLabels(self.headerBach)

    

    def cargar_table_libretaNotas(self, listNotasGlobales):
        self.tblNotasGlobales.setRowCount(len(listNotasGlobales))
        for (index_row, row) in enumerate(listNotasGlobales):
            for (index_cell, cell) in enumerate(row):
                self.tblNotasGlobales.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))