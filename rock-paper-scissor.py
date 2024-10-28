import random

def get_choice():
    player_choice = input("Enter a choice(rock, paper, scissors):")
    options = ["rock","paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices



def check_win(player, computer):
    # print("You chose "+player +", computer chose "+ computer)
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player =="rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        elif computer == "paper":
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper! You lose!"
        elif computer == "rock":
            return "Paper covers rock! You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        elif computer == "paper":
            return "Scissors cut paper! You Win!"
        

choice = get_choice()

result = check_win(choice["player"], choice["computer"])
print(result)
