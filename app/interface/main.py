import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from rules import Rules
from game import Game


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Кто хочет стать миллионером')
        self.setGeometry(0, 0, 1920, 1080)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(background_menu.jpg)}")

        # Вывод основного приветствия
        self.main_text = QtWidgets.QLabel("Кто хочет стать миллионером", self)
        self.main_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_text.move(850, 5)
        self.main_text.setFont(QFont('Times New Roman', 18))
        self.main_text.setGeometry(0, 0, 1920, 30)
        # self.main_text.setStyleSheet("border: 1px solid black;")
        self.main_text.setAlignment(Qt.AlignCenter)

        # Кнопка Начать игру
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setObjectName('Button')
        self.btn1.setStyleSheet('#Button{background-color:lightgreen}')
        self.btn1.move(820, 450)
        self.btn1.setText("Начать игру")
        self.btn1.setFixedWidth(300)
        self.btn1.setFixedHeight(40)
        self.btn1.clicked.connect(self.show_window_game)


        # Кнопка Правила игры
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setObjectName('Button2')
        self.btn2.setStyleSheet('#Button2{background-color:lightgreen}')
        self.btn2.move(820, 500)
        self.btn2.setText("Правила игры")
        self.btn2.setFixedWidth(300)
        self.btn2.setFixedHeight(40)
        self.btn2.clicked.connect(self.show_window_rules)

        # Кнопка выхода на рабочий стол
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setObjectName('Button3')
        self.btn3.setStyleSheet('#Button3{background-color:lightgreen}')
        self.btn3.move(820, 950)
        self.btn3.setText("Выйти на рабочий стол")
        self.btn3.setFixedWidth(300)
        self.btn3.setFixedHeight(40)
        self.btn3.clicked.connect(self.close_window)

    # Показ окна с правилами
    def show_window_rules(self):
        self.w1 = Rules()
        self.w1.show()

    def show_window_game(self):
        self.w2 = Game()
        self.w2.show()

    # Функция выхода на рабочий стол
    def close_window(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
