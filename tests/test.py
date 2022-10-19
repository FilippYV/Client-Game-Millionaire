import json

import pytest

from app.core.path_utils import get_data_user_json_path
from app.core.program_utils import save_json, get_user_id


def test_write_new_data_in_file_user():
    new_data = {"user_id": "nfubcilcoahqsbwdstpjqrlih"}
    save_json(new_data)
    filename = get_data_user_json_path()
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert new_data == data


def test_get_user_id_for_login_in_game():
    data = get_user_id()
    assert data is not None
