import sys


def parse_board(input):
    return list(input.strip())


while True:
    input_line = sys.stdin.readline().strip()
    if not input_line:
        break

    board = parse_board(input_line)

    # Implement AI logic here.
    # Choose an index (0-8) to replace.
    move = 0  # Replace with AI's move.

    print(move)