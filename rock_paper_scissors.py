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
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!" 
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!" 
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!" 
        else:
            return "Rock smashes scissors! You lose!"
      

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(resultpap)



       #elif player == "rock" and computer == "paper":
#p_choice = choices["player"]
#c_choice = choices["computer"]
## To continue: https://youtu.be/eWRfhZUzrAc?t=2633