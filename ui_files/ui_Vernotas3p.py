# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vernotas3p.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_ViewVeNotas(object):
    def setupUi(self, ViewVeNotas):
        if not ViewVeNotas.objectName():
            ViewVeNotas.setObjectName(u"ViewVeNotas")
        ViewVeNotas.resize(808, 548)
        ViewVeNotas.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label = QLabel(ViewVeNotas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 81, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtEstudNotasDe = QLineEdit(ViewVeNotas)
        self.txtEstudNotasDe.setObjectName(u"txtEstudNotasDe")
        self.txtEstudNotasDe.setEnabled(False)
        self.txtEstudNotasDe.setGeometry(QRect(20, 30, 421, 21))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.txtEstudNotasDe.setFont(font1)
        self.txtEstudNotasDe.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtEstudNotasDe.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.line = QFrame(ViewVeNotas)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 150, 771, 16))
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(ViewVeNotas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 130, 81, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(ViewVeNotas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 180, 91, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(ViewVeNotas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 240, 91, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_2 = QFrame(ViewVeNotas)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 260, 771, 16))
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(ViewVeNotas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 340, 101, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_3 = QFrame(ViewVeNotas)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 360, 771, 16))
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(ViewVeNotas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 440, 131, 16))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_4 = QFrame(ViewVeNotas)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 460, 771, 16))
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.lblIdEstudiantevn = QLabel(ViewVeNotas)
        self.lblIdEstudiantevn.setObjectName(u"lblIdEstudiantevn")
        self.lblIdEstudiantevn.setGeometry(QRect(170, 120, 47, 13))
        self.lblIdEstudiantevn.setStyleSheet(u"color:  rgb(40, 40, 40);")
        self.label_6 = QLabel(ViewVeNotas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 81, 16))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_19 = QLabel(ViewVeNotas)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(130, 180, 91, 16))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(ViewVeNotas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 180, 91, 16))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20 = QLabel(ViewVeNotas)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(350, 180, 91, 16))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(ViewVeNotas)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(460, 180, 91, 16))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21 = QLabel(ViewVeNotas)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(570, 180, 121, 16))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10 = QLabel(ViewVeNotas)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 280, 91, 16))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11 = QLabel(ViewVeNotas)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(460, 280, 91, 16))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22 = QLabel(ViewVeNotas)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(130, 280, 91, 16))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_23 = QLabel(ViewVeNotas)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(350, 280, 91, 16))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24 = QLabel(ViewVeNotas)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(570, 280, 121, 16))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12 = QLabel(ViewVeNotas)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(240, 280, 91, 16))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(ViewVeNotas)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 380, 91, 16))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25 = QLabel(ViewVeNotas)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(570, 380, 121, 16))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(ViewVeNotas)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(460, 380, 91, 16))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26 = QLabel(ViewVeNotas)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(350, 380, 91, 16))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(ViewVeNotas)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(240, 380, 91, 16))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_27 = QLabel(ViewVeNotas)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(130, 380, 91, 16))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16 = QLabel(ViewVeNotas)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 480, 91, 16))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28 = QLabel(ViewVeNotas)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(570, 480, 121, 16))
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(ViewVeNotas)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(460, 480, 91, 16))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_29 = QLabel(ViewVeNotas)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(350, 480, 91, 16))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18 = QLabel(ViewVeNotas)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(240, 480, 91, 16))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(ViewVeNotas)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(130, 480, 91, 16))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31 = QLabel(ViewVeNotas)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(340, 60, 81, 16))
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtNotaFinal = QLineEdit(ViewVeNotas)
        self.txtNotaFinal.setObjectName(u"txtNotaFinal")
        self.txtNotaFinal.setEnabled(False)
        self.txtNotaFinal.setGeometry(QRect(340, 80, 101, 21))
        self.txtNotaFinal.setFont(font1)
        self.txtNotaFinal.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cbxCalifPeriodo = QComboBox(ViewVeNotas)
        self.cbxCalifPeriodo.setObjectName(u"cbxCalifPeriodo")
        self.cbxCalifPeriodo.setGeometry(QRect(20, 80, 281, 25))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.cbxCalifPeriodo.setFont(font2)
        self.cbxCalifPeriodo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.lblIdEstVerNotasGlobal = QLabel(ViewVeNotas)
        self.lblIdEstVerNotasGlobal.setObjectName(u"lblIdEstVerNotasGlobal")
        self.lblIdEstVerNotasGlobal.setGeometry(QRect(480, 20, 47, 13))
        self.label_32 = QLabel(ViewVeNotas)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(700, 180, 121, 16))
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33 = QLabel(ViewVeNotas)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(700, 280, 121, 16))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(ViewVeNotas)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(700, 380, 121, 16))
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35 = QLabel(ViewVeNotas)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(700, 480, 121, 16))
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtNotaFinal_9 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_9.setObjectName(u"txtNotaFinal_9")
        self.txtNotaFinal_9.setEnabled(False)
        self.txtNotaFinal_9.setGeometry(QRect(700, 300, 81, 21))
        self.txtNotaFinal_9.setFont(font1)
        self.txtNotaFinal_9.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_10 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_10.setObjectName(u"txtNotaFinal_10")
        self.txtNotaFinal_10.setEnabled(False)
        self.txtNotaFinal_10.setGeometry(QRect(20, 300, 81, 21))
        self.txtNotaFinal_10.setFont(font1)
        self.txtNotaFinal_10.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_11 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_11.setObjectName(u"txtNotaFinal_11")
        self.txtNotaFinal_11.setEnabled(False)
        self.txtNotaFinal_11.setGeometry(QRect(350, 300, 81, 21))
        self.txtNotaFinal_11.setFont(font1)
        self.txtNotaFinal_11.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_12 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_12.setObjectName(u"txtNotaFinal_12")
        self.txtNotaFinal_12.setEnabled(False)
        self.txtNotaFinal_12.setGeometry(QRect(570, 300, 81, 21))
        self.txtNotaFinal_12.setFont(font1)
        self.txtNotaFinal_12.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_13 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_13.setObjectName(u"txtNotaFinal_13")
        self.txtNotaFinal_13.setEnabled(False)
        self.txtNotaFinal_13.setGeometry(QRect(130, 300, 81, 21))
        self.txtNotaFinal_13.setFont(font1)
        self.txtNotaFinal_13.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_13.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_14 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_14.setObjectName(u"txtNotaFinal_14")
        self.txtNotaFinal_14.setEnabled(False)
        self.txtNotaFinal_14.setGeometry(QRect(240, 300, 81, 21))
        self.txtNotaFinal_14.setFont(font1)
        self.txtNotaFinal_14.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_14.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_15 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_15.setObjectName(u"txtNotaFinal_15")
        self.txtNotaFinal_15.setEnabled(False)
        self.txtNotaFinal_15.setGeometry(QRect(460, 300, 81, 21))
        self.txtNotaFinal_15.setFont(font1)
        self.txtNotaFinal_15.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_15.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_8 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_8.setObjectName(u"txtNotaFinal_8")
        self.txtNotaFinal_8.setEnabled(False)
        self.txtNotaFinal_8.setGeometry(QRect(700, 200, 81, 21))
        self.txtNotaFinal_8.setFont(font1)
        self.txtNotaFinal_8.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_2 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_2.setObjectName(u"txtNotaFinal_2")
        self.txtNotaFinal_2.setEnabled(False)
        self.txtNotaFinal_2.setGeometry(QRect(20, 200, 81, 21))
        self.txtNotaFinal_2.setFont(font1)
        self.txtNotaFinal_2.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_5 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_5.setObjectName(u"txtNotaFinal_5")
        self.txtNotaFinal_5.setEnabled(False)
        self.txtNotaFinal_5.setGeometry(QRect(350, 200, 81, 21))
        self.txtNotaFinal_5.setFont(font1)
        self.txtNotaFinal_5.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_7 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_7.setObjectName(u"txtNotaFinal_7")
        self.txtNotaFinal_7.setEnabled(False)
        self.txtNotaFinal_7.setGeometry(QRect(570, 200, 81, 21))
        self.txtNotaFinal_7.setFont(font1)
        self.txtNotaFinal_7.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_7.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_3 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_3.setObjectName(u"txtNotaFinal_3")
        self.txtNotaFinal_3.setEnabled(False)
        self.txtNotaFinal_3.setGeometry(QRect(130, 200, 81, 21))
        self.txtNotaFinal_3.setFont(font1)
        self.txtNotaFinal_3.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_4 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_4.setObjectName(u"txtNotaFinal_4")
        self.txtNotaFinal_4.setEnabled(False)
        self.txtNotaFinal_4.setGeometry(QRect(240, 200, 81, 21))
        self.txtNotaFinal_4.setFont(font1)
        self.txtNotaFinal_4.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_6 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_6.setObjectName(u"txtNotaFinal_6")
        self.txtNotaFinal_6.setEnabled(False)
        self.txtNotaFinal_6.setGeometry(QRect(460, 200, 81, 21))
        self.txtNotaFinal_6.setFont(font1)
        self.txtNotaFinal_6.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_16 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_16.setObjectName(u"txtNotaFinal_16")
        self.txtNotaFinal_16.setEnabled(False)
        self.txtNotaFinal_16.setGeometry(QRect(700, 400, 81, 21))
        self.txtNotaFinal_16.setFont(font1)
        self.txtNotaFinal_16.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_16.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_17 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_17.setObjectName(u"txtNotaFinal_17")
        self.txtNotaFinal_17.setEnabled(False)
        self.txtNotaFinal_17.setGeometry(QRect(20, 400, 81, 21))
        self.txtNotaFinal_17.setFont(font1)
        self.txtNotaFinal_17.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_17.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_18 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_18.setObjectName(u"txtNotaFinal_18")
        self.txtNotaFinal_18.setEnabled(False)
        self.txtNotaFinal_18.setGeometry(QRect(350, 400, 81, 21))
        self.txtNotaFinal_18.setFont(font1)
        self.txtNotaFinal_18.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_18.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_19 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_19.setObjectName(u"txtNotaFinal_19")
        self.txtNotaFinal_19.setEnabled(False)
        self.txtNotaFinal_19.setGeometry(QRect(570, 400, 81, 21))
        self.txtNotaFinal_19.setFont(font1)
        self.txtNotaFinal_19.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_19.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_20 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_20.setObjectName(u"txtNotaFinal_20")
        self.txtNotaFinal_20.setEnabled(False)
        self.txtNotaFinal_20.setGeometry(QRect(130, 400, 81, 21))
        self.txtNotaFinal_20.setFont(font1)
        self.txtNotaFinal_20.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_20.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_21 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_21.setObjectName(u"txtNotaFinal_21")
        self.txtNotaFinal_21.setEnabled(False)
        self.txtNotaFinal_21.setGeometry(QRect(240, 400, 81, 21))
        self.txtNotaFinal_21.setFont(font1)
        self.txtNotaFinal_21.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_21.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_22 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_22.setObjectName(u"txtNotaFinal_22")
        self.txtNotaFinal_22.setEnabled(False)
        self.txtNotaFinal_22.setGeometry(QRect(460, 400, 81, 21))
        self.txtNotaFinal_22.setFont(font1)
        self.txtNotaFinal_22.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_22.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_23 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_23.setObjectName(u"txtNotaFinal_23")
        self.txtNotaFinal_23.setEnabled(False)
        self.txtNotaFinal_23.setGeometry(QRect(700, 500, 81, 21))
        self.txtNotaFinal_23.setFont(font1)
        self.txtNotaFinal_23.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_23.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_24 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_24.setObjectName(u"txtNotaFinal_24")
        self.txtNotaFinal_24.setEnabled(False)
        self.txtNotaFinal_24.setGeometry(QRect(20, 500, 81, 21))
        self.txtNotaFinal_24.setFont(font1)
        self.txtNotaFinal_24.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_24.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_25 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_25.setObjectName(u"txtNotaFinal_25")
        self.txtNotaFinal_25.setEnabled(False)
        self.txtNotaFinal_25.setGeometry(QRect(350, 500, 81, 21))
        self.txtNotaFinal_25.setFont(font1)
        self.txtNotaFinal_25.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_25.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_26 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_26.setObjectName(u"txtNotaFinal_26")
        self.txtNotaFinal_26.setEnabled(False)
        self.txtNotaFinal_26.setGeometry(QRect(570, 500, 81, 21))
        self.txtNotaFinal_26.setFont(font1)
        self.txtNotaFinal_26.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_26.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_27 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_27.setObjectName(u"txtNotaFinal_27")
        self.txtNotaFinal_27.setEnabled(False)
        self.txtNotaFinal_27.setGeometry(QRect(130, 500, 81, 21))
        self.txtNotaFinal_27.setFont(font1)
        self.txtNotaFinal_27.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_27.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_28 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_28.setObjectName(u"txtNotaFinal_28")
        self.txtNotaFinal_28.setEnabled(False)
        self.txtNotaFinal_28.setGeometry(QRect(240, 500, 81, 21))
        self.txtNotaFinal_28.setFont(font1)
        self.txtNotaFinal_28.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_28.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.txtNotaFinal_29 = QLineEdit(ViewVeNotas)
        self.txtNotaFinal_29.setObjectName(u"txtNotaFinal_29")
        self.txtNotaFinal_29.setEnabled(False)
        self.txtNotaFinal_29.setGeometry(QRect(460, 500, 81, 21))
        self.txtNotaFinal_29.setFont(font1)
        self.txtNotaFinal_29.setStyleSheet(u"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.txtNotaFinal_29.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.lblIdGrado = QLabel(ViewVeNotas)
        self.lblIdGrado.setObjectName(u"lblIdGrado")
        self.lblIdGrado.setGeometry(QRect(490, 80, 47, 13))

        self.retranslateUi(ViewVeNotas)

        QMetaObject.connectSlotsByName(ViewVeNotas)
    # setupUi

    def retranslateUi(self, ViewVeNotas):
        ViewVeNotas.setWindowTitle(QCoreApplication.translate("ViewVeNotas", u"Notas estudiante", None))
        self.label.setText(QCoreApplication.translate("ViewVeNotas", u"Notas de", None))
        self.txtEstudNotasDe.setText("")
        self.txtEstudNotasDe.setPlaceholderText(QCoreApplication.translate("ViewVeNotas", u"Juan Perez", None))
        self.label_2.setText(QCoreApplication.translate("ViewVeNotas", u"Trimestre I", None))
        self.label_7.setText(QCoreApplication.translate("ViewVeNotas", u"Act I", None))
        self.label_3.setText(QCoreApplication.translate("ViewVeNotas", u"Trimestre II", None))
        self.label_4.setText(QCoreApplication.translate("ViewVeNotas", u"Trimestre III", None))
        self.label_5.setText(QCoreApplication.translate("ViewVeNotas", u"Trimestre IIII", None))
        self.lblIdEstudiantevn.setText(QCoreApplication.translate("ViewVeNotas", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("ViewVeNotas", u"Materia", None))
        self.label_19.setText(QCoreApplication.translate("ViewVeNotas", u"Act I (35%)", None))
        self.label_8.setText(QCoreApplication.translate("ViewVeNotas", u"Act II", None))
        self.label_20.setText(QCoreApplication.translate("ViewVeNotas", u"Act II (35%)", None))
        self.label_9.setText(QCoreApplication.translate("ViewVeNotas", u"Examen", None))
        self.label_21.setText(QCoreApplication.translate("ViewVeNotas", u"Examen (30%)", None))
        self.label_10.setText(QCoreApplication.translate("ViewVeNotas", u"Act I", None))
        self.label_11.setText(QCoreApplication.translate("ViewVeNotas", u"Examen", None))
        self.label_22.setText(QCoreApplication.translate("ViewVeNotas", u"Act I (35%)", None))
        self.label_23.setText(QCoreApplication.translate("ViewVeNotas", u"Act II (35%)", None))
        self.label_24.setText(QCoreApplication.translate("ViewVeNotas", u"Examen (30%)", None))
        self.label_12.setText(QCoreApplication.translate("ViewVeNotas", u"Act II", None))
        self.label_13.setText(QCoreApplication.translate("ViewVeNotas", u"Act I", None))
        self.label_25.setText(QCoreApplication.translate("ViewVeNotas", u"Examen (30%)", None))
        self.label_14.setText(QCoreApplication.translate("ViewVeNotas", u"Examen", None))
        self.label_26.setText(QCoreApplication.translate("ViewVeNotas", u"Act II (35%)", None))
        self.label_15.setText(QCoreApplication.translate("ViewVeNotas", u"Act II", None))
        self.label_27.setText(QCoreApplication.translate("ViewVeNotas", u"Act I (35%)", None))
        self.label_16.setText(QCoreApplication.translate("ViewVeNotas", u"Act I", None))
        self.label_28.setText(QCoreApplication.translate("ViewVeNotas", u"Examen (30%)", None))
        self.label_17.setText(QCoreApplication.translate("ViewVeNotas", u"Examen", None))
        self.label_29.setText(QCoreApplication.translate("ViewVeNotas", u"Act II (35%)", None))
        self.label_18.setText(QCoreApplication.translate("ViewVeNotas", u"Act II", None))
        self.label_30.setText(QCoreApplication.translate("ViewVeNotas", u"Act I (35%)", None))
        self.label_31.setText(QCoreApplication.translate("ViewVeNotas", u"Nota Final", None))
        self.txtNotaFinal.setText(QCoreApplication.translate("ViewVeNotas", u"1", None))
        self.txtNotaFinal.setPlaceholderText("")
        self.lblIdEstVerNotasGlobal.setText(QCoreApplication.translate("ViewVeNotas", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("ViewVeNotas", u"Promedio", None))
        self.label_33.setText(QCoreApplication.translate("ViewVeNotas", u"Promedio", None))
        self.label_34.setText(QCoreApplication.translate("ViewVeNotas", u"Promedio", None))
        self.label_35.setText(QCoreApplication.translate("ViewVeNotas", u"Promedio", None))
        self.txtNotaFinal_9.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_9.setPlaceholderText("")
        self.txtNotaFinal_10.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_10.setPlaceholderText("")
        self.txtNotaFinal_11.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_11.setPlaceholderText("")
        self.txtNotaFinal_12.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_12.setPlaceholderText("")
        self.txtNotaFinal_13.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_13.setPlaceholderText("")
        self.txtNotaFinal_14.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_14.setPlaceholderText("")
        self.txtNotaFinal_15.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_15.setPlaceholderText("")
        self.txtNotaFinal_8.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_8.setPlaceholderText("")
        self.txtNotaFinal_2.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_2.setPlaceholderText("")
        self.txtNotaFinal_5.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_5.setPlaceholderText("")
        self.txtNotaFinal_7.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_7.setPlaceholderText("")
        self.txtNotaFinal_3.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_3.setPlaceholderText("")
        self.txtNotaFinal_4.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_4.setPlaceholderText("")
        self.txtNotaFinal_6.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_6.setPlaceholderText("")
        self.txtNotaFinal_16.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_16.setPlaceholderText("")
        self.txtNotaFinal_17.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_17.setPlaceholderText("")
        self.txtNotaFinal_18.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_18.setPlaceholderText("")
        self.txtNotaFinal_19.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_19.setPlaceholderText("")
        self.txtNotaFinal_20.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_20.setPlaceholderText("")
        self.txtNotaFinal_21.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_21.setPlaceholderText("")
        self.txtNotaFinal_22.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_22.setPlaceholderText("")
        self.txtNotaFinal_23.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_23.setPlaceholderText("")
        self.txtNotaFinal_24.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_24.setPlaceholderText("")
        self.txtNotaFinal_25.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_25.setPlaceholderText("")
        self.txtNotaFinal_26.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_26.setPlaceholderText("")
        self.txtNotaFinal_27.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_27.setPlaceholderText("")
        self.txtNotaFinal_28.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_28.setPlaceholderText("")
        self.txtNotaFinal_29.setText(QCoreApplication.translate("ViewVeNotas", u"12.45", None))
        self.txtNotaFinal_29.setPlaceholderText("")
        self.lblIdGrado.setText(QCoreApplication.translate("ViewVeNotas", u"TextLabel", None))
    # retranslateUi

