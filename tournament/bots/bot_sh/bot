#!/bin/bash

parse_board() {
    local input=$1
    board=($(echo "$input" | fold -w1))
}

while read -r input; do
    parse_board "$input"

    # Implement AI logic here.
    # Choose an index (0-8) to replace.
    move=0  # Replace with AI's move.

    echo "$move"
done