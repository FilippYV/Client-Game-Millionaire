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

