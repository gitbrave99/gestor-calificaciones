# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWithAllFJfgJc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 662)
        icon = QIcon()
        icon.addFile(u"./assets/img/registronotas.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.WidgetCentral = QWidget(MainWindow)
        self.WidgetCentral.setObjectName(u"WidgetCentral")
        self.WidgetCentral.setMinimumSize(QSize(875, 621))
        self.verticalLayout = QVBoxLayout(self.WidgetCentral)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.WidgetCentral)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #C2C7CB;\n"
"     position: absolute;\n"
"     top: -0.5em;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     alignment: center;\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     background: rgb(4,75,124);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
"     alignment: center;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: rgb(38,159,243);\n"
"     alignment: center;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
"     alignment: center;\n"
" }")
        self.tabWidget.setIconSize(QSize(50, 50))
        self.tabWidget.setMovable(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 100, 81, 16))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtCalifProfesor = QLineEdit(self.tab_2)
        self.txtCalifProfesor.setObjectName(u"txtCalifProfesor")
        self.txtCalifProfesor.setGeometry(QRect(20, 60, 281, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.txtCalifProfesor.setFont(font1)
        self.txtCalifProfesor.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtCalifProfesor.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btnActualizarNota = QPushButton(self.tab_2)
        self.btnActualizarNota.setObjectName(u"btnActualizarNota")
        self.btnActualizarNota.setEnabled(False)
        self.btnActualizarNota.setGeometry(QRect(180, 230, 111, 28))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnActualizarNota.setFont(font2)
        self.btnActualizarNota.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnActualizarNota.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(182,172,28);\n"
"	border: 2px solid rgb(222,209,23);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(222,209,23);\n"
"	border:2px solid rgb(182,172,28);\n"
"}\n"
"\n"
"\n"
"")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 40, 81, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActIII = QDoubleSpinBox(self.tab_2)
        self.cbxActIII.setObjectName(u"cbxActIII")
        self.cbxActIII.setGeometry(QRect(730, 180, 121, 22))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.cbxActIII.setFont(font3)
        self.cbxActIII.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActIII.setMaximum(10.000000000000000)
        self.cbxActII = QDoubleSpinBox(self.tab_2)
        self.cbxActII.setObjectName(u"cbxActII")
        self.cbxActII.setGeometry(QRect(575, 180, 121, 22))
        self.cbxActII.setFont(font3)
        self.cbxActII.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActII.setMaximum(10.000000000000000)
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(575, 160, 141, 16))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnAgregarNota = QPushButton(self.tab_2)
        self.btnAgregarNota.setObjectName(u"btnAgregarNota")
        self.btnAgregarNota.setGeometry(QRect(20, 230, 141, 28))
        self.btnAgregarNota.setFont(font2)
        self.btnAgregarNota.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarNota.setStyleSheet(u"QPushButton\n"
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
"\n"
"")
        self.txtBuscarRegistroNota = QLineEdit(self.tab_2)
        self.txtBuscarRegistroNota.setObjectName(u"txtBuscarRegistroNota")
        self.txtBuscarRegistroNota.setGeometry(QRect(490, 312, 301, 21))
        self.txtBuscarRegistroNota.setFont(font1)
        self.txtBuscarRegistroNota.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtBuscarRegistroNota.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbxCalifMateria = QComboBox(self.tab_2)
        self.cbxCalifMateria.setObjectName(u"cbxCalifMateria")
        self.cbxCalifMateria.setGeometry(QRect(420, 60, 281, 25))
        self.cbxCalifMateria.setFont(font3)
        self.cbxCalifMateria.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 81, 16))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxCalifGrados = QComboBox(self.tab_2)
        self.cbxCalifGrados.setObjectName(u"cbxCalifGrados")
        self.cbxCalifGrados.setGeometry(QRect(20, 120, 281, 25))
        self.cbxCalifGrados.setFont(font3)
        self.cbxCalifGrados.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(730, 160, 141, 16))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActI = QDoubleSpinBox(self.tab_2)
        self.cbxActI.setObjectName(u"cbxActI")
        self.cbxActI.setGeometry(QRect(420, 180, 121, 22))
        self.cbxActI.setFont(font3)
        self.cbxActI.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActI.setMaximum(10.000000000000000)
        self.btnEliminarRegistroNota = QPushButton(self.tab_2)
        self.btnEliminarRegistroNota.setObjectName(u"btnEliminarRegistroNota")
        self.btnEliminarRegistroNota.setGeometry(QRect(820, 420, 101, 28))
        self.btnEliminarRegistroNota.setFont(font2)
        self.btnEliminarRegistroNota.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminarRegistroNota.setStyleSheet(u"QPushButton\n"
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
"\n"
"\n"
"")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 160, 131, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 131, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(430, 305, 51, 31))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(144, 150, 155);\n"
"	border: 2px solid rgb(91,92,93);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(91,92,93);\n"
"	border:2px solid rgb(144, 150, 155);\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.cbxCalifPeriodo = QComboBox(self.tab_2)
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.setObjectName(u"cbxCalifPeriodo")
        self.cbxCalifPeriodo.setGeometry(QRect(420, 120, 281, 25))
        self.cbxCalifPeriodo.setFont(font3)
        self.cbxCalifPeriodo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 10, 161, 21))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtCalifEstudiante = QLineEdit(self.tab_2)
        self.txtCalifEstudiante.setObjectName(u"txtCalifEstudiante")
        self.txtCalifEstudiante.setGeometry(QRect(20, 180, 281, 21))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.txtCalifEstudiante.setFont(font4)
        self.txtCalifEstudiante.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"	color: rgb(32, 194, 243);\n"
