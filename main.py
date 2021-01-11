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
    E. Attempt to ride bike
    F. Status Check
    Q. QUIT
    ----
"""

WIN_DISTANCE = """
The dude gives up. You copped a bike >:)

You continue the run back home, leaning the bike against the wall,
Knowing you'll never ride the bike anyways.


"""

WIN_RIDE = """
Magically, you begin to pedal!

The dude doesn't stand a chance as you cruise up to 30 km/h

With a light breeze blowing past your face, and the sun shining brighter than ever,

You pedal back home with a cheerful grin on your face, satisfied with your achievement.

"""

LOSE_HUNGER = """
You're too hungry to move forward, and collapse on the ground.

The last thing you see before passing out is the dude taking the bike back,

pedalling farther and farther away...

"""

LOSE_TRIP = """
You trip on a pebble and twist your ankle.

Unable to move forward, the dude catches up.

You painfully watch your dream fade away slowly

as he pedals away with the bike.

"""

LOSE_DISTANCE = """
You feel a hand on your back, pulling your shirt

Desperately, you try to free yourself, but with no success.

The bike falls from your hands, and with a defeated face

you watch him steal your dream away from you.

"""

LOSE_ENERGY = """
Your shoulders and legs can't take it anymore, and you drop the bike.

You know you've reached your limit, and collapse on the ground.

After what seems like mere seconds, you open your eyes and realize your in bed.

Was it all a dream?

"""


# CONSTANTS
MAX_ENERGY = 50
MAX_RICE = 3
DISTANCE_WIN = 100
STARVATION = 40


def main():
    pass

    # TODO: Display intro
    type_slow(INTRODUCTION)
    time.sleep(1)

    # Variables
    done = False
    travelled = 0  # 100 km is the goal
    dude_distance = -25  # Game ends once they catch up
    turns = 0
    rice = MAX_RICE  # Max is 3
    energy = MAX_ENERGY  # Max is 50
    hunger = 0

    # Main Loop
    while not done:
        # Display hunger
        if hunger > (STARVATION - 15):
            print("~~~~~~~~Your stomach rumbles, you need to eat something soon...~~~~~~~~")
        elif hunger > (STARVATION - 30):
            print("~~~~~~~~Your hunger is small, but manageable.~~~~~~~~")
        print(CHOICES)
        user_choice = input("What's the move?\n").lower().strip("!,.? ")

        if user_choice == "a":
            if rice > 0:
                rice -= 1
                hunger = 0
                print("\n--------yum :)--------")
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
            if random.random() < 0.01:
                type_slow(WIN_RIDE)
            else:
                print("--------You try to ride the bike, with no success.--------")
                print("--------The dude seems to be closing the gap...--------")
                energy -= random.randrange(2, 7)
                dude_distance += random.randrange(7, 14)

        elif user_choice == "f":
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

        if user_choice not in ["a", "f"]:
            if user_choice in ["b", "c", "e"]:
                hunger += random.randrange(7, 18)
                turns += 1
            else:
                print("Please pick a valid choice.")

        if hunger >= STARVATION:
            type_slow(LOSE_HUNGER)
            done = True

        elif travelled >= DISTANCE_WIN:
            type_slow(WIN_DISTANCE)
            done = True

        elif dude_distance >= 0:
            type_slow(LOSE_DISTANCE)
            done = True

        elif random.random() < 0.01:
            type_slow(LOSE_TRIP)
            done = True

        elif energy <= 0:
            type_slow(LOSE_ENERGY)
            done = True

        if rice < MAX_RICE and random.random() < 0.05:
            rice = MAX_RICE
            print("~~~~~~~~ Mom stops by and refills your rice. Thanks Mom!~~~~~~~~")

        time.sleep(1.5)
        # TODO: Change the environment based on user choice and RNG
        # TODO: Random event Generator
    print(f"******** You used {turns} turns. ********")


def type_slow(slow_string):
    for char in slow_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)


if __name__ == "__main__":
    main()

