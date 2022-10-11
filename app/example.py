import json
import os


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


def output_in_terminal():
    for i in range(3):
        question = 0
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