"}\n"
"")
        self.txtCalifEstudiante.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 160, 171, 16))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnCancelEditNota = QPushButton(self.tab_2)
        self.btnCancelEditNota.setObjectName(u"btnCancelEditNota")
        self.btnCancelEditNota.setEnabled(False)
        self.btnCancelEditNota.setGeometry(QRect(310, 230, 111, 28))
        self.btnCancelEditNota.setFont(font2)
        self.btnCancelEditNota.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelEditNota.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background: rgb(7,172,185);\n"
"	border: 2px solid rgb(11,227,244);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(11,227,244);\n"
"	border:2px solid rgb(7,172,185);\n"
"}\n"
"\n"
"\n"
"")
        self.btnExportExcel = QPushButton(self.tab_2)
        self.btnExportExcel.setObjectName(u"btnExportExcel")
        self.btnExportExcel.setGeometry(QRect(450, 230, 141, 28))
        self.btnExportExcel.setFont(font2)
        self.btnExportExcel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExportExcel.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background: rgb(14,133,88);\n"
"	border: 2px solid rgb(10,169,109);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(10,169,109);\n"
"	border:2px solid rgb(14,133,88);\n"
"}\n"
"\n"
"\n"
"")
        self.btnEditarCalifSelectEstudiante = QPushButton(self.tab_2)
        self.btnEditarCalifSelectEstudiante.setObjectName(u"btnEditarCalifSelectEstudiante")
        self.btnEditarCalifSelectEstudiante.setGeometry(QRect(820, 380, 101, 28))
        self.btnEditarCalifSelectEstudiante.setFont(font2)
        self.btnEditarCalifSelectEstudiante.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditarCalifSelectEstudiante.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(9,167,48);\n"
"	border: 2px solid rgb(38,204,78);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(38,204,78);\n"
"	border:2px solid rgb(9,167,48);\n"
"}\n"
"\n"
"\n"
"")
        self.btnRefreshRegistroNotas = QPushButton(self.tab_2)
        self.btnRefreshRegistroNotas.setObjectName(u"btnRefreshRegistroNotas")
        self.btnRefreshRegistroNotas.setGeometry(QRect(820, 460, 101, 28))
        self.btnRefreshRegistroNotas.setFont(font2)
        self.btnRefreshRegistroNotas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRefreshRegistroNotas.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(96,99,99);\n"
"	border: 2px solid rgb(143,158,159);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(143,158,159);\n"
"	border:2px solid rgb(96,99,99);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assets/img/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRefreshRegistroNotas.setIcon(icon2)
        self.btnRefreshRegistroNotas.setIconSize(QSize(16, 16))
        self.cbxVerNotasPeriodo = QComboBox(self.tab_2)
        self.cbxVerNotasPeriodo.setObjectName(u"cbxVerNotasPeriodo")
        self.cbxVerNotasPeriodo.setGeometry(QRect(20, 308, 161, 25))
        self.cbxVerNotasPeriodo.setFont(font3)
        self.cbxVerNotasPeriodo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 290, 191, 16))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tblListRegistroNotas = QTableWidget(self.tab_2)
        if (self.tblListRegistroNotas.columnCount() < 10):
            self.tblListRegistroNotas.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblListRegistroNotas.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tblListRegistroNotas.setObjectName(u"tblListRegistroNotas")
        self.tblListRegistroNotas.setEnabled(True)
        self.tblListRegistroNotas.setGeometry(QRect(10, 340, 801, 251))
        self.tblListRegistroNotas.setStyleSheet(u"QWidget{\n"
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
        self.tblListRegistroNotas.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tblListRegistroNotas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(230, 292, 191, 16))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxVerMateriaPeriodo = QComboBox(self.tab_2)
        self.cbxVerMateriaPeriodo.setObjectName(u"cbxVerMateriaPeriodo")
        self.cbxVerMateriaPeriodo.setGeometry(QRect(230, 310, 161, 25))
        self.cbxVerMateriaPeriodo.setFont(font3)
        self.cbxVerMateriaPeriodo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.txtidCalificacion = QLabel(self.tab_2)
        self.txtidCalificacion.setObjectName(u"txtidCalificacion")
        self.txtidCalificacion.setGeometry(QRect(640, 30, 47, 13))
        self.txtidCalificacion.setStyleSheet(u"color:  rgb(40, 40, 40);")
        self.btnBorrarDb = QPushButton(self.tab_2)
        self.btnBorrarDb.setObjectName(u"btnBorrarDb")
        self.btnBorrarDb.setEnabled(True)
        self.btnBorrarDb.setGeometry(QRect(820, 530, 91, 51))
        self.btnBorrarDb.setFont(font2)
        self.btnBorrarDb.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBorrarDb.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background: rgb(250,10,69);\n"
