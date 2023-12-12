with open("input.txt") as f:
    lines = f.readlines()

# part A
print("part A\n")

digits = []
values = []
sumofvalues = 0

# store lines without letters
for line in lines:
    digits.append("")
    values.append("")
    
    for character in line:
        if (character.isdigit()):
            digits[-1] += character
    print("\nline digits: " + digits[-1])
    
    # store first and last digit of every line to a list
    values[-1] += digits[-1][0]    
    values[-1] += digits[-1][-1]
    print("value: " + values[-1])
    
    # add the 2-digit value to the total sum
    sumofvalues += int(values[-1])
        
print("\nSum of values: " + str(sumofvalues))

# part B
print("\npart B")

writtennumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitsb = []
valuesb = []
sumofvaluesb = 0

for line in lines:
    digitsb.append("")
    valuesb.append("")
    print("\nline: " + line)
    
    # replace every written number with number#number (one -> one1one)
    for i in range(0, len(writtennumbers)):
        line = line.replace(writtennumbers[i], writtennumbers[i] + str(i + 1) + writtennumbers[i])
    print("modified line: " + line)
    
    # store lines without letters
    for character in line:
        if (character.isdigit()):
            digitsb[-1] += character
    print("line digits: " + digitsb[-1])
    
    # store first and last digit of every line to a list
    valuesb[-1] += digitsb[-1][0]    
    valuesb[-1] += digitsb[-1][-1]
    print("value: " + valuesb[-1])
    
    # add the 2-digit value to the total sum
    sumofvaluesb += int(valuesb[-1])
    print("sum: " + str(sumofvaluesb))
        
print("\nSum of values: " + str(sumofvaluesb))