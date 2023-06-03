#!/usr/bin/python3
import random
def roll_dice():
    print("Welcome to dice simulator")
    value = input("Press S button to start: ")
    if value == "S":    
        random_nr = random.randint(1,6)
        print(f"Your dice value is {random_nr}")
        print("Do u want to play again? ")
        val = input("Type yes to roll again: ")
        if val == "yes":
            ran_nr = random.randint(1,6)
            print(f"Your dice value is {ran_nr}")
    else:
        print("Wrong button try again")
while True:
    roll_dice()
    break
