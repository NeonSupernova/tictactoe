import sys

def find_winning_move(board: str, player: str) -> int:
    """Check for a winning move for the player and return the position if found."""
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == player and board[pos[2]] == 'E':
            return pos[2]
        if board[pos[1]] == board[pos[2]] == player and board[pos[0]] == 'E':
            return pos[0]
        if board[pos[0]] == board[pos[2]] == player and board[pos[1]] == 'E':
            return pos[1]
    return -1


class TicTacToeBot:
    def __init__(self, player: str):
        self.player = player
        self.opponent = 'O' if player == 'X' else 'X'

    def make_move(self, board: str) -> str:
        """Determine the best move for the player and return the updated board."""
        # Check for a winning move
        winning_move = find_winning_move(board, self.player)
        if winning_move != -1:
            return self.update_board(board, winning_move)

        # Check for a blocking move
        blocking_move = find_winning_move(board, self.opponent)
        if blocking_move != -1:
            return self.update_board(board, blocking_move)

        # Take the center if available
        if board[4] == 'E':
            return self.update_board(board, 4)

        # Take any corner if available
        for corner in [0, 2, 6, 8]:
            if board[corner] == 'E':
                return self.update_board(board, corner)

        # Take any open side if available
        for side in [1, 3, 5, 7]:
            if board[side] == 'E':
                return self.update_board(board, side)

        return board  # Return the board if no moves are possible (shouldn't happen in a normal game)

    def update_board(self, board: str, position: int) -> str:
        """Update the board with the player's move at the specified position."""
        return board[:position] + self.player + board[position + 1:]


# Read from stdin and write to stdout
if __name__ == "__main__":
    for line in sys.stdin:
        ip = line.strip().upper()
        if len(ip) < 10:
            continue  # Skip invalid input lines

        player = ip[0]
        board = ip[1:]

        bot = TicTacToeBot(player)
        updated_board = bot.make_move(board)

        # Print to stdout
        print(updated_board)