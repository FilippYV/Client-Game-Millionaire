import json
import requests

from app.erors_funck import FailUserName, FailServerEror, ErrorInput
from app.interface.game import Game

url_server = "https://server-game-millionaire.herokuapp.com"


# filename = '../static/user.json'
#
#
# def recording_users_in_json(new_data):
#     '''
#     записываем пользователей в json
#     '''
#     with open(filename, encoding='utf-8') as file:
#         data = json.load(file)
#         data["list"].append(new_data)
#         with open(filename, "w", encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False, indent=3)
#
#
# def read_json():
#     '''
#     читам json файл с пользователями
#     '''
#     with open(filename, 'r', encoding='utf-8') as file:
#         return json.load(file)
#
#
# def name_verification(name):
#     '''
#     проверка на наличие хеша
#     '''
#     if len(name) < 1:
#         raise FailUserName()
#     hash_user = None
#     cach = read_json()
#     for i in range(len(cach["list"])):
#         if name == cach["list"][i]["name_user"]:
#             hash_user = cach["list"][i]["user_id"]
#             break
#     try:
#         if hash_user is not None:
#             id_user_in_game = get_data_about_user_user_id(hash_user)
#         else:
#             id_user_in_game = get_data_about_user_regist(name)
#         return id_user_in_game
#     except FailServerEror:
#         print("Eror server!!!")
#
#
# def get_data_about_user_user_id(hash_user):
#     '''
#     вход при помощи user id
#     '''
#     command = "get_data_about_user"
#     get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": hash_user}))
#     if get_user.ok:
#         data = get_user.json()
#         return data["answer"]["user_id"]
#     else:
#         print("Eror server!!!")
#         raise FailServerEror()
#
#
# def get_data_about_user_regist(name_user):
#     '''
#     вход c регистрацией ногового пользователя
#     '''
#     command = "get_data_about_user"
#     get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"name_user": name_user}))
#     if get_user.ok:
#         data = get_user.json()
#         new_data = {"name_user": data["answer"]["name"], "user_id": data["answer"]["user_id"]}
#         recording_users_in_json(new_data)
#         return new_data["user_id"]
#     else:
#         print("Eror server!!!")
#         raise FailServerEror()
#
#
# def input_a_name_to_the_server():
#     '''
#     функция ...
#     '''
#     name_user = str(input('Введите имя - '))
#     # name_verification(name_user)
#     id_user_in_game = name_verification(name_user)
#     count_question = 1
#     for i in range(15):
#         get_question(id_user_in_game, count_question)


def input_a_name_to_the_server_main(id_user_in_game):
    '''
    функция ...
    '''
    count_question = 1
    for i in range(15):
        get_question(id_user_in_game, count_question)
        # user_answer_to(id_user_in_game, count_question)


def check_answer_user(id_user_in_game, user_answer, count_question):
    command = "check_answer_user"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game,
                                                                         "answer_id": user_answer}))
    if get_user.ok:
        data = get_user.json()
        if data["answer"]["correct_answer"] == True:
            return True
        else:
            return False


# def exclude_two_answers(id_user_in_game, user_answer, count_question):
#     command = "exclude_two_answers"
#     get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game}))
#     if get_user.ok:
#         data = get_user.json()
#         print(data)
#         print(f"Вопрос : {data['answer']['question']}")
#         print("-" * 25)
#         print(f"Ответ №1: {data['answer']['answers'][0]}")
#         print(f"Ответ №2: {data['answer']['answers'][1]}")
#         try:
#             user_answer_to(id_user_in_game, count_question)
#         except ErrorInput:
#             print("Error input!!!")
#             exit(1)



def get_question(id_user_in_game, count_question):
    command = "get_question_with_answers"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game}))
    if get_user.ok:
        data = get_user.json()
        mass = [[f"Вопрос №{count_question + 1}"],
                [f"{data['answer']['question']}"],
                [f"Ответ №4: {data['answer']['answers'][0]}"],
                [f"Ответ №3: {data['answer']['answers'][1]}"],
                [f"Ответ №2: {data['answer']['answers'][2]}"],
                [f"Ответ №1: {data['answer']['answers'][3]}"]]
        return mass

        # user_answer_to(id_user_in_game, count_question)

        # count_question += 1
        # if count_question == 2 or 7 or 10 or 13:
        #     x = choosing_an_action(id_user_in_game)
        #     if x == True:
        #         pass
        #     elif x == False:
        #         print('=' * 25)
        #         print('Вы выиграли')
        #         exit(0)
        # user_answer = int(input('Введите число от 1 до 4 - '))
        # match user_answer:
        #     case 1 | 2 | 3 | 4 :
        #         check_answer_user(id_user_in_game, user_answer)
        #     case -1:
        #         exclude_two_answers(id_user_in_game, user_answer)
        #     case _:
        #         raise CommandNotFound()


# def user_answer_to(id_user_in_game, count_question):
#     user_answer = int(input("Выбор: "))
#     match user_answer:
#         case 1 | 2 | 3 | 4:
#             check_answer_user(id_user_in_game, user_answer - 1, count_question)
#         case -1:
#             exclude_two_answers(id_user_in_game, user_answer, count_question)
#         case _:
#             raise ErrorInput()


def user_answer_one(id_user_in_game, count_question):
    user_answer = 1
    x = check_answer_user(id_user_in_game, user_answer - 1, count_question)
    return x

def user_answer_two(id_user_in_game, count_question):
    user_answer = 2
    x = check_answer_user(id_user_in_game, user_answer - 1, count_question)
    return x

def user_answer_three(id_user_in_game, count_question):
    user_answer = 3
    x = check_answer_user(id_user_in_game, user_answer - 1, count_question)
    return x

def user_answer_four(id_user_in_game, count_question):
    user_answer = 4
    x = check_answer_user(id_user_in_game, user_answer - 1, count_question)
    return x


def cost_user(id_user_in_game):
    command = "get_data_about_user"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game}))
    print(get_user)


def choosing_an_action(id_user_in_game):
    command = "get_data_about_user"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game}))
    if get_user.ok:
        data = get_user.json()
        data = data["answer"]["money"]
        print(f"Вы заработали: {data} рублей")
        print("Хотите забрать выигрыш?")
        print("Введите 1 для продолжения")
        x = int(input("Выбор: "))
        if x == 1:
            return True
        else:
            return False


def showing_questions():
    # вывод вопросов в интерфейс
    pass


def sending_a_response_to_the_server():
    # при нажатии на кнопки интерфейса
    pass


def server_error_handling():
    # обработка ошибок сервера
    pass


def show_start_menu_game():
    '''
    показываем все элементы интерфейса которые нужны в главном меню
    '''
    pass


def show_entering_the_user_name():
    '''
    показываем все элементы интерфейса которые нужны при вводе имени
    '''
    pass


def show_question():
    '''
    показываем вопрос и варианты ответа и копку подсказок подсказки
    '''
    pass


def entering_the_user_name():
    '''
    при входе в игру вводим имя игрока
    '''
    #  надпись которая должна быть поверх строчки ввода имени
    # (строчка ввода имени, пока её нет будет ввод в переменную)
    user_name_stroka = str(input())
    # после нажатия на кнопку отправки
    # переход на начало игры, а именно первый вопрос ->
    showing_questions()
