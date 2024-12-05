import random
import os

print("RPS!")

def get_user_choice():
    while True:
        try:
            choice = input("Please enter rock, paper, or scissors: ").lower()
            if choice not in ["rock", "paper", "scissors"]:
                raise ValueError
        except ValueError:
            print("Please enter 'rock', 'paper', 'scissors'.")
        else:
            return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    return "Computer wins!"

def rps():
    user_score = 0
    computer_score = 0

    while True:
        os.system('clear')
       

        print("Current Scores - You: {}, Computer: {}".format(user_score, computer_score))

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        game_result = determine_winner(user_choice, computer_choice)

        print(f"User choice: {user_choice}")
        print(f"Comp choice: {computer_choice}")
        print(f"{game_result}")

        if game_result == "You win!":
            user_score += 1
        elif game_result == "Computer wins!":
            computer_score += 1

        n_round = input("Want to play again? Type y or n: ").lower() in ["y", "yes"]
        if not n_round:
            print("Thanks for playing!")
            break

rps()
