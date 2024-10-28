from .utils import Tokens
from .sentry import Sentry

class Board:
    def __init__(self):
        """ Initialize the tic-tac-toe board. """
        self.board = [Tokens.EMPTY for _ in range(9)]  # Empty board with 9 cells

    def display(self):
        """ Display the current board state. """
        print(f"{self.board[0].value} | {self.board[1].value} | {self.board[2].value}")
        print("-" * 9)
        print(f"{self.board[3].value} | {self.board[4].value} | {self.board[5].value}")
        print("-" * 9)
        print(f"{self.board[6].value} | {self.board[7].value} | {self.board[8].value}")

    def is_valid_move(self, move: str) -> bool:
        """ Check if the move is valid (within bounds and on an empty space). """
        print(len(move) == 9) # FIXME
        return len(move) == 9

    def update(self, move: str):
        """ Place the player's move on the board. """
        if self.is_valid_move(move):
            move = list(move)
            for i in range(len(move)):
                match move[i]:
                    case Tokens.X.value:
                        move[i] = Tokens.X
                    case Tokens.O.value:
                        move[i] = Tokens.O
                    case _:
                        move[i] = Tokens.EMPTY
            self.board = move
        else:
            raise ValueError("Invalid move!")

    def is_winner(self, bot) -> bool:
        """ Check if the given symbol has won. """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(self.board[i] == bot.symbol for i in combo) for combo in winning_combinations)

    @property
    def is_full(self) -> bool:
        """ Check if the board is full (draw condition). """
        return all(space != Tokens.EMPTY for space in self.board)

    @property
    def board_state(self):
        """ Return the board state as a string for the bot to read. """
        return ''.join([i.value for i in self.board])

