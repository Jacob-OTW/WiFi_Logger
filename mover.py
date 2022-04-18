import shutil


def move(file_name):
    src = f"C:/Users/Jacob/Desktop/Coding/Python/WiFi-Logger/{file_name}"
    dst = "C:/Users/Jacob/Desktop/Coding/Python/WiFi-Logger/Saved"
    shutil.copy(src, dst)