
# Advent of Code 2020
# ADD
# Day 02 Part 2

# Get puzzle input as a list 
f = open('Day02/Day02_2_PuzzleInput.txt', 'r')
puzzle_input = f.read()
puzzle_input_list = puzzle_input.split('\n')

# Solve problem 
solution_counter = 0
for data in puzzle_input_list:
    try:
        pp_number_low = int(data[0 : data.find('-')])
        pp_number_high = int(data[data.find('-') + 1 : data.find(' ')])
        pp_char = str(data[data.find(' ') + 1 : data.find(':')])
        pp_pass = str(data[data.find(':') + 2 : ])
        try:
            if pp_pass[pp_number_low-1] ==  pp_char and pp_pass[pp_number_high-1] !=  pp_char:
                solution_counter += 1
            elif pp_pass[pp_number_low-1] !=  pp_char and pp_pass[pp_number_high-1] ==  pp_char:
                solution_counter += 1
            else:
                pass
        except IndexError:
            pass
    except ValueError:
        print("ERROR: Input data '{}' is not valid".format(data))
print("Number of correct passwords is: {}".format(solution_counter))

