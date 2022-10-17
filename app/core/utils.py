import json
import os
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent.parent


def get_env_path():
    return os.path.join(get_project_root(), ".env")


def get_path_for_fonts(name_font: str):
    return os.path.join(get_project_root(), rf"static\fonts\{name_font}.otf")


def get_path_for_images(name_image: str):
    return os.path.join(get_project_root(), rf"static\images\{name_image}.jpg")


def get_data_user():
    with open(get_user_json_path(), 'r', encoding="utf-8") as fr:
        data = json.loads(fr.read())
        return data


def save_data_user(data: dict):
    with open(get_user_json_path(), 'w', encoding="utf-8") as fw:
        fw.write(json.dumps(data))


def get_user_json_path():
    return os.path.join(get_project_root(), r"static\user.json")
