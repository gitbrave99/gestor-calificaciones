# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiConfirmDeletegGTSDQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(312, 246)
        Form.setMinimumSize(QSize(312, 246))
        Form.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.lblMensaje = QLabel(Form)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setGeometry(QRect(40, 120, 231, 71))
        self.lblMensaje.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnEliminarRegistro = QPushButton(Form)
        self.btnEliminarRegistro.setObjectName(u"btnEliminarRegistro")
        self.btnEliminarRegistro.setGeometry(QRect(170, 200, 121, 28))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminarRegistro.setFont(font)
        self.btnEliminarRegistro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminarRegistro.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background: rgb(126,2,24);\n"
"	border: 2px solid rgb(203,18,51);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(203,18,51);\n"
"	border:2px solid rgb(126,2,24);\n"
"}\n"
"")
        self.btnCancelarEliminar = QPushButton(Form)
        self.btnCancelarEliminar.setObjectName(u"btnCancelarEliminar")
        self.btnCancelarEliminar.setGeometry(QRect(20, 200, 121, 28))
        self.btnCancelarEliminar.setFont(font)
        self.btnCancelarEliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelarEliminar.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(11,70,181);\n"
"	border: 2px solid rgb(39,105,229);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(39,105,229);\n"
"	border:2px solid rgb(11,70,181);\n"
"}\n"
"")
        self.btnCancelEstud_2 = QPushButton(Form)
        self.btnCancelEstud_2.setObjectName(u"btnCancelEstud_2")
        self.btnCancelEstud_2.setGeometry(QRect(100, 30, 131, 81))
        self.btnCancelEstud_2.setFont(font)
        self.btnCancelEstud_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelEstud_2.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background: rgb(126,2,24);\n"
"	border: 2px solid rgb(203,18,51);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(203,18,51);\n"
"	border:2px solid rgb(126,2,24);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/img/deleteconfirm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCancelEstud_2.setIcon(icon)
        self.btnCancelEstud_2.setIconSize(QSize(64, 64))
        self.lblIdRegAeliminar = QLabel(Form)
        self.lblIdRegAeliminar.setObjectName(u"lblIdRegAeliminar")
        self.lblIdRegAeliminar.setGeometry(QRect(30, 30, 47, 13))
        self.lblIdRegAeliminar.setStyleSheet(u"color: rgb(40, 40, 40);")
        self.lblTablaaEliminar = QLabel(Form)
        self.lblTablaaEliminar.setObjectName(u"lblTablaaEliminar")
        self.lblTablaaEliminar.setGeometry(QRect(20, 70, 47, 13))
        self.lblTablaaEliminar.setStyleSheet(u"color: rgb(40, 40, 40);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Eliminar", None))
        self.lblMensaje.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u00bfEsta seguro que quiere</span></p><p align=\"center\"><span style=\" font-size:14pt;\">eliminar?</span></p></body></html>", None))
        self.btnEliminarRegistro.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.btnCancelarEliminar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnCancelEstud_2.setText("")
        self.lblIdRegAeliminar.setText("")
        self.lblTablaaEliminar.setText("")
    # retranslateUi

