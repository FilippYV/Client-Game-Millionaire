import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()

        self.setWindowTitle("Игра")
        self.setGeometry(300, 250, 780, 742)
        self.setObjectName("MainWindow1")
        self.setStyleSheet("#MainWindow1{background-color:beige}")

        self.question_text = QtWidgets.QLabel("vnsonbponBblkjfbvlibibwribjis npnboanb[onr[sobn[ornb[oinbiobn[aonb[", self)
        self.question_text.move(500, 500)
        self.question_text.setFont(QFont('Times New Roman', 14))
        self.question_text.setGeometry(0, 0, 1920, 900)
        self.question_text.setAlignment(Qt.AlignCenter)

        self.question_text = QtWidgets.QLabel("Деньги:",
                                              self)
        self.question_text.move(500, 500)
        self.question_text.setFont(QFont('Times New Roman', 14))
        self.question_text.setGeometry(0, 0, 1920, 30)
        self.question_text.setAlignment(Qt.AlignLeft)

        self.bttn1 = QtWidgets.QPushButton(self)
        self.bttn1.setObjectName('Button')
        self.bttn1.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn1.move(600, 600)
        self.bttn1.setText("Ответ1")
        self.bttn1.setFixedWidth(300)
        self.bttn1.setFixedHeight(40)
        self.bttn1.clicked.connect(self.dialog_window)


        self.bttn2 = QtWidgets.QPushButton(self)
        self.bttn2.setObjectName('Button')
        self.bttn2.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn2.move(1150, 600)
        self.bttn2.setText("Ответ2")
        self.bttn2.setFixedWidth(300)
        self.bttn2.setFixedHeight(40)

        self.bttn3 = QtWidgets.QPushButton(self)
        self.bttn3.setObjectName('Button')
        self.bttn3.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn3.move(600, 700)
        self.bttn3.setText("Ответ3")
        self.bttn3.setFixedWidth(300)
        self.bttn3.setFixedHeight(40)

        self.bttn4 = QtWidgets.QPushButton(self)
        self.bttn4.setObjectName('Button')
        self.bttn4.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn4.move(1150, 700)
        self.bttn4.setText("Ответ4")
        self.bttn4.setFixedWidth(300)
        self.bttn4.setFixedHeight(40)
        self.bttn4.clicked.connect(self.window_win)

    def dialog_window(self):
        self.msgBox = QMessageBox().warning(self, 'Выигрыш', "Хотите забрать свой выигрыш?",
                                            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

    def window_win(self):
        self.winbox = QMessageBox().warning(self, 'Победа', "Поздравляем, Вы победили!",
                                            QMessageBox.StandardButton.Ok)



