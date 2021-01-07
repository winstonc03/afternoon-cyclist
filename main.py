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
You don't know how to ride a bike so you carry it over your head.

ONE GOAL: Don't give the bike back lol

Reach the end before the dude catches you.
"""

CHOICES = """
    ----
    E. Status Check
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
    travelled = 0 # 100 km is the goal
    dude_distance = -20 # Game ends once they catch up
    turns = 0
    rice = 3 # Max is 3
    energy = 50 # Max is 50
    hunger = 0




    # Main Loop
    while not done:
        # TODO: Check if reached END GAME

        # TODO: Present the User their choices
        print(CHOICES)

        user_choice = input("What's the move?\n").lower().strip("!,.? ")

        if user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled: {travelled}")
            print(f"\tDistance from dude: {abs(dude_distance)}km")
            print(f"\tYou have {rice} rice left.")
            print(f"\tEnergy Left: {energy}")
            print(f"\tTurns used: {turns}")
            print(f"\t---------------\n")

        elif user_choice == "q":
            print("Thanks for Playing")
            done = True

        time.sleep(1.5)

        # TODO: Change the environment based on user choice and RNG
        # TODO: Random event Generator


def type_slow(slow_string):
    for l in slow_string:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)


if __name__ == "__main__":
    main()


