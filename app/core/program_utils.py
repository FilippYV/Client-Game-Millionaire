import json

import requests

from app.core.path_utils import get_data_user_json_path

url_server = "https://server-game-millionaire.herokuapp.com"
filename = get_data_user_json_path()


def save_json(new_data: dict):
    '''
    записываем пользователей в json
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        data = json.dumps(new_data)
        file.write(data)


def read_json():
    '''
    читам json файл с пользователями
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_user_id():
    """
        Получить user_id
    :return:
    """
    cache = read_json()
    user_id = cache["user_id"]
    if user_id is not None:
        new_user_id = get_data_about_user_user_id(user_id)
    else:
        new_user_id = get_data_about_user_regist("DefaultName")
    return new_user_id


def get_number_money_user(hash_user) -> str:
    """
        Получение кол-во монет пользователя
    :param hash_user:
    :return:
    """
    return get_data_about_user_user_id(hash_user)["money"]


def get_data_about_user_user_id(user_id):
    '''
        вход при помощи user id
    '''
    command = "get_data_about_user"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": user_id}))
    if get_user.ok:
        data = get_user.json()
        if data["status"] == "success":
            return data["answer"]
    else:
        data = get_user.json()
        print(f'Ошибка на сервере!!!\n{data}')
        exit(2)


def get_data_about_user_regist(name_user):
    '''
        регистрация нового пользователя
    '''
    command = "get_data_about_user"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"name_user": name_user}))
    if get_user.ok:
        data = get_user.json()
        new_data = {"user_id": data["answer"]["user_id"]}
        try:
            save_json(new_data)
        except FileAvailabilityError():
            print("Ошибка файла!!!")
        return data["answer"]
    else:
        data = get_user.json()
        print(f'Ошибка на сервере!!!\n{data[0]}')
        exit(2)


def input_a_name_to_the_server_main(id_user_in_game):
    count_question = 1
    for i in range(16):
        get_block_question_and_answers(id_user_in_game, count_question)


def check_answer_user(id_user_in_game, user_answer):
    command = "check_answer_user"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game,
                                                                         "answer_id": user_answer}))

    if get_user.ok:
        data = get_user.json()
        return data["answer"]["correct_answer"]
    else:
        data = get_user.json()
        print(f'Ошибка на сервере!!!\n{data[0]}')
        exit(2)


def get_block_question_and_answers(id_user_in_game, count_question):
    command = "get_question_with_answers"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game}))
    if get_user.ok:
        data = get_user.json()
        if data["status"] == "success":
            return data["answer"]
    else:
        data = get_user.json()
        print(f'Ошибка на сервере!!!\n{data[0]}')
        exit(2)


def stop_game_fail(id_user_in_game):
    command = "finish_game"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game,
                                                                         "collect_winnings": False}))
    if get_user.ok:
        data = get_user.json()
        return data
    else:
        data = get_user.json()
        print(f'Ошибка на сервере!!!\n{data[0]}')
        exit(2)


def stop_game_correct(id_user_in_game):
    command = "finish_game"
    get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": id_user_in_game,
                                                                         "collect_winnings": True}))
    if get_user.ok:
        data = get_user.json()
        return data
    else:
        data = get_user.json()
        print(f'Ошибка на сервере!!!\n{data[0]}')
        exit(2)
