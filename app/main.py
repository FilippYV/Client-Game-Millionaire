import sys

from PyQt5.QtWidgets import QApplication

from app.code_program import input_a_name_to_the_server_main, stop_game_fail, get_data_about_user_user_id, \
    get_data_about_user_regist


def qvestion_funck():
    # get_data_about_user_regist('Sergay')
    id_user_in_game = "kffyukmrstkcvmbolxldxxhby"
    stop_game_fail(id_user_in_game)
    # input_a_name_to_the_server_main(id_user_in_game)


if __name__ == '__main__':
    qvestion_funck()