"	border: 2px solid rgb(188,48,82);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(188,48,82);\n"
"	border:2px solid rgb(250,10,69);\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assets/img/warning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBorrarDb.setIcon(icon3)
        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 270, 881, 16))
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.btnVerNotasEstudiante = QPushButton(self.tab_2)
        self.btnVerNotasEstudiante.setObjectName(u"btnVerNotasEstudiante")
        self.btnVerNotasEstudiante.setGeometry(QRect(820, 340, 101, 28))
        self.btnVerNotasEstudiante.setFont(font2)
        self.btnVerNotasEstudiante.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVerNotasEstudiante.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(40,160,162);\n"
"	border: 2px solid rgb(36,195,197);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(36,195,197);\n"
"	border:2px solid rgb(40,160,162);\n"
"}\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"./assets/img/notas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tblListEstud = QTableWidget(self.tab_3)
        if (self.tblListEstud.columnCount() < 3):
            self.tblListEstud.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblListEstud.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblListEstud.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblListEstud.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.tblListEstud.setObjectName(u"tblListEstud")
        self.tblListEstud.setEnabled(True)
        self.tblListEstud.setGeometry(QRect(10, 290, 791, 301))
        self.tblListEstud.setStyleSheet(u"QWidget{\n"
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
        self.tblListEstud.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tblListEstud.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 40, 81, 16))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtRegNomEstud = QLineEdit(self.tab_3)
        self.txtRegNomEstud.setObjectName(u"txtRegNomEstud")
        self.txtRegNomEstud.setGeometry(QRect(20, 60, 281, 21))
        self.txtRegNomEstud.setFont(font1)
        self.txtRegNomEstud.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtRegNomEstud.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtRegNieEstud = QLineEdit(self.tab_3)
        self.txtRegNieEstud.setObjectName(u"txtRegNieEstud")
        self.txtRegNieEstud.setGeometry(QRect(20, 130, 281, 21))
        self.txtRegNieEstud.setFont(font1)
        self.txtRegNieEstud.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtRegNieEstud.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 110, 81, 16))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtBuscarEstuds = QLineEdit(self.tab_3)
        self.txtBuscarEstuds.setObjectName(u"txtBuscarEstuds")
        self.txtBuscarEstuds.setGeometry(QRect(70, 265, 281, 21))
        self.txtBuscarEstuds.setFont(font1)
        self.txtBuscarEstuds.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtBuscarEstuds.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 255, 51, 31))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(144, 150, 155);\n"
