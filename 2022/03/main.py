def split_sack(sack):
    half_point = len(sack)//2
    first_half = sack[:half_point]
    second_half = sack[half_point:]
    return first_half, second_half

def letter_to_prio(letter):
    """ Converts the letter to the priority"""
    if letter == letter.lower():
        # a = 97 -> 1
        letter_prio = ord(letter) - 96
    elif letter == letter.upper():
        # A = 65 -> 26
        letter_prio = ord(letter) - 38
    return letter_prio


if __name__ == "__main__":
    # Split the string
    answer = 0
    with open("C:\\Users\\cody2\\aoc\\aoc\\2022\\03\\data.txt", 'r') as file:
        sacks = file.readlines()
    for sack in sacks:
        first_half, second_half = split_sack(sack)
        for letter in first_half:
            if letter in second_half: # Thats my guy
                answer += letter_to_prio(letter)
                break
    print("Part one answer:", answer)
    
    # Part 2
    index = 0
    answer = 0
    while True:
        sack1 = sacks[index]
        sack2 = sacks[index+1]
        sack3 = sacks[index+2]

        for letter in sack1:
            if letter in sack2 and letter in sack3:
                #Victory!
                prio = letter_to_prio(letter)
                # print(prio, letter)
                answer += prio
                break
        index += 3
        if index >= len(sacks):
            break
    print("Part two answer: ", answer)