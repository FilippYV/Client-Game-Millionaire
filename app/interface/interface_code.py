import json
import random
import time
import os
from app.interface.eror_and_right.eror_funck import CommandNotFound, QuestionSerchEror
from app.interface.eror_and_right.eror_funck import ErrorFilePresence, ErrorFilePresence


def changing_the_interface():  # Очистка окна консоли
    print(25 * "\n")


def time_sleep_one_seconds():  # Секундное ожидание программы
    time.sleep(1)


def stop_game():  # Остановка игры
    exit(0)


def stop_game_out():  # Вывод программы при выходе из игры
    print("Ждём вас снова!)")


def main_menue_selection():  # Функция выбора действия в меню
    try:
        entering_the_start_menu = str(input())
        entering_the_start_menu = entering_the_start_menu.lower()
        start_text_to_go_or_end(entering_the_start_menu)
    except CommandNotFound:
        print("Ошибка ввода")


def main_menue_game_out():  # Меню игры вывод
    cash_text = f"Рады видеть вас в нашей игре: Кто хочет стать милионером?"
    out_slow(cash_text)
    cash_text = f"{15 * '-'}\nНачать\n{15 * '-'}\nТоп игроков\n{15 * '-'}\nВыход\n{15 * '-'}"
    out_slow(cash_text)
    print(f"Введите 'начать' или 'топ' или 'выход'")
    print('Командная строка : ', end='')


def start_text_to_go_or_end(menue_entering_a_response):  # Меню игры функция выбора
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


def out_top_players():  # Вывод топа игроков
    print("Топ игроков!")


def out_slow(cash_text):  # Функция посимвольного вывода
    for i in range(len(cash_text)):
        # time.sleep(0.09)
        print(cash_text[i], end='')
    print('')


def entering_a_name():  # Ввод имя игрока
    name_player = str(input())


def entering_a_name_out():  # Ввод имя игрока  консольный вывод
    print("Представтесь - ", end='')


def funck_name_user():  # Функция ввода имени
    entering_a_name_out()
    entering_a_name()
    mass_rand = rand_question()
    try:
        output_in_terminal(mass_rand)
    except QuestionSerchEror:
        print("Ошибка в поиске вопроса")


def get_question_with_answers(key_level: str, number_block: int) -> dict:
    url = "C:/Users/filip/PycharmProjects/client-game-millionaire/static/question.json"
    try:
        data = get_data_from_json(url)
    except ErrorFilePresence:
        print("Ошибка, нет файла с вопросами!!!")
        stop_game()
    data = get_data_from_json(url)
    # так не надо, но ладно)
    # Валидация данных
    if key_level not in set(data.keys()):
        raise QuestionSerchEror

    blocks = data[key_level]
    if (0 <= number_block < len(blocks)) is False:
        raise QuestionSerchEror

    selected_block = data[key_level][number_block]

    question = selected_block["question"]
    answers = selected_block["answers"]
    right_answer = selected_block["right_answer"]

    return {
        "question": question,
        "answers": answers,
        "right_answer": right_answer
    }


def get_data_from_json(path_to_json: str) -> dict:
    if os.path.exists(path_to_json) is False:
        raise ErrorFilePresence
    with open(path_to_json, 'r', encoding='utf-8') as fr:
        data = json.loads(fr.read())
        return data


def rand_question():  # Функция создание рандомного массива
    mass_rand = []
    while len(mass_rand) < 3:
        x = random.randint(0, 5)
        if x not in mass_rand:
            mass_rand.append(x)
    return mass_rand


def chek_fireproof_amount(count, prize):  # Условия для появления меню забрать выигрыш
    if 1 <= count <= 15:
        if count == 3 or count == 6 or count == 9 or count == 12:
            funck_fireproof_amount_out(count, prize)