"	border: 2px solid rgb(91,92,93);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(91,92,93);\n"
"	border:2px solid rgb(144, 150, 155);\n"
"}\n"
"\n"
"")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(25, 25))
        self.btnAgregarEstud = QPushButton(self.tab_3)
        self.btnAgregarEstud.setObjectName(u"btnAgregarEstud")
        self.btnAgregarEstud.setGeometry(QRect(340, 120, 81, 28))
        self.btnAgregarEstud.setFont(font2)
        self.btnAgregarEstud.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarEstud.setStyleSheet(u"QPushButton\n"
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
        self.btnEditSelectEstud = QPushButton(self.tab_3)
        self.btnEditSelectEstud.setObjectName(u"btnEditSelectEstud")
        self.btnEditSelectEstud.setGeometry(QRect(810, 290, 111, 28))
        self.btnEditSelectEstud.setFont(font2)
        self.btnEditSelectEstud.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditSelectEstud.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(9,167,48);\n"
"	border: 2px solid rgb(38,204,78);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(38,204,78);\n"
"	border:2px solid rgb(9,167,48);\n"
"}\n"
"\n"
"\n"
"")
        self.btnEliminarEstud = QPushButton(self.tab_3)
        self.btnEliminarEstud.setObjectName(u"btnEliminarEstud")
        self.btnEliminarEstud.setGeometry(QRect(810, 330, 111, 28))
        self.btnEliminarEstud.setFont(font2)
        self.btnEliminarEstud.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminarEstud.setStyleSheet(u"QPushButton\n"
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
        self.btnActualizarEstud = QPushButton(self.tab_3)
        self.btnActualizarEstud.setObjectName(u"btnActualizarEstud")
        self.btnActualizarEstud.setEnabled(False)
        self.btnActualizarEstud.setGeometry(QRect(440, 120, 101, 28))
        self.btnActualizarEstud.setFont(font2)
        self.btnActualizarEstud.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnActualizarEstud.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(182,172,28);\n"
"	border: 2px solid rgb(222,209,23);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(222,209,23);\n"
"	border:2px solid rgb(182,172,28);\n"
"}\n"
"\n"
"\n"
"")
        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(350, 10, 201, 21))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.tab_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(340, 40, 81, 16))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxRegGradoEstud = QComboBox(self.tab_3)
        self.cbxRegGradoEstud.setObjectName(u"cbxRegGradoEstud")
        self.cbxRegGradoEstud.setGeometry(QRect(340, 60, 281, 25))
        self.cbxRegGradoEstud.setFont(font3)
        self.cbxRegGradoEstud.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnCancelEstud = QPushButton(self.tab_3)
        self.btnCancelEstud.setObjectName(u"btnCancelEstud")
        self.btnCancelEstud.setEnabled(False)
        self.btnCancelEstud.setGeometry(QRect(560, 120, 91, 28))
        self.btnCancelEstud.setFont(font2)
        self.btnCancelEstud.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelEstud.setStyleSheet(u"QPushButton\n"
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
        self.lblEstudianteToEdit = QLabel(self.tab_3)
        self.lblEstudianteToEdit.setObjectName(u"lblEstudianteToEdit")
        self.lblEstudianteToEdit.setGeometry(QRect(580, 20, 47, 13))
        self.lblEstudianteToEdit.setStyleSheet(u"color:  rgb(40, 40, 40);")
        self.label_31 = QLabel(self.tab_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 200, 161, 16))
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxVerEstudiantesDeRegEst = QComboBox(self.tab_3)
        self.cbxVerEstudiantesDeRegEst.setObjectName(u"cbxVerEstudiantesDeRegEst")
        self.cbxVerEstudiantesDeRegEst.setGeometry(QRect(20, 220, 281, 25))
        self.cbxVerEstudiantesDeRegEst.setFont(font3)
        self.cbxVerEstudiantesDeRegEst.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnRefreshEstudiantes = QPushButton(self.tab_3)
        self.btnRefreshEstudiantes.setObjectName(u"btnRefreshEstudiantes")
        self.btnRefreshEstudiantes.setGeometry(QRect(810, 370, 111, 28))
        self.btnRefreshEstudiantes.setFont(font2)
        self.btnRefreshEstudiantes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRefreshEstudiantes.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(96,99,99);\n"
"	border: 2px solid rgb(143,158,159);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(143,158,159);\n"
"	border:2px solid rgb(96,99,99);\n"
"}\n"
"\n"
"")
        self.btnRefreshEstudiantes.setIcon(icon2)
        self.btnRefreshEstudiantes.setIconSize(QSize(16, 16))
        self.line_2 = QFrame(self.tab_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 170, 891, 16))
        self.line_2.setMidLineWidth(4)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        icon5 = QIcon()
        icon5.addFile(u"./assets/img/estudiantes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tblListGrados = QTableWidget(self.tab_4)
        if (self.tblListGrados.columnCount() < 3):
            self.tblListGrados.setColumnCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblListGrados.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblListGrados.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblListGrados.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        self.tblListGrados.setObjectName(u"tblListGrados")
        self.tblListGrados.setEnabled(True)
        self.tblListGrados.setGeometry(QRect(350, 90, 451, 161))
        self.tblListGrados.setStyleSheet(u"QWidget{\n"
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
        self.tblListGrados.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tblListGrados.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.txtRegGrado = QLineEdit(self.tab_4)
        self.txtRegGrado.setObjectName(u"txtRegGrado")
        self.txtRegGrado.setGeometry(QRect(20, 60, 291, 21))
        self.txtRegGrado.setFont(font1)
        self.txtRegGrado.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtRegGrado.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btnAgregarGrado = QPushButton(self.tab_4)
        self.btnAgregarGrado.setObjectName(u"btnAgregarGrado")
        self.btnAgregarGrado.setGeometry(QRect(20, 180, 81, 28))
        self.btnAgregarGrado.setFont(font2)
        self.btnAgregarGrado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarGrado.setStyleSheet(u"QPushButton\n"
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
"\n"
"\n"
"")
        self.label_25 = QLabel(self.tab_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 40, 81, 16))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnActualizarGrado = QPushButton(self.tab_4)
        self.btnActualizarGrado.setObjectName(u"btnActualizarGrado")
        self.btnActualizarGrado.setEnabled(False)
        self.btnActualizarGrado.setGeometry(QRect(110, 180, 101, 28))
        self.btnActualizarGrado.setFont(font2)
        self.btnActualizarGrado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnActualizarGrado.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(182,172,28);\n"
"	border: 2px solid rgb(222,209,23);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(222,209,23);\n"
"	border:2px solid rgb(182,172,28);\n"
"}\n"
"")
        self.pushButton_28 = QPushButton(self.tab_4)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(350, 55, 51, 31))
        self.pushButton_28.setFont(font2)
        self.pushButton_28.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(144, 150, 155);\n"
