#include <iostream>
#include <string>

void parse_board(const std::string &input, char board[9]) {
    for (int i = 0; i < 9; i++) {
        board[i] = input[i];
    }
}

int main() {
    std::string input;
    char board[9];

    while (std::getline(std::cin, input)) {
        parse_board(input, board);

        // Implement AI logic here.
        // Choose an index (0-8) to replace.
        int move = 0; // Replace with AI's move.

        std::cout << move << std::endl;
    }

    return 0;
}