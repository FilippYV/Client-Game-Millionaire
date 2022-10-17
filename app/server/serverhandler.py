import json

import requests

from app.core.errors import FailedToConnect, FailedToGetUserId
from app.core.utils import get_data_user, save_data_user
from app.server.commands import Commands


class ServerHandler:
    def __init__(self) -> None:
        self._main_url = "https://server-game-millionaire.herokuapp.com"

        data_about_user = self.__get_data_about_user()
        self._user_id = data_about_user["user_id"]

    def get_data_about_user(self) -> dict:
        """
            Получить информацию о пользователе
        :return:
        """
        return self.__get_data_about_user()

    def get_question_with_answers(self) -> dict:
        """
            Получить вопрос и ответы блока
        :return:
        """
        return self.__get_question_with_answers()

    def check_answer_user(self, answer_id: int) -> dict:
        """
            Проверить правильность ответа на вопрос
        :return:
        """
        return self.__check_answer_user(answer_id)

    def __get_data_about_user(self) -> dict:
        user_id = get_data_user()["user_id"]
        if user_id is None:
            data_about_user = self.__post_request(Commands.GET_DATA_ABOUT_USER, {"name_user": "DefaultName"})
            save_data_user({"user_id": data_about_user["answer"]["user_id"]})
        else:
            data_about_user = self.__post_request(Commands.GET_DATA_ABOUT_USER, {"user_id": user_id})
        return data_about_user["answer"]

    def __get_question_with_answers(self) -> dict:
        if self._user_id is None:
            raise FailedToGetUserId()

        question_with_answers = self.__post_request(Commands.GET_QUESTION_WITH_ANSWERS,
                                                    {"user_id": self._user_id})
        return question_with_answers["answer"]

    def __check_answer_user(self, answer_id: int) -> dict:
        if self._user_id is None:
            raise FailedToGetUserId()

        check_answer = self.__post_request(Commands.CHECK_ANSWER_USER,
                                           {"user_id": self._user_id, "answer_id": answer_id})
        return check_answer["answer"]

    def __post_request(self, command: str, data: dict) -> dict:
        response = requests.post(f"{self._main_url}/{command}", data=json.dumps(data))
        if response.ok:
            return response.json()
        else:
            raise FailedToConnect()
