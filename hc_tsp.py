import random
import numpy as np

def generate_matrix(coordinate):
    return np.linalg.norm(coordinate[:, None] - coordinate, axis=2)

def solution(matrix):
    return list(np.random.permutation(len(matrix)))

def path_length(matrix, solution):
    return sum(matrix[solution[i]][solution[i - 1]] for i in range(len(solution)))

def neighbors(matrix, solution):
    best_path, best_neighbor = float('inf'), []

    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = solution[j], solution[i]
            current_path = path_length(matrix, neighbor)

            if current_path < best_path:
                best_path = current_path
                best_neighbor = neighbor

    return best_neighbor, best_path

def hill_climbing(coordinate):
    matrix = generate_matrix(coordinate)
    current_solution = solution(matrix)
    current_path = path_length(matrix, current_solution)
    best_neighbor, best_neighbor_path = neighbors(matrix, current_solution)

    while best_neighbor_path < current_path:
        current_solution = best_neighbor
        current_path = best_neighbor_path
        best_neighbor, best_neighbor_path = neighbors(matrix, current_solution)

    return current_path, current_solution

coordinate = np.array([[1,2], [30,21], [56,23], [8,18], [20,50], [3,4], [11,6], [6,7], [15,20], [10,9], [12,12]])
final_solution = hill_climbing(coordinate)
print("The solution is \n", final_solution[1])













































# Hill climbing is a heuristic search algorithm used in optimization problems to find the best possible solution. It's named 'hill climbing' because of its analogy to climbing a hill to reach the peak, where the goal is to ascend to the highest point (the best solution) in the problem space.

# Theory of Hill Climbing:
# Current State:

# In the context of the Travelling Salesman Problem (TSP) or similar optimization problems, hill climbing starts with an initial solution, often chosen randomly.

# Evaluation Function:
# It uses an evaluation function to determine the quality of the current solution. In TSP, it could be the total distance of the tour.

# Generating Neighbors:
# Hill climbing generates neighboring solutions by making small incremental changes to the current solution. For example, in TSP, it might swap two cities in the tour.

# Selection of Next State:
# It selects the neighboring solution that optimizes or improves the evaluation function (i.e., moves towards the 'higher ground' or better solution). If no such better solution is found among the neighbors, it terminates.

# Iterative Improvement:
# The algorithm iteratively explores neighboring solutions until it reaches a peak or the best possible solution in the local area of the search space. It stops when it cannot find a better solution among the immediate neighbors.

# Local Optima:
# One limitation of hill climbing is that it can get stuck at a local optimum if the algorithm cannot find any better solution in the immediate neighborhood, even if a globally better solution exists elsewhere in the search space.

# Variations:
# There are variations of hill climbing like steepest ascent hill climbing (selects the best among all neighboring states) and stochastic hill climbing (picks a random neighbor that improves the evaluation function).


# Imagine you're climbing a hill and can only see the immediate terrain around you.
# You take steps in the direction that leads you to a higher position.
# Once you cannot step higher from your current position (you're at the peak or there's no higher ground in your immediate vicinity), you stop climbing.




# Here's what the code does:

# Initial Setup:

# It creates a map showing the distances between each pair of cities.
# Starts from a random path that visits all cities once and ends where it started.
# Improvement Process:

# It checks neighboring paths by swapping the order of two cities and calculates the distance of each new path.
# If it finds a path shorter than the current one, it swaps to this new path.
# Continues doing this until it can't find a shorter path by swapping cities.
# Result:

# Finally, it returns the shortest path it found that visits all cities once and returns to the starting point.



# Code:-

#1) generate_matrix(coordinate):
# Input:

# coordinate: It represents an array of coordinates (like [x, y] pairs) indicating the positions of various points or cities.
# Purpose:

# This function calculates distances between each pair of coordinates and constructs a matrix where each cell represents the distance between two points.
# Working Explanation:

# np.linalg.norm(coordinate[:, None] - coordinate, axis=2):
# np.linalg.norm: This NumPy function calculates the Euclidean distance between points.
# coordinate[:, None] - coordinate: It computes the difference between each pair of coordinates to get the distances between them.
# axis=2: Specifies the axis along which the norms are computed, resulting in a 2D distance matrix.
# Output:

# The function returns a distance matrix where each element matrix[i][j] represents the distance between the ith and jth coordinates. Essentially, it provides a complete overview of distances between all pairs of points in the given set of coordinates.
# Summary:
# The generate_matrix function efficiently computes the distances between all pairs of coordinates, creating a matrix that serves as a reference for the distances between locations. This matrix is crucial for solving problems like the Travelling Salesman Problem, where finding the shortest path between various points is necessary.


# 2)solution(matrix):
# Input:

# matrix: The distance matrix representing distances between different points or cities.
# Purpose:

# This function creates a random initial solution for the TSP problem.
# It returns a list representing a random permutation of indices from 0 to len(matrix)-1, which corresponds to visiting each city once.
# Working Explanation:

# np.random.permutation(len(matrix)):
# np.random.permutation shuffles the indices from 0 to len(matrix)-1 randomly.
# This creates a random order in which the cities will be visited.
# Output:

# The function returns a list where each element represents the order in which cities will be visited initially, forming a random solution to start the optimization process.
# Summary:
# The solution function serves to create a starting point for the optimization process by generating a random order of visiting cities. This initial solution is essential for optimization algorithms like hill climbing or genetic algorithms to begin the search for an improved solution.


# 3)path_length(matrix, solution):
# Inputs:

# matrix: The distance matrix representing distances between different points or cities.
# solution: A list representing the order of visiting cities, forming a particular path or route.
# Purpose:

# This function computes the total distance traveled following a particular path specified by the solution.
# Working Explanation:

# sum(matrix[solution[i]][solution[i - 1]] for i in range(len(solution))):
# It calculates the sum of distances between consecutive cities in the given solution.
# for i in range(len(solution)): Iterates through each city in the solution list.
# matrix[solution[i]][solution[i - 1]]: Retrieves the distance between the current city (solution[i]) and the previous city (solution[i - 1]) from the distance matrix.
# sum(): Adds up all these distances to compute the total path length.
# Output:

# The function returns the total distance traveled by following the specified path/order of cities in the solution list.


# 4)neighbors(matrix, solution):
# Inputs:

# matrix: The distance matrix representing distances between different points or cities.
# solution: A list representing the order of visiting cities, forming a particular path or route.
# Purpose:

# This function explores neighboring solutions by swapping the order of two cities in the given solution.
# It evaluates these neighboring solutions to find the one with the shortest path length.
# Working Explanation:

# for i in range(len(solution)): & for j in range(i + 1, len(solution))::

# Nested loops iterate over each pair of cities in the given solution to create neighboring solutions by swapping their positions.
# This generates all possible neighboring solutions without changing the original solution.
# neighbor[i], neighbor[j] = solution[j], solution[i]:

# Swaps the positions of two cities in the solution list to create a neighboring solution.
# current_path = path_length(matrix, neighbor):

# Calculates the total path length of the newly generated neighboring solution using the path_length function.
# if current_path < best_path::

# Compares the path length of the current neighboring solution with the best path found so far.
# If the current path is shorter than the best-known path, it updates the best path length (best_path) and the best neighboring solution (best_neighbor).
# Output:

# The function returns the best neighboring solution (best_neighbor) found among all generated neighbors, along with its corresponding shortest path length (best_path).


# 5)hill_climbing(coordinate):
# Input:

# coordinate: An array representing coordinates (like [x, y] pairs) indicating the positions of various points or cities.
# Purpose:

# This function performs the hill climbing algorithm to optimize the path for visiting all cities and returning to the starting point with the shortest possible distance.
# Working Explanation:

# matrix = generate_matrix(coordinate):

# Computes the distance matrix representing distances between different cities based on their coordinates.
# current_solution = solution(matrix):

# Generates an initial random solution for visiting the cities.
# current_path = path_length(matrix, current_solution):

# Calculates the total path length of the current solution.
# best_neighbor, best_neighbor_path = neighbors(matrix, current_solution):

# Finds the best neighboring solution and its corresponding path length.
# Hill Climbing Loop:

# while best_neighbor_path < current_path:
# Enters a loop that continues as long as a better neighboring solution is found.
# Updates the current solution and its path length to the best neighboring solution and its path length.
# Continues until no better solution is found among the neighboring solutions.
# Output:

# Returns the shortest path length (current_path) and the corresponding solution (current_solution) found through hill climbing.


# 6)
# coordinate = np.array([[1,2], [30,21], [56,23], [8,18], [20,50], [3,4], [11,6], [6,7], [15,20], [10,9], [12,12]]):
# Defines a set of coordinates representing different cities or points.
# final_solution = hill_climbing(coordinate):
# Initiates the hill climbing algorithm using the coordinates provided.
# The hill_climbing function optimizes the route to visit all cities once and return to the starting city, aiming to find the shortest possible path.
# print("The solution is \n", final_solution[1]):
# Prints the final solution found by the hill climbing algorithm.
# final_solution[1] retrieves the second element of the tuple returned by hill_climbing, which represents the actual best path or sequence of cities to visit.
# In summary, this code sets up a problem where the goal is to find the best path to travel through different cities represented by coordinates. The hill_climbing function is applied to solve this optimization problem, and the final solution (the sequence of cities to visit) is printed out.


