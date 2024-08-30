import unittest
from unittest.mock import patch
from io import StringIO
import sys
import time

# Import the functions from the game module
from rock_paper_scissors import determine_winner, get_player_choice, print_game_rules,count_down

class TestRockPaperScissors(unittest.TestCase):

    def test_determine_winner(self):
        """Test the determine_winner function."""
        self.assertEqual(determine_winner("rock", "scissors"), "player1")
        self.assertEqual(determine_winner("scissors", "paper"), "player1")
        self.assertEqual(determine_winner("paper", "rock"), "player1")
        self.assertEqual(determine_winner("scissors", "rock"), "player2")
        self.assertEqual(determine_winner("paper", "scissors"), "player2")
        self.assertEqual(determine_winner("rock", "rock"), "tie")
        self.assertEqual(determine_winner("paper", "paper"), "tie")
        self.assertEqual(determine_winner("scissors", "scissors"), "tie")


    def test_get_player_choice(self):
        """Test the get_player_choice function."""
        # Valid choices
        # Mock input for valid choices
        with patch('builtins.input', side_effect=['rock']):
            self.assertEqual(get_player_choice(1), 'rock')
        
        with patch('builtins.input', side_effect=['paper']):
            self.assertEqual(get_player_choice(2), 'paper')

        with patch('builtins.input', side_effect=['scissors']):
            self.assertEqual(get_player_choice(1), 'scissors')

        # Invalid choices followed by a valid choice
        # Mock input for invalid choices followed by a valid choice
        with patch('builtins.input', side_effect=['invalid', 'rock']):
            self.assertEqual(get_player_choice(2), 'rock')


    def test_print_game_rules(self):
        """Test the print_rules function."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_game_rules()
            output = fake_out.getvalue()
            self.assertIn("Welcome to Rock, Paper, Scissors!", output)
            self.assertIn("Rock crushes Scissors", output)
            self.assertIn("Scissors cuts Paper", output)
            self.assertIn("Paper covers Rock", output)

    @patch('time.sleep', return_value=None)  # Mock time.sleep to speed up the test
    def test_count_down(self, mock_sleep):
        """Test the count_down function."""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            count_down(3)  # Test with a countdown of 3 seconds
            output = fake_stdout.getvalue()

            # Check if the countdown messages are in the output
            self.assertIn('Game starts in 3 seconds...', output)
            self.assertIn('Game starts in 2 seconds...', output)
            self.assertIn('Game starts in 1 seconds...', output)
            self.assertIn("Let's begin!", output)


if __name__ == '__main__':
    unittest.main()
