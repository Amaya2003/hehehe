class Board():
    def __init__(self, n):
        self.n = n
        self.spaces = n * n
        self.constraints = [0 for i in range(self.spaces)]
        self.queenSpaces = []

    def getPossibleMoves(self):
        possibleMoves = []
        for move, numConstraints in enumerate(self.constraints):
            if numConstraints == 0:
                possibleMoves.append(move)
        return possibleMoves

    def makeMove(self, space):
        self.queenSpaces.append(space)
        self.addOrRemoveConstraints(space)

    def removeMove(self, space):
        self.queenSpaces.remove(space)
        self.addOrRemoveConstraints(space, add=False)

    def addOrRemoveConstraints(self, move, add=True):
        if add:
            mutationFx = self.addConstraint
        else:
            mutationFx = self.removeConstraint
        row = move // self.n
        col = move % self.n
        rdStartRow = row + col
        ldStartRow = row - col

        for i in range(self.n):
            mutationFx(self.rcToSpace(row, i))
            mutationFx(self.rcToSpace(i, col))
            if rdStartRow > -1:
                mutationFx(self.rcToSpace(rdStartRow, i))
                rdStartRow -= 1
            if ldStartRow < self.n:
                mutationFx(self.rcToSpace(ldStartRow, i))
                ldStartRow += 1

    def addConstraint(self, move):
        if not move == -1:
            self.constraints[move] += 1

    def removeConstraint(self, move):
        if not move == -1:
            self.constraints[move] -= 1

    def rcToSpace(self, row, col):
        space = row * self.n + col
        if space >= self.spaces or space < 0:
            return -1
        else:
            return space

    def solveNQueens(self):
        if len(self.queenSpaces) == self.n:
            return True  # All queens are placed successfully

        possibleMoves = self.getPossibleMoves()

        for move in possibleMoves:
            self.makeMove(move)
            if self.solveNQueens():
                return True  # Found a solution
            self.removeMove(move)

        return False  # No solution found

    def printBoard(self):
        for r in range(self.n):
            row = ""
            for c in range(self.n):
                if self.rcToSpace(r, c) in self.queenSpaces:
                    row += "Q"
                else:
                    row += "-"
                row += "  "
            print(row)


# Example usage:
n = 8  # Change this value for different board sizes
board = Board(n)
if board.solveNQueens():
    print(f"Solution for {n}-Queens Problem:")
    board.printBoard()
else:
    print(f"No solution found for {n}-Queens Problem.")






































# Variables:

# Definition: Variables represent the unknowns or entities in the problem that need to be assigned values.
# Example: In the N-Queens problem, each variable represents the column position of a queen in a particular row.
# Domains:

# Definition: The domain of a variable is the set of possible values it can take.
# Example: In the N-Queens problem, the domain of each variable is the set of all column positions in the corresponding row.
# Constraints:

# Definition: Constraints are conditions or relationships between variables that must be satisfied in the assignment.
# Example: In the N-Queens problem, the constraints ensure that no two queens threaten each other, meaning no two queens can be in the same row, column, or diagonal.
# Objective Function (Optional):

# Definition: An objective function is used to optimize a specific criterion in the problem (e.g., minimize or maximize a value).
# Example: In the N-Queens problem, the primary objective is to find a valid arrangement of queens, so an explicit objective function may not be necessary.
# Solution:

# Definition: A solution to a CSP is an assignment of values to variables that satisfies all constraints.
# Example: In the N-Queens problem, a solution is a placement of queens on the chessboard such that no two queens threaten each other.
# Search and Backtracking:

# Definition: CSPs are often solved using search algorithms, and backtracking is a common approach where the algorithm systematically explores potential solutions and backtracks when it encounters inconsistencies.
# Example: In the N-Queens solver, backtracking is used to explore different configurations of queens and find a valid placement.
# Constraint Propagation:

# Definition: Constraint propagation is the process of using existing constraints to narrow down the domain of variables.
# Example: In the N-Queens code, constraint propagation is implicit in the addOrRemoveConstraints method, which updates the constraints based on the current move.

















# Initialization:

# The Board class is created with an __init__ method that sets up the chessboard with a given size (n).
# The chessboard is represented as a list of squares (spaces), and each square has an associated list of constraints initialized to zero.
# Possible Moves:

# The getPossibleMoves method identifies squares where a queen can potentially be placed, i.e., squares with zero constraints.
# Making a Move:

# The makeMove method places a queen on a specified square, updates the list of queens (queenSpaces), and adjusts the constraints accordingly.
# Removing a Move:

# The removeMove method removes a queen from a square, updates the list of queens, and adjusts the constraints accordingly.
# Constraint Adjustment:

# The addOrRemoveConstraints method updates constraints based on the placement or removal of a queen. It considers rows, columns, and diagonals.
# Solving the N-Queens Problem:

# The solveNQueens method uses backtracking to find a solution to the N-Queens problem.
# It checks if all queens are placed successfully. If yes, it returns True.
# If not, it gets possible moves, makes a move, and recursively calls itself. If a solution is found, it returns True. If not, it backtracks by removing the move.
# If no solution is found for a particular configuration, it returns False.
# Printing the Board:

# The printBoard method displays the chessboard, marking squares with queens as 'Q' and empty squares as '-'.
# Example Usage:

# An instance of the Board class is created with a given size (n).
# The solveNQueens method is called to find a solution.
# If a solution is found, the chessboard is printed; otherwise, a message is displayed.
# In simple terms, the code uses a Constraint Satisfaction Problem (CSP) approach to solve the N-Queens problem. It iteratively explores possible queen placements, adjusts constraints based on these placements, and backtracks if inconsistencies are encountered. The goal is to find a configuration where no two queens threaten each other, and the solution is displayed on the chessboard.





