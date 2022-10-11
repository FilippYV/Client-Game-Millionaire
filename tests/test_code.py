import pytest
from app.interface.interface_code import start_text_to_go_or_end, rand_question
from app.eror_and_right.eror_funck import CommandNotFound
from app.eror_and_right.right_comand import NotFoundEror


def test_start_game_wrong_command_noumbers():
    menue_entering_a_response = "123"
    with pytest.raises(CommandNotFound):
        start_text_to_go_or_end(menue_entering_a_response)


def test_start_game_right_command_word():
    menue_entering_a_response = 'start'
    start = start_text_to_go_or_end(menue_entering_a_response)
    assert start == True


def test_rand_question():
    start = rand_question()
    assert len(start) == 3
    assert len(set(start)) == 3

# def test_perform_operation_divisions_by_zero():
#     """
#         Тестируем деление на ноль
#     :return:
#     """
#
#     # Данные на вход
#     sign = '/'
#     a = 0
#     b = 10
#
#     # Вызов функции и тестирование
#     with pytest.raises(ZeroDivisionError):
#         perform_operation(sign, a, b)
