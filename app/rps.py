# This is the rock paper siccors game

print("Welcome to the game")

player_choice = input("Please input an option: ('rock', 'paper', 'scissors')")
print("USER CHOICE:", player_choice)

import random
VALID_OPTIONS = ["rock", "paper", "scissors"]

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", computer_choice)

if player_choice == computer_choice:
    result = "TIE GAME"
elif player_choice == "rock" and computer_choice == "scissors":
    result = "USER WINS"
elif player_choice == "rock" and computer_choice == "paper":
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "rock":
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "paper":
    result = "USER WINS"
elif player_choice == "paper" and computer_choice == "rock":
    result = "COMP WINS"
elif player_choice == "paper" and computer_choice == "scissors":
    result = "COMP WINS"

print(result)