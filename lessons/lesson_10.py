# Interview questions excersizes:
import time as T
import random as R


# find the biggest sequence
def f1(msg):
    max_seq = curr_seq = 1
    max_char = curr_char = msg[0]
    for i in range(1, len(msg)):
        if msg[i] == curr_char:
            curr_seq += 1
        else:
            curr_char = msg[i]
            curr_seq = 1
        if curr_seq > max_seq:
            max_seq = curr_seq
            max_char = curr_char
    return max_char * max_seq


def guess_game():
    def success(count):
        if count == 0:
            print(".\n.\n.\n.\n.\nNice seeing you, bye bye !")
            return None

        return print(f"Nice!! i did it\n\nIt took me {count} tries!\n\nSee next time!! ")

    opening_string = "Hello, and welcome to the GUESSING GAME!\nNow, you will pick a number between 1 and 100,\nand i will guess it."
    print(opening_string)
    T.sleep(3)
    first_guess = False
    guess = 1
    gues_counter = 1
    num = input("Enter you number here: ")
    while guess != num:
        if not first_guess:
            guess = R.randint(1, 100)
            T.sleep(1.5)
            print(f"---\t  {guess}  \t---")
            first_guess = True
        else:
            T.sleep(1.5)
            print(f"---\t  {guess}  \t---")
            choice = input(
                "If guess is too high enter 'H',\nif its too low enter 'L',\nif its the right number enter 'R',/nAnd if you want to exit press 'E'.")
            if choice == 'H':
                gues_counter += 1
                guess = R.randint(1, guess)
            elif choice == 'L':
                gues_counter += 1
                guess = R.randint(guess, 100)
            elif choice == 'R':
                sucess(gues_counter)
            elif choice == 'E':
                success(0)
                exit(0)
            else:
                Print("Bac choice, try again.")


def fizz_buzz():
    for num in range(1, 101):
        # T.sleep(0.25)
        if num % 3 == 0:
            if num % 5 == 0:
                print("Fizzbuzz")
            print("Fizz", end='')
        elif num % 5 == 0:
            if num % 3 == 0:
                print("Fizzbuzz")
            print("Buzz", end='')
        else:
            print(num, end='')


def run10():
    # print(f1('aaabbbccccdd'))
    # guess_game()
    fizz_buzz()
