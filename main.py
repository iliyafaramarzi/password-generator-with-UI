from logging import PlaceHolder
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import random

class windows(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(300,300,500,400)
        self.setMinimumSize(500,400)
        self.setMaximumSize(500,400)
        self.setWindowTitle('Password Generator')
        self.ui()

    def ui(self):
        self.chars = QtWidgets.QTextEdit(self, placeholderText='characters')
        self.chars.move(50,50)
        self.chars.resize(400,50)
        self.lenght = QtWidgets.QTextEdit(self, placeholderText='lenght')        
        self.lenght.move(50,150)
        self.lenght.resize(400,50)
        self.button = QtWidgets.QPushButton(self)
        self.button.move(190,250)
        self.button.setText('Generate')
        self.button.clicked.connect(self.click)
        self.final = QtWidgets.QTextEdit(self, readOnly = True)
        self.final.move(50,300)
        self.final.resize(400,50)


    def click(self):
        try:
            if self.chars.toPlainText() == 'about':
                self.final.setText('created by iliya faramarzi\nTelegram: @iliyafaramarzi\ninstagram : faramarziiliya')

            
            elif self.chars.toPlainText() != '' and self.lenght.toPlainText() != '' and int(self.lenght.toPlainText()):
                password = random.choices(self.chars.toPlainText(), k = int(self.lenght.toPlainText()))
                self.final.setText(''.join(password))
        
        except ValueError:
            QtWidgets.QMessageBox.about(self, 'error', 'please enter just number in secend text box')
            self.lenght.setText('')

def main():
    app = QApplication([])
    win = windows()
    win.show()
    sys.exit(app.exec_())

main()