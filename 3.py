import random

print("RPS!")

def get_user_choice():
  choice = input("Please enter rock, paper, or scissors: ")
  return choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  comp_choice = random.choice(choices)
  return comp_choice

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print("Tie.")

  elif (user_choice == "scissors" and computer_choice == "paper") or \
  (user_choice == "paper" and computer_choice == "rock") or \
  (user_choice =="rock" and computer_choice=="scissors"):
    print("You win!")

  else:
    print("Computer wins!")



user_choice = get_user_choice()
computer_choice = get_computer_choice()
print(f"Computer: {computer_choice}")
determine_winner(user_choice, computer_choice)

