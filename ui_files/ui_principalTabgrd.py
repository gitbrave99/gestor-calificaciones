# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principalTabgrd.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 662)
        icon = QIcon()
        icon.addFile(u"../assets/img/registronotas.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.label_4.setGeometry(QRect(420, 120, 81, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtCalifProfesor = QLineEdit(self.tab_2)
        self.txtCalifProfesor.setObjectName(u"txtCalifProfesor")
        self.txtCalifProfesor.setGeometry(QRect(10, 80, 281, 21))
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
        self.btnActualizarNota.setGeometry(QRect(180, 250, 111, 28))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
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
        self.label_2.setGeometry(QRect(420, 60, 81, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActIII = QDoubleSpinBox(self.tab_2)
        self.cbxActIII.setObjectName(u"cbxActIII")
        self.cbxActIII.setGeometry(QRect(700, 210, 121, 22))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.cbxActIII.setFont(font3)
        self.cbxActIII.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActII = QDoubleSpinBox(self.tab_2)
        self.cbxActII.setObjectName(u"cbxActII")
        self.cbxActII.setGeometry(QRect(560, 210, 121, 22))
        self.cbxActII.setFont(font3)
        self.cbxActII.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(560, 190, 131, 16))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnAgregarNota = QPushButton(self.tab_2)
        self.btnAgregarNota.setObjectName(u"btnAgregarNota")
        self.btnAgregarNota.setGeometry(QRect(20, 250, 141, 28))
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
        self.txtBuscarRegistroNota.setGeometry(QRect(420, 300, 281, 21))
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
        self.cbxCalifMateria.addItem("")
        self.cbxCalifMateria.addItem("")
        self.cbxCalifMateria.addItem("")
        self.cbxCalifMateria.setObjectName(u"cbxCalifMateria")
        self.cbxCalifMateria.setGeometry(QRect(420, 80, 281, 25))
        self.cbxCalifMateria.setFont(font3)
        self.cbxCalifMateria.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 81, 16))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxCalifGrados = QComboBox(self.tab_2)
        self.cbxCalifGrados.addItem("")
        self.cbxCalifGrados.addItem("")
        self.cbxCalifGrados.setObjectName(u"cbxCalifGrados")
        self.cbxCalifGrados.setGeometry(QRect(10, 140, 281, 25))
        self.cbxCalifGrados.setFont(font3)
        self.cbxCalifGrados.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(700, 190, 141, 16))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxActI = QDoubleSpinBox(self.tab_2)
        self.cbxActI.setObjectName(u"cbxActI")
        self.cbxActI.setGeometry(QRect(420, 210, 121, 22))
        self.cbxActI.setFont(font3)
        self.cbxActI.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnEliminarRegistroNota = QPushButton(self.tab_2)
        self.btnEliminarRegistroNota.setObjectName(u"btnEliminarRegistroNota")
        self.btnEliminarRegistroNota.setGeometry(QRect(770, 420, 111, 28))
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
        self.btnVerNotasXEstudiante = QPushButton(self.tab_2)
        self.btnVerNotasXEstudiante.setObjectName(u"btnVerNotasXEstudiante")
        self.btnVerNotasXEstudiante.setGeometry(QRect(770, 338, 111, 28))
        self.btnVerNotasXEstudiante.setFont(font2)
        self.btnVerNotasXEstudiante.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVerNotasXEstudiante.setStyleSheet(u"QPushButton\n"
"{	\n"
"	background:rgb(18,159,165);\n"
"	border: 2px solid rgb(35,199,207);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(35,199,207);\n"
"	border:2px solid rgb(18,159,165);\n"
"}\n"
"\n"
"\n"
"")
        self.tblRegistroNotas = QTableWidget(self.tab_2)
        if (self.tblRegistroNotas.columnCount() < 5):
            self.tblRegistroNotas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblRegistroNotas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblRegistroNotas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblRegistroNotas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblRegistroNotas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblRegistroNotas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tblRegistroNotas.rowCount() < 1):
            self.tblRegistroNotas.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblRegistroNotas.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblRegistroNotas.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblRegistroNotas.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblRegistroNotas.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblRegistroNotas.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblRegistroNotas.setItem(0, 4, __qtablewidgetitem10)
        self.tblRegistroNotas.setObjectName(u"tblRegistroNotas")
        self.tblRegistroNotas.setGeometry(QRect(10, 331, 751, 251))
        self.tblRegistroNotas.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tblRegistroNotas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 190, 131, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 131, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(710, 292, 51, 31))
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
        icon1.addFile(u"../assets/img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.cbxCalifPeriodo = QComboBox(self.tab_2)
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.addItem("")
        self.cbxCalifPeriodo.setObjectName(u"cbxCalifPeriodo")
        self.cbxCalifPeriodo.setGeometry(QRect(420, 140, 281, 25))
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
        self.txtCalifEstudiante.setGeometry(QRect(10, 210, 281, 21))
        self.txtCalifEstudiante.setFont(font1)
        self.txtCalifEstudiante.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtCalifEstudiante.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 190, 81, 16))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnCancelEditNota = QPushButton(self.tab_2)
        self.btnCancelEditNota.setObjectName(u"btnCancelEditNota")
        self.btnCancelEditNota.setGeometry(QRect(310, 250, 111, 28))
        self.btnCancelEditNota.setFont(font2)
        self.btnCancelEditNota.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelEditNota.setStyleSheet(u"QPushButton\n"
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
        self.btnExportExcel = QPushButton(self.tab_2)
        self.btnExportExcel.setObjectName(u"btnExportExcel")
        self.btnExportExcel.setGeometry(QRect(450, 250, 131, 28))
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
        self.btnEditarSelectEstudiante = QPushButton(self.tab_2)
        self.btnEditarSelectEstudiante.setObjectName(u"btnEditarSelectEstudiante")
        self.btnEditarSelectEstudiante.setGeometry(QRect(770, 380, 111, 28))
        self.btnEditarSelectEstudiante.setFont(font2)
        self.btnEditarSelectEstudiante.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditarSelectEstudiante.setStyleSheet(u"QPushButton\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../assets/img/notas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tblListEstud = QTableWidget(self.tab_3)
        if (self.tblListEstud.columnCount() < 3):
            self.tblListEstud.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblListEstud.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblListEstud.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblListEstud.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        if (self.tblListEstud.rowCount() < 1):
            self.tblListEstud.setRowCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblListEstud.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblListEstud.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblListEstud.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblListEstud.setItem(0, 2, __qtablewidgetitem17)
        self.tblListEstud.setObjectName(u"tblListEstud")
        self.tblListEstud.setGeometry(QRect(10, 290, 771, 291))
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
        self.tblListEstud.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 81, 16))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtRegNomEstud = QLineEdit(self.tab_3)
        self.txtRegNomEstud.setObjectName(u"txtRegNomEstud")
        self.txtRegNomEstud.setGeometry(QRect(20, 80, 281, 21))
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
        self.txtRegNieEstud.setGeometry(QRect(20, 140, 281, 21))
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
        self.label_11.setGeometry(QRect(20, 120, 81, 16))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtBuscarEstuds = QLineEdit(self.tab_3)
        self.txtBuscarEstuds.setObjectName(u"txtBuscarEstuds")
        self.txtBuscarEstuds.setGeometry(QRect(10, 260, 281, 21))
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
        self.pushButton_6.setGeometry(QRect(300, 250, 51, 31))
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
        self.btnAgregarEstud.setGeometry(QRect(20, 180, 121, 28))
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
        self.btnEditSelectEstud.setGeometry(QRect(790, 300, 90, 28))
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
        self.btnEliminarEstud.setGeometry(QRect(790, 340, 91, 28))
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
        self.btnActualizarEstud.setGeometry(QRect(160, 180, 121, 28))
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
        self.cbxEstudOrderBy = QComboBox(self.tab_3)
        self.cbxEstudOrderBy.addItem("")
        self.cbxEstudOrderBy.addItem("")
        self.cbxEstudOrderBy.addItem("")
        self.cbxEstudOrderBy.setObjectName(u"cbxEstudOrderBy")
        self.cbxEstudOrderBy.setGeometry(QRect(580, 260, 201, 25))
        self.cbxEstudOrderBy.setFont(font3)
        self.cbxEstudOrderBy.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.label_30 = QLabel(self.tab_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(340, 60, 81, 16))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cbxRegGradoEstud = QComboBox(self.tab_3)
        self.cbxRegGradoEstud.addItem("")
        self.cbxRegGradoEstud.addItem("")
        self.cbxRegGradoEstud.addItem("")
        self.cbxRegGradoEstud.setObjectName(u"cbxRegGradoEstud")
        self.cbxRegGradoEstud.setGeometry(QRect(340, 80, 281, 25))
        self.cbxRegGradoEstud.setFont(font3)
        self.cbxRegGradoEstud.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnCancelEstud = QPushButton(self.tab_3)
        self.btnCancelEstud.setObjectName(u"btnCancelEstud")
        self.btnCancelEstud.setGeometry(QRect(310, 180, 91, 28))
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
        self.lblEstudianteToEdit.setGeometry(QRect(350, 130, 47, 13))
        icon3 = QIcon()
        icon3.addFile(u"../assets/img/estudiantes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tblListGrados = QTableWidget(self.tab_4)
        if (self.tblListGrados.columnCount() < 3):
            self.tblListGrados.setColumnCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblListGrados.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tblListGrados.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tblListGrados.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        self.tblListGrados.setObjectName(u"tblListGrados")
        self.tblListGrados.setGeometry(QRect(10, 290, 771, 291))
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
        self.tblListGrados.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cbxGradosOrderBy = QComboBox(self.tab_4)
        self.cbxGradosOrderBy.addItem("")
        self.cbxGradosOrderBy.addItem("")
        self.cbxGradosOrderBy.addItem("")
        self.cbxGradosOrderBy.setObjectName(u"cbxGradosOrderBy")
        self.cbxGradosOrderBy.setGeometry(QRect(580, 260, 201, 25))
        self.cbxGradosOrderBy.setFont(font3)
        self.cbxGradosOrderBy.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.txtRegGrado = QLineEdit(self.tab_4)
        self.txtRegGrado.setObjectName(u"txtRegGrado")
        self.txtRegGrado.setGeometry(QRect(20, 60, 281, 21))
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
        self.btnAgregarGrado.setGeometry(QRect(20, 190, 121, 28))
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
        self.btnActualizarGrado.setGeometry(QRect(160, 190, 121, 28))
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
        self.pushButton_28.setGeometry(QRect(300, 250, 51, 31))
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
        self.btnGradoEdit.setGeometry(QRect(790, 300, 90, 28))
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
        self.btnGradoEliminar.setGeometry(QRect(790, 340, 91, 28))
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
        self.label_29.setGeometry(QRect(20, 120, 81, 16))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtSearchGrado = QLineEdit(self.tab_4)
        self.txtSearchGrado.setObjectName(u"txtSearchGrado")
        self.txtSearchGrado.setGeometry(QRect(10, 260, 281, 21))
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
        self.cbxRegSeccion.setObjectName(u"cbxRegSeccion")
        self.cbxRegSeccion.setGeometry(QRect(20, 140, 281, 25))
        self.cbxRegSeccion.setFont(font3)
        self.cbxRegSeccion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnCancelGrado = QPushButton(self.tab_4)
        self.btnCancelGrado.setObjectName(u"btnCancelGrado")
        self.btnCancelGrado.setEnabled(False)
        self.btnCancelGrado.setGeometry(QRect(300, 190, 91, 28))
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
        icon4 = QIcon()
        icon4.addFile(u"../assets/img/grados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tblListMaterias = QTableWidget(self.tab)
        if (self.tblListMaterias.columnCount() < 3):
            self.tblListMaterias.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tblListMaterias.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblListMaterias.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tblListMaterias.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        if (self.tblListMaterias.rowCount() < 1):
            self.tblListMaterias.setRowCount(1)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tblListMaterias.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblListMaterias.setItem(0, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tblListMaterias.setItem(0, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tblListMaterias.setItem(0, 2, __qtablewidgetitem27)
        self.tblListMaterias.setObjectName(u"tblListMaterias")
        self.tblListMaterias.setGeometry(QRect(10, 290, 771, 291))
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
        self.tblListMaterias.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cbxMateriaOrderBy = QComboBox(self.tab)
        self.cbxMateriaOrderBy.addItem("")
        self.cbxMateriaOrderBy.addItem("")
        self.cbxMateriaOrderBy.addItem("")
        self.cbxMateriaOrderBy.setObjectName(u"cbxMateriaOrderBy")
        self.cbxMateriaOrderBy.setGeometry(QRect(580, 260, 201, 25))
        self.cbxMateriaOrderBy.setFont(font3)
        self.cbxMateriaOrderBy.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.txtRegMateria = QLineEdit(self.tab)
        self.txtRegMateria.setObjectName(u"txtRegMateria")
        self.txtRegMateria.setGeometry(QRect(20, 60, 281, 21))
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
        self.btnAgregarMateria.setGeometry(QRect(20, 180, 121, 28))
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
        self.btnActualizarMateria.setGeometry(QRect(160, 180, 121, 28))
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
        self.pushButton_23 = QPushButton(self.tab)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setEnabled(True)
        self.pushButton_23.setGeometry(QRect(300, 250, 51, 31))
        self.pushButton_23.setFont(font2)
        self.pushButton_23.setStyleSheet(u"QPushButton\n"
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
        self.pushButton_23.setIcon(icon1)
        self.pushButton_23.setIconSize(QSize(25, 25))
        self.btnMateriaEdit = QPushButton(self.tab)
        self.btnMateriaEdit.setObjectName(u"btnMateriaEdit")
        self.btnMateriaEdit.setGeometry(QRect(790, 300, 90, 28))
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
        self.btnEliminarMateria.setGeometry(QRect(790, 340, 91, 28))
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
        self.txtSearchMaterias = QLineEdit(self.tab)
        self.txtSearchMaterias.setObjectName(u"txtSearchMaterias")
        self.txtSearchMaterias.setGeometry(QRect(10, 260, 281, 21))
        self.txtSearchMaterias.setFont(font1)
        self.txtSearchMaterias.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtSearchMaterias.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbxRegMatGrado = QComboBox(self.tab)
        self.cbxRegMatGrado.addItem("")
        self.cbxRegMatGrado.addItem("")
        self.cbxRegMatGrado.addItem("")
        self.cbxRegMatGrado.setObjectName(u"cbxRegMatGrado")
        self.cbxRegMatGrado.setGeometry(QRect(20, 130, 281, 25))
        self.cbxRegMatGrado.setFont(font3)
        self.cbxRegMatGrado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btnCancelMateriaEdit = QPushButton(self.tab)
        self.btnCancelMateriaEdit.setObjectName(u"btnCancelMateriaEdit")
        self.btnCancelMateriaEdit.setGeometry(QRect(300, 180, 91, 28))
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
        icon5 = QIcon()
        icon5.addFile(u"../assets/img/materias.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.WidgetCentral)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro De Notas", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"Materias", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Periodo", None))
        self.txtCalifProfesor.setText(QCoreApplication.translate("MainWindow", u"William Armando", None))
        self.txtCalifProfesor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.btnActualizarNota.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Materia", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Actividad II (35%)", None))
        self.btnAgregarNota.setText(QCoreApplication.translate("MainWindow", u"Agregar Nota", None))
        self.txtBuscarRegistroNota.setText("")
        self.txtBuscarRegistroNota.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isamel quijada", None))
        self.cbxCalifMateria.setItemText(0, QCoreApplication.translate("MainWindow", u"Sociales", None))
        self.cbxCalifMateria.setItemText(1, QCoreApplication.translate("MainWindow", u"Matem\u00e1tica", None))
        self.cbxCalifMateria.setItemText(2, QCoreApplication.translate("MainWindow", u"Cicncias Naturales", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Profesor", None))
        self.cbxCalifGrados.setItemText(0, QCoreApplication.translate("MainWindow", u"Bachillerato General", None))
        self.cbxCalifGrados.setItemText(1, QCoreApplication.translate("MainWindow", u"Tercer Ciclo", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Actividad III (30%)", None))
        self.btnEliminarRegistroNota.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnVerNotasXEstudiante.setText(QCoreApplication.translate("MainWindow", u"Ver Notas", None))
        ___qtablewidgetitem = self.tblRegistroNotas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tblRegistroNotas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Estudiante", None));
        ___qtablewidgetitem2 = self.tblRegistroNotas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Act I (35%)", None));
        ___qtablewidgetitem3 = self.tblRegistroNotas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Act II (35%)", None));
        ___qtablewidgetitem4 = self.tblRegistroNotas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Act III (30%)", None));
        ___qtablewidgetitem5 = self.tblRegistroNotas.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tblRegistroNotas.isSortingEnabled()
        self.tblRegistroNotas.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tblRegistroNotas.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.tblRegistroNotas.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Salina Monterrosa, Tifanny Lizbeth", None));
        ___qtablewidgetitem8 = self.tblRegistroNotas.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem9 = self.tblRegistroNotas.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem10 = self.tblRegistroNotas.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.tblRegistroNotas.setSortingEnabled(__sortingEnabled)

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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.btnCancelEditNota.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btnExportExcel.setText(QCoreApplication.translate("MainWindow", u"Exportar Excel", None))
        self.btnEditarSelectEstudiante.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        ___qtablewidgetitem11 = self.tblListEstud.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem12 = self.tblListEstud.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Estudiante", None));
        ___qtablewidgetitem13 = self.tblListEstud.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"NIE", None));
        ___qtablewidgetitem14 = self.tblListEstud.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled1 = self.tblListEstud.isSortingEnabled()
        self.tblListEstud.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tblListEstud.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem16 = self.tblListEstud.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Salina Monterrosa, Tifanny Lizbeth", None));
        ___qtablewidgetitem17 = self.tblListEstud.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.tblListEstud.setSortingEnabled(__sortingEnabled1)

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.txtRegNomEstud.setText("")
        self.txtRegNomEstud.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.txtRegNieEstud.setText("")
        self.txtRegNieEstud.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Juan Perez", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nie", None))
        self.txtBuscarEstuds.setText("")
        self.txtBuscarEstuds.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isamel quijada", None))
        self.pushButton_6.setText("")
        self.btnAgregarEstud.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnEditSelectEstud.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnEliminarEstud.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnActualizarEstud.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Registro De Estudiantes", None))
        self.cbxEstudOrderBy.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordenar Por", None))
        self.cbxEstudOrderBy.setItemText(1, QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.cbxEstudOrderBy.setItemText(2, QCoreApplication.translate("MainWindow", u"NIE", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.cbxRegGradoEstud.setItemText(0, QCoreApplication.translate("MainWindow", u"Bachillerato General", None))
        self.cbxRegGradoEstud.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.cbxRegGradoEstud.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))

        self.btnCancelEstud.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lblEstudianteToEdit.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "")
        ___qtablewidgetitem18 = self.tblListGrados.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem19 = self.tblListGrados.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Grado", None));
        ___qtablewidgetitem20 = self.tblListGrados.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Secci\u00f3n", None));
        self.cbxGradosOrderBy.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordenar Por", None))
        self.cbxGradosOrderBy.setItemText(1, QCoreApplication.translate("MainWindow", u"Grado", None))
        self.cbxGradosOrderBy.setItemText(2, QCoreApplication.translate("MainWindow", u"Secci\u00f3n", None))

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
        self.txtSearchGrado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isamel quijada", None))
        self.cbxRegSeccion.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.cbxRegSeccion.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.cbxRegSeccion.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))

        self.btnCancelGrado.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lblIdGradoEdit.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "")
        ___qtablewidgetitem21 = self.tblListMaterias.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem22 = self.tblListMaterias.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Materia", None));
        ___qtablewidgetitem23 = self.tblListMaterias.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Grado", None));
        ___qtablewidgetitem24 = self.tblListMaterias.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled2 = self.tblListMaterias.isSortingEnabled()
        self.tblListMaterias.setSortingEnabled(False)
        ___qtablewidgetitem25 = self.tblListMaterias.item(0, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.tblListMaterias.item(0, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"asdf", None));
        ___qtablewidgetitem27 = self.tblListMaterias.item(0, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.tblListMaterias.setSortingEnabled(__sortingEnabled2)

        self.cbxMateriaOrderBy.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordenar Por", None))
        self.cbxMateriaOrderBy.setItemText(1, QCoreApplication.translate("MainWindow", u"Materia", None))
        self.cbxMateriaOrderBy.setItemText(2, QCoreApplication.translate("MainWindow", u"Grado", None))

        self.txtRegMateria.setText("")
        self.txtRegMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sociales", None))
        self.btnAgregarMateria.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Materia", None))
        self.btnActualizarMateria.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.pushButton_23.setText("")
        self.btnMateriaEdit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Registro De Materias", None))
        self.btnEliminarMateria.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.txtSearchMaterias.setText("")
        self.txtSearchMaterias.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Isamel quijada", None))
        self.cbxRegMatGrado.setItemText(0, QCoreApplication.translate("MainWindow", u"Bachillerato General", None))
        self.cbxRegMatGrado.setItemText(1, QCoreApplication.translate("MainWindow", u"9 Grado", None))
        self.cbxRegMatGrado.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))

        self.btnCancelMateriaEdit.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lblMateriaToEdit.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
    # retranslateUi

