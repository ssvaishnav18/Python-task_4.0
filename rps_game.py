import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, comp):
    if user == comp:
        return "tie"
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        return "user"
    else:
        return "computer"


print("===== ROCK - PAPER - SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose one: rock / paper / scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a Tie!")
    elif result == "user":
        print("You Win!")
        user_score += 1
    else:
        print("You Lose!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break
