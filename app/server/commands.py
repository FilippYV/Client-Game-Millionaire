from enum import Enum


class Commands(str, Enum):
    FINISH_GAME = "finish_game"
    GET_DATA_ABOUT_USER = "get_data_about_user"
    GET_QUESTION_WITH_ANSWERS = "get_question_with_answers"
    CHECK_ANSWER_USER = "check_answer_user"
    EXCLUDE_TWO_ANSWERS = "exclude_two_answers"
