from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys
from cryptography.fernet import Fernet



with open("key.txt", "rb") as file:
    key = file.read()

keyCrypted = Fernet(key)

def crypted_file(text):
    encrypted = keyCrypted.encrypt(text)
    with open("myFile.txt", "rt") as file:
        file.write(encrypted)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        texter = self.textBox.toPlainText()
        with open("myFile.txt", "at") as file:
            file.write(texter)
            file.write("\n")
            #crypted_file(texter)

        self.textBox.clear()

    def initUI(self):
        self.setGeometry(710, 390, 500, 300)
        self.setWindowTitle("Encypt your Data")

        self.b = QtWidgets.QPushButton(self)
        self.b.setText("Enter")
        self.b.move(190,200)
        self.b.clicked.connect(self.button_clicked)

        self.textBox = QTextEdit(self)
        self.textBox.setGeometry(100, 50, 300, 130)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

window()

