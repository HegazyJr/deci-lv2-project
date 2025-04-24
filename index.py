# Imports
from time import sleep  # Used to delay between messages
import random  # Used for randomizing story outcomes

# Global Variables
user_name = ""     # Player's name
achive = "null"    # Player's achievement
score = 0          # Player's score
run = True         # Control flag (not used)

# Random choices to influence the path
random_one = [1, 2]
random_two = [1, 2, 3, 4]
one = random.choice(random_one)     # Used in choose_two()
three = random.choice(random_two)   # Used to determine asteroid outcome

def intro():
    """Start of the game. Introduces the situation and asks the first main decision."""
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

    # Loop to handle invalid input until user enters '1' or '2'
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("1] Explore the asteroid \n2] Return to Earth\n")
        if choice not in ["1", "2"]:
            print("Invalid input. Please choose 1 or 2.")

    # Random outcome based on 'three'
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

def choose_two():
    """Handles the second major decision if player chooses to go back to Earth."""
    global score
    score -= 5  # Penalty for refusing to explore the asteroid
    print(f"Your score : {score} Point")
    print(f"{user_name} decides to return to Earth and informs the boss.")
    sleep(1)
    print("Boss: 'No, you must explore the asteroid!'")

    # Input validation loop for choice
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("1] Obey and go to the asteroid\n2] Disobey and return to Earth\n")
        if choice not in ["1", "2"]:
            print("Invalid input. Please choose 1 or 2.")

    # Branching based on previously generated random number
    if choice == "1":
        e_one()
    else:
        if one == 1:
            e_two()
        else:
            e_two_2()

def e_one():
    """Outcome: Obeys boss but is too late. Earth destroyed."""
    set_achivement("slow decision", f"{user_name} obeys but asteroid disappears and Earth is destroyed.")

def e_two():
    """Outcome: Disobeys and returns to Earth, sees asteroid."""
    set_achivement("big crowd", f"{user_name} returns and sees a huge asteroid over Earth!")

def e_two_2():
    """Outcome: Returns to Earth but it's already destroyed."""
    set_achivement("big crowd", f"{user_name} returns and sees Earth already destroyed.")

def a_one():
    """Outcome: Crashes into the asteroid, heroic ending."""
    set_achivement("the legend", f"{user_name} crashes into asteroid to save Earth. Boom!")

def a_two():
    """Outcome: Runs out of fuel and dies alone."""
    set_achivement("unlucky man", f"{user_name} runs out of fuel and dies in space.")

def a_three():
    """Outcome: Studies asteroid and becomes a famous hero."""
    set_achivement("famous hero", f"{user_name} studies the asteroid and becomes a hero.")

def a_four():
    """Outcome: Helps destroy asteroid, but dies on return."""
    set_achivement("unlucky hero", f"{user_name} helps destroy the asteroid, but dies on return.")

def set_achivement(name, story):
    """Sets the final achievement and score, prints story, asks to replay."""
    global achive, score
    achive = name
    print(story)
    sleep(1)
    print(f"Achievement: {achive}")

    # Assign score based on ending. These are fixed values.
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

def get_valid_input(prompt, valid_choices):
    """Asks for input until valid response is given. Useful for y/n prompts."""
    choice = ""
    while choice not in valid_choices:
        choice = input(prompt).lower()
        if choice not in valid_choices:
            # .join makes a readable string from list like ["y", "n"] => y, n
            print(f"Invalid input. Please choose from {', '.join(valid_choices)}.")
    return choice

# Ask to play again (outside functions, but should be inside game loop ideally)
again = get_valid_input("Do you want to play again? (y/n): ", ["y", "n"])

# Start the game
intro()
