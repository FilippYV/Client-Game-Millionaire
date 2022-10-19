import os.path
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent.parent


def get_data_user_json_path() -> str:
    return os.path.join(get_project_root(), r"static\user.json")


def get_ico_path() -> str:
    return os.path.join(get_project_root(), r"static\ico.ico")