def funck_fireproof_amount_out(count, prize):  # Условие забрать выигрыш или продолжить играть
    print("Хотите продолжить играть или заберёте выигрыш?")
    # print("Введите 'забрать' или 'продолжить':")
    try:
        choosing_an_answer_option = str(input("Введите 'забрать' или 'продолжить':"))
        choosing_an_answer_option = choosing_an_answer_option.lower()
        funck_fireproof_amount(choosing_an_answer_option, prize)
    except CommandNotFound:
        print("Ошибка ввода")


def out_prize(prize):  # Вывод выигрыша
    print(f'Ваш выигрыш : {prize}')


def calculation_prize(cost_blok: str, prize_size_count: int, count: str):
    try:
        data_cost = get_data_from_json("C:/Users/filip/PycharmProjects/client-game-millionaire/static/question.json")
    except ErrorFilePresence:
        print("Ошибка, нет файла с вопросами!!!")
        stop_game()
    data_cost = get_data_from_json("C:/Users/filip/PycharmProjects/client-game-millionaire/static/question.json")
    if cost_blok not in set(data_cost.keys()):
        raise QuestionSerchEror
    prize = data_cost[cost_blok][prize_size_count][count]
    return prize


def funck_fireproof_amount(choosing_an_answer_option, prize):
    match choosing_an_answer_option:
        case "продолжить":
            pass
        case "забрать":
            stop_game_vis_prize(prize)
        case _:
            raise CommandNotFound()
    pass


def stop_game_vis_prize(prize):
    out_prize(prize)
    stop_game_out()
    stop_game()


