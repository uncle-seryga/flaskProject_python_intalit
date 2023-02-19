import random

import db_controller


class Game:
    letters_in_game = []

    def __init__(self):
        self.data = random.choice(db_controller.Words().get_all())[1]

    def set_mask(self):
        return '*' * self.data.__len__()

    def update_mask(self):
        word = ""
        for x in self.data:
            if x in self.letters_in_game:
                word += x
            else:
                word += '*'
        return word

    def check_if_letter(self, letter):
        self.letters_in_game.append(letter)


obj = Game()
while True:

    obj.check_if_letter(input('>'))
    print(obj.update_mask())
    if obj.update_mask().count('*') == 0:
        break
