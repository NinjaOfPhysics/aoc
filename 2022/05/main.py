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



if __name__ == "__main__":
    # Get all of these stacks into arrays
    with open('test_data.txt', 'r') as file:
        lines = file.readlines()
    # How many rows are there? Find the line with only numbers in it, that's the number of columns we have. 
    number_of_stacks = get_number_of_stacks(lines)

    # Each row of of stacks should be divided by the 
    stack_character_count = len(lines[0]) // number_of_stacks
    # Divite up the line into all the parts
    stack_ranges = stack_char_ranges(stack_character_count, lines[0])
    print(stack_ranges)

