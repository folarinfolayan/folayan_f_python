# import the random package so that we can generate random numbers 
from random import randint

# choices is an array => a container that can hold multipl items # arrays are 0-based -> the first item is 0, second item is 1 etc 
choices = ["Rock", "Paper","Scissors"] 

# giving the user the option to play rps again
play_again = ["yes", "no"]

# make the computer choose a random number 
computer_choice = choices[randint(0,2)] 

#loop for player life
player_life = (3)

#loop for computer life
computer_life = (3)

#player inputs their choice 
player_choice = input("Player enter your weapon of choice: Rock, Paper, Scissors?\n") 

# print the choice made by computer 
print("Computer Chooses: ", computer_choice)

if player_choice == computer_choice:
        print("Tie!")
elif player_choice == "Rock":
    if computer_choice == "Paper":
            print("You lose!", computer_choice, "covers", player_choice)
            player_life -= 1
            print("Player has lost 1 life, Player has", player_life, "lives left")
    else:
            print("You win!", player_choice, "smashes", computer_choice)
            computer_life -= 1
            print("Computer has lost 1 life, Computer has", computer_life, "lives left")
elif player_choice == "Paper":
    if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player_choice)
            player_life -= 1
            print("Player has lost 1 life, Player has", player_life, "lives left")
    else:
            print("You win!", player_choice, "covers", computer_choice)
            computer_life -= 1
            print("Computer has lost 1 life, Computer has", computer_life, "lives left")            
elif player_choice == "Scissors":
    if computer_choice == "Rock":
            print("You lose...", computer_choice, "smashes", player_choice)
            player_life -= 1
            print("Player has lost 1 life, Player has", player_life, "lives left")
    else:
            print("You win!", player_choice, "cut", computer_choice)
            computer_life -= 1
            print("Computer has lost 1 life, Computer has", computer_life, "lives left")
else:
            print("Invalid choice")
            player_choice = input("Player enter your weapon of choice: Rock, Paper, Scissors?\n") 
if player_life <= (0) or computer_life <= (0):
    pass
    play_again = input("You have lost the game, would you like to play again: yes, no?")
