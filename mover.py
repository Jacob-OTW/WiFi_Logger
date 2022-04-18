import shutil

project_path = 'C:/Users/Jacob/Desktop/Coding/Python/WiFi-Logger/'


def move(file_name):
    src = f"{project_path}{file_name}"
    dst = f"{project_path}Saved"
    shutil.copy(src, dst)