def output_in_terminal(mass_rand):  # функция вывода интерфейса основного меню
    count = 0
    for i in mass_rand:
        count += 1
        question = 1
        try:
            selected_question_and_answers = get_question_with_answers("level_1", i)
        except ErrorFilePresence:
            print("Ошибка, нет файла!")
            stop_game()
        selected_question_and_answers = get_question_with_answers("level_1", i)  # так нельзя но можно :)
        print(100 * '-')
        print(f"Вопрос №{count}: {selected_question_and_answers['question']}")
        print(100 * '-')
        for j in range(len(selected_question_and_answers["answers"])):
            print(f'{question}) Ответ: {selected_question_and_answers["answers"][j]}')
            question += 1
        print("\nВведите вариант ответа: ", end='')
        answer_user = (int(input()) - 1)
        if answer_user == selected_question_and_answers["right_answer"]:
            print("Иии...")
            time_sleep_one_seconds()
            print("Это правильынй ответ!!!")
            time_sleep_one_seconds()
            prize = calculation_prize("id_cost", 0, str(count))
            out_prize(prize)
            time_sleep_one_seconds()
            print()
            chek_fireproof_amount(count, prize)
        else:
            print("Иии...")
            time_sleep_one_seconds()
            print("Ответ неверный!")
            time_sleep_one_seconds()
            print("\nВы проиграли :(")
            stop_game_out()
            return
    for i in mass_rand:
        count += 1
        question = 1
        try:
            selected_question_and_answers = get_question_with_answers("level_2", i)
        except ErrorFilePresence:
            print("Ошибка, нет файла!")
            stop_game()
        selected_question_and_answers = get_question_with_answers("level_2", i)  # так нельзя но можно :)
        print(100 * '-')
        print(f"Вопрос №{count}: {selected_question_and_answers['question']}")
        print(100 * '-')
        for j in range(len(selected_question_and_answers["answers"])):
            print(f'{question}) Ответ: {selected_question_and_answers["answers"][j]}')
            question += 1
        print("\nВведите вариант ответа: ", end='')
        answer_user = (int(input()) - 1)
        if answer_user == selected_question_and_answers["right_answer"]:
            print("Иии...")
            time_sleep_one_seconds()
            print("Это правильынй ответ!!!")
            time_sleep_one_seconds()
            prize = calculation_prize("id_cost", 0, str(count))
            out_prize(prize)
            time_sleep_one_seconds()
            print()
            chek_fireproof_amount(count, prize)
        else:
            print("Иии...")
            time_sleep_one_seconds()
            print("Ответ неверный!")
            time_sleep_one_seconds()
            print("\nВы проиграли :(")
            stop_game_out()
            return
    for i in mass_rand:
        count += 1
        question = 1
        try:
            selected_question_and_answers = get_question_with_answers("level_3", i)
        except ErrorFilePresence:
            print("Ошибка, нет файла!")
            stop_game()
        selected_question_and_answers = get_question_with_answers("level_3", i)  # так нельзя но можно :)
        print(100 * '-')
        print(f"Вопрос №{count}: {selected_question_and_answers['question']}")
        print(100 * '-')
        for j in range(len(selected_question_and_answers["answers"])):
            print(f'{question}) Ответ: {selected_question_and_answers["answers"][j]}')
            question += 1
        print("\nВведите вариант ответа: ", end='')
        answer_user = (int(input()) - 1)
        if answer_user == selected_question_and_answers["right_answer"]:
            print("Иии...")
            time_sleep_one_seconds()
            print("Это правильынй ответ!!!")
            time_sleep_one_seconds()
            prize = calculation_prize("id_cost", 0, str(count))
            out_prize(prize)
            time_sleep_one_seconds()
            print()
            chek_fireproof_amount(count, prize)
        else:
            print("Иии...")
            time_sleep_one_seconds()
            print("Ответ неверный!")
            time_sleep_one_seconds()
            print("\nВы проиграли :(")
            stop_game_out()
            return
    for i in mass_rand:
        count += 1
        question = 1
        try:
            selected_question_and_answers = get_question_with_answers("level_4", i)
        except ErrorFilePresence:
            print("Ошибка, нет файла!")
            stop_game()
        selected_question_and_answers = get_question_with_answers("level_4", i)  # так нельзя но можно :)
        print(100 * '-')
        print(f"Вопрос №{count}: {selected_question_and_answers['question']}")
        print(100 * '-')
        for j in range(len(selected_question_and_answers["answers"])):
            print(f'{question}) Ответ: {selected_question_and_answers["answers"][j]}')
            question += 1
        print("\nВведите вариант ответа: ", end='')
        answer_user = (int(input()) - 1)
        if answer_user == selected_question_and_answers["right_answer"]:
            print("Иии...")
            time_sleep_one_seconds()
            print("Это правильынй ответ!!!")
            time_sleep_one_seconds()
            prize = calculation_prize("id_cost", 0, str(count))
            out_prize(prize)
            time_sleep_one_seconds()
            print()
            chek_fireproof_amount(count, prize)
        else:
            print("Иии...")
            time_sleep_one_seconds()
            print("Ответ неверный!")
            time_sleep_one_seconds()
            print("\nВы проиграли :(")
            stop_game_out()
            return
    for i in mass_rand:
        count += 1
        question = 1
        try:
            selected_question_and_answers = get_question_with_answers("level_5", i)
        except ErrorFilePresence:
            print("Ошибка, нет файла!")
            stop_game()
        selected_question_and_answers = get_question_with_answers("level_5", i)  # так нельзя но можно :)
        print(100 * '-')
        print(f"Вопрос №{count}: {selected_question_and_answers['question']}")
        print(100 * '-')
        for j in range(len(selected_question_and_answers["answers"])):
            print(f'{question}) Ответ: {selected_question_and_answers["answers"][j]}')
            question += 1
        print("\nВведите вариант ответа: ", end='')
        answer_user = (int(input()) - 1)
        if answer_user == selected_question_and_answers["right_answer"]:
            print("Иии...")
            time_sleep_one_seconds()
            print("Это правильынй ответ!!!")
            time_sleep_one_seconds()
            prize = calculation_prize("id_cost", 0, str(count))
            out_prize(prize)
            time_sleep_one_seconds()
            print()
            chek_fireproof_amount(count, prize)
        else:
            print("Иии...")
            time_sleep_one_seconds()
            print("Ответ неверный!")
            time_sleep_one_seconds()
            print("\nВы проиграли :(")
            stop_game_out()
            return
    print('Поздравляем вас!!!\nВы победили в нашей игре!!!')


def funck_code_game():
    main_menue_game_out()
    main_menue_selection()
