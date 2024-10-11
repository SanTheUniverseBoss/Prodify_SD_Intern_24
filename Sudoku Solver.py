# Function to check if a number can be placed at the given row, column
def is_valid(board, row, col, num):
    # Check if the number exists in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number exists in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number exists in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    # Find an empty cell (denoted by 0)
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        # If no empty cells are found, the board is solved
        return True

    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recursively attempt to solve the rest of the board
            if solve_sudoku(board):
                return True

            # If placing num doesn't lead to a solution, reset the cell (backtrack)
            board[row][col] = 0

    # If no valid numbers can be placed, return False
    return False

# Function to find an empty cell in the board (denoted by 0)
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Function to print the Sudoku board
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Print horizontal separator
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  # Print vertical separator
            if j == 8:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")

# Example Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve and display the Sudoku puzzle
if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists.")
