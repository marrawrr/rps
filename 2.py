import random

print("RPS!")
def get_user_choice():
    choice = input("Please enter rock, paper, or scissors:")
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    return choice

print(get_user_choice())
print(get_computer_choice())

