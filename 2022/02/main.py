a = 'rock'
b = 'paper'
c = 'scissors'
import numpy as np

winner_key = np.array([[3, 0, 6], [6, 3, 0], [0, 6, 3]])
value_key = {'A': 1, 'B': 2, 'C': 3,
             'X': 1, 'Y': 2, 'Z': 3}

def partOne():
    total_score = 0
    with open("data.txt", 'r') as file:
        for line in file:
            oponent, you = list(line.strip('\n').split(' '))
            oponent_index = value_key[oponent]
            you_index = value_key[you]
            round_score = you_index + winner_key[you_index-1, oponent_index-1]
            total_score += round_score
            #print(f"Oponent: {oponent}, You: {you}, Points: {round_score}")
    print(f"Total score is: {total_score}")

def partTwo():
    total_score = 0
    with open("data.txt", 'r') as file:
        for line in file:
            opponent, result = list(line.strip('\n').split(' '))
            if result =='X': 
                # I need to lose.
                you = (value_key[opponent] + 1) % 3 + 1
            elif result == 'Y':
                # Need to draw
                you = value_key[opponent]
            elif result == 'Z':
                you = value_key[opponent]%3 + 1
                
            opponent_index = value_key[opponent]
            round_score = you + winner_key[you-1, opponent_index-1]
            total_score += round_score
            #print(f"Oponent: {oponent}, You: {you}, Points: {round_score}")
    print(f"Total score is: {total_score}")
if __name__ == "__main__":
    #partOne()
    partTwo()
    