import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choices()
print(choices)

## To continue: https://www.youtube.com/watch?v=eWRfhZUzrAc&t=1108s