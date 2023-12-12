lines = []
numbersum = 0

with open("input.txt") as f:
    for line in f:
        lines.append("")
        lines[-1] = line.strip()

# part A
print("part A\n")

# y is rows, x is characters in a row, s is for skipping characters when there is a large number
for y in range(0, len(lines)):
    print("\nline " + str(y) + "\n")
    x = 0
    
    while (x < len(lines[y])):
        adjacent = ""
        s = 0

        if (lines[y][x].isdigit()):
            number = lines[y][x]
            
            # first we pick up characters that are adjacent no matter the number length
            if (x > 0):
                adjacent += lines[y][x - 1]
            if (x > 0 and y > 0):
                adjacent += lines[y - 1][x - 1]
            if (x > 0 and y < (len(lines) - 1)):
                adjacent += lines[y + 1][x - 1]
            if (y > 0):
                adjacent += lines[y - 1][x]
            if (y < (len(lines) - 1)):
                adjacent += lines[y + 1][x]
            if (y > 0 and x < (len(lines[y]) - 1)):
                adjacent += lines[y - 1][x + 1]
            if (y < (len(lines) - 1) and x < (len(lines[y]) - 1)):
                adjacent += lines[y + 1][x + 1]
                
            # if number is longer we also pick up more adjacent characters
            s = 1
            if (x < (len(lines[y]) - 1)):
                while (lines[y][x + s].isdigit()):
                    number += lines[y][x + s]
                    s = s + 1
                    if (y > 0 and (x + s) < (len(lines[y]) - 1)):
                        adjacent += lines[y - 1][x + s]
                    if (y < (len(lines) - 1) and (x + s) < (len(lines[y]) - 1)):
                        adjacent += lines[y + 1][x + s]
                    if ((x + s) > (len(lines[y]) - 1)):
                        break
            print("number: " + str(number))
            
            # finally we pick up last adjacent character
            if ((x + s) < (len(lines[y]) - 1)):
                adjacent += lines[y][x + s]
            print("adjacent: " + adjacent)
            
            # check if there is a symbol in adjacent characters
            for char in adjacent:
                if (char != "."):
                    numbersum += int(number)
                    print("sum: " + str(numbersum))
                    break
                
            x += s
        else:
            x += 1
        
print("\nsum: " + str(numbersum))

# part B
print("\npart B\n")

ratiosum = 0

for y in range(0, len(lines)):
    print("\nline " + str(y) + "\n")
    x = 0
    
    for x in range(0, len(lines[y])):
        
        # if character is gear, we check adjacent characters for numbers
        if (lines[y][x] == "*"):
            print("gear, row " + str(y) + " char " + str(x))
            numbers = []
            
            # left
            if (x > 0):
                if(lines[y][x - 1].isdigit()):
                    numbers.append("")
                    number = lines[y][x - 1]
                    if ((x - 1) > 0):
                        s = 2
                        while (lines[y][x - s].isdigit()):
                            number = lines[y][x - s] + number
                            s = s + 1
                            if ((x - s) < 0):
                                break
                    numbers[-1] = number
                    print("number: " + number)
                    
            # right
            if (x < (len(lines[y]) - 1)):
                if (lines[y][x + 1].isdigit()):
                    numbers.append("")
                    number = lines[y][x + 1]
                    if ((x + 1) < (len(lines[y]) - 1)):
                        s = 2
                        while (lines[y][x + s].isdigit()):
                            number += lines[y][x + s]
                            s = s + 1
                            if ((x + s) > (len(lines[y]) - 1)):
                                break
                    numbers[-1] = number
                    print("number: " + number)
                    
            # up
            if (y > 0):
                if (lines[y - 1][x].isdigit()):
                    numbers.append("")
                    number = lines[y - 1][x]
                    if ((x + 1) < (len(lines[y]) - 1)):
                        s = 1
                        while (lines[y - 1][x + s].isdigit()):
                            number += lines[y - 1][x + s]
                            s = s + 1
                            if ((x + s) > (len(lines[y]) - 1)):
                                break
                    if ((x - 1) > 0):
                        s = 1
                        while (lines[y - 1][x - s].isdigit()):
                            number = lines[y - 1][x - s] + number
                            s = s + 1
                            if ((x - s) < 0):
                                break
                    numbers[-1] = number
                    print("number: " + number)
                    
                # up diagonals
                else:
                    if (y > 0):
                        if (lines[y - 1][x - 1].isdigit()):
                            numbers.append("")
                            number = lines[y - 1][x - 1]
                            if ((x - 1) > 0):
                                s = 2
                                while (lines[y - 1][x - s].isdigit()):
                                    number = lines[y - 1][x - s] + number
                                    s = s + 1
                                    if ((x - s) < 0):
                                        break
                            numbers[-1] = number
                            print("number: " + number)
                    if (y > 0):
                        if (lines[y - 1][x + 1].isdigit()):
                            numbers.append("")
                            number = lines[y - 1][x + 1]
                            if ((x + 1) < (len(lines[y]) - 1)):
                                s = 2
                                while (lines[y - 1][x + s].isdigit()):
                                    number += lines[y - 1][x + s]
                                    s = s + 1
                                    if ((x + s) > (len(lines[y]) - 1)):
                                        break
                            numbers[-1] = number
                            print("number: " + number)
                            
            # down
            if (y < (len(lines) - 1)):
                if (lines[y + 1][x].isdigit()):
                    numbers.append("")
                    number = lines[y + 1][x]
                    if ((x + 1) < (len(lines[y]) - 1)):
                        s = 1
                        while (lines[y + 1][x + s].isdigit()):
                            number += lines[y + 1][x + s]
                            s = s + 1
                            if ((x + s) > (len(lines[y]) - 1)):
                                break
                    if ((x - 1) > 0):
                        s = 1
                        while (lines[y + 1][x - s].isdigit()):
                            number = lines[y + 1][x - s] + number
                            s = s + 1
                            if ((x - s) < 0):
                                break
                    numbers[-1] = number
                    print("number: " + number)
                    
                # down diagonals
                else:
                    if (y < (len(lines) - 1)):
                        if (lines[y + 1][x - 1].isdigit()):
                            numbers.append("")
                            number = lines[y + 1][x - 1]
                            if ((x - 1) > 0):
                                s = 2
                                while (lines[y + 1][x - s].isdigit()):
                                    number = lines[y + 1][x - s] + number
                                    s = s + 1
                                    if ((x - s) < 0):
                                        break
                            numbers[-1] = number
                            print("number: " + number)
                    if (y < (len(lines) - 1)):
                        if (lines[y + 1][x + 1].isdigit()):
                            numbers.append("")
                            number = lines[y + 1][x + 1]
                            if ((x + 1) < (len(lines[y]) - 1)):
                                s = 2
                                while (lines[y + 1][x + s].isdigit()):
                                    number += lines[y + 1][x + s]
                                    s = s + 1
                                    if ((x + s) > (len(lines[y]) - 1)):
                                        break
                            numbers[-1] = number
                            print("number: " + number)
                            
            # count gear ratio if there are exactly 2 numbers adjacent to the gear
            if(len(numbers) == 2):
                ratiosum += int(numbers[0]) * int(numbers[1])
                print("gear found! sum: " + str(ratiosum))
                
print("\nsum: " + str(ratiosum))