# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerLibreta.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_VerNotas(object):
    def setupUi(self, VerNotas):
        if not VerNotas.objectName():
            VerNotas.setObjectName(u"VerNotas")
        VerNotas.resize(680, 490)
        VerNotas.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_31 = QLabel(VerNotas)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 130, 111, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(VerNotas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 81, 16))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtNotaFinal = QLineEdit(VerNotas)
        self.txtNotaFinal.setObjectName(u"txtNotaFinal")
        self.txtNotaFinal.setEnabled(False)
        self.txtNotaFinal.setGeometry(QRect(20, 150, 101, 21))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.txtNotaFinal.setFont(font1)
        self.txtNotaFinal.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtEstudNotasDe = QLineEdit(VerNotas)
        self.txtEstudNotasDe.setObjectName(u"txtEstudNotasDe")
        self.txtEstudNotasDe.setEnabled(False)
        self.txtEstudNotasDe.setGeometry(QRect(20, 30, 421, 21))
        self.txtEstudNotasDe.setFont(font1)
        self.txtEstudNotasDe.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtEstudNotasDe.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.tblNotasGlobales = QTableWidget(VerNotas)
        if (self.tblNotasGlobales.columnCount() < 6):
            self.tblNotasGlobales.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblNotasGlobales.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblNotasGlobales.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblNotasGlobales.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblNotasGlobales.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblNotasGlobales.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblNotasGlobales.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblNotasGlobales.setObjectName(u"tblNotasGlobales")
        self.tblNotasGlobales.setGeometry(QRect(20, 190, 641, 281))
        self.tblNotasGlobales.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: #55aaff;\n"
"	padding: 2px;\n"
"\n"
"	border:1px solid #fffff8;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	gridline-color: #ff00ff;\n"
"	font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"	background-color: #55aaff;\n"
"	border: 1px solid #ff0000;\n"
"}")
        self.txtGradoEstudiante = QLineEdit(VerNotas)
        self.txtGradoEstudiante.setObjectName(u"txtGradoEstudiante")
        self.txtGradoEstudiante.setEnabled(False)
        self.txtGradoEstudiante.setGeometry(QRect(20, 90, 271, 21))
        self.txtGradoEstudiante.setFont(font1)
        self.txtGradoEstudiante.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtGradoEstudiante.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_2 = QLabel(VerNotas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 81, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(VerNotas)

        QMetaObject.connectSlotsByName(VerNotas)
    # setupUi

    def retranslateUi(self, VerNotas):
        VerNotas.setWindowTitle(QCoreApplication.translate("VerNotas", u"Form", None))
        self.label_31.setText(QCoreApplication.translate("VerNotas", u"Total Puntos", None))
        self.label.setText(QCoreApplication.translate("VerNotas", u"Notas de", None))
        self.txtNotaFinal.setText("")
        self.txtNotaFinal.setPlaceholderText("")
        self.txtEstudNotasDe.setText("")
        self.txtEstudNotasDe.setPlaceholderText("")
        ___qtablewidgetitem = self.tblNotasGlobales.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VerNotas", u"Materia", None));
        ___qtablewidgetitem1 = self.tblNotasGlobales.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VerNotas", u"Trimestre I", None));
        ___qtablewidgetitem2 = self.tblNotasGlobales.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VerNotas", u"Trimestre II", None));
        ___qtablewidgetitem3 = self.tblNotasGlobales.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VerNotas", u"Trimestre III", None));
        ___qtablewidgetitem4 = self.tblNotasGlobales.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VerNotas", u"Trimestre IV", None));
        ___qtablewidgetitem5 = self.tblNotasGlobales.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VerNotas", u"Final", None));
        self.txtGradoEstudiante.setText("")
        self.txtGradoEstudiante.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("VerNotas", u"Grado", None))
    # retranslateUi

