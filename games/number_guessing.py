import random


class NumberGuessing:

    def play(self):
        replay = True

        while replay:
            print("Welcome to the Number Guessing game. You have TEN chances to guess "
                  "the correct number range from '0' to '1000'")

            mysterious_number = random.randint(0, 1001)
            is_win = False

            for i in range(10):
                user_number = self.__get_user_guessed_number__()
                is_win, result = self.__check_number__(user_number, mysterious_number, 9 - i)
                print(result)
                if is_win:
                    break
            if not is_win:
                print("GAME OVER! You have lost all your chances, the mysterious number was {0}".format(mysterious_number))

            replay = self.__get_user_replay_result__()

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

    def __get_user_guessed_number__(self):
        while True:
            user_input_raw = input("Please enter a number you guess is correct: ")
            if user_input_raw.isdigit():
                break
            else:
                print("'{0}' is not a number".format(user_input_raw))
        return int(user_input_raw)

    def __check_number__(self, user_number, mysterious_number, left_chances):
        message = "Congratulation you have guessed the number correctly."
        is_correct = True

        if user_number > mysterious_number:
            message = "Wrong number! Pick a smaller number. You have {0} chance(s) left".format(left_chances)
            is_correct = False

        elif user_number < mysterious_number:
            message = "Wrong number! Pick a larger number. You have {0} chance(s) left".format(left_chances)
            is_correct = False

        return is_correct, message
