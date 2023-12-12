with open("input.txt") as f:
    lines = f.readlines()

rgbstring = ["red", "green", "blue"]
rgbmax = [12,13,14]
idsum = 0
powersum = 0

for line in lines:
    rgbhigh = [0,0,0]
    
    line = line.split("\n")[0]
    idstring = line.split(":")[0]
    print("\nidstring: " + idstring + "\n")
    idvalue = int(idstring.split()[1])
    line = line.split(":")[1]
    
    # split rest of the line first to reveals and then to colors
    reveals = line.split(";")
    for reveal in reveals:
        print("reveal: " + reveal)
        colors = reveal.split(",")
        for color in colors:
            # go through all 3 possible colors and store the value if it's the highest so far
            for i in range(0, 3):
                if (color.split()[1] == rgbstring[i] and int(color.split()[0]) > rgbhigh[i]):
                    rgbhigh[i] = int(color.split()[0])         
    print("\nredhigh: " + str(rgbhigh[0]) + " , " + "greenhigh: " + str(rgbhigh[1]) + " , " + "bluehigh: " + str(rgbhigh[2]))
    
    # add game id to sum if highest values are below maximums
    if (rgbhigh[0] <= rgbmax[0] and rgbhigh[1] <= rgbmax[1] and rgbhigh[2] <= rgbmax[2]):
        idsum += idvalue
        print("game ok")
    else:
        print("game is impossible")
        
    power = rgbhigh[0] * rgbhigh[1] * rgbhigh[2]
    powersum += power
        
print("\nsum of game IDs: " + str(idsum))
print("sum of game powers: " + str(powersum))