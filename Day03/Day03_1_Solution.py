
# Advent of Code 2020
# ADD
# Day 03 Part 1

# Get puzzle input as a list 
f = open('Day03/Day03_PuzzleInput.txt', 'r')
puzzle_input = f.read()
puzzle_input_list = puzzle_input.split('\n')

# Coordinates for grid map are 'x' positive to the right and 'y' positive to the bottom
x = 0
y = 0

# Pattern is repeated to the right 
pattern_len = len(puzzle_input_list[0])

# Check every input line
tree_counter = 0
for y in range(len(puzzle_input_list)):
    if puzzle_input_list[y][x] == '#':
        tree_counter += 1
    x = (x + 3) % pattern_len

# Solution
print(tree_counter)


