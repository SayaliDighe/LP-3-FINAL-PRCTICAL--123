#include <iostream>
using namespace std;

const int N = 8;
int board[N][N] = {0};

// Function to check if it's safe to place a queen at (row, col)
bool isSafe(int row, int col) {
    // Check this column for any other queen
    for (int i = 0; i < row; i++)
        if (board[i][col] == 1)
            return false;

    // Check upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1)
            return false;

    // Check upper right diagonal
    for (int i = row, j = col; i >= 0 && j < N; i--, j++)
        if (board[i][j] == 1)
            return false;

    return true;
}

// Function to solve the 8-Queens problem
bool solve(int row) {
    if (row == N) // All queens are placed
        return true;

    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1; // Place queen

            if (solve(row + 1)) // Recur to place rest of the queens
                return true;

            board[row][col] = 0; // Backtrack
        }
    }
    return false;
}

int main() {
    board[0][0] = 1; // Place the first queen at (0, 0)

    if (solve(1)) { // Start solving from the second row
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << (board[i][j] ? "Q " : ". ");
            }
            cout << endl;
        }
    } else {
        cout << "No solution exists" << endl;
    }

    return 0;
}