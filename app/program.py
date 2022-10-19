import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy, QMainWindow, QMessageBox, QApplication
from qtpy import QtGui

from app.core.path_utils import get_ico_path
from app.core.program_utils import check_answer_user, get_user_id
from app.core.program_utils import get_block_question_and_answers, stop_game_fail, stop_game_correct, \
    get_number_money_user


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__number_current_question = 0
        self.__current_cost = 0.0
        self.__income = 0.0
        self.__header_menu = QFont("Times New Roman", 32)
        self.__header_game = QFont("Times New Roman", 15)
        self.__score_font = QFont("Times New Roman", 14)
        self.setWindowTitle("Кто хочет стать миллионером")
        self.setGeometry(0, 0, 1920, 1080)
        self.setObjectName("MainWindow")
        self.setWindowIcon(QtGui.QIcon(get_ico_path()))

        # Вывод основного приветствия
        self.__main_title_label = self.__create_label("Кто хочет стать миллионером?",
                                                      (850, 15), self.__header_menu,
                                                      (0, 0, 1920, 155),
                                                      Qt.AlignCenter)
        self.__current_user_id = get_user_id()["user_id"]
        # Инициализаця меню
        self.__init_menu_ui()
        # Инициализация игры
        self.__init_game_ui(True)

        # Правила
        self.textEdit = QtWidgets.QTextBrowser(self)
        self.textEdit.setText("Тут текст")
        self.textEdit.setGeometry(10, 11, 1900, 800)
        self.textEdit.setFont(QFont('Times New Roman', 24))
        self.textEdit.setAlignment(Qt.AlignJustify)
        self.textEdit.hide()

        self.button_take = QtWidgets.QPushButton(self)
        self.button_take.setObjectName('Button')
        self.button_take.move(1600, 950)
        self.button_take.setText("Забрать")
        self.button_take.setFixedWidth(300)
        self.button_take.setFixedHeight(40)
        self.button_take.hide()

        self.button_pass = QtWidgets.QPushButton(self)
        self.button_pass.setObjectName('Button')
        self.button_pass.move(1600, 950)
        self.button_pass.setText("Продолжить игру")
        self.button_pass.setFixedWidth(300)
        self.button_pass.setFixedHeight(40)
        self.button_pass.hide()

    def __init_menu_ui(self, hide_all: bool = False) -> None:
        # Вывод кол-во монет
        money = get_number_money_user(self.__current_user_id)
        self.__score_user = self.__create_label(f"Ваш счет: {money}",
                                                (500, 500), self.__score_font,
                                                (0, 0, 1920, 45),
                                                Qt.AlignLeft)

        # Кнопка Начать игру
        self.__button_start = self.__create_button(
            "Начать играть",
            "button_start",
            "{background-color:lightgreen}",
            (820, 450), 300, 40, self.game_menu)

        # Кнопка Правила игры
        self.__button_rules = self.__create_button(
            "Правила игры",
            "button_rules",
            "{background-color:lightgreen}",
            (820, 500), 300, 40, self.game_rules
        )

        # Кнопка выхода на рабочий стол
        self.__button_exit = self.__create_button(
            "Выйти",
            "button_exit",
            "{background-color:lightgreen}",
            (820, 950), 300, 40, self.__close_window
        )
        self.__menu_elements_ui = (self.__button_start, self.__button_rules, self.__button_exit)

        if hide_all:
            self.__hide_qt_elements(self.__menu_elements_ui)

    def __init_game_ui(self, hide_all: bool = False) -> None:
        self.__question_label = self.__create_label("Вопрос?",
                                                    (500, 500), self.__header_game,
                                                    (0, 0, 1920, 750), Qt.AlignCenter)

        self.__button_exit_menu = self.__create_button(
            "Выйти в меню",
            "button_exit_menu",
            None, (820, 950), 300, 40, self.__exit_menu)

        self.__button_answer_one = self.__create_button(
            "Ответ1",
            "button_answer_one", None,
            (500, 600), 300, 40, partial(self.__send_answer, 0)
        )

        self.__button_answer_two = self.__create_button(
            "Ответ2",
            "button_answer_two", None,
            (1150, 600), 300, 40, partial(self.__send_answer, 1)
        )

        self.__button_answer_three = self.__create_button(
            "Ответ3",
            "button_answer_three", None,
            (500, 700), 300, 40, partial(self.__send_answer, 2)
        )

        self.__button_answer_four = self.__create_button(
            "Ответ3",
            "button_answer_four", None,
            (1150, 700), 300, 40, partial(self.__send_answer, 3)
        )

        self.__button_next_question = self.__create_button(
            "Следующий вопрос",
            "button_next_question",
            None,
            (1600, 950),
            300, 40, self.game_menu
        )

        self.__game_elements_ui = (self.__question_label,
                                   self.__button_answer_one,
                                   self.__button_answer_two,
                                   self.__button_answer_three,
                                   self.__button_answer_four,
                                   self.__button_next_question,
                                   self.__button_exit_menu)
        self.__buttons_answer = (self.__button_answer_one,
                                 self.__button_answer_two,
                                 self.__button_answer_three,
                                 self.__button_answer_four)
        if hide_all:
            self.__hide_qt_elements(self.__game_elements_ui)

    @staticmethod
    def __hide_qt_elements(qt_elements) -> None:
        if qt_elements is not None:
            for qt_element in qt_elements:
                qt_element.hide()

    @staticmethod
    def __change_state_qt_elements(qt_elements, state: bool) -> None:
        if qt_elements is not None:
            for qt_element in qt_elements:
                qt_element.setEnabled(state)

    @staticmethod
    def __show_qt_elements(qt_elements) -> None:
        if qt_elements is not None:
            for qt_element in qt_elements:
                qt_element.show()

    @staticmethod
    def __change_style_qt_elements(qt_elements, style: str) -> None:
        if qt_elements is not None:
            for qt_element in qt_elements:
                qt_element.setStyleSheet(style)

    def __create_button(self,
                        text: str,
                        object_name: str,
                        style: str | None,
                        pos: tuple['int', 'int'],
                        width: int,
                        height: int,
                        command) -> QtWidgets.QPushButton:
        new_button = QtWidgets.QPushButton(self)
        new_button.setObjectName(object_name)
        if style is not None:
            new_button.setStyleSheet(f"#{object_name}{style}")
        new_button.move(*pos)
        new_button.setText(text)
        new_button.setFixedWidth(width)
        new_button.setFixedHeight(height)
        new_button.clicked.connect(command)
        return new_button

    def __create_label(self, text: str,
                       pos: tuple['int', 'int'],
                       q_font: QFont,
                       geometry: tuple['int', 'int', 'int', 'int'],
                       alignment: Qt.Alignment) -> QtWidgets.QLabel:
        new_label = QtWidgets.QLabel(text, self)
        new_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        new_label.move(*pos)
        new_label.setFont(q_font)
        new_label.setGeometry(*geometry)
        new_label.setAlignment(alignment)
        return new_label

    def __hide_menu(self) -> None:
        self.__hide_qt_elements(self.__menu_elements_ui)

    def __hide_game(self) -> None:
        self.__hide_qt_elements(self.__game_elements_ui)

    def __show_menu(self) -> None:
        self.__show_qt_elements(self.__menu_elements_ui)

    def __show_game(self) -> None:
        self.__show_qt_elements(self.__game_elements_ui)

    def __default_style_for_buttons_answer(self) -> None:
        self.__change_style_qt_elements(self.__buttons_answer, "{}")

    def show_menu(self):
        money = get_number_money_user(self.__current_user_id)
        self.__number_current_question = 0
        self.__income = 0
        self.__score_user.setText(f"Денег всего: {money}")
        self.__score_user.show()
        self.__main_title_label.setText("Кто хочет стать миллионером?")
        self.__hide_game()
        self.__show_menu()
        self.setWindowTitle("Меню")
        self.textEdit.hide()

    def __set_question_and_answers(self):
        block_question_answers = get_block_question_and_answers(self.__current_user_id,
                                                                self.__number_current_question)
        question = block_question_answers["question"]
        self.__current_cost = block_question_answers["cost"]
        self.__score_user.setText(f"Ваш заработок: {self.__income}")
        self.__default_style_for_buttons_answer()
        self.__buttons_game_on()
        self.__question_label.setText(question)
        self.__main_title_label.setText(f"Вопрос №{self.__number_current_question + 1}")
        self.setWindowTitle(f"Игра: {question}")
        self.__hide_menu()
        self.__show_game()
        self.__button_next_question.hide()

        answers = block_question_answers["answers"]
        for answer in answers:
            answer_id = answer["id"]
            answer_text = answer["text"]
            self.__buttons_answer[answer_id].setText(answer_text)

    def game_menu(self):
        if self.__number_current_question == 0:
            stop_game_fail(self.__current_user_id)
        if self.__number_current_question == 3:
            self.dialog_window()
        elif self.__number_current_question == 6:
            self.dialog_window()
        elif self.__number_current_question == 9:
            self.dialog_window()
        elif self.__number_current_question == 12:
            self.dialog_window()
        elif self.__number_current_question == 15:
            self.stop_game_count()
        else:
            self.__set_question_and_answers()

    def __update_income_text(self) -> None:
        self.__income += self.__current_cost
        self.__score_user.setText(f"Ваш заработок: {self.__income}")

    def __send_answer(self, answer_id: int) -> None:
        data = check_answer_user(self.__current_user_id,
                                 answer_id)
        selected_button = self.__buttons_answer[answer_id]
        if data:
            self.__next_question()
            self.__update_income_text()
            selected_button.setText("Правильный ответ")
            selected_button.setStyleSheet("background-color:lightgreen")

            self.__button_next_question.show()
        else:
            selected_button.setStyleSheet("background-color:red")
            self.__button_exit_menu.show()
            stop_game_fail(self.__current_user_id)
        self.__buttons_game_off()

    def game_rules(self):
        self.__score_user.hide()
        self.setWindowTitle('Правила')
        self.__main_title_label.hide()
        self.__button_start.hide()
        self.__button_exit.hide()
        self.__button_rules.hide()
        self.__button_exit_menu.setText("Выйти в меню")
        self.textEdit.show()
        self.__button_exit_menu.show()

    def __next_question(self):
        self.__number_current_question += 1

    def __exit_menu(self):
        self.show_menu()

    def exit_in_main_menu(self):
        self.__main_title_label.setText("Кто хочет стать миллионером?")
        self.__question_label.hide()
        self.__button_answer_three.hide()
        self.__button_answer_two.hide()
        self.__button_answer_three.hide()
        self.__button_answer_four.hide()
        self.setWindowTitle('Кто хочет стать миллионером')
        self.show_menu()
        self.__button_exit_menu.hide()
        self.__button_exit.show()

    def __buttons_game_off(self):
        """
            Переключает состояние игровых кнопок в состояние выкл
        :return:
        """
        self.__change_state_qt_elements(self.__buttons_answer, False)

    def __buttons_game_on(self):
        """
            Переключает состояние игровых кнопок в состояние вкл
        :return:
        """
        self.__change_state_qt_elements(self.__buttons_answer, True)

    def dialog_window(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("Направо подешь...")
        message_box.setText("Хотите забрать выигрыш?")
        message_box.setInformativeText("Если хотите забрать деньги нажмите 'Yes'\n"
                                       "Если хотите продолжить нажмите 'No'")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setWindowIcon(QtGui.QIcon(get_ico_path()))
        result = message_box.exec_()

        if result == QMessageBox.Yes:
            self.stop_game_count()
            return
        elif result == QMessageBox.No:
            self.__set_question_and_answers()
            return

    def __close_window(self):
        """
            Выход из программы
        :return:
        """
        sys.exit(app.exec_())

    def stop_game_count(self):
        self.__main_title_label.setText("Кто хочет стать миллионером?")
        self.__hide_game()
        stop_game_correct(self.__current_user_id)
        self.__question_label.show()
        self.__button_exit_menu.show()
        self.__question_label.setText(f"Поздравляем вы виграли!!!\n\n\nВаш выигрыш составил - {self.__income}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
