from game import game_num
from game import difficult as d


"""Number game"""

def run():
    """
    Function run game
    If input "Y" will start function game_num and func difficult

    :return:

    """
    while True:
        if input("Start game[Y/N")[0].upper() != "Y":
            break
        else:
            game_num(d())

run()