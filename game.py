import random
import time


def difficult():
    """
    function input difficult level
    1 - easy(1-30)
    2- normal(1-50)
    3 = hard(1-100)
    :return:
    integer
    """
    while True:
        level = input("easy 1-30[1]\nnormal 1-50[2]\nhard 1-100[3]\nDifficult level: ")
        if not level.isdigit():
            print(f"It's not a number: {level}")
            continue

        else:
            level = int(level)
            if level not in [1, 2, 3]:
                print("Only in range 1-3")
                continue
            elif level == 1:
                user_l = 30
                pass
            elif level == 2:
                user_l = 50
                pass
            else:
                user_l = 100
                pass
        return user_l


def check_input():
    """
    Func to check guess input
    :return:
     int(input)
    """
    while True:
        user_g = input("Your guess?")
        if not user_g.isdigit():
            print(f"It's not a number: {user_g}")
            continue
        else:
            return int(user_g)


def game_num(n):
    max_gauses = 5
    secret = random.randint(1, n)
    win = False

    for i in range(max_gauses):
        number = check_input()

        if number == secret:  # if winner
            win = True
            pr = "*You Win!\U0001F91F*"
            print(f"{'*' * len(pr)}\n{pr}\n{'*' * len(pr)}")
            break
        else:  # to print small or high guess
            if number < secret:
                print("Your guess to small")
                pass
            else:
                print("Your guess to high")
                pass

    if not win:  # if not winner
        pr = f"*Game Over! Secret number was-{secret}\U0001F91F*"
        print(f"{'*' * len(pr)}\n{pr}\n{'*' * len(pr)}")
        time.sleep(4)
