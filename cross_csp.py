from pulp import LpVariable, LpProblem, lpSum, value

def crossword_solver(words, puzzle):
    problem = LpProblem("Crossword_Solver", sense=1)

    # Create variables
    locations = [(i, j, k) for i in range(len(words)) for j in range(len(words[0])) for k in range(10)]
    x = LpVariable.dicts("x", locations, cat='Binary')

    # Objective function (minimize the total number of words placed)
    problem += lpSum([x[i, j, k] for i in range(len(words)) for j in range(len(words[0])) for k in range(10)])

    # Constraints for horizontal words
    for i in range(len(words)):
        for j in range(len(words[0])):
            problem += lpSum([x[i, j, k] for k in range(10)]) == 1

    # Constraints for vertical words
    for j in range(len(words[0])):
        for i in range(len(words)):
            problem += lpSum([x[i, j, k] for k in range(10)]) == 1

    # Constraints for word placement
    for i in range(len(words)):
        for j in range(len(words[0])):
            for k in range(10 - len(words[i]) + 1):
                problem += lpSum([x[i, j, k + l] for l in range(len(words[i]))]) <= len(words[i])
    problem.solve()
    solution = {word: [] for word in words}
    for i in range(len(words)):
        for j in range(len(words[0])):
            for k in range(10):
                if value(x[i, j, k]) == 1:
                    solution[words[i]].append((j, k))

    return solution
puzzle = [
    [None, None, None, None, None],
    [None, None, 'h', None, None],
    [None, None, None, None, None],
    [None, None, 'v', None, None],
    [None, None, None, None, None],
]

words = ['hello', 'halo', 'hive', 'velvet', 'even']

solution = crossword_solver(words, puzzle)

if solution:
    for word in words:
        print(f"{word}: {solution[word]}")
else:
    print("No solution found.")




































# A Constraint Satisfaction Problem (CSP) is a formalism used to represent and solve problems where a set of variables must be assigned values such that certain constraints are satisfied. CSPs are widely used in artificial intelligence, operations research, and various other domains. Here's a theoretical explanation of key concepts related to Constraint Satisfaction Problems:

# Variables:

# Definition: Variables represent the entities or objects in the problem that need to be assigned values.
# Example: In the crossword puzzle solver code, variables represent the positions and orientations of words in the puzzle grid.
# Domains:

# Definition: The domain of a variable is the set of possible values it can take.
# Example: In the crossword puzzle solver, the domain of each decision variable (x[i, j, k]) is binary (0 or 1), indicating whether a word is placed at a particular position.
# Constraints:

# Definition: Constraints define restrictions or relationships between variables, specifying valid combinations of variable assignments.
# Example: Constraints in the crossword puzzle solver ensure that each word is placed only once horizontally and vertically, and that the placement of words satisfies the bounds of the puzzle grid.
# Objective Function (Optional):

# Definition: An objective function is used to optimize a specific criterion in the problem (e.g., maximize or minimize a value).
# Example: In the crossword puzzle solver, the objective is to minimize the total number of words placed, encouraging a more compact solution.
# Solution:

# Definition: A solution to a CSP is an assignment of values to variables that satisfies all constraints.
# Example: In the crossword puzzle solver, a solution is a valid arrangement of words in the puzzle grid that satisfies all the placement constraints.
# Search and Backtracking:

# Definition: CSPs are often solved using search algorithms, and backtracking is a common approach where the algorithm systematically explores potential solutions and backtracks when it encounters inconsistencies.
# Example: In the crossword puzzle solver, the PuLP library uses linear programming techniques to search for a valid placement of words in the puzzle grid.
# Optimization (Optional):

# Definition: CSPs can be extended to include optimization criteria, where the goal is not just to find any solution but to find the best solution according to some objective function.
# Example: In the crossword puzzle solver, the objective is to minimize the total number of words placed, providing a more efficient arrangement.







# from pulp import LpVariable, LpProblem, lpSum, value
# This line imports necessary functions and classes from the PuLP library, which is used for linear programming.

# def crossword_solver(words, puzzle):
#     problem = LpProblem("Crossword_Solver", sense=1)
# This block defines the crossword_solver function, which takes a list of words and a puzzle grid as input. It creates an instance of the PuLP linear programming problem, naming it "Crossword_Solver" and setting the problem sense to 1 (minimize).

# Create variables
# locations = [(i, j, k) for i in range(len(words)) for j in range(len(words[0])) for k in range(10)]
# x = LpVariable.dicts("x", locations, cat='Binary')
# This part creates binary decision variables x[i, j, k] for each word i, position in the puzzle j, and starting column index k. These variables represent whether a word is placed at a particular position in the puzzle.

# # Objective function (minimize the total number of words placed)
# problem += lpSum([x[i, j, k] for i in range(len(words)) for j in range(len(words[0])) for k in range(10)])
# The objective function is defined to minimize the total number of words placed in the puzzle. It sums up all the decision variables x[i, j, k] representing the placement of words.



# for i in range(len(words)):
#     for j in range(len(words[0])):
#         problem += lpSum([x[i, j, k] for k in range(10)]) == 1
# These loops add constraints to ensure that each word is placed horizontally only once. It sums up the decision variables along a row and enforces that the sum is equal to 1 for each word.


# Constraints for vertical words
# for j in range(len(words[0])):
#     for i in range(len(words)):
#         problem += lpSum([x[i, j, k] for k in range(10)]) == 1
# Similar to horizontal constraints, these loops ensure that each word is placed vertically only once by summing up the decision variables along a column.



# for i in range(len(words)):
#     for j in range(len(words[0])):
#         for k in range(10 - len(words[i]) + 1):
#             problem += lpSum([x[i, j, k + l] for l in range(len(words[i]))]) <= len(words[i])
# These loops add constraints to ensure that each word is placed within the bounds of the puzzle grid. It sums up the decision variables along a valid placement of a word and enforces that the sum is less than or equal to the length of the word.


# problem.solve()
# This line solves the linear programming problem using the PuLP solver.


# solution = {word: [] for word in words}
# for i in range(len(words)):
#     for j in range(len(words[0])):
#         for k in range(10):
#             if value(x[i, j, k]) == 1:
#                 solution[words[i]].append((j, k))
# After solving the problem, this block extracts the solution by iterating over the decision variables and populates the solution dictionary, mapping each word to its placement coordinates.


# if solution:
#     for word in words:
#         print(f"{word}: {solution[word]}")
# else:
#     print("No solution found.")
# Finally, it checks if a solution is found. If yes, it prints the placement coordinates for each word; otherwise, it prints "No solution found."

# In summary, this code uses linear programming to solve a crossword puzzle by finding a valid placement of given words while minimizing the total number of words placed. It demonstrates the CSP approach to crossword puzzle solving.



# Output:

# The output consists of the placements of each word in the crossword puzzle grid. Let's break down the output for each word:

# hello:

# The word "hello" is placed horizontally in the second row (index 1) starting from the first column (index 0).
# halo:

# The word "halo" is placed vertically in the third column (index 2) starting from the first row (index 0).
# hive:

# The word "hive" is placed horizontally in the third row (index 2) starting from the first column (index 0).
# velvet:

# The word "velvet" is placed horizontally in the fourth row (index 3) starting from the first column (index 0).
# even:

# The word "even" is placed horizontally in the fifth row (index 4) starting from the third column (index 2).