"	border: 2px solid rgb(91,92,93);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(91,92,93);\n"
"	border:2px solid rgb(144, 150, 155);\n"
"}\n"
"\n"
"")
        self.pushButton_28.setIcon(icon1)
        self.pushButton_28.setIconSize(QSize(25, 25))
        self.btnGradoEdit = QPushButton(self.tab_4)
        self.btnGradoEdit.setObjectName(u"btnGradoEdit")
        self.btnGradoEdit.setGeometry(QRect(810, 90, 111, 28))
        self.btnGradoEdit.setFont(font2)
        self.btnGradoEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGradoEdit.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(9,167,48);\n"
"	border: 2px solid rgb(38,204,78);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(38,204,78);\n"
"	border:2px solid rgb(9,167,48);\n"
"}\n"
"\n"
"")
        self.label_28 = QLabel(self.tab_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(350, 10, 201, 21))
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnGradoEliminar = QPushButton(self.tab_4)
        self.btnGradoEliminar.setObjectName(u"btnGradoEliminar")
        self.btnGradoEliminar.setGeometry(QRect(810, 130, 111, 28))
        self.btnGradoEliminar.setFont(font2)
        self.btnGradoEliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGradoEliminar.setStyleSheet(u"QPushButton\n"
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
"\n"
"")
        self.label_29 = QLabel(self.tab_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 110, 81, 16))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtSearchGrado = QLineEdit(self.tab_4)
        self.txtSearchGrado.setObjectName(u"txtSearchGrado")
        self.txtSearchGrado.setGeometry(QRect(405, 65, 181, 21))
        self.txtSearchGrado.setFont(font1)
        self.txtSearchGrado.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtSearchGrado.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbxRegSeccion = QComboBox(self.tab_4)
        self.cbxRegSeccion.addItem("")
        self.cbxRegSeccion.addItem("")
        self.cbxRegSeccion.addItem("")
        self.cbxRegSeccion.addItem("")
        self.cbxRegSeccion.setObjectName(u"cbxRegSeccion")
        self.cbxRegSeccion.setGeometry(QRect(20, 130, 291, 25))
        self.cbxRegSeccion.setFont(font3)
        self.cbxRegSeccion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnCancelGrado = QPushButton(self.tab_4)
        self.btnCancelGrado.setObjectName(u"btnCancelGrado")
        self.btnCancelGrado.setEnabled(False)
        self.btnCancelGrado.setGeometry(QRect(220, 180, 91, 28))
        self.btnCancelGrado.setFont(font2)
        self.btnCancelGrado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelGrado.setStyleSheet(u"QPushButton\n"
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
        self.lblIdGradoEdit = QLabel(self.tab_4)
        self.lblIdGradoEdit.setObjectName(u"lblIdGradoEdit")
        self.lblIdGradoEdit.setGeometry(QRect(590, 20, 47, 13))
        self.lblIdGradoEdit.setStyleSheet(u"color:  rgb(40, 40, 40);")
        self.txtBuscarEstudsRegGrados = QLineEdit(self.tab_4)
        self.txtBuscarEstudsRegGrados.setObjectName(u"txtBuscarEstudsRegGrados")
        self.txtBuscarEstudsRegGrados.setGeometry(QRect(70, 285, 281, 21))
        self.txtBuscarEstudsRegGrados.setFont(font1)
        self.txtBuscarEstudsRegGrados.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtBuscarEstudsRegGrados.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.pushButton_7 = QPushButton(self.tab_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 275, 51, 31))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(144, 150, 155);\n"
