import pytest
from interface.interface_code import start_text_to_go_or_end
from interface.eror_funck import CommandNotFound


def test_start_game():
    entering_the_start_menu = 'ytn'
    with pytest.raises(CommandNotFound):
        start_text_to_go_or_end(entering_the_start_menu)


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
