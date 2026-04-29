import java.util.*;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> results = new ArrayList<>();
        char[][] board = new char[n][n];
        
        // Initialize the board with empty spaces
        for (int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }
        
        // Use sets to track occupied paths
        Set<Integer> cols = new HashSet<>();
        Set<Integer> posDiag = new HashSet<>(); // row + col
        Set<Integer> negDiag = new HashSet<>(); // row - col
        
        backtrack(0, n, board, results, cols, posDiag, negDiag);
        return results;
    }

    private void backtrack(int row, int n, char[][] board, List<List<String>> results,
                           Set<Integer> cols, Set<Integer> posDiag, Set<Integer> negDiag) {
        // Base case: If we've placed queens in all rows, we found a solution
        if (row == n) {
            results.add(construct(board));
            return;
        }

        for (int col = 0; col < n; col++) {
            if (cols.contains(col) || posDiag.contains(row + col) || negDiag.contains(row - col)) {
                continue; // Queen is under attack, skip this column
            }

            // Place the queen
            board[row][col] = 'Q';
            cols.add(col);
            posDiag.add(row + col);
            negDiag.add(row - col);

            // Move to the next row
            backtrack(row + 1, n, board, results, cols, posDiag, negDiag);

            // Backtrack: Remove the queen and clear the paths
            board[row][col] = '.';
            cols.remove(col);
            posDiag.remove(row + col);
            negDiag.remove(row - col);
        }
    }

    private List<String> construct(char[][] board) {
        List<String> path = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            path.add(new String(board[i]));
        }
        return path;
    }
}