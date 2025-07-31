# This is the rock paper siccors game

print("Welcome to the game")

player_choice = input("Please input an option: ('rock', 'paper', 'scissors')")
print("USER CHOICE:", player_choice)

import random
VALID_OPTIONS = ["rock", "paper", "scissors"]

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", computer_choice)

print("WINNER: TODO")