# main.py
# Afternoon Cyclist
# A text-based adventure game.
# 10/10 IGN

import sys
import textwrap
import time

INTRODUCTION = """"
Welcome to Afternoon Cyclist

We've stolen a bike. We don't really feel like giving it back.
This bike is special.

ONE GOAL: Don't give the bike back lol

Reach the end before the dude catches you.
"""

CHOICES = """
    ----
    Q. QUIT
    ----
"""



def main():
    pass

    # TODO: Display intro
    type_slow(INTRODUCTION)
    time.sleep(1)

    # Variables
    done = False


    # Main Loop
    while not done:
        # TODO: Check if reached END GAME

        # TODO: Present the User their choices
        print(CHOICES)

        user_choice = input("What's the move?\n").lower().strip("!,.? ")

        if user_choice == "q":
            print("Thanks for Playing")
            done = True

        # TODO: Change the environment based on user choice and RNG
        # TODO: Random event Generator


def type_slow(slow_string):
    for l in slow_string:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)


if __name__ == "__main__":
    main()


