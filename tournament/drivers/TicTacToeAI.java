import java.util.Scanner;

public class TicTacToeAI {
    public static char[] parseBoard(String input) {
        return input.trim().toCharArray();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            String input = scanner.nextLine();
            char[] board = parseBoard(input);

            // Implement AI logic here.
            // Choose an index (0-8) to replace.
            int move = 0;  // Replace with AI's move.

            System.out.println(move);
        }
        scanner.close();
    }
}