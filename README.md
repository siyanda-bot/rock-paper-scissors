Rock, Paper, Scissors Game
Description

A simple command-line Rock, Paper, Scissors game for two players, implemented in Python 3. The game features:

    Displaying game rules
    Collecting player choices
    Determining the winner of each round
    Displaying current scores
    Countdown before starting the game

Features

    Game Rules: Displays the rules of Rock, Paper, Scissors.
    Player Choices: Players input their choices for each round.
    Determine Winner: Computes the winner based on the players' choices.
    Score Display: Shows scores after each round.
    Countdown: Counts down before the game starts.

Installation

Ensure you have Python 3 installed on your system. No additional packages are required.

    Clone the repository:

    bash

git clone https://github.com/siyanda-bot/rock-paper-scissors.git

Navigate to the project directory:

bash

    cd rock-paper-scissors

Usage

    Run the game:

    bash

    python3 rock_paper_scissors.py

    Follow the prompts to play the game. Enter rock, paper, or scissors when asked for your choice.

Testing

The project includes unit tests to ensure the correct functionality of the game logic.

    Run the tests:

    bash

    python3 -m unittest test_rock_paper_scissors.py

Code Structure

    rock_paper_scissors.py: Contains the main game logic and functions.
    test_rock_paper_scissors.py: Contains unit tests for the game functions.

Functions

    print_game_rules(): Prints the rules of Rock, Paper, Scissors.
    get_player_choice(player_number, choice=None): Gets the player's choice or simulates it for testing.
    determine_winner(player1_choice, player2_choice): Determines the winner based on the players' choices.
    display_score(player1_score, player2_score, round_number): Displays the scores after each round.
    count_down(seconds_to_count_down): Displays a countdown before the game starts.

Testing

The project includes tests for the following functions:

    determine_winner: Tests the function for various scenarios.
    get_player_choice: Tests valid and invalid choices.
    print_game_rules: Verifies the correct display of game rules.
    count_down: Tests the countdown functionality, with mocked sleep for faster execution.

License

This project is licensed under the MIT License. See the LICENSE file for details.

