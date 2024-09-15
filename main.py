import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


def generate_word():
    user_word = input("Enter a word: ").upper()
    try:
        word = [nato_dict[user_letter] for user_letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_word()
    else:
        print(word)


generate_word()
