use std::io::{self, BufRead, Write};

fn parse_board(input: &str) -> [char; 9] {
    let mut board = [' '; 9];
    for (i, c) in input.chars().enumerate().take(9) {
        board[i] = c;
    }
    board
}

fn main() {
    let stdin = io::stdin();
    let mut stdout = io::stdout();
    let input_handle = stdin.lock();
    let mut lines = input_handle.lines();

    while let Some(Ok(input)) = lines.next() {
        // Parse input into board
        let board = parse_board(&input);

        // Implement AI logic here.
        // Example: choose the first empty space (marked by ' ')
        let mut move_index = 0;
        for (i, &cell) in board.iter().enumerate() {
            if cell == ' ' {
                move_index = i;
                break;
            }
        }

        // Output move
        writeln!(stdout, "{}", move_index).expect("Failed to write");
        stdout.flush().expect("Failed to flush stdout");
    }
}