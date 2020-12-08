
# Advent of Code 2020
# ADD
# Day 03 Part 2

# Get puzzle input as a list 
f = open('Day03/Day03_PuzzleInput.txt', 'r')
puzzle_input = f.read()
puzzle_input_list = puzzle_input.split('\n')

# Pattern is repeated to the right 
pattern_len = len(puzzle_input_list[0])

# Route slope input
slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

def check_trees(n_right, n_down):
    """
    Receive n_right and n_down as the pattern to follow
    Return how many tress '#' are in the route to the bottom 
    """
    x = 0
    y = 0
    tree_counter = 0
    # Check every input line
    for y in range(0, len(puzzle_input_list), n_down):
        if puzzle_input_list[y][x] == '#':
            tree_counter += 1
        x = (x + n_right) % pattern_len
    return tree_counter

# Solution
product = 1
for s in slope:
    solution = check_trees(s[0], s[1])
    print("Right {}, down {} --> {} trees".format(s[0], s[1], solution))
    product *= solution

print("Product of trees is --> ", product)


