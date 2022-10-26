import sys
from controllers.Main_controller import MainViewc
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QScreen
# class Algito(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MainViewc()
    myApp.show()

    myApp.show()

    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = myApp.frameGeometry()
    geo.moveCenter(center)
    myApp.move(geo.topLeft())

    sys.exit(app.exec_())



