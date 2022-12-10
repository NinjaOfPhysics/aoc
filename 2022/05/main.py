import re

def get_number_of_stacks(lines):
    for line in lines:
        if re.search('^[0-9 ]*$', line): # Only numbers and spaces
            x = [int(i) for i in re.findall('[0-9]+', line)]
            number_of_stacks = max(x)
            return number_of_stacks
    raise NameError("No stack line found, faulty input")

def stack_char_ranges(stack_character_count, line):
    stack_ranges = []
    for i in range(0,len(line),stack_character_count):
        stack_ranges.append(range(i, stack_character_count+i))
    return stack_ranges

def setup_initial_stacks(lines, stack_ranges):
    stack_dict = {}
    for i in range(number_of_stacks):
        stack_dict[i+1] = []
     # Now i need to 'read' the stacks in the data file and put them in the right dictionary
    for line in lines:
        if '[' in line:
            # Then it's a stack line
            for r in range(len(stack_ranges)):
                stack_container = line[stack_ranges[r][0]: stack_ranges[r][-1]]
                stack_container = stack_container.strip()
                if stack_container:
                    # Remove brackets and add value to stack value
                    stack_value = stack_container[stack_container.find('[')+1]
                    stack_dict[r+1].insert(0, stack_value)
    return stack_dict

def move(move_command, stack_dict):
    commands = re.findall('[0-9]+', move_command)
    number_to_move, stack_from, stack_to = [int(c) for c in commands]
    for _ in range(int(number_to_move)):
        stack_dict[stack_to].append(stack_dict[stack_from].pop())
    return stack_dict

def move9001(move_command, stack_dict):
    commands = re.findall('[0-9]+', move_command)
    number_to_move, stack_from, stack_to = [int(c) for c in commands]
    stack_move = stack_dict[stack_from][-number_to_move:]
    del stack_dict[stack_from][-number_to_move:]
    stack_dict[stack_to].extend(stack_move)
    return stack_dict


def get_top_of_stacks(stack_dict):
    top_string = ''
    keys = stack_dict.keys()
    keys = sorted(keys)
    for key in keys:
        top_string += stack_dict[key][-1]
    return top_string

if __name__ == "__main__":
    # Get all of these stacks into arrays
    with open('data.txt', 'r') as file:
        lines = file.readlines()
    # How many rows are there? Find the line with only numbers in it, that's the number of columns we have. 
    number_of_stacks = get_number_of_stacks(lines)

    # Each row of of stacks should be divided by the 
    stack_character_count = len(lines[0]) // number_of_stacks
    # Divite up the line into all the parts
    stack_ranges = stack_char_ranges(stack_character_count, lines[0])
    
    stack_dict = setup_initial_stacks(lines, stack_ranges)     
    
    move_lines = [line for line in lines if line.startswith('move')]
    for move_line in move_lines:
        stack_dict = move(move_line, stack_dict)
    answer = get_top_of_stacks(stack_dict)
    print(answer)

    # Part two
    stack_dict = setup_initial_stacks(lines, stack_ranges)
    for move_line in move_lines:
        stack_dict = move9001(move_line, stack_dict)
    answer = get_top_of_stacks(stack_dict)
    print(answer)