import shutil
import os


def show_files(path : str) _> list:

    return os.listdir(path)


def remove_files(path : str) -> None:
    return os.remove(path)