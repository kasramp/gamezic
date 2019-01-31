import os
import random

from games import Game


class Handkerchief(Game):

    def get_name(self):
        return "Handkerchief AKA Hangman"

    def play(self):
        replay = True
        while replay:
            print("This is a renamed version of the classic 'Hangman' game named 'Handkerchief'.\n"
                  "As a player you have TEN chances to guess the correct word\n"
                  "Instead of hanging a man we hang a just washed handkerchief to serve you :-)\n"
                  "Of course if you lose")
            random_word, random_word_length = self.__get_random_word_from_collection__()
            print(random_word)
            user_word_matrix = ['_'] * random_word_length
            print("The random word has '{random_word_length}' characters".format(random_word_length=random_word_length))
            print(user_word_matrix)
            is_win = False
            i = 0
            while i < 10:
                input_character = self.__get_user_guessed_character__()
                if input_character not in random_word:
                    i += 1
                    print("'{0}' is not appeared in the word. \n"
                          "You have {1} chances left".format(input_character, 9 - i))
                else:
                    user_word_matrix = self.__print_partial_completed_word__(
                        random_word, input_character, user_word_matrix)
                    if ''.join(user_word_matrix) == random_word:
                        is_win = True
                        print("Congratulations you have completed the word!")
                        break

            if not is_win:
                print("GAME OVER! You have lost all your chances, the mysterious word was {0}".format(random_word))
            replay = self.__get_user_replay_result__()

    def __get_user_guessed_character__(self):
        while True:
            user_input_raw = input("Please enter a character you guess it exists in the random word: ")
            if user_input_raw.isalpha():
                break
            else:
                print("'{0}' is not an alphabetic character".format(user_input_raw))
        return user_input_raw[0]

    def __get_random_word_from_collection__(self):
        os.getcwd()
        current_directory = os.getcwd()
        word_collection_file = os.path.join(current_directory, "data/words.txt")
        file_handle = open(word_collection_file, "r")
        random_word = str(random.choice(file_handle.read().splitlines())).lower()
        file_handle.close()
        return random_word, len(random_word)

    def __print_partial_completed_word__(self, random_word, user_input: str, user_word_matrix):
        user_input = user_input.lower()
        for i in range(len(random_word)):
            if random_word[i] == user_input:
                user_word_matrix[i] = user_input
        print(user_word_matrix)
        return user_word_matrix

    def __get_user_replay_result__(self):
        while True:
            user_input_raw = input("Would you like to play again (Y/N)? ")
            user_input = user_input_raw[0].lower()
            if user_input == "n":
                return False
            elif user_input == "y":
                return True
            else:
                print("Wrong input. Please try again!")
