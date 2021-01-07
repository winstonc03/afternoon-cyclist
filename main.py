# main.py
# Afternoon Cyclist
# A text-based adventure game.
# 10/10 IGN

import sys, textwrap, time, random

INTRODUCTION = """
Welcome to Afternoon Cyclist

We've stolen a bike. We don't really feel like giving it back.
This bike is special.
You don't know how to ride a bike so you carry it over your head.

GOAL: Don't give the bike back lol

Reach the end before the dude catches you.
"""

CHOICES = """
    ----
    A. Eat Rice
    B. Light Jog
    C. Full Sprint
    D. Sit down on a bench
    E. Status Check
    Q. QUIT
    ----
"""

WIN_MESSAGE = """
The dude gives up. You copped a bike >:)

You continue the run back home, leaning the bike against the wall,
Knowing you'll never ride the bike anyways.


"""

HUNGER_MESSAGE = """
You're too hungry to move forward, and collapse on the ground.

The dude catches up


"""

def main():
    pass

    # TODO: Display intro
    type_slow(INTRODUCTION)
    time.sleep(1)

    # CONSTANTS

    MAX_ENERGY = 50
    MAX_RICE = 3
    WIN_DISTANCE = 100
    STARVATION = 100

    # Variables
    done = False
    travelled = 0  # 100 km is the goal
    dude_distance = -20  # Game ends once they catch up
    turns = 0
    rice = MAX_RICE  # Max is 3
    energy = MAX_ENERGY  # Max is 50
    hunger = 0




    # Main Loop
    while not done:
        print(CHOICES)
        user_choice = input("What's the move?\n").lower().strip("!,.? ")

        if user_choice == "a":
            if rice > 0:
                rice -= 1
                hunger = 0
                print("\n--------yum--------")
                print("--------Your hunger is satisfied--------\n")
            else:
                print("\n--------You don't have any rice :(--------")

        if user_choice == "b":
            energy -= random.randrange(2, 7)
            user_current_distance = random.randrange(5, 7)
            dude_current_distance = random.randrange(12, 20)
            dude_distance -= user_current_distance - dude_current_distance
            travelled += user_current_distance
            print("--------You take it easy, thinking about your next meal--------")
            print("--------The dude seems to have run faster seeing you slow down...--------")
            print(f"\n--------You travelled {user_current_distance} kms.--------\n")

        if user_choice == "c":
            energy -= random.randrange(5, 11)
            user_current_distance = random.randrange(10, 16)
            dude_current_distance = random.randrange(7, 15)
            dude_distance -= user_current_distance - dude_current_distance
            travelled += user_current_distance
            print("--------You play in your headphones and SPRINT.--------")
            print(f"\n--------You travelled {user_current_distance} kms.--------\n")

        if user_choice == "d":
            # Refueling
            energy = MAX_ENERGY
            dude_distance += random.randrange(7, 14)
            print("--------Your legs feel refreshed again, but the dude's catching up!--------")
            print("--------You hoist your bike back above your head and continue running.--------\n")

        elif user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tDistance from dude: {abs(dude_distance)}km")
            print(f"\tkm travelled: {travelled}")
            print(f"\tYou have {rice} rice left.")
            print(f"\tEnergy Left: {energy}")
            print(f"\tTurns used: {turns}")
            print(f"\t---------------\n")

        elif user_choice == "q":
            print("Thanks for Playing")
            done = True

        if user_choice not in ["a","e"]:
            hunger += random.randrange(5, 12)

        if hunger >= STARVATION:
            type_slow(HUNGER_MESSAGE)
            done = True

        if travelled >= WIN_DISTANCE:
            type_slow(WIN_MESSAGE)
            done = True

        if random.random() < 0.02:
            print("You tripped and twisted your ankle")
            done = True

        if rice < MAX_RICE and random.random() < 0.05:
            rice = MAX_RICE
            print("~~~~~~~~ Mom stops by and refills your rice. Thanks Mom!~~~~~~~~")

        time.sleep(1.5)
        # TODO: Change the environment based on user choice and RNG
        # TODO: Random event Generator


def type_slow(slow_string):
    for char in slow_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)


if __name__ == "__main__":
    main()


