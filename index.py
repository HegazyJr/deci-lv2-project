# Imports
from time import sleep
import random

# Variables
user_name = ""
achive = "null"
score = 0

# Random values to shape the story outcome
random_one = [1, 2]
random_two = [1, 2, 3, 4]
one = random.choice(random_one)
three = random.choice(random_two)

# Main intro function
def intro():
    global user_name
    print("In a spacecraft...")
    sleep(1)
    print("The spacecraft is moving through space to explore...")
    sleep(1)
    user_name = input("Enter your character name: ")
    print(f"As {user_name} watches space, a huge asteroid appears heading fast toward Earth!")
    sleep(1)
    print(f"{user_name} remembers a quote: 'No risk, no fun!'")
    sleep(1)
    choice = input("1] Explore the asteroid \n2] Return to Earth\n")

    if choice == "1":
        if three == 1:
            a_one()
        elif three == 2:
            a_two()
        elif three == 3:
            a_three()
        elif three == 4:
            a_four()
    elif choice == "2":
        choose_two()

# Story Branch: Return to Earth
def choose_two():
    print(f"{user_name} decides to return to Earth and informs the boss.")
    sleep(1)
    print("Boss: 'No, you must explore the asteroid!'")
    choice = int(input("1] Obey and go to the asteroid\n2] Disobey and return to Earth\n"))

    if choice == 1:
        e_one()
    else:
        if one == 1:
            e_two()
        else:
            e_two_2()

# Outcomes
def e_one():
    set_achivement("slow decision", f"{user_name} obeys but asteroid disappears and Earth is destroyed.")
    
def e_two():
    set_achivement("big crowd", f"{user_name} returns and sees a huge asteroid over Earth!")

def e_two_2():
    set_achivement("big crowd", f"{user_name} returns and sees Earth already destroyed.")

def a_one():
    set_achivement("the legend", f"{user_name} crashes into asteroid to save Earth. Boom!")

def a_two():
    set_achivement("unlucky man", f"{user_name} runs out of fuel and dies in space.")

def a_three():
    set_achivement("famous hero", f"{user_name} studies the asteroid and becomes a hero.")

def a_four():
    set_achivement("unlucky hero", f"{user_name} helps destroy the asteroid, but dies on return.")

# Set achievement and score based on result
def set_achivement(name, story):
    global achive, score
    achive = name
    print(story)
    sleep(1)
    print(f"Achievement: {achive}")

    # Score system
    scores = {
        "big crowd": "10 points",
        "unlucky man": "30 points",
        "the legend": "100 points",
        "unlucky hero": "50 points",
        "famous hero": "40 points",
        "slow decision": "20 points"
    }
    score = scores.get(achive, "0 points")
    print(f"Score: {score}")

    # Replay
    again = input("Do you want to play again? (y/n): ")
    if again.lower() == "y":
        intro()
    else:
        exit()

# Start the game
intro()
