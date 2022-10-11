import pytest
from app.interface.interface_code import start_text_to_go_or_end, rand_question
# from app.interface.interface_code import chek_fireproof_amount, funck_fireproof_amount
from app.interface.interface_code import get_question_with_answers, ErrorFilePresence
from app.interface.eror_and_right.eror_funck import CommandNotFound, QuestionSerchEror


def test_start_game_wrong_command_noumbers():
    menue_entering_a_response = "123"
    with pytest.raises(CommandNotFound):
        start_text_to_go_or_end(menue_entering_a_response)


def test_rand_question():
    start = rand_question()
    assert len(start) == 3
    assert len(set(start)) == 3


def test_difficulty_level_question():
    key_level = "level_777"
    with pytest.raises(QuestionSerchEror):
        get_question_with_answers(key_level, 1)


def test_number_of_questions():
    key_level = "level_1"
    with pytest.raises(QuestionSerchEror):
        get_question_with_answers(key_level, 777)


def test_fireproof_amount():
    key_level = "level_1"
    with pytest.raises(ErrorFilePresence):
        get_question_with_answers(key_level, 1)


def test_error_file_presence():
    key_level = "level_1"
    with pytest.raises(ErrorFilePresence):
        get_question_with_answers(key_level, 0)


def test_count_fange():
    key_level = "level_1"
    with pytest.raises(ErrorFilePresence):
        get_question_with_answers(key_level, 0)

# def test_fireproof_amount():
#     count = 16
#     with pytest.raises(ErrorClountFireproofAmount):
#         chek_fireproof_amount(count)