"	border: 2px solid rgb(91,92,93);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(91,92,93);\n"
"	border:2px solid rgb(144, 150, 155);\n"
"}\n"
"\n"
"")
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(25, 25))
        self.tblListEstudRegGrados = QTableWidget(self.tab_4)
        if (self.tblListEstudRegGrados.columnCount() < 3):
            self.tblListEstudRegGrados.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblListEstudRegGrados.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblListEstudRegGrados.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblListEstudRegGrados.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        self.tblListEstudRegGrados.setObjectName(u"tblListEstudRegGrados")
        self.tblListEstudRegGrados.setEnabled(True)
        self.tblListEstudRegGrados.setGeometry(QRect(10, 310, 781, 281))
        self.tblListEstudRegGrados.setStyleSheet(u"QWidget{\n"
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
        self.tblListEstudRegGrados.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tblListEstudRegGrados.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btnRefreshGrados = QPushButton(self.tab_4)
        self.btnRefreshGrados.setObjectName(u"btnRefreshGrados")
        self.btnRefreshGrados.setGeometry(QRect(810, 170, 111, 28))
        self.btnRefreshGrados.setFont(font2)
        self.btnRefreshGrados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRefreshGrados.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(96,99,99);\n"
"	border: 2px solid rgb(143,158,159);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(143,158,159);\n"
"	border:2px solid rgb(96,99,99);\n"
"}\n"
"\n"
"")
        self.btnRefreshGrados.setIcon(icon2)
        self.btnRefreshGrados.setIconSize(QSize(16, 16))
        self.line_3 = QFrame(self.tab_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 255, 891, 16))
        self.line_3.setMidLineWidth(4)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        icon6 = QIcon()
        icon6.addFile(u"./assets/img/grados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon6, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tblListMaterias = QTableWidget(self.tab)
        if (self.tblListMaterias.columnCount() < 2):
            self.tblListMaterias.setColumnCount(2)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tblListMaterias.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tblListMaterias.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        self.tblListMaterias.setObjectName(u"tblListMaterias")
        self.tblListMaterias.setEnabled(True)
        self.tblListMaterias.setGeometry(QRect(430, 285, 371, 311))
        self.tblListMaterias.setStyleSheet(u"QWidget{\n"
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
        self.tblListMaterias.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tblListMaterias.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.txtRegMateria = QLineEdit(self.tab)
        self.txtRegMateria.setObjectName(u"txtRegMateria")
        self.txtRegMateria.setGeometry(QRect(20, 60, 291, 21))
        self.txtRegMateria.setFont(font1)
        self.txtRegMateria.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtRegMateria.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.btnAgregarMateria = QPushButton(self.tab)
        self.btnAgregarMateria.setObjectName(u"btnAgregarMateria")
        self.btnAgregarMateria.setGeometry(QRect(20, 180, 81, 28))
        self.btnAgregarMateria.setFont(font2)
        self.btnAgregarMateria.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAgregarMateria.setStyleSheet(u"QPushButton\n"
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
        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 40, 81, 16))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnActualizarMateria = QPushButton(self.tab)
        self.btnActualizarMateria.setObjectName(u"btnActualizarMateria")
        self.btnActualizarMateria.setEnabled(False)
        self.btnActualizarMateria.setGeometry(QRect(120, 180, 101, 28))
        self.btnActualizarMateria.setFont(font2)
        self.btnActualizarMateria.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnActualizarMateria.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(182,172,28);\n"
"	border: 2px solid rgb(222,209,23);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:rgb(222,209,23);\n"
"	border:2px solid rgb(182,172,28);\n"
"}\n"
"")
        self.btnMateriaEdit = QPushButton(self.tab)
        self.btnMateriaEdit.setObjectName(u"btnMateriaEdit")
        self.btnMateriaEdit.setGeometry(QRect(810, 290, 111, 28))
        self.btnMateriaEdit.setFont(font2)
        self.btnMateriaEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMateriaEdit.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(9,167,48);\n"
