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

