tab = []
result = []
goalList = ["a", "b", "c", "d", "e"]

def parSolution(N):
    for i in range(N):
        if goalList[i] != result[i]:
            return False
    return True

def Onblock(index, count):
    # break point of recursive call
    if count == len(goalList)+1:
        return True
    # copy tab of index value to result
    block = tab[index]
    # stack block
    result.append(block)
    print(result)
    if parSolution(count):
        print("Pushed a result solution ")
        # remove block from tab
        tab.remove(block)
        Onblock(0, count + 1)
    else:
        print("result solution not possible, back to the tab")
        # pop out if no partial solution
        result.pop()
        Onblock(index+1, count)

def Ontab(problem):
    # check if everything in stack is on the tab
    if len(problem) != 0:
        tab.append(problem.pop())
        Ontab(problem)
    # if everything is on the tab the we return true
    else:
        return True

def goal_stack_planing(problem):
    # pop problem and put in tab
    Ontab(problem)
    # print index and number of blocks on result stack
    if Onblock(0, 1):
        print(result)

if __name__ == "__main__":
    problem = ["c", "a", "e", "d", "b"]
    print("Goal Problem")
    for k, j in zip(goalList, problem):
        print(k+"    "+j)
    goal_stack_planing(problem)
    print("result Solution")
    print(result)





# Goal stack planning is a problem-solving method used in artificial intelligence. It's like solving a puzzle by breaking it into smaller pieces. Imagine you have a goal you want to achieve, but it's complex. To solve it, you break it down into smaller, manageable sub-goals, sort of like making a to-do list for the main goal. Each sub-goal is like a step you take toward reaching the main goal.

# In goal stack planning, you start with the main goal and break it down into smaller tasks or sub-goals. These sub-goals are organized in a stack-like structure. You work on achieving each sub-goal, which helps you eventually reach the main goal.



# Process:

# Move blocks from the initial disordered state (problem) to the tab (tab list).
# Initiate the goal stack planning by attempting to place blocks onto the result stack.
# During block placement, it checks if the current arrangement matches the desired goal state.
# If the current arrangement matches the goal, it proceeds to the next block or sub-goal.
# If the arrangement doesn’t match, it backtracks, adjusting the placements to try different configurations.
# Continues this recursive process until either achieving the goal state or exhausting all possible arrangements.


# tab: An empty list meant to store blocks.
# result: An empty list intended to keep track of the sequence of blocks arranged toward the goal state.
# goalList: A list containing a predefined desired arrangement of blocks, representing the goal state that the algorithm aims to achieve.
# Here's a breakdown of each list:


# tab: Initially empty, this list is used to simulate a storage area or table where blocks can be placed and manipulated.
# result: Also empty at the start, this list will store the sequence of blocks as they are arranged to reach the desired goal state.
# goalList: Contains a specific arrangement of blocks ("a", "b", "c", "d", "e"), representing the desired end state that the algorithm will try to achieve.


# Function Name: parSolution
# Arguments: It takes a single argument N, which represents the number of elements to compare in the goalList and result.
# Functionality:
# It iterates through the first N elements of both goalList and result lists using the for loop.
# Inside the loop, it checks if the element at index i in the goalList does not match the corresponding element in the result list.
# If there is a mismatch at any point, indicating that the current arrangement doesn't match the goal, the function returns False.
# If all elements up to N match between goalList and result, it returns True, indicating that the current arrangement is identical to the desired goal state up to that point.
# Essentially, this function serves to compare the first N elements of result and goalList lists. If they are identical up to index N, it confirms that the current arrangement of blocks in result matches the desired arrangement specified in goalList. If there's any deviation, it returns False.


# Function Name: Onblock
# Arguments:
# index: Represents the index of the block in the tab list that is being considered for placement onto the result.
# count: Keeps track of the number of blocks placed onto the result stack.
# Functionality:
# Termination Condition: If the count of blocks placed on the result stack equals len(goalList) + 1, indicating that all blocks have been placed successfully, it returns True.
# Block Placement:
# It retrieves the block from the tab list at the given index and appends it to the result list.
# The function then prints the current state of the result list (for demonstration purposes).
# Validation:
# It checks if the current arrangement of blocks in result matches any partial solution using the parSolution function.
# If a partial solution is found (parSolution returns True), it indicates success, removes the block from tab, and recursively calls Onblock with an incremented count to continue placing more blocks.
# If no partial solution is found, it backtracks by removing the last block from result and tries the next block in the tab list for placement by recursively calling Onblock with an incremented index.
# This function recursively attempts different block placements onto the result stack while considering the goal state. If it finds a partial solution, it continues placing blocks to achieve the overall goal configuration. If a partial solution is not possible, it backtracks and explores alternative block placements.


# Function Name: Ontab

# Argument:

# problem: Represents the list of blocks yet to be placed on the tab.
# Functionality:

# Recursion:
# If the length of the problem list is not zero, indicating there are still blocks to be moved, the function executes the following:
# It takes a block from the end of the problem list using problem.pop() and appends this block to the tab list.
# It then recursively calls itself (Ontab(problem)) with the modified problem list, moving the next block from problem to tab.
# This recursive process continues until all blocks from the problem list are transferred to the tab.
# Termination Condition:
# Once all blocks are moved to the tab, the length of problem becomes zero.
# At this point, the function returns True to indicate that all blocks have been successfully transferred to the tab.

# Function Name: goal_stack_planing

# Argument:

# problem: Represents the initial configuration of blocks that need to be arranged.
# Functionality:

# Initialization:
# It starts by moving blocks from the problem list to the tab list using the Ontab(problem) function.
# Block Placement:
# It then attempts to place blocks onto the result stack to achieve the goal configuration using the Onblock(0, 1) function.
# If the Onblock function returns True, indicating a successful arrangement, it prints the final configuration stored in the result list.
# If the arrangement fails to meet the goal, it doesn't explicitly handle the failure case here, relying on the Onblock function's internal operations and recursive calls to adjust the block placements.



# if __name__ == "__main__":: This condition checks if the script is being run directly as the main program.
# problem = ["c", "a", "e", "d", "b"]: It initializes the problem variable with a list representing the initial configuration of blocks.
# print("Goal Problem"): Prints a label indicating the start of the problem.
# for k, j in zip(goalList, problem):: This loop iterates over the goalList and problem lists simultaneously using zip.
# print(k+" "+j): Within the loop, it prints pairs of elements from goalList and problem side by side, indicating the correspondence between the goal configuration and the initial configuration.
# goal_stack_planing(problem): Calls the goal_stack_planing function with the problem list as an argument, initiating the goal stack planning process based on the provided initial configuration.
# print("result Solution"): Prints a label indicating the display of the result.
# print(result): Prints the result list, which should contain the final arrangement of blocks after attempting to achieve the goal state through the goal stack planning process.