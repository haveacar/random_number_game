import os, random, time
from datetime import datetime

FILE_NAME = os.path.join(os.path.dirname(__file__), "static.txt")
random_num = random.randint(1, 101)
max_guesses = 7
RED_COLOR = "\u001b[38;5;9m"
RESET_COLOR = "\u001b[0m"
YELLOW_COLOR = "\u001b[38;5;11m"

"""Numbers game"""


def draw_winner():
    """
    func print winner
    :return:
    """
    star_line = len(name) * "*"
    print(f"{star_line}\n{RED_COLOR}*WIN!:*{RESET_COLOR}\n{star_line}")
    for i in range(len(name)):
        time.sleep(0.5)
        print(YELLOW_COLOR + name[i] + RESET_COLOR, end="")
    print(f"\n{star_line}")
    pass


def static():
    """
    Update statistic
    """
    time_now = datetime.now().strftime("%H:%M %d.%m.%Y")
    with open(FILE_NAME, "a") as f:
        f.write(f"\nCongratulation Winner {name} at {time_now}")
    pass


def draw_line():
    """
    Draw line with timing

    :return:
    """
    star_arrow = 20 * ">"
    for i in range(len(star_arrow)):
        time.sleep(0.1)
        print(RED_COLOR + star_arrow[i] + RESET_COLOR, end="")

    pass


while True:
    # start game
    if input("Do you want play? (Y/N)")[0].upper() != 'Y':
        break
    name = input("Please write Your name")  # name of user
    winner = False

    # Difficult
    level = int(input(
        F"To EASY(1-25) level press {1}\nTo NORMAL(1-50) level press {2}\nTo HARD(1-100) level press {3}\nLevel:"))
    if level not in [1, 2, 3]:  # check incorrect difficult input
        print("Incorrect input")
        continue

    elif level == 1:
        random_num = random.randint(1, 25)
        num_print = 25
        pass
    elif level == 2:
        random_num = random.randint(1, 50)
        num_print = 50
        pass
    elif level == 3:
        random_num = random.randint(1, 101)
        num_print = 100
        pass

    # game logic
    for i in range(max_guesses):
        draw_line()
        guess = input(f"Enter number from 1 to {num_print}: ")
        if not guess.isdigit() or int(guess) not in range(1, 101):
            print("Yep! Wrong input\U0001F60F")

        else:
            guess = int(guess)

            if guess == random_num:
                draw_winner()
                static()
                winner = True
                break
                time.sleep(4)

            else:
                if guess < random_num:
                    print("Your guess to small\U0001F60F")
                else:
                    print("Your guess to High\U0001F60F")

    if not winner:
        draw_line()
        print(F"GAME OVER {name}!\nNumber was: {random_num}")
        time.sleep(4)
