import MyWindow
from PyQt5 import QtWidgets, QtCore

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parrent=None):
        QtWidgets.QDialog.__init__(self, parrent)
        self.my_widget = MyWindow.MyWindow()
        self.my_widget.vbox.setContentsMargins(0, 0, 0, 0)
        self.btn = QtWidgets.QPushButton("изменить надпись")
        mainbox = QtWidgets.QVBoxLayout()
        mainbox.addWidget(self.my_widget)
        mainbox.addWidget(self.btn)
        self.setLayout(mainbox)
        self.btn.clicked.connect(self.click_btn)


    def click_btn(self):
        self.my_widget.label.setText("новая надпись")
        self.btn.setDisabled(True)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Диалог")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec())



