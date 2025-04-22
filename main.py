# imprts
from time import sleep
import random
random_one = [1,2]
achive = "null"
one = random.choice(random_one)
two = random.choice(random_one)
random_two = [1,2,3,4]
three = random.choice(random_two)
# game
# intro
first_choose = 00
user_name = ""

    # te earth 
e_first_choose = 0
def choose_two():
    print(f"{user_name} are take his crowd choose to back to earth")
    sleep(0.5)
    print(f"{user_name} back to space station and told his boss")
    sleep(0.5)
    print("boss: no you can't back to earth \n you should go to this asteroid and explore it ")

    e_first_choose = int(input("1]Go to asteroid \n 2] disagree with boss and back to earth \n   "))
    if e_first_choose == 1:
        e_one()
    elif e_first_choose==2:
        if one == 1:
            e_two()
        elif one == 2:
            e_two_2()

def e_two():
    print(f"{user_name} are decide to back to earth ")
    sleep(0.5)
    print(f"after 3 month")
    sleep(0.5)
    print(f"{user_name} back to home and he see something wierd in sky ")
    sleep(0.5)
    print(f"{user_name}: oh my god, it is asteroid")
    achive = "big crowd"
    score =0
    if achive == "big crowd":
        score = "10 point"
    elif achive == "unlucky man":
        score = "20 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")

# end
def e_one():
    print(f"{user_name} are decide to back to asteroid ")
    sleep(0.5)
    print(f"after 1 month")
    sleep(0.5)
    print(f"{user_name} back to asteroid and he didn't remember the asteroid was very fast ")
    sleep(0.5)
    print(f"{user_name} called his boss")
    sleep(0.5)
    print(f"{user_name}: boss!! , the asteroid i can't find him ")
    sleep(0.5)
    print(f"boss: i have 2 news")
    sleep(0.5)
    print(f"boss: first, the earth are destoried by your crowd and your slow and secend \n we are live with a big stupid and do you know how this stupied it is you.")
    achive = "slow decision"
    score =0
    if achive == "big crowd":
        score = "10 point"
    if achive == "slow decision":
        score = "20 point"
    elif achive == "unlucky man":
        score = "30 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")
    again = input("do you want play again:(y/n)")
    if again == "y":
        intro()
    else:
        exit   
# end
def e_two_2():
    print(f"{user_name} are decide to back to earth ")
    sleep(0.5)
    print(f"after 1 month")
    sleep(0.5)
    print(f"when {user_name} moving in space he look to earth and he see the worst view ever ")
    sleep(0.5)
    print(f"{user_name}: oh my god, earth are destoried!!")
    achive = "big crowd"
    score =0
    if achive == "big crowd":
        score = "10 point"
    elif achive == "unlucky man":
        score = "30 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")
    again = input("do you want play again:(y/n)")
    if again == "y":
        intro()
    else:
        exit   
# end



# fisrt random 
def a_one():
    print(f"{user_name} are decide to go to explore astoried ")
    sleep(0.5)
    print(f"{user_name} look the asteroid going to him ")
    sleep(0.5)
    print(f"{user_name}: oh my god, this asteroid are going to destory earth if i dont do someting ")
    sleep(0.5)
    print(f"BOOOOOOOOOM!!!")
    achive = "the legend"
    score =0
    if achive == "big crowd":
        score = "10 point"
    elif achive == "unlucky man":
        score = "30 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")
    again = input("do you want play again:(y/n)")
    if again == "y":
        intro()
    else:
        exit   
# secend random
def a_two():
    print(f"{user_name}: oh my god,my fuel are near to empty")
    sleep(0.5)
    print(f"after 3 days ,{user_name} are die")
    achive = "unlucky man"
    score =0
    if achive == "big crowd":
        score = "10 point"
    elif achive == "unlucky man":
        score = "30 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")  
    again = input("do you want play again:(y/n)")
    if again == "y":
        intro()
    else:
        exit        

# third random
def a_three():
    print(f"{user_name} are decide to go to asteroid ")
    sleep(0.5)
    print(f"after 2 month")
    sleep(0.5)
    print(f"{user_name} discovered what this asteroid made by ")
    sleep(0.5)
    print(f"{user_name}: hello boss this the information .......")
    sleep(0.5)
    print(f"after 2 month {user_name} become hero ")
    achive = "famous hero"
    score =0
    if achive == "big crowd":
        score = "10 point"
    elif achive == "unlucky man":
        score = "30 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")
    again = input("do you want play again:(y/n)")
    if again == "y":
        intro()
    else:
        exit   
# four random
def a_four():
    sleep(0.5)
    print(f"{user_name} is decide to go to asteroid ")
    sleep(0.5)
    print(f"{user_name} get information and go to space station ")
    sleep(0.5)
    print(f"{user_name}: this is information we should destory it by the big bang (unclear bomb)")
    sleep(0.5)
    print(f"boss: sure {user_name} we will do it , ... \n and you are a hero ")
    sleep(0.5)
    print(f"{user_name} are decide to back to earth after they destory to earth but .... \n part of asteroid are destory his space craft")
    achive = "unlucky hero"
    score =0
    if achive == "big crowd":
        score = "10 point"
    elif achive == "unlucky man":
        score = "30 point"
    elif achive == "the legend":
        score = "100 point"
    elif achive == "unlucky hero":
        score = "50 point"
    elif achive == "famous hero":
        score = "40 point"
    print(achive)
    print(f"score: {score}")
    again = input("do you want play again:(y/n)")
    if again == "y":
        intro()
    else:
        exit   
# ifs
first_choose = 0
def intro():
    print("In a spacecarft")
    sleep(1)
    print("...")
    sleep(0.5)
    print("the spacecraft are started from earth do explore the space ")
    sleep(0.5)
    print("and when the spacecraft are moving in space ...")
    sleep(0.5)
    user_name = input("Enter your character name ? ")
    sleep(0.5)
    print(f"and when the spacecraft are moving in space {user_name} look after it is a huge asteroid and it is moving very fast")
    sleep(0.5)
    print(f"{user_name} look for his friend words and it was 'no risk no fun'")
    sleep(0.5)
    print(f"{user_name} are look back to asteroid and he discover this asteroid go to earth")
    sleep(0.5)
    print("....")
    sleep(0.5)
    
    f_ch =input("1] Go to explore this asteroid \n 2] Back to Earth \n  ")
    # print(f_ch)
    # print(three)
    if f_ch == "1":
        if three == 1:
            a_one()
        elif three == 2:
            a_two()
        elif three == 3:
            a_three()
        elif three == 4:
            a_four()
    elif f_ch =="2":
        choose_two()
intro()



# achivement
score =0
if achive == "big crowd":
    score = "10 point"
elif achive == "unlucky man":
    score = "20 point"
elif achive == "the legend":
    score = "100 point"
elif achive == "unlucky hero":
    score = "50 point"
elif achive == "famous hero":
    score = "40 point"