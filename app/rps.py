# This is the rock paper siccors game
import random

VALID_OPTIONS = ["rock", "paper", "scissors"]

# here the input variable can be named any other way not necessarily the one used for input 
def determine_winner(player_choice, computer_choice):
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
            # result = "COMP WINS" this was a bug
            result = "USER WINS"
        elif player_choice == "paper" and computer_choice == "scissors":
            result = "COMP WINS"
        return result

# ONLY RUN THE CODE INDENTED INSIDE
# ... IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
# ... BUT NOT IF WE ARE IMPORTING

if __name__ == "__main__":

    #player_choice = input("Please input an option: ('rock', 'paper', 'scissors')")
    print("Welcome to the game")
    player_choice = input("Please input an option: ('rock', 'paper', 'scissors')")
    print("USER CHOICE:", player_choice)
    computer_choice = random.choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", computer_choice)

    result_message = determine_winner(player_choice, computer_choice)
    print(result_message)
