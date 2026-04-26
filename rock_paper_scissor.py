"""
AI-BASED ROCK PAPER SCISSOR GAME
--------------------------------
AUTHOR : Rajneesh Kaur(Cherry)

DESCRIPTION:
A command line rock paper scissor game with an adaptive ai opponent that predicts user
behaviour using frequency based analysis.

FEATURES :
- play again loop
- score tracking (Best of 3/Best of 5)
- AI-Based move prediction
- input validation

"""
import random
from collections import Counter

choices = ["rock","paper","scissor"]

def main():
    """ Entry point of the game """
    print("---------WELCOME TO AI ROCK PAPER SCISSOR----------")
    while True:
        rounds_to_win = select_mode()
        play_game(rounds_to_win)

        if not play_again():
            print("thanks for playing!")
            break

def select_mode():
    """allow users to select game mode."""
    while True:
        print("\nSelect Mode:")
        print("1. Best of 3")
        print("2. Best of 5")

        choice = input("Enter Choice(1/2):").strip()
        if choice == "1":
            return 2
        elif choice == "2":
            return 3
        else:
            print("invalid choice! please choose 1 or 2 !")

def play_game(rounds_to_win):
    """runs the main game loop."""
    user_score = 0
    computer_score = 0
    user_history = []

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\n Score - You: {user_score} | Computer: {computer_score}")
        user_move = get_user_move()
        user_history.append(user_move)

        computer_move = get_ai_move(user_history)
        print(f"YOU CHOSE: {user_move}")
        print(f"COMPUTER CHOSE: {computer_move}")

        winner = decide_winner(user_move, computer_move)

        if winner == "user":
            user_score += 1
            print("you win this round")

        elif winner == "computer":
            computer_score += 1
            print("computer win this match!")

        else:
            print("it's a tie!")

    show_final_result(user_score, computer_score)
def get_user_move():
    """get validated user input"""
    while True:
        move = input("choose(rock/paper/scissor): ").lower().strip()
        if move in choices:
            return move
        print("Invalid Choice. Try Again")


def get_ai_move(history):
    """
    AI predicts user's most frequent move and counters it.
    falls back to random choice if no history exists.
    
    """        
    if not history:
        return random.choice(choices)  
    most_common_move = Counter(history).most_common(1)[0][0]

    counter_moves = {
        "rock":"paper",
        "paper":"scissor",
        "scissor":"rock"
    }                

    return counter_moves[most_common_move]


def decide_winner(user,computer):
    """ Determine round Winner """
    if user == computer:
        return "tie"
    
    winning_cases = {
        ("rock","scissor"),
        ("scissor","paper"),
        ("paper","rock")  
     }
    return "user" if (user,computer) in winning_cases else "computer"
def show_final_result(user_score, computer_score):
    """
    Display final game result
    """
    print("\n Final Result:")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("YOU WON THE GAME! CONGRATS!")

    else:
        print("COMPUTER WON THE GAME!")

def play_again():
    """ ask user if they want to play again"""   
    choice = input("\n do you want to play again?(yes/no):").lower().strip()
    return choice == "yes"

if __name__ == "__main__":

    main()