#include <stdio.h>
#include <stdlib.h>

void parse_board(char *input, char board[9]) {
    for (int i = 0; i < 9; i++) {
        board[i] = input[i];
    }
}

int main() {
    char input[10];  // 9 characters for the board + 1 for null terminator
    char board[9];

    while (fgets(input, sizeof(input), stdin) != NULL) {
        parse_board(input, board);

        // Implement AI logic here.
        // Choose an index (0-8) to replace.
        int move = 0; // Replace with AI's move.

        printf("%d\n", move);  // Output the move.
        fflush(stdout);
    }

    return 0;
}