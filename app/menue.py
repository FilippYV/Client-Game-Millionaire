import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from app.code_program import get_question, user_answer_one, user_answer_two, user_answer_three, \
    user_answer_four, stop_game_fail, stop_game_correct, get_data_about_user_user_id

id_user_in_game = "kffyukmrstkcvmbolxldxxhby"


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.cost = 0.0
        # self.bank = get_data_about_user_user_id(id_user_in_game)
        self.setWindowTitle('Кто хочет стать миллионером')
        self.setGeometry(0, 0, 1920, 1080)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(background_menu.jpg)}")

        # Вывод основного приветствия
        self.main_text = QtWidgets.QLabel("Кто хочет стать миллионером?", self)
        self.main_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_text.move(850, 5)
        self.main_text.setFont(QFont('Times New Roman', 32))
        self.main_text.setGeometry(0, 0, 1920, 45)
        # self.main_text.setStyleSheet("border: 1px solid black;")
        self.main_text.setAlignment(Qt.AlignCenter)

        # Кнопка Начать игру
        self.btn_start = QtWidgets.QPushButton(self)
        self.btn_start.setObjectName('Button')
        self.btn_start.setStyleSheet('#Button{background-color:lightgreen}')
        self.btn_start.move(820, 450)
        self.btn_start.setText("Начать игру")
        self.btn_start.setFixedWidth(300)
        self.btn_start.setFixedHeight(40)
        self.btn_start.clicked.connect(self.game_menue)

        # Кнопка Правила игры
        self.btn_rules = QtWidgets.QPushButton(self)
        self.btn_rules.setObjectName('Button2')
        self.btn_rules.setStyleSheet('#Button2{background-color:lightgreen}')
        self.btn_rules.move(820, 500)
        self.btn_rules.setText("Правила игры")
        self.btn_rules.setFixedWidth(300)
        self.btn_rules.setFixedHeight(40)
        self.btn_rules.clicked.connect(self.game_rules)

        # Кнопка выхода на рабочий стол
        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setObjectName('Button3')
        self.btn_exit.setStyleSheet('#Button3{background-color:lightgreen}')
        self.btn_exit.move(820, 950)
        self.btn_exit.setText("Выйти на рабочий стол")
        self.btn_exit.setFixedWidth(300)
        self.btn_exit.setFixedHeight(40)
        self.btn_exit.clicked.connect(self.close_window)

        '''
        
        '''

        self.question_text = QtWidgets.QLabel("1", self)
        self.question_text.move(500, 500)
        self.question_text.setFont(QFont('Times New Roman', 24))
        self.question_text.setGeometry(0, 0, 1920, 750)
        self.question_text.setAlignment(Qt.AlignCenter)
        self.question_text.hide()

        self.csore_user_menue = QtWidgets.QLabel((f'Всего денег {get_data_about_user_user_id(id_user_in_game)}'),
                                                 self)
        self.csore_user_menue.move(500, 500)
        self.csore_user_menue.setFont(QFont('Times New Roman', 14))
        self.csore_user_menue.setGeometry(0, 0, 1920, 30)
        self.csore_user_menue.setAlignment(Qt.AlignLeft)
        self.csore_user_menue.show()

        self.csore_user = QtWidgets.QLabel((f'Всего денег {self.count}'), self)
        self.csore_user.move(500, 500)
        self.csore_user.setFont(QFont('Times New Roman', 14))
        self.csore_user.setGeometry(0, 0, 1920, 30)
        self.csore_user.setAlignment(Qt.AlignLeft)
        self.csore_user.hide()

        self.bttn1 = QtWidgets.QPushButton(self)
        self.bttn1.setObjectName('Button')
        # self.bttn1.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn1.move(500, 600)
        self.bttn1.setText("Ответ1")
        self.bttn1.setFixedWidth(300)
        self.bttn1.setFixedHeight(40)
        self.bttn1.hide()
        # self.bttn1.clicked.connect(user_answer_one)

        self.bttn2 = QtWidgets.QPushButton(self)
        self.bttn2.setObjectName('Button')
        # self.bttn2.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn2.move(1150, 600)
        self.bttn2.setText("Ответ2")
        self.bttn2.setFixedWidth(300)
        self.bttn2.setFixedHeight(40)
        self.bttn2.hide()
        # self.bttn2.clicked.connect(user_answer_two)

        self.bttn3 = QtWidgets.QPushButton(self)
        self.bttn3.setObjectName('Button')
        # self.bttn3.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn3.move(500, 700)
        self.bttn3.setText("Ответ3")
        self.bttn3.setFixedWidth(300)
        self.bttn3.setFixedHeight(40)
        self.bttn3.hide()
        # self.bttn3.clicked.connect(user_answer_three)

        self.bttn4 = QtWidgets.QPushButton(self)
        self.bttn4.setObjectName('Button')
        # self.bttn4.setStyleSheet('#Button{background-color:lightgreen}')
        self.bttn4.move(1150, 700)
        self.bttn4.setText("Ответ4")
        self.bttn4.setFixedWidth(300)
        self.bttn4.setFixedHeight(40)
        self.bttn4.hide()
        # self.bttn4.clicked.connect(user_answer_four)

        self.textEdit = QtWidgets.QTextBrowser(self)
        self.textEdit.setText(
            'Игра Кто хочет стать миллионером? - это конкурс викторина, '
            'в котором участники должны правильно ответить на ряд вопросов с несколькими вариантами ответов, '
            'чтобы перейти на следующий уровень. '
            'Всего 15 вопросов, каждый вопрос стоит определенной суммы денег, '
            'участники не имеют никаких временных ограничений для предоставления ответа. '
            'Участники также получают три вида подсказок, чтобы помочь себе, '
            'если они застряли на конкретном вопросе.\n'
            '-----------------------------------------------------------------------------------------------------------\n'
            'Вопросы “Кто хочет стать миллионером?” структурированы в соответствии с пятью различными уровнями, '
            'причем уровень сложности постепенно увеличивается. Каждый уровень содержит три вопроса.\n'
            '-----------------------------------------------------------------------------------------------------------\n'
            'Вопросы, сгруппированные на одном уровне, будут иметь одинаковую сложность. '
            'Например: вопросы 1-3 составляют первый уровень и будут содержать самые простые вопросы. '
            'Второй уровень (вопросы 4–6) будет несколько сложнее, за ним следует третий уровень (вопросы 7–9). '
            'Четвертый уровень (вопросы 10–12) будет состоять из действительно сложных вопросов, '
            'за которыми следует пятый и последний уровень (вопросы 13–15), имеющий самые сложные вопросы в игре.\n'
            '-----------------------------------------------------------------------------------------------------------\n'
            'Важно помнить, что вопросы, составляющие каждый уровень,'
            'не обязательно будут относиться к одним и тем же или даже сходным темам,'
            'но их общий уровень сложности будет одинаковым. Немаловажно,'
            'что уровни вопросов не следует путать с «несгораемыми суммами» или структурой ценностей вопросов,'
            'что они собой являют объясняется ниже.')
        self.textEdit.setGeometry(10, 11, 1900, 800)
        self.textEdit.setFont(QFont('Times New Roman', 24))
        self.textEdit.setAlignment(Qt.AlignJustify)
        self.textEdit.hide()

        # Кнопка для закрытия правил
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setObjectName('Button')
        # self.btn1.setStyleSheet('#Button{background-color:lightgreen}')
        self.btn1.move(820, 950)
        self.btn1.setText("Выйти в меню")
        self.btn1.setFixedWidth(300)
        self.btn1.setFixedHeight(40)
        self.btn1.clicked.connect(self.count_reset)
        self.btn1.hide()

        self.bttn1.clicked.connect(self.out_otvet_1)
        self.bttn2.clicked.connect(self.out_otvet_2)
        self.bttn3.clicked.connect(self.out_otvet_3)
        self.bttn4.clicked.connect(self.out_otvet_4)

        self.bttn_go = QtWidgets.QPushButton(self)
        self.bttn_go.setObjectName('Button')
        self.bttn_go.move(1600, 950)
        self.bttn_go.setText("Следующий вопрос")
        self.bttn_go.setFixedWidth(300)
        self.bttn_go.setFixedHeight(40)
        self.bttn_go.clicked.connect(self.game_menue)
        self.bttn_go.hide()

        self.button_take = QtWidgets.QPushButton(self)
        self.button_take.setObjectName('Button')
        self.button_take.move(1600, 950)
        self.button_take.setText("Забрать")
        self.button_take.setFixedWidth(300)
        self.button_take.setFixedHeight(40)
        # self.button_take.clicked.connect(self.game_menue)
        self.button_take.hide()

        self.button_pass = QtWidgets.QPushButton(self)
        self.button_pass.setObjectName('Button')
        self.button_pass.move(1600, 950)
        self.button_pass.setText("Продолжить игру")
        self.button_pass.setFixedWidth(300)
        self.button_pass.setFixedHeight(40)
        # self.button_pass.clicked.connect(self.game_menue)
        self.button_pass.hide()

    def main_menue(self):
        self.csore_user.hide()
        self.count = 0
        self.cost = 0
        self.csore_user_menue.setText(f'Денег всего: {get_data_about_user_user_id(id_user_in_game)}')
        self.csore_user_menue.show()
        self.main_text.setText("Кто хочет стать миллионером?")
        self.textEdit.hide()
        self.question_text.hide()
        self.bttn1.hide()
        self.bttn2.hide()
        self.bttn3.hide()
        self.bttn4.hide()
        self.bttn_go.hide()
        self.setWindowTitle('Меню')
        self.btn_start.show()
        self.btn_exit.show()
        self.btn_rules.show()
        self.main_text.show()
        self.textEdit.hide()
        self.btn1.hide()

    def game_menue_x(self):
        self.mass = get_question(id_user_in_game, self.count)
        self.csore_user_menue.hide()
        self.bttn_go.hide()
        self.button_on()
        self.setWindowTitle('Игра')
        self.btn_start.hide()
        self.btn_exit.hide()
        self.btn_rules.hide()
        self.btn_exit.hide()

        self.bttn1.setStyleSheet('')
        self.bttn2.setStyleSheet('')
        self.bttn3.setStyleSheet('')
        self.bttn4.setStyleSheet('')

        self.question_text.setText(self.mass[1][0])
        self.question_text.show()
        self.bttn1.setText(self.mass[2][0])
        self.bttn1.show()
        self.bttn2.setText(self.mass[3][0])
        self.bttn2.show()
        self.bttn3.setText(self.mass[4][0])
        self.bttn3.show()
        self.bttn4.setText(self.mass[5][0])
        self.bttn4.show()
        self.btn1.show()
        self.main_text.setText(f"Вопрос №{self.count + 1}")
        self.csore_user.show()

    def game_menue(self):
        if self.count == 0:
            stop_game_fail(id_user_in_game)
        if self.count == 1:
            self.dialog_window()
        elif self.count == 6:
            self.dialog_window()
        elif self.count == 9:
            self.dialog_window()
        elif self.count == 12:
            self.dialog_window()
        elif self.count == 15:
            self.stop_game_count()
        else:
            self.game_menue_x()

    def cost_calculation(self):
        print('2')
        self.cost += float(self.mass[-1])
        print('3')

    def out_otvet_1(self):
        if user_answer_one(id_user_in_game, self.count - 1) == True:
            self.count_question()
            self.cost_calculation()
            self.csore_user.setText(f'Выигрыш: {self.cost}')
            self.btn1.show()
            self.bttn1.setText("Правильный ответ")
            self.bttn1.setStyleSheet('#Button{background-color:lightgreen}')
            self.bttn_go.show()
            self.button_off()
        else:
            self.bttn1.setStyleSheet("background-color : red")
            self.btn1.show()
            self.button_off()
            stop_game_fail(id_user_in_game)

    def out_otvet_2(self):
        if user_answer_two(id_user_in_game, self.count - 1) == True:
            self.count_question()
            self.cost_calculation()
            self.csore_user.setText(f'Выигрыш: {self.cost}')
            self.btn1.show()
            self.bttn2.setText("Правильный ответ")
            self.bttn2.setStyleSheet('#Button{background-color:lightgreen}')
            self.bttn_go.show()
            self.button_off()
        else:
            self.bttn2.setStyleSheet("background-color : red")
            self.btn1.show()
            self.button_off()
            stop_game_fail(id_user_in_game)

    def out_otvet_3(self):
        if user_answer_three(id_user_in_game, self.count - 1) == True:
            self.count_question()
            self.cost_calculation()
            self.csore_user.setText(f'Выигрыш: {self.cost}')
            self.btn1.show()
            self.bttn3.setText("Правильный ответ")
            self.bttn3.setStyleSheet('#Button{background-color:lightgreen}')
            self.bttn_go.show()
            self.button_off()
        else:
            self.bttn3.setStyleSheet("background-color : red")
            self.btn1.show()
            self.button_off()
            stop_game_fail(id_user_in_game)

    def out_otvet_4(self):
        if user_answer_four(id_user_in_game, self.count - 1) == True:
            self.count_question()
            self.cost_calculation()
            self.csore_user.setText(f'Выигрыш: {self.cost}')
            self.btn1.show()
            self.bttn4.setText("Правильный ответ")
            self.bttn4.setStyleSheet('#Button{background-color:lightgreen}')
            self.bttn_go.show()
            self.button_off()
            print('11')
        else:
            self.bttn4.setStyleSheet("background-color : red")
            self.btn1.show()
            self.button_off()
            stop_game_fail(id_user_in_game)

    def game_rules(self):
        self.csore_user_menue.hide()
        self.setWindowTitle('Правила')
        self.main_text.hide()
        self.btn_start.hide()
        self.btn_exit.hide()
        self.btn_rules.hide()
        self.btn1.setText("Выйти в меню")
        self.textEdit.show()
        self.btn1.show()

    def count_question(self):
        self.count += 1

    def count_reset(self):
        self.main_menue()

    def exit_in_main_menue(self):
        self.main_text.setText('Кто хочет стать миллионером')
        self.question_text.hide()
        self.csore_user.hide()
        self.bttn1.hide()
        self.bttn2.hide()
        self.bttn3.hide()
        self.bttn4.hide()
        self.setWindowTitle('Кто хочет стать миллионером')
        self.main_menue()
        self.btn1.hide()
        self.btn_exit.show()

    def button_off(self):
        self.bttn1.setEnabled(False)
        self.bttn2.setEnabled(False)
        self.bttn3.setEnabled(False)
        self.bttn4.setEnabled(False)

    def button_on(self):
        self.bttn1.setEnabled(True)
        self.bttn2.setEnabled(True)
        self.bttn3.setEnabled(True)
        self.bttn4.setEnabled(True)

    def dialog_window(self):
        self.fork = QMessageBox()
        self.fork.setText("Хотите забрать выигрыш?")
        self.fork.setStandardButtons(QMessageBox.Save | QMessageBox.Ignore)
        self.fork.buttonClicked.connect(self.fork_panck)
        self.fork.exec_()

    def fork_panck(self, btn):
        if btn.text() == "Save":
            self.stop_game_count()
        elif btn.text() == "Ignore":
            self.game_menue_x()

    # Функция выхода на рабочий стол
    def close_window(self):
        sys.exit(app.exec_())

    def stop_game_count(self):
        self.main_text.setText("Кто хочет стать миллионером?")
        self.textEdit.hide()
        self.bttn1.hide()
        self.bttn2.hide()
        self.bttn3.hide()
        self.bttn4.hide()
        self.bttn_go.hide()
        self.question_text.show()
        stop_game_correct(id_user_in_game)
        self.question_text.setText(f"Поздравляем вы виграли!!!\n\n\nВаш выигрыш составил - {self.cost}")
        self.btn1.show()
        self.csore_user_menue.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
