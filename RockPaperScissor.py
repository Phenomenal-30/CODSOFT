import random

choices = ["rock", "paper", "scissors"]
player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)
while True:
    if player_choice in choices:
        if player_choice == computer_choice:
            print("User choice: ",player_choice)
            print("Computer choice: ",computer_choice)
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
            print("User choice: ",player_choice)
            print("Computer choice: ",computer_choice)
            print("You win!")
        else:
            print("User choice: ",player_choice)
            print("Computer choice: ",computer_choice)
            print("Computer wins!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    repeat=input("Do you want to play again(y/n)").lower()
    if repeat=='n':
        break
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)