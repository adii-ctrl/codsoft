import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        choice = input("Please choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

    return result

def main():
    user_score = 0
    computer_score = 0
    round_number = 1

    print(" Welcome to Rock-Paper-Scissors Game! \n")

    while True:
        print(f"\n--- Round {round_number} ---")
        result = play_round()

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            break
        round_number += 1

    print("\nThanks for playing! Final Score:")
    print(f"You: {user_score} | Computer: {computer_score}")
    print(" Goodbye!")

if __name__ == "__main__":
    main()
