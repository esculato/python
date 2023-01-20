import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock","paper","scissors"]  
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

#choices = get_choices()
#print(choices)

def check_win(player, computer):
  # print("You chose " + player + ". computer chose" + computer)
    print(f"You chose {player}, computer chose {computer}.") # f-string
    if player == computer:
        return "It's a tie!" #parenthesis are option () with return
    elif player 
    return [player, computer]

check_win("rock","paper")


## To continue: https://youtu.be/eWRfhZUzrAc?t=1901