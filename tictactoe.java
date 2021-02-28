package tictactoe;

import java.util.*;

public class Main {
    public static String winner = "";
    public static boolean flag = true;

    public static void main(String[] args) {
        // write your code here
        Scanner scanner = new Scanner(System.in);
        String[][] table = new String[3][3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                table[i][j] = " ";
            }
        }
        DisplayGrid(table);

        while (true) {
            try {
                System.out.print("Enter the coordinates: ");
                int first = Integer.parseInt(scanner.next()) - 1;
                int second = Integer.parseInt(scanner.next()) - 1;

                if (first >= 0 && first < 3 && second >= 0 && second < 3) {
                    if (!"X".equals(table[first][second]) && !"O".equals(table[first][second])) {
                        if (flag) {
                            table[first][second] = "X";
                            flag = false;
                        } else {
                            table[first][second] = "O";
                            flag = true;
                        }
                        DisplayGrid(table);

                        if (CheckWinner(table)) {
                            if ("draw".equals(winner)) {
                                System.out.println("Draw");
                            } else if (!flag) {
                                System.out.println("X wins");
                            } else {
                                System.out.println("O wins");
                            }
                            break;
                        }
                    } else {
                        System.out.println("This cell is occupied! Choose another one!");
                    }
                } else {
                    System.out.println("Coordinates should be from 1 to 3!");
                }
            } catch (NumberFormatException numberFormatException) {
                System.out.println("You should enter numbers!");
            }
        }
    }

    public static void DisplayGrid(String[][] grid) {
        System.out.println("---------");
        System.out.printf("| %s %s %s |\n", grid[0][0], grid[0][1], grid[0][2]);
        System.out.printf("| %s %s %s |\n", grid[1][0], grid[1][1], grid[1][2]);
        System.out.printf("| %s %s %s |\n", grid[2][0], grid[2][1], grid[2][2]);
        System.out.println("---------");
    }

    public static boolean CheckWinner(String[][] grid) {
        List<String> list = new ArrayList<>();

        for (String[] strings : grid) {
            list.addAll(Arrays.asList(strings));
        }

        if (!list.contains(" ")) {
            winner = "draw";
            return true;
        } else {
            return (grid[0][0].equals(grid[0][1]) && grid[0][0].equals(grid[0][2]) && !" ".equals(grid[0][0])) ||
                    (grid[1][0].equals(grid[1][1]) && grid[1][0].equals(grid[1][2]) && !" ".equals(grid[1][0])) ||
                    (grid[2][0].equals(grid[2][1]) && grid[2][0].equals(grid[2][2]) && !" ".equals(grid[2][0])) ||
                    (grid[0][0].equals(grid[1][0]) && grid[0][0].equals(grid[2][0]) && !" ".equals(grid[0][0])) ||
                    (grid[0][1].equals(grid[1][1]) && grid[0][1].equals(grid[2][1]) && !" ".equals(grid[0][1])) ||
                    (grid[0][2].equals(grid[1][2]) && grid[0][2].equals(grid[2][2]) && !" ".equals(grid[0][2])) ||
                    (grid[0][0].equals(grid[1][1]) && grid[0][0].equals(grid[2][2]) && !" ".equals(grid[0][0])) ||
                    (grid[0][2].equals(grid[1][1]) && grid[0][2].equals(grid[2][0]) && !" ".equals(grid[0][2]));
        }
    }
}
