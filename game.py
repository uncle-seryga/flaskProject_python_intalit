import random
import sqlite3

class Words:
    connect = sqlite3.connect('words.db')
    cursor = connect.cursor()
    def __init__(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS words (words)""")
# List of words to choose from

    def __str__(self):
        self.cursor.execute("""SELECT * FROM users""")
        word_list = self.cursor.fetchall()
        return random.choice(word_list)



# Function to display the hidden word
def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


# Function to get the user's guess
def get_guess(guess):
    while True:
        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("Please enter a single letter.")
