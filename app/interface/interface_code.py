import json
import random
import time
import os
from app.eror_and_right.eror_funck import CommandNotFound
from app.eror_and_right.right_comand import NotFoundEror


def changing_the_interface():  # Очистка окна консоли
    print(25 * "\n")


def time_sleep_one_seconds():
    time.sleep(1)


def stop_game():  # Остановка игры
    return


def stop_game_out():
    print("Ждём вас снова!)")


def main_menue_selection():
    try:
        entering_the_start_menu = str(input())
        entering_the_start_menu = entering_the_start_menu.lower()
        start_text_to_go_or_end(entering_the_start_menu)
    except CommandNotFound:
        print("Ошибка ввода")


def main_menue_game_out():  # Меню игры
    cash_text = "Рады видеть вас в нашей игре: Кто хочет стать милионером?"
    out_slow(cash_text)
    cash_text = "Начать\nТоп игроков\nВыход"
    out_slow(cash_text)
    print('Командная строка : ', end='')


def start_text_to_go_or_end(menue_entering_a_response):
    match menue_entering_a_response:
        case "начать" | "go" | "start" | "поехали":
            changing_the_interface()
            funck_name_user()
        case "top" | "топ":
            changing_the_interface()
            out_top_players()
        case "выход" | "exit" | "ex":
            stop_game_out()
            stop_game()
        case _:
            raise CommandNotFound()


def out_top_players():
    print("Топ игроков!")


def out_slow(cash_text):  # Функция посимвольного вывода
    for i in range(len(cash_text)):
        # time.sleep(0.09)
        print(cash_text[i], end='')
    print('')


def entering_a_name():
    name_player = str(input())


def entering_a_name_out():
    cash_text = "Представтесь - "
    out_slow(cash_text)


def funck_name_user():
    entering_a_name_out()
    entering_a_name()
    mass_rand = rand_question()
    output_in_terminal(mass_rand)


def get_question_with_answers(key_level: str, number_block: int) -> dict:
    data = get_data_from_json("question.json")

    # Валидация данных
    if key_level not in set(data.keys()):
        raise Exception()  # todo заглушка

    blocks = data[key_level]
    if (0 <= number_block < len(blocks)) is False:
        raise Exception()  # todo заглушка

    selected_block = data[key_level][number_block]

    question = selected_block["question"]
    answer_1 = selected_block["answer_1"]
    answer_2 = selected_block["answer_2"]
    answer_3 = selected_block["answer_3"]
    answer_4 = selected_block["answer_4"]
    right_answer = selected_block["right_answer"]

    return {
        "question": question,
        "answers": [answer_1, answer_2, answer_3, answer_4],
        "right_answer": right_answer
    }


def get_data_from_json(path_to_json: str) -> dict:
    if os.path.exists(path_to_json) is False:
        raise Exception()  # todo заглушка

    with open(path_to_json, 'r', encoding='utf-8') as fr:
        data = json.loads(fr.read())
        return data


def rand_question():
    mass_rand = []
    while len(mass_rand) < 3:
        x = random.randint(0, 2)
        if x not in mass_rand:
            mass_rand.append(x)
    return mass_rand


def output_in_terminal(mass_rand):
    for i in mass_rand:
        question = 1
        selected_question_and_answers = get_question_with_answers("level_1", i)
        print(f"Вопрос: {selected_question_and_answers['question']}")
        for answer in selected_question_and_answers["answers"]:
            print(f"{question}) Ответ: {answer}")
            question += 1
        print("Введите верный: ", end='')
        answer_user = int(input())
        if answer_user == selected_question_and_answers["right_answer"]:
            print("Молодец!, Верно")
        else:
            print("Вы проиграли")
            return


def funck_code_game():
    main_menue_game_out()
    main_menue_selection()
