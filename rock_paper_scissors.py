import random
import time

def print_game_rules():
    """Prints the rules of Rock, Paper, Scissors."""
    print("\n" + "=" * 40)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 40)
    print("Rules:")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("=" * 40)

def get_player_choice(player_number, choice=None):
    """Gets the player's choice or returns a given choice for testing.

    Parameters:
    player_number (int): The player's number (1 or 2).
    choice (str): Optional; if provided, simulates the player's choice.

    Returns:
    str: The player's choice (rock, paper, or scissors).
    """
    valid_choices = {"rock", "paper", "scissors"}

    if choice is None:
        while True:
            user_choice = input(
                f"Player {player_number}, enter your choice (rock/paper/scissors): "
            ).lower()
            if user_choice in valid_choices:
                return user_choice
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    else:
        if choice in valid_choices:
            return choice
        raise ValueError("Invalid choice for testing")

def determine_winner(player1_choice, player2_choice):
    """
    Determine the winner between two choices.

    Parameters:
    player1_choice (str): The first player's choice.
    player2_choice (str): The second player's choice.

    Returns:
    str: The result of the game ('tie', 'player1', or 'player2').
    """
    if player1_choice == player2_choice:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if winning_combinations.get(player1_choice) == player2_choice:
        return "player1"
    else:
        return "player2"

def display_score(player1_score: int, player2_score: int, round_number: int) -> None:
    """
    Displays the current score of the players.

    Parameters:
    player1_score (int): The score of player 1.
    player2_score (int): The score of player 2.
    round_number (int): The current round number.
    """
    print("\n" + "=" * 40)
    print(f"Round {round_number} Score:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    print("=" * 40)


def count_down(seconds_to_count_down: int) -> None:
    """
    Displays a countdown.

    Parameters:
    seconds_to_count_down (int): The number of seconds to count down.
    """
    for seconds_left in range(seconds_to_count_down, 0, -1):
        print(f"\rGame starts in {seconds_left} seconds...", end="")
        time.sleep(1)
    print("\rLet's begin!                    ")

def main():
    """
    Main function to run the Rock, Paper, Scissors game with two players.
    """
    print_game_rules()
    player_1_score = 0
    player_2_score = 0
    round_number = 1
    max_rounds = 3

    count_down(3)

    while round_number <= max_rounds:
        player_1_choice = get_player_choice(1)
        player_2_choice = get_player_choice(2)

        print(f"\nRound {round_number}:")
        print(f"Player 1 chose {player_1_choice}")
        print(f"Player 2 chose {player_2_choice}")

        winner = determine_winner(player_1_choice, player_2_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player1":
            player_1_score += 2 if player_2_choice == "scissors" and player_1_choice == "rock" else 1
            print("Player 1 wins this round!")
        else:
            player_2_score += 2 if player_1_choice == "scissors" and player_2_choice == "rock" else 1
            print("Player 2 wins this round!")

        display_score(player_1_score, player_2_score, round_number)

        round_number += 1

        if round_number <= max_rounds:
            input("Press Enter to continue to the next round...")

    print("\nGame Over!")
    print(f"Final Score - Player 1: {player_1_score} | Player 2: {player_2_score}")
    if player_1_score > player_2_score:
        print("Player 1 is the overall winner!")
    elif player_2_score > player_1_score:
        print("Player 2 is the overall winner!")
    else:
        print("The game is a tie!")


if __name__ == "__main__":
    main()
