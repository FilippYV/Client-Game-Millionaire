import json
import time
from interface.eror_funck import CommandNotFound
from tkinter import Tk, ttk


# def start_window():
#     window = Tk()
#     window.title("Кто хочет стать милионером?")
#     window.geometry("500x500")
#     window.resizable(False, False)
#     menue_lable = ttk.Label(window, text="Меню", font=('Times New Roman', 32, 'bold'))
#     menue_lable.pack()
#     button_start = ttk.Button(window, text="Начать", width=20,
#                               command=start_funck_button
#
#                               )
#
#     button_start.pack()
#     window.mainloop()
#
#
# def start_funck_button():
#     pass


def changing_the_interface():  # Очистка окна консоли
    time.sleep(1)
    print(25 * "\n")


def stop_game():  # Остановка игры
    exit(0)


def main_menue_game():  # Меню игры
    # start_window()
    cash_text = "Рады видеть вас в нашей игре: Кто хочет стать милионером?"
    out_slow(cash_text)
    cash_text = "Вы хотите начать?"
    out_slow(cash_text)
    entering_the_start_menu = str(input())
    start_text_to_go_or_end(entering_the_start_menu)


def start_text_to_go_or_end(menue_entering_a_response):
    menue_entering_a_response = menue_entering_a_response.lower()
    match menue_entering_a_response:
        case "да" | "go" | "yes":
            time.sleep(0.5)
            print("\nОтлично!!!")
            changing_the_interface()
            entering_a_name()
        case "top" | "топ":
            time.sleep(0.5)
            print("\nТоп игроков!!!")
            top_players()
        case "нет" | "не" | "не хочу":
            print("Ждём вас снова!)")
            time.sleep(1)
            stop_game()
        case _:
            print("Eror!!!\nОтветте на вопрос для подолжения")
            raise CommandNotFound()


def top_players():
    pass


def out_slow(cash_text):  # Функция посимвольного вывода
    for i in range(len(cash_text)):
        # time.sleep(0.09)
        print(cash_text[i], end='')
    print("")


def entering_a_name():
    cash_text = "Представтесь - "
    out_slow(cash_text)
    name_player = str(input())
    changing_the_interface()
    print(f"Здарвствуйте - {name_player}")
    sorting_questions()


def sorting_questions():
    question = []
    with open('question.json', 'r', encoding='utf-8') as fr:
        d = json.loads(fr.read())
        for block in d["level_3"]:
            question.append(block)
    for i in question:
        print(i)


def question():
    pass

# def test_get_tracks_by_search_not_correct(setup_yandex_music):
#     track_name = "gdfgdfggfd"
#     Yandex_music = setup_yandex_music["yandex_music"]
#     with pytest.raises(TrackNotFound):
#         Yandex_music.get_tracks_by_search(track_name)
