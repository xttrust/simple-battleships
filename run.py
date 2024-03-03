import random
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
    """
    SHEET = SHEET  # Class variable to store the Google Sheets spreadsheet object

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
                    if all(coord not in [coord for coords in self.ships.values() for coord in coords] for coord in ship_coords):
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
                break
            self.tries -= 1
        else:
            print("Game over! You've run out of tries.")

if __name__ == "__main__":
    game = BattleshipGame()
    game.play()

