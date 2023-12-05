class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.row_num = len(grid)
        self.col_num = len(grid[0])

    def is_valid(self, row, col, num):
        # Check if number already exists in the row
        for x in range(self.col_num):
            if self.grid[row][x] == num:
                return False

        # Check if number already exists in the column
        for x in range(self.row_num):
            if self.grid[x][col] == num:
                return False

        # Check if number already exists in the box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve_sudoku(self):
        for i in range(self.row_num):
            for j in range(self.col_num):
                if self.grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self.grid[i][j] = num

                            if self.solve_sudoku():
                                return True

                            self.grid[i][j] = 0

                    return False

        return True

# Define a sudoku puzzle
grid = [
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

solver = SudokuSolver(grid)
solver.solve_sudoku()

# Print the solved puzzle
for row in solver.grid:
    print(row)








































# A Constraint Satisfaction Problem (CSP) is a formalism used to model a problem as a set of objects whose states must satisfy several constraints. These problems are often solved through search algorithms and are widely used in artificial intelligence and operations research. Here's a breakdown of key concepts related to CSP:

# Variables: Variables represent the objects or entities in the problem that need to be assigned values. In the context of the Sudoku solver, each cell in the Sudoku grid is a variable, and the goal is to assign a number to each variable.

# Domains: The domain of a variable is the set of possible values it can take. In Sudoku, the domain of each cell is the set of numbers from 1 to 9.

# Constraints: Constraints define the relationships between variables and restrict the possible combinations of values that variables can take. In Sudoku, the constraints are the rules of the game, which state that no two cells in the same row, column, or 3x3 subgrid can contain the same number.

# Solution: A solution to a CSP is an assignment of values to variables that satisfies all the constraints. In the context of the Sudoku solver, a solution is a filled-in Sudoku grid where every row, column, and 3x3 subgrid contains the numbers 1 to 9 with no repetitions.

# Search and Backtracking: CSPs are often solved using search algorithms. Backtracking is a common approach where the algorithm systematically explores potential solutions and backtracks when it encounters an inconsistency (a violation of constraints). The Sudoku solver code you provided is an example of a backtracking algorithm applied to a CSP.

# Optimization: CSPs can be extended to include optimization criteria, where the goal is not just to find any solution but to find the best solution according to some objective function. This involves exploring the search space to optimize a specific criterion.




#1) def __init__(self, grid):

# This line defines the initialization method for the class. It takes two parameters: self (the instance of the class) and grid, which represents the Sudoku puzzle grid.
# self.grid = grid

# This line assigns the grid parameter to the self.grid attribute of the class. The grid attribute is used to store the Sudoku puzzle grid, allowing other methods in the class to access and manipulate it.
# self.row_num = len(grid)

# This line calculates and assigns the number of rows in the Sudoku grid to the self.row_num attribute. It uses the len() function to determine the length of the outer list of the grid, representing the number of rows.
# self.col_num = len(grid[0])

# Similarly, this line calculates and assigns the number of columns in the Sudoku grid to the self.col_num attribute. It uses the len() function on the first row of the grid (grid[0]) to determine the number of columns.




#2)

# First Block in def is_valid(self, row, col, num):

# Certainly! The is_valid method checks whether placing a given number (num) at a specified position (row, col) in the Sudoku grid violates the rules of Sudoku. Here's a detailed explanation of each block in the code:

# This block iterates through each column in the specified row (row) and checks if the number (num) already exists in that row. If it finds a match, indicating that the number is already present in the row, the method returns False, indicating that placing the number at the given position is invalid.

# Second Block in def is_valid(self, row, col, num):

# Similarly, this block iterates through each row in the specified column (col) and checks if the number (num) already exists in that column. If it finds a match, the method returns False, indicating that placing the number at the given position is invalid.

# Third Block in def is_valid(self, row, col, num):

# This block checks if the number (num) already exists in the 3x3 box (subgrid) that contains the specified position (row, col). It calculates the starting position (start_row, start_col) of the box and iterates through the elements within that box. If it finds a match, the method returns False.



# 3)def solve_sudoku(self):


# for i in range(self.row_num):
#     for j in range(self.col_num):
# These nested loops iterate over each cell in the Sudoku grid, considering each row (i) and column (j) one by one.

# if self.grid[i][j] == 0:
# It checks if the current cell is empty (contains 0). If the cell is not empty, it means the number is already given in the puzzle, and the algorithm proceeds to the next cell.

# for num in range(1, 10):
# This loop iterates over numbers from 1 to 9, attempting to place each number in the empty cell.

# if self.is_valid(i, j, num):
# It checks if placing the current number (num) in the current cell (i, j) is valid using the is_valid method. If it's valid, the number is temporarily placed in the cell.

# if self.solve_sudoku():
#     return True
# The method calls itself recursively, attempting to solve the Sudoku puzzle with the current number placed in the cell. If the recursive call returns True, it means the puzzle is solved, and the method returns True to the previous level of recursion.


# self.grid[i][j] = 0
# If the recursive call does not succeed, indicating that the current placement didn't lead to a solution, the algorithm backtracks by resetting the current cell to 0 (empty).

# return False
# If all numbers have been tried and none led to a solution, the method returns False, indicating that the puzzle cannot be solved with the current configuration.

# return True
# If the outer loops have iterated over all cells and the puzzle is solved, the method returns True.



# 4)

# This block defines a 9x9 Sudoku puzzle grid. Zeros represent empty cells that need to be filled during the solving process.

# solver = SudokuSolver(grid)
# An instance of the SudokuSolver class is created with the provided Sudoku puzzle grid.

# solver.solve_sudoku()
# The solve_sudoku method is called on the solver instance, attempting to solve the Sudoku puzzle.

# for row in solver.grid:
#     print(row)
# After the puzzle is solved, this block iterates through each row of the solved puzzle and prints it.