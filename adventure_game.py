from time import sleep
import random

# Global Variables
user_name = ""
achive = "null"
score = 0
turns = 0
max_turns = 3
max_score = 100

random_one = [1, 2]
random_two = [1, 2, 3, 4]

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

def play_round():
    """Plays one round of the game"""
    global score, turns
    one = random.choice(random_one)
    three = random.choice(random_two)

    # Input choice
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("1] Explore the asteroid \n2] Return to Earth\n")
        if choice not in ["1", "2"]:
            print("Invalid input. Please choose 1 or 2.")

    if choice == "1":
        if three == 1:
            a_one()
        elif three == 2:
            a_two()
        elif three == 3:
            a_three()
        elif three == 4:
            a_four()
    else:
        choose_two(one)

    turns += 1

def choose_two(one):
    global score
    score -= 5  # Penalty
    print(f"Your score: {score} Points")
    print(f"{user_name} decides to return to Earth and informs the boss.")
    sleep(1)
    print("Boss: 'No, you must explore the asteroid!'")
    sleep(1)

    choice = ""
    while choice not in ["1", "2"]:
        choice = input("1] Obey and go to the asteroid\n2] Disobey and return to Earth\n")
        if choice not in ["1", "2"]:
            print("Invalid input. Please choose 1 or 2.")

    if choice == "1":
        e_one()
    else:
        if one == 1:
            e_two()
        else:
            e_two_2()

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

def set_achivement(name, story):
    global achive, score
    achive = name
    print(story)
    sleep(1)
    print(f"Achievement: {achive}")

    scores = {
        "big crowd": 10,
        "unlucky man": 30,
        "the legend": 100,
        "unlucky hero": 50,
        "famous hero": 40,
        "slow decision": 20
    }
    earned = scores.get(achive, 0)
    score += earned
    print(f"Score earned this round: {earned}")
    print(f"Total score: {score}")

def get_valid_input(prompt, valid_choices):
    choice = ""
    while choice not in valid_choices:
        choice = input(prompt).lower()
        if choice not in valid_choices:
            print(f"Invalid input. Please choose from {', '.join(valid_choices)}.")
    return choice

#  Game Start
print(" Welcome to the Asteroid Adventure!")
intro()

# Game Loop with clear end condition
while turns < max_turns and score < max_score:
    print(f"\n Round {turns + 1}")
    play_round()

# End of Game
print("\nGAME OVER ")
print(f"Final score: {score}")
print(f"Rounds played: {turns}")

again = get_valid_input("Do you want to play again? (y/n): ", ["y", "n"])
if again == "y":
    # Reset values and restart
    score = 0
    turns = 0
    intro()
    while turns < max_turns and score < max_score:
        print(f"\n Round {turns + 1}")
        play_round()
    print("\nGAME OVER AGAIN ")
    print(f"Final score: {score}")
    print(f"Rounds played: {turns}")
else:
    print("Thanks for playing!")
