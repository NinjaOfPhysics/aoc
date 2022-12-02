if __name__ == "__main__":
    most_cal = 0
    second_most = 0
    thrid_most = 0
    cal_elf_carry = 0
    with open("data.txt", 'r') as file:
        for line in file:
            if line != '\n':
                fruit_cal = int(line.strip())
                cal_elf_carry += fruit_cal
            else:
                if most_cal < cal_elf_carry:
                    thrid_most = second_most
                    second_most = most_cal
                    most_cal = cal_elf_carry
                elif second_most < cal_elf_carry < most_cal:
                    thrid_most = second_most
                    second_most = cal_elf_carry
                elif thrid_most < cal_elf_carry < second_most:
                    thrid_most = cal_elf_carry
                cal_elf_carry = 0

    print(f"Most calories carried: {most_cal}\nSecond most Calories carried: {second_most}\nThrid most Calories carried: {thrid_most}\nTotal: {most_cal+second_most+thrid_most}")