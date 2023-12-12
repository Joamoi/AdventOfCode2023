# part A

with open("input.txt") as f:
    lines = f.readlines()

pointsum = 0
i = 0

for i in range(0, len(lines)):
    numbers = lines[i].split(":")[1]
    winnumbers = numbers.split("|")[0].split()
    mynumbers = numbers.split("|")[1].split()
    points = 0
    
    for mynumber in mynumbers:
        for winnumber in winnumbers:
            if (mynumber == winnumber):
                if (points == 0):
                    points = 1
                else:
                    points = 2 * points
                    
    pointsum += points
    print("card " + str(i) + "  \t" + str(points) + " points\ttotal: " + str(pointsum))

print("\ntotal points: " + str(pointsum) + "\n")

# part B

numbers = []
copycount = []
cardsum = 0

for line in lines:
    numbers.append("")
    numbers[-1] = line.split(":")[1]
    copycount.append(1)
   
i = 0

for i in range(0, len(numbers)):
    winnumbers = numbers[i].split("|")[0].split()
    mynumbers = numbers[i].split("|")[1].split()
    matches = 0
    
    for mynumber in mynumbers:
        for winnumber in winnumbers:
            if (mynumber == winnumber):
                matches += 1
                
    # we check all copies of current card at the same time and add all copies of next games according to amount of matches
    for j in range (0, matches):
        copycount[i + j + 1] += copycount[i]
        
    # we add all copies of the card to the total sum
    cardsum += copycount[i]
    print(str(copycount[i]) + "\tcopies of " + str(i) + "\t" + str(matches) + " matches\ttotal: " + str(cardsum))
    
print("total cards: " + str(cardsum))