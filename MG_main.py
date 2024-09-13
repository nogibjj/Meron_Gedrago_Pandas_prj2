from data_description import *


def data_describe():
    data = load_dataset()
    return data.describe()


def save_to_mk():
    with open("test.md", "a") as file:
        file.write("test")  # you can add your visualization here


if __name__ == "__main__":
    save_to_mk()
