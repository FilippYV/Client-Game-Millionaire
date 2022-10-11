# import time
# import os
# import subprocess
# import tkinter as tk
#
# import pytest
# from interface.Interface_code import Interface_game
#
#
# def main_menue_game -> None:
#     cash_text = "Рады видеть вас в нашей игре: Кто хочет стать милионером?"
#     out_slow(cash_text)
#     cash_text = "Вы хотите начать?"
#     out_slow(cash_text)
#     cash_text = "( Да \ Нет )"
#     out_slow(cash_text)
#     start_text_to_go_or_end()
#
#
#
# def changing_the_interface():
#     time.sleep(1)
#     print(25 * "\n")
#
#
# def stop_game():
#     exit(0)
#     os.system('cls||clear')
#
#
# def out_slow(cash_text):
#     for i in range(len(cash_text)):
#         time.sleep(0.06)
#         print(cash_text[i], end='')
#     print("")
#
#
# def Entering_a_name():
#     cash_text = "Представтесь - "
#     out_slow(cash_text)
#     name_player = str(input())
#     changing_the_interface()
#     print(f"Здарвствуйте - {name_player}")
#
#
# def start_text_to_go_or_end():
#     menue_comand_game = str(input())
#     menue_comand_game.lower()
#     match menue_comand_game:
#         case "да" | "go" | "старт" | "начать" | "поехали" | "конечно":
#             time.sleep(0.5)
#             print("\nОтлично!!!")
#             changing_the_interface()
#             Entering_a_name()
#         case "нет" | "не" | "не хочу":
#             print("Ждём вас снова!)")
#             time.sleep(1)
#             stop_game()
#         case _:
#             print("Eror!!!\nОтветте на вопрос для подолжения")
#             start_text_to_go_or_end()
#
#
# if __name__ == '__main__':
#     main()
