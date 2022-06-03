import random
# "R" stands for Rock
# "S" stands for Scissors
# "P" stands for Paper
while True:
    user_action = input("Enter a choice(R, P, S): ")
    possible_actions = ["R", "S", "P"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("R smashes S! You wins!")
        else:
            print("P covers R! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("P covers R! You win!")
        else:
            print("S cuts P! You lose.")
    elif user_action == "S":
        if computer_actions == "P":
            print("S cuts P! You wins!")
        else:
            print("R smashes S! You lose.")
    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        break
