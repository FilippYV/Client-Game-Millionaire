# import pytest
#
# from app.code_program import name_verification, recording_users_in_json
# from app.erors_funck import FailUserName, FailFileUsers
#
#
# def test_correct_user_name():
#     name = ''
#     with pytest.raises(FailUserName):
#         name_verification(name)
#
# def test_exist_user_file():
#     filename = '../static/user.json'
#     data = 'name'
#     with pytest.raises(FailFileUsers):
#         recording_users_in_json(data, filename)
