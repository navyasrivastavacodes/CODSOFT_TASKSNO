# -----------------------------------------
# Rock Paper Scissors Game
# User vs Computer
# Features:
# - Random computer choice
# - Input validation
# - Replay option
# -----------------------------------------

import random

game_choices = ["rock", "paper", "scissors"]

while True:

    computer_choice = random.choice(game_choices)

    user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()

    print("You chose:", user_choice)

    if user_choice not in game_choices:
        print("Invalid choice!")

    else:
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a Draw!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You Win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You Win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You Win!")
        else:
            print("Computer Wins!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again == "no":
        print("Thank you for playing!")
        break
    elif play_again == "yes":
        continue
    else:
        print("Invalid choice! Please enter 'yes' or 'no'.")