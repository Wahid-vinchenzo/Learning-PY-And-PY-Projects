import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

# Player and Move defined as immutable data structures
class Player(NamedTuple):
    label: str     # 'X' or 'O'
    color: str     # Color for each player

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""  # Will be filled when player makes a move

# Game constants
BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

# Game logic class
class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)  # Cycle through players automatically
        self.board_size = board_size
        self.current_player = next(self._players)  # Start with player X
        self.winner_combo = []       # Winning combination positions
        self._current_moves = []     # Stores the board state
        self._has_winner = False     # Flag to check if someone won
        self._winning_combos = []    # Stores all possible win combinations
        self._setup_board()          # Initialize board

    def _setup_board(self):
        # Create a 2D list with empty moves for all cells
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()  # Precalculate win conditions

    def _get_winning_combos(self):
        # List all possible win combinations: rows, columns, diagonals
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def is_valid_move(self, move):
        # Valid if the cell is empty and no one has won yet
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        # Store the move and check if it's a winning move
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        return self._has_winner

    def is_tied(self):
        # All cells filled, and no winner
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def toggle_player(self):
        # Switch turn to next player
        self.current_player = next(self._players)

    def reset_game(self):
        # Clear board for new game
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []
        self.current_player = next(self._players)  # Reset starting player

# GUI Class using tkinter
class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self.configure(bg="black")  # Entire window background color
        self._cells = {}            # Dict to map button -> (row, col)
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_menu(self):
        # Top Menu bar with Play Again and Exit
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_board_display(self):
        # Text label to show messages like turn or win
        display_frame = tk.Frame(master=self, bg="black")
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
            fg="white",
            bg="black"
        )
        self.display.pack()

    def _create_board_grid(self):
        # Main button grid (3x3)
        grid_frame = tk.Frame(master=self, bg="black")
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="white",
                    bg="black",
                    width=3,
                    height=2,
                    highlightbackground="gray",
                    borderwidth=2,
                    relief="raised"
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)  # Bind left click
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        # Main handler when player clicks a cell
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)

        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)

            if self._game.is_tied():
                self._update_display("Tied game!", "yellow")
                self.after(1500, self.reset_board)  # Auto-reset after 1.5 sec

            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
                self.after(1500, self.reset_board)  # Auto-reset after 1.5 sec

            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        # Show X/O on button with color
        clicked_btn.config(
            text=self._game.current_player.label,
            fg=self._game.current_player.color
        )

    def _update_display(self, msg, color="white"):
        # Update top message text and color
        self.display.config(text=msg, fg=color)

    def _highlight_cells(self):
        # Highlight winning cells
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        # Reset game state and clear all buttons
        self._game.reset_game()
        self._update_display("Ready?", "white")
        for button in self._cells.keys():
            button.config(highlightbackground="gray", text="", fg="white")

# Entry point of the game
def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()

# Run the game if file is executed directly
if __name__ == "__main__":
    main()
