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
        player_hits (int): Number of hits by the player.
        cpu_hits (int): Number of hits by the CPU.
    """
    SHEET = SHEET  # Class variable to store the Google Sheets spreadsheet object
    RESULTS_WORKSHEET = results

    def __init__(self, board_size=10, num_ships=4, max_tries=10):
        """
        Initialize the BattleshipGame with a default board size of 10, 4 ships, and 10 tries.
        """
        self.board_size = board_size
        self.board = [['-' for _ in range(board_size)] for _ in range(board_size)]
        self.ships = {}
        self.generate_ships(num_ships)
        self.guesses = []
        self.tries = max_tries
        self.player_name = None
        self.datetime = None
        self.game_id = None
        self.outcome = None
        self.player_hits = 0
        self.cpu_hits = 0

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

    def check_guess(self, row, col, player):
        """
        Check if the player's guess hits a ship.

        Args:
            row (int): The row of the guess.
            col (int): The column of the guess.
            player (str): The player making the guess ('player' or 'cpu').

        Returns:
            str: A message indicating the result of the guess.
        """
        for ship_name, ship_coords in self.ships.items():
            if (row, col) in ship_coords:
                if player == 'player':
                    self.player_hits += 1
                    self.board[row][col] = 'X'  # Mark the hit on the board
                    if self.player_hits == 4:
                        return f"Hit! You sank all the battleships first!\nCongratulations! You win!"
                    else:
                        return f"Hit! You sank {ship_name}!"
                else:
                    self.cpu_hits += 1
                    self.board[row][col] = 'O'  # Mark the hit on the board
                    if self.cpu_hits == 4:
                        return "The CPU sunk all the battleships!\nYou lost!"
                    else:
                        return "The CPU hit the battleship!"
        self.board[row][col] = 'M'  # Mark the miss on the board
        return "Miss!"

    def player_guess(self):
        """
        Prompt the player to make a guess and return the row and column indices.
        """
        while True:
            try:
                guess_row = int(input("Guess Row (1-10): ")) - 1
                guess_col = string.ascii_uppercase.index(input("Guess Col (A-J): ").upper())
                if not (0 <= guess_row < self.board_size and 0 <= guess_col < self.board_size):
                    raise ValueError
                if (guess_row, guess_col) in self.guesses:
                    print("You guessed that one already.")
                    continue
                self.guesses.append((guess_row, guess_col))
                return guess_row, guess_col
            except ValueError:
                print("Please enter valid row (1-10) and column (A-J) values.")

    def cpu_guess(self):
        """
        Generate a random guess for the CPU and return the row and column indices.
        """
        guess_row = random.randint(0, self.board_size - 1)
        guess_col = random.randint(0, self.board_size - 1)
        return guess_row, guess_col


    def reset_game(self):
        """Reset the game state."""
        self.board = [['-' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = {}
        self.generate_ships(4)
        self.guesses = []
        self.tries = 10
        self.outcome = None
        self.player_hits = 0
        self.cpu_hits = 0
    

    def save_results(self):
        """
        Save the game results to the Google Sheets spreadsheet.
        """
        if self.player_name and self.datetime and self.outcome:
            # Generate a unique game ID
            self.game_id = random.randint(1000, 9999)

            self.RESULTS_WORKSHEET.append_row(
                [self.game_id, self.player_name, self.datetime, self.player_hits, self.cpu_hits, self.outcome])
            print("\nGame results saved successfully.")
        else:
            print("\nUnable to save game results: missing information.")


    def play(self):
       """Play the battleship game."""
        print("Welcome to Simple Battleships!")
        print("\nSimple Battleships is a classic game where you try to sink the hidden ships before your opponent (CPU).")
        print("The game board consists of a grid with rows labeled 1 through 10 and columns labeled A through J.")
        print("You will have 10 attempts to guess the location of all 4 ships on the board.")
        print("The computer will also have 10 attempts to guess the location of the ships.")
        print("Each ship occupies a single cell on the board.")
        print("If your guess hits a ship, it will be marked as 'X' on the board. For CPU, it will be marked as 'O'.")
        print("If your or CPU's guess misses, it will be marked as 'M' on the board.")
        print("Your goal is to sink more ships than the CPU.\n")

        self.player_name = input("Enter your name: ")
        self.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Welcome to Simple Battleships, {self.player_name}!")
        self.print_board()

        while self.tries > 0:
            print(f"\nYou have {self.tries} tries left.")
            # Player's turn
            print("\nPlayer's turn:")
            guess_row, guess_col = self.player_guess()
            result = self.check_guess(guess_row, guess_col, 'player')
            print(result)
            self.print_board()
            if "Congratulations" in result:
                self.outcome = "Win"
                break

            # CPU's turn
            print("\nCPU's turn:")
            guess_row, guess_col = self.cpu_guess()
            result = self.check_guess(guess_row, guess_col, 'cpu')
            print(result)
            self.print_board()
            if "You lost" in result:
                self.outcome = "Loss"
                break

            self.tries -= 1
        else:
            print("\nGame over! You've run out of tries.")
            if self.player_hits > self.cpu_hits:
                print(f"\nCongratulations! You win! Player Hits: {self.player_hits}, CPU Hits: {self.cpu_hits}")
                self.outcome = "Win"
            elif self.player_hits < self.cpu_hits:
                print(f"\nYou lost! Player Hits: {self.player_hits}, CPU Hits: {self.cpu_hits}")
                self.outcome = "Loss"
            else:
                print("\nIt's a tie! Player Hits: {self.player_hits}, CPU Hits: {self.cpu_hits}")
                self.outcome = "Tie"

        # Save game results to Google Sheets
        self.save_results()

        # Display a message to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.reset_game()
            self.play()
        else:
            print("Thank you for playing Simple Battleships!")
        

if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
