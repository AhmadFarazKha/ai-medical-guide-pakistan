import os

def create_directories_if_not_exist(directories: list):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
