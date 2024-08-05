import random
def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_score = 0
    user_score = 0
    while True:
        print("\nRock Paper Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        user_choice = input("Enter your choice (1/2/3/4): ")
        if user_choice == "4":
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break
        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please choose a valid option.")
            continue
        user_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break
if __name__ == "__main__":
    play_game()