"	border: 2px solid rgb(38,204,78);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(38,204,78);\n"
"	border:2px solid rgb(9,167,48);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label_27 = QLabel(self.tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(350, 10, 201, 21))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnEliminarMateria = QPushButton(self.tab)
        self.btnEliminarMateria.setObjectName(u"btnEliminarMateria")
        self.btnEliminarMateria.setGeometry(QRect(810, 330, 111, 28))
        self.btnEliminarMateria.setFont(font2)
        self.btnEliminarMateria.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEliminarMateria.setStyleSheet(u"QPushButton\n"
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
        self.label_24 = QLabel(self.tab)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 110, 81, 16))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxRegMatGrado = QComboBox(self.tab)
        self.cbxRegMatGrado.addItem("")
        self.cbxRegMatGrado.addItem("")
        self.cbxRegMatGrado.setObjectName(u"cbxRegMatGrado")
        self.cbxRegMatGrado.setGeometry(QRect(20, 130, 291, 25))
        self.cbxRegMatGrado.setFont(font3)
        self.cbxRegMatGrado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnCancelMateriaEdit = QPushButton(self.tab)
        self.btnCancelMateriaEdit.setObjectName(u"btnCancelMateriaEdit")
        self.btnCancelMateriaEdit.setEnabled(False)
        self.btnCancelMateriaEdit.setGeometry(QRect(240, 180, 91, 28))
        self.btnCancelMateriaEdit.setFont(font2)
        self.btnCancelMateriaEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelMateriaEdit.setStyleSheet(u"QPushButton\n"
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
        self.lblMateriaToEdit = QLabel(self.tab)
        self.lblMateriaToEdit.setObjectName(u"lblMateriaToEdit")
        self.lblMateriaToEdit.setGeometry(QRect(580, 20, 47, 16))
        self.lblMateriaToEdit.setStyleSheet(u"color:  rgb(40, 40, 40);")
        self.tblListGradosRegMateria = QTableWidget(self.tab)
        if (self.tblListGradosRegMateria.columnCount() < 2):
            self.tblListGradosRegMateria.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tblListGradosRegMateria.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblListGradosRegMateria.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        if (self.tblListGradosRegMateria.rowCount() < 2):
            self.tblListGradosRegMateria.setRowCount(2)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tblListGradosRegMateria.setVerticalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tblListGradosRegMateria.setVerticalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblListGradosRegMateria.setItem(0, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tblListGradosRegMateria.setItem(0, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tblListGradosRegMateria.setItem(1, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tblListGradosRegMateria.setItem(1, 1, __qtablewidgetitem28)
        self.tblListGradosRegMateria.setObjectName(u"tblListGradosRegMateria")
        self.tblListGradosRegMateria.setEnabled(True)
        self.tblListGradosRegMateria.setGeometry(QRect(10, 285, 401, 311))
        self.tblListGradosRegMateria.setStyleSheet(u"QWidget{\n"
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
        self.tblListGradosRegMateria.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tblListGradosRegMateria.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btnRefreshMaterias = QPushButton(self.tab)
        self.btnRefreshMaterias.setObjectName(u"btnRefreshMaterias")
        self.btnRefreshMaterias.setGeometry(QRect(810, 370, 111, 28))
        self.btnRefreshMaterias.setFont(font2)
        self.btnRefreshMaterias.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRefreshMaterias.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(96,99,99);\n"
"	border: 2px solid rgb(143,158,159);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(143,158,159);\n"
"	border:2px solid rgb(96,99,99);\n"
"}\n"
"\n"
"")
        self.btnRefreshMaterias.setIcon(icon2)
        self.btnRefreshMaterias.setIconSize(QSize(16, 16))
        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 230, 891, 16))
        self.line_4.setMidLineWidth(4)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        icon7 = QIcon()
        icon7.addFile(u"./assets/img/materias.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon7, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.WidgetCentral)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro De Notas", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Trimestre", None))
        self.txtCalifProfesor.setText("")
        self.txtCalifProfesor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.btnActualizarNota.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Materia", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Actividad II (35%)", None))
        self.btnAgregarNota.setText(QCoreApplication.translate("MainWindow", u"Agregar Nota", None))
        self.txtBuscarRegistroNota.setText("")
        self.txtBuscarRegistroNota.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Profesor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Actividad III (30%)", None))
        self.btnEliminarRegistroNota.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Actividad I (35%)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Grado a calificar", None))
        self.pushButton_5.setText("")
        self.cbxCalifPeriodo.setItemText(0, QCoreApplication.translate("MainWindow", u"I", None))
        self.cbxCalifPeriodo.setItemText(1, QCoreApplication.translate("MainWindow", u"II", None))
        self.cbxCalifPeriodo.setItemText(2, QCoreApplication.translate("MainWindow", u"III", None))
        self.cbxCalifPeriodo.setItemText(3, QCoreApplication.translate("MainWindow", u"IIII", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Registro De Notas", None))
        self.txtCalifEstudiante.setText("")
        self.txtCalifEstudiante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Estudiante a calificar", None))
        self.btnCancelEditNota.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btnExportExcel.setText(QCoreApplication.translate("MainWindow", u"Exportar Excel", None))
        self.btnEditarCalifSelectEstudiante.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnRefreshRegistroNotas.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ver Notas del Trimestre", None))
        ___qtablewidgetitem = self.tblListRegistroNotas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tblListRegistroNotas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cod", None));
        ___qtablewidgetitem2 = self.tblListRegistroNotas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Estudiante", None));
        ___qtablewidgetitem3 = self.tblListRegistroNotas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Act I", None));
        ___qtablewidgetitem4 = self.tblListRegistroNotas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"(35%)", None));
        ___qtablewidgetitem5 = self.tblListRegistroNotas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Act II", None));
        ___qtablewidgetitem6 = self.tblListRegistroNotas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"(35%)", None));
        ___qtablewidgetitem7 = self.tblListRegistroNotas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Examen", None));
        ___qtablewidgetitem8 = self.tblListRegistroNotas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"(30%)", None));
        ___qtablewidgetitem9 = self.tblListRegistroNotas.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Promedio", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ver Materia", None))
        self.txtidCalificacion.setText("")
        self.btnBorrarDb.setText(QCoreApplication.translate("MainWindow", u"Borrar \n"
" Datos", None))
        self.btnVerNotasEstudiante.setText(QCoreApplication.translate("MainWindow", u"Ver notas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        ___qtablewidgetitem10 = self.tblListEstud.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem11 = self.tblListEstud.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Estudiante", None));
        ___qtablewidgetitem12 = self.tblListEstud.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"NIE", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.txtRegNomEstud.setText("")
        self.txtRegNomEstud.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.txtRegNieEstud.setText("")
        self.txtRegNieEstud.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.txtBuscarEstuds.setText("")
        self.txtBuscarEstuds.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.pushButton_6.setText("")
        self.btnAgregarEstud.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnEditSelectEstud.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnEliminarEstud.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnActualizarEstud.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Registro De Estudiantes", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.btnCancelEstud.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lblEstudianteToEdit.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Ver Estudiantes de:", None))
        self.btnRefreshEstudiantes.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
        ___qtablewidgetitem13 = self.tblListGrados.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem14 = self.tblListGrados.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Grado", None));
        ___qtablewidgetitem15 = self.tblListGrados.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Secci\u00f3n", None));
        self.txtRegGrado.setText("")
        self.txtRegGrado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bachillerato ...", None))
        self.btnAgregarGrado.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.btnActualizarGrado.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.pushButton_28.setText("")
        self.btnGradoEdit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Registro De Grados", None))
        self.btnGradoEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Secci\u00f3n", None))
        self.txtSearchGrado.setText("")
        self.txtSearchGrado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"9 Grado", None))
        self.cbxRegSeccion.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.cbxRegSeccion.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.cbxRegSeccion.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.cbxRegSeccion.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))

        self.btnCancelGrado.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lblIdGradoEdit.setText("")
        self.txtBuscarEstudsRegGrados.setText("")
        self.txtBuscarEstudsRegGrados.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.pushButton_7.setText("")
        ___qtablewidgetitem16 = self.tblListEstudRegGrados.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem17 = self.tblListEstudRegGrados.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Estudiante", None));
        ___qtablewidgetitem18 = self.tblListEstudRegGrados.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"NIE", None));
        self.btnRefreshGrados.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "")
        ___qtablewidgetitem19 = self.tblListMaterias.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem20 = self.tblListMaterias.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Materia", None));
        self.txtRegMateria.setText("")
        self.txtRegMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sociales", None))
        self.btnAgregarMateria.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Materia", None))
        self.btnActualizarMateria.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnMateriaEdit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Registro De Materias", None))
        self.btnEliminarMateria.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.cbxRegMatGrado.setItemText(0, QCoreApplication.translate("MainWindow", u"1 2 3 Ciclo", None))
        self.cbxRegMatGrado.setItemText(1, QCoreApplication.translate("MainWindow", u"Bachillerato", None))

        self.btnCancelMateriaEdit.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lblMateriaToEdit.setText("")
        ___qtablewidgetitem21 = self.tblListGradosRegMateria.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem22 = self.tblListGradosRegMateria.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Ciclo", None));
        ___qtablewidgetitem23 = self.tblListGradosRegMateria.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem24 = self.tblListGradosRegMateria.verticalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tblListGradosRegMateria.isSortingEnabled()
        self.tblListGradosRegMateria.setSortingEnabled(False)
        ___qtablewidgetitem25 = self.tblListGradosRegMateria.item(0, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.tblListGradosRegMateria.item(0, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"1 2 3 Ciclo", None));
        ___qtablewidgetitem27 = self.tblListGradosRegMateria.item(1, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem28 = self.tblListGradosRegMateria.item(1, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Bachillerato", None));
        self.tblListGradosRegMateria.setSortingEnabled(__sortingEnabled)

        self.btnRefreshMaterias.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
    # retranslateUi

