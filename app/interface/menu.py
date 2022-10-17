from tkinter import Tk, W, E, N, S, Label, Grid, BOTTOM, LEFT, TOP, PhotoImage, Canvas, Text
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter.font as tkFont
from functools import partial
from PIL import Image, ImageTk
from app.core.utils import get_path_for_fonts, get_path_for_images
from app.server.serverhandler import ServerHandler


class Game:
    def __init__(self):
        self._root = Tk()

        # Инициализация окон
        self._menu_center = None
        self._quiz = None

        self._root.title("Кто хочет стать миллионером?")

        self._root.minsize(width=350, height=500)
        self._root.resizable(width=0, height=0)

        # Инициализация серверной логики
        self._server_handler = ServerHandler()

        # Инициализация игровых компонентов
        self.__init_fonts()
        self.__init_background()

        self._root.grid_rowconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1)

    def open_menu(self) -> None:
        self.__init_menu()

    def open_quiz(self) -> None:
        self.__init_quiz()

    def __init_fonts(self) -> None:
        leto_text_sans_defect = get_path_for_fonts("LetoTextSansDefect")
        self._leto_text_sans_defect_font_bold_16 = tkFont.Font(family=leto_text_sans_defect, size=16, weight="bold")
        self._leto_text_sans_defect_font_12 = tkFont.Font(family=leto_text_sans_defect, size=12)

    def __init_menu(self) -> None:
        # отключение quiz (не совсем корректно работает)
        if self._quiz is not None:
            self._quiz.grid_forget()

        self._menu_center = Frame(self._root)

        self.__init_money_info()

        name_game = Label(self._menu_center, text="Меню", width=15, font=self._leto_text_sans_defect_font_bold_16)
        name_game.grid(row=0, column=0, pady=20)
        start_button = Button(self._menu_center, text="Играть", width=15, command=self.open_quiz)
        start_button.grid(row=1, column=0, pady=10)
        rules_button = Button(self._menu_center, text="Правила", width=15)
        rules_button.grid(row=2, column=0, pady=10)

        self._menu_center.grid(row=1, column=1)

    def __init_quiz(self) -> None:
        # todo отключение меню
        if self._menu_center is not None:
            self._menu_center.grid_forget()

        self._quiz = Frame(self._root)

        selected_block = self._server_handler.get_question_with_answers()

        question = Text(self._quiz, width=17, height=3, wrap='word',
                        font=self._leto_text_sans_defect_font_bold_16)
        question.insert("1.0", selected_block["question"])
        question.config(state="disabled")
        question.grid(row=0, column=0)

        answers = []
        for index in range(len(selected_block["answers"])):
            button_command = partial(self.__next_question, index)
            answer = Button(self._quiz, text=f"{selected_block['answers'][index]}", width=25,
                            command=button_command)
            answer.grid(row=index + 2, column=0, pady=10)
            answers.append(answer)

        self._quiz.grid(row=1, column=1)

    def __init_money_info(self) -> None:
        money_player = Label(self._root, text="Денег: 0₽", font=self._leto_text_sans_defect_font_12)
        money_player.place(relx=0.01, rely=0.01)

    def __init_background(self) -> None:
        background_image_path = get_path_for_images("background_menu")
        filename = Image.open(background_image_path)
        resize_image = filename.resize((400, 540))
        background_image = ImageTk.PhotoImage(resize_image)
        background_label = Label(self._root, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def __next_question(self, number_answer: int) -> None:
        data = self._server_handler.check_answer_user(number_answer)
        if data["correct_answer"]:
            self.__init_quiz()
        else:
            self.__init_menu()

    def mainloop(self) -> None:
        self._root.mainloop()


def main() -> None:
    window = Game()
    window.open_menu()
    window.mainloop()


if __name__ == "__main__":
    main()


