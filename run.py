import random
import string
import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('simple-battleships')

results = SHEET.worksheet('results')


class BattleshipGame:
    """
    A class representing a simple battleship game.

    Attributes:
        board_size (int): The size of the game board.
        board (list): A 2D list representing the game board.
        ships (dict): A dictionary containing ship names as keys and their coordinates as values.
        guesses (list): A list to store the player's guesses.
        tries (int): Number of tries the player has.
        player_name (str): Name of the player.
        datetime (str): Datetime when the game was played.
        game_id (int): Unique ID of the game.
        outcome (str): Outcome of the game (Win/Loss).
    """
    SHEET = SHEET  # Class variable to store the Google Sheets spreadsheet object
    RESULTS_WORKSHEET = results

    def __init__(self, board_size=10, num_ships=4, max_tries=10):
        """
        Initialize the BattleshipGame with a default board size of 10, 4 ships, and 10 tries.
        """
        self.board_size = board_size
        self.board = [['O' for _ in range(board_size)] for _ in range(board_size)]
        self.ships = {}
        self.generate_ships(num_ships)
        self.guesses = []
        self.tries = max_tries
        self.player_name = None
        self.datetime = None
        self.game_id = None
        self.outcome = None

    def generate_ships(self, num_ships):
        """
        Randomly generate ships and their coordinates on the game board.
        """
        ship_names = [f"Ship{i}" for i in range(1, num_ships + 1)]  # Names of the ships
        for ship_name in ship_names:
            while True:
                # Randomly select a starting position
                start_row = random.randint(0, self.board_size - 1)
                start_col = random.randint(0, self.board_size - 1)

                # Check if the ship fits in the selected position
                end_row = start_row + 2  # 3 consecutive dots vertically
                end_col = start_col + 2  # 3 consecutive dots horizontally
                if end_row < self.board_size and end_col < self.board_size:
                    ship_coords = [(start_row + i, start_col) for i in range(3)]  # Vertical ship
                    if all(coord not in [coord for coords in self.ships.values() for coord in coords] for coord in
                           ship_coords):
                        # Add ship coordinates to the dictionary
                        self.ships[ship_name] = ship_coords
                        break

    def print_board(self):
        """
        Print the current state of the game board.
        """
        print("  " + " ".join(string.ascii_uppercase[:self.board_size]))
        for i, row in enumerate(self.board):
            print(i + 1, " ".join(row))

    def check_guess(self, row, col):
        """
        Check if the player's guess hits a ship.

        Args:
            row (int): The row of the guess.
            col (int): The column of the guess.

        Returns:
            str: A message indicating the result of the guess.
        """
        for ship_name, ship_coords in self.ships.items():
            if (row, col) in ship_coords:
                self.board[row][col] = 'X'  # Mark the hit on the board
                return f"Hit! You sank {ship_name}!"
        self.board[row][col] = 'M'  # Mark the miss on the board
        return "Miss!"

    def play(self):
        """Play the battleship game."""
        print("Welcome to Simple Battleships!")
        print("\nSimple Battleships is a classic game where you try to sink the hidden ships of your opponent.")
        print("The game board consists of a grid with rows labeled 1 through 10 and columns labeled A through J.")
        print("You will have 10 attempts to guess the location of the ships on the board.")
        print("Each ship occupies a single cell on the board.")
        print("If your guess hits a ship, it will be marked as 'X' on the board.")
        print("If your guess misses, it will be marked as 'M' on the board.")
        print("Your goal is to sink all the ships with as few guesses as possible.\n")

        self.player_name = input("Enter your name: ")
        self.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Welcome to Simple Battleships, {self.player_name}!")
        self.print_board()
        while self.tries > 0:
            print(f"You have {self.tries} tries left.")
            try:
                guess_row = int(input("Guess Row (1-10): ")) - 1
                guess_col = string.ascii_uppercase.index(input("Guess Col (A-J): ").upper())
            except ValueError:
                print("Please enter valid row (1-10) and column (A-J) values.")
                continue
            if guess_row < 0 or guess_row >= self.board_size or guess_col < 0 or guess_col >= self.board_size:
                print("Oops, that's not even in the ocean.")
                continue
            if (guess_row, guess_col) in self.guesses:
                print("You guessed that one already.")
                continue
            self.guesses.append((guess_row, guess_col))
            result = self.check_guess(guess_row, guess_col)
            print(result)
            self.print_board()
            if all(all(cell == 'X' for cell in row) for row in self.board):
                print("Congratulations! You sunk all the battleships!")
                self.outcome = "Win"
                break
            self.tries -= 1
        else:
            print("Game over! You've run out of tries.")
            self.outcome = "Loss"

        # Save game results to Google Sheets
        self.save_results()

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.reset()
            self.play()
        else:
            print("Thank you for playing Simple Battleships!")

    def save_results(self):
        """
        Save the game results to the Google Sheets spreadsheet.
        """
        if self.player_name and self.datetime and self.outcome:
            # Generate a unique game ID
            self.game_id = random.randint(1000, 9999)

            self.RESULTS_WORKSHEET.append_row(
                [self.game_id, self.player_name, self.datetime, 10 - self.tries, self.outcome])
            print("Game results saved successfully.")
        else:
            print("Unable to save game results: missing information.")

    def reset(self):
        """
        Reset the game for a new play session.
        """
        self.board = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = {}
        self.guesses = []
        self.tries = 10
        self.player_name = None
        self.datetime = None
        self.game_id = None
        self.outcome = None


if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
