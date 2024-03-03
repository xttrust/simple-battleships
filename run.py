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

