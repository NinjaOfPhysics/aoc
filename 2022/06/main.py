import pdb

def check_marker(char, marker):
    if char in marker:
        #print(char, "is in", marker)
        marker = marker[1:]
        marker = check_marker(char, marker)
    #print("returning", marker)
    return marker

if __name__ == "__main__":
    with open("data.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        marker = ''
        count = 0
        for char in line:
            #pdb.set_trace()
            count += 1
            marker = check_marker(char, marker)
            marker += char
            if len(marker) == 4:
                print(marker, count)
                break
    
    # Part 2
    for line in lines:
        marker = ''
        count = 0
        for char in line:
            #pdb.set_trace()
            count += 1
            marker = check_marker(char, marker)
            marker += char
            if len(marker) == 14:
                print(marker, count)
                break
    
    
