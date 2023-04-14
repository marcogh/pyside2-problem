from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QDialogButtonBox
from disappear import Ui_MainWindow

import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.showLabel)
        self.ui.buttonBox.rejected.connect(self.hideLabel)

        self._label_height = self.ui.label.height()
        self.hideLabel()

        self.show()

    def showLabel(self):
        self.ui.label.show()
        self.resize(
            self.width(),
            self.height() - self._label_height
        )
        print('show label')

    def hideLabel(self):
        self.resize(
            self.width(),
            self.height() - self._label_height
        )
        print('hide label')
        self.ui.label.hide()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
