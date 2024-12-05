import random

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
        return "You win!"
    if user_choice == "Rock" and computer_choice == "Scissors":
        return "You win!"
    if user_choice == "Paper" and computer_choice == "Rock":
        return "You win!"
    if user_choice == "Scissors" and computer_choice == "Paper":
        return "You win!"

    return "Computer wins!"

def rps():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    game = determine_winner(user_choice, computer_choice)

    print(f"User choice: {user_choice}")
    print(f"Comp choice: {computer_choice}")

    print(f"{game}") 
while True:
  rps()
  n_round = input("Want to play again? Type y or n:") in ["y","Y", "yes","YES", "yES","YeS","YEs","yEs","yeS"]
  if not n_round:
    print("Maybe next time?")
    break
