# Advent of Code 2020
# ADD
# Day 01 Part 2

# Get puzzle input as a list 
f = open('puzzle_input_p2.txt', 'r')
puzzle_input = f.read()
puzzle_input = puzzle_input.split()

# Find solution 
def get_values(input):
    try:
        for value1 in input:
            for value2 in input:
                for value3 in input:
                    if (int(value1) + int(value2) + int(value3)) == 2020:
                        return [int(value1), int(value2), int(value3)]
                    else:
                        pass
        print("ERROR: Solution not found")
    except:
        print("ERROR: Input is not valid")


# Show solution                 
values = get_values(puzzle_input)
solution = values[0] * values[1] * values[2]
print("Solution is {} * {} * {} = {}".format(values[0], values[1], values[2], solution))