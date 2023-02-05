import random

import db_controller


def get_word():
    data = db_controller.Words().get_all()
    return random.choice(data)[1]


def set_mask(word: str):
    return '*' * word.__len__()

