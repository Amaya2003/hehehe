import networkx as nx
import time
import heapq

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'C'},
    'E': {'B', 'F'},
    'F': {'C', 'E'},
}

G = nx.Graph(graph)

# Define start and goal nodes
start_node = 'A'
goal_node = 'F'

# Depth-First Search (DFS)
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for next_node in graph[node] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))
    return None

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in graph[node] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None

# A* Algorithm
def heuristic(node, goal):
    # Define a simple heuristic function for A*
    return len(set(goal) - set(node))

def astar(graph, start, goal):
    open_list = [(heuristic(start, goal), start, [start])]
    while open_list:
        open_list.sort()  # Sort by heuristic cost
        _, node, path = open_list.pop(0)
        for next_node in graph[node] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                new_path = path + [next_node]
                cost = len(new_path) + heuristic(next_node, goal)
                open_list.append((cost, next_node, new_path))
    return None

# Measure execution time of each algorithm
start_time = time.time()
dfs_path = dfs(graph, start_node, goal_node)
dfs_time = time.time() - start_time

start_time = time.time()
bfs_path = bfs(graph, start_node, goal_node)
bfs_time = time.time() - start_time

start_time = time.time()
astar_path = astar(graph, start_node, goal_node)
astar_time = time.time() - start_time

# Print the paths and execution times
print("DFS Path:", dfs_path)
print("DFS Time:", dfs_time)

print("BFS Path:", bfs_path)
print("BFS Time:", bfs_time)

print("A* Path:", astar_path)
print("A* Time:", astar_time)

# Plot the execution times
algorithms = ['DFS', 'BFS', 'A*']
times = [dfs_time, bfs_time, astar_time]















































# 1. Depth-First Search (DFS):
# Idea: Explore as far as possible along each branch before backtracking.
# Implementation:
# Utilizes a stack to manage the exploration.
# Starts at the initial node and explores as deeply as possible before backtracking.
# Path Finding:
# Returns a path from the start node to the goal node.
# 2. Breadth-First Search (BFS):
# Idea: Explore all the neighbors at the present depth prior to moving on to nodes at the next depth.
# Implementation:
# Utilizes a queue to manage the exploration.
# Explores all neighbors at the current level before moving to the next level.
# Path Finding:
# Returns a path from the start node to the goal node.
# 3. A* Algorithm:
# Idea: A combination of uniform cost search and greedy best-first search.
# Implementation:
# Utilizes a priority queue based on the cost function (path length + heuristic).
# Incorporates a heuristic function to guide the search.
# Heuristic Function:
# A simple heuristic is defined that counts the nodes not yet in the path.
# Path Finding:
# Returns a path from the start node to the goal node.
# Heuristic Function:
# A heuristic is a function that estimates the cost of reaching the goal from a given node.
# In A*, the heuristic guides the search by providing an estimate of the remaining cost.
# The provided heuristic is a basic one that counts the number of nodes not yet in the path.
# Execution Time Measurement:
# The time module is used to measure the execution time of each algorithm.
# Execution time is crucial for assessing the efficiency of an algorithm.
# Output:
# Paths and execution times for DFS, BFS, and A* are printed.
# The results can be analyzed to compare the efficiency and paths found by each algorithm.









# Graph Representation:
# The graph is like a map with locations (nodes) connected by paths (edges).
# It's represented as a dictionary, where each location (node) has a set of neighboring locations.
# Search Algorithms:
# 1. Depth-First Search (DFS):
# Idea: Imagine exploring a maze by going as far as you can down one path before turning back.
# Code:
# It starts at the beginning and explores as deep as possible along one path.
# Uses a stack (like a pile of books) to remember where it's been.
# Path Finding:
# Finds a path from the starting point to the destination.
# 2. Breadth-First Search (BFS):
# Idea: Picture exploring a maze level by level, checking all nearby paths before moving on.
# Code:
# It starts at the beginning and explores all nearby locations before going deeper.
# Uses a queue (like people waiting in line) to remember where to explore next.
# Path Finding:
# Finds a path from the starting point to the destination.
# 3. A* Algorithm:
# Idea: Imagine exploring a city, considering both the distance traveled and a good estimate of the remaining distance.
# Code:
# It combines the benefits of looking at nearby locations (like BFS) and considering the total distance (like DFS).
# Uses a priority queue (like a to-do list sorted by priority) to decide where to go next.
# Heuristic Function:
# Has a smart way to guess how far away the destination is, helping it make good decisions.
# Path Finding:
# Finds a path from the starting point to the destination.
# Heuristic Function:
# Idea: It's a clever guess about the remaining distance to the destination.
# Code:
# The heuristic used here is a simple one, counting how many locations are left to visit.
# Purpose:
# Helps guide A* to explore paths that seem promising based on the clever guess.
# Execution Time Measurement:
# Idea: Imagine timing how long it takes to solve a puzzle.
# Code:
# It uses the time module to measure how long each algorithm takes to find a solution.
# Purpose:
# Helps compare how fast each algorithm is.
# Output:
# Idea: After exploring the maze, it's like writing down the best path and how long it took to find it.
# Code:
# Prints out the paths found by DFS, BFS, and A*.
# Also prints how much time each algorithm took.
# Purpose:
# Helps see which algorithm found the best path and how quickly.
# Plotting Execution Times (Incomplete):
# Idea: Picture making a chart to compare how fast each algorithm is.
# Code:
# There's an incomplete part for plotting this information.
# Normally, you'd use a library like matplotlib to create a visual chart.
# Purpose:
# Makes it easy to see which algorithm is faster.
# In summary, the code is like exploring a maze with different strategies (DFS, BFS, A*). Each strategy has its way of finding the best path, and the code helps compare them by looking at the paths found and how quickly they find them. The heuristics are like smart guesses, and the execution time measurements help figure out which strategy works best for a given situation.