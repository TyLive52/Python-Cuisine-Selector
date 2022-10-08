#Title What type of cuisine do I want today?

import random
import time
import random


def question():
    cuisine = ("American", "Chinese", "Mexican", "Japanese", "Brazilian", "Italian")
    selection = random.choice(cuisine)
    if selection == "American": print("Let's find a" + " American" + " restaurant!")
    elif selection == "Chinese": print("Let's find a" + " Chinese" + " restaurant!")
    elif selection == "Mexican": print("Let's find a" + " Mexican" + " restaurant!")
    elif selection == "Japanese": print("Let's find a" + " Japanese" + " restaurant!")
    elif selection == "Brazilian": print("Let's find a" + " Brazilian" + " restaurant!")
    elif selection == "Italian": print("Let's find a" + " Italian" + " restaurant!")



answer = input("Are you hungry? (yes/no)").lower().strip()
while True:
    if answer == "yes":
        question()
    elif answer == "no":
        print("Okay maybe later then?")
        time.sleep(7)
        exit()
    retry = input("Would you like to keep looking? (yes/no)")
    if retry == "yes":
        pass
    elif retry == "no":
        print("Enjoy!")
        time.sleep(7)
        break
