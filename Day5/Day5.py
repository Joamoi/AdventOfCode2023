with open("input.txt") as f:
    lines = f.readlines()

# we create a 3D list (maps[][][]) where 1. number = category, 2. number = row, 3. number = range type
maps = []
i = 1
while (i < len(lines)):
    if (lines[i] == "\n"):
        maps.append([])
        i += 2
    else:
        maps[-1].append([])
        maps[-1][-1] = lines[i].split()
        i += 1

# we use the same function in parts A and B to go from seed to location
def getlocation(seed):
    location = seed
    for map in maps:
        for row in map:
            lowerlimit = int(row[1])
            upperlimit = int(row[1]) + int(row[2])
            jump = int(row[0]) - int(row[1])
            if (lowerlimit <= location < upperlimit):
                location += jump
                break
    return location

# part A
seeds = lines[0].split(":")[1].split()
bestlocation = 999999999999

# we go from seed to location for every seed
for seed in seeds:
    location = getlocation(int(seed))
    if (location < bestlocation):
        bestlocation = location

print("lowest location number in part A: " + str(bestlocation) + "\n")

# part B
seedlows = []
seedranges = []
bestlocation = 999999999999

# we split seed values to low seed values and ranges
for i in range(len(seeds)):
    if(i%2 == 0):
        seedlows.append(seeds[i])
    else:
        seedranges.append(seeds[i])

# there are too many seeds to go through individually so do an iteration
for i in range(len(seedlows)):
    seedlow = int(seedlows[i])
    seedhigh = seedlow + int(seedranges[i])
    print("\nstarting seeds " + str(seedlow) + " and " + str(seedhigh) + "\n")
    iterseeds = []
    iterseeds.append(seedlow)
    iterseeds.append(seedhigh)
    
    iterdone = False
    
    # we check if lowest and highest seed keep the same gap when converted to locations
    while (iterdone == False):
        iterseeds.sort()
        seedgap =  iterseeds[1] - iterseeds[0]
        #print("iteration between seeds " + str(iterseeds[0]) + " and " + str(iterseeds[1]))
        print("seedgap: " + str(seedgap))
        locationlow = getlocation(iterseeds[0])
        locationhigh = getlocation(iterseeds[1])
        locationgap = locationhigh - locationlow
        #print("locationgap: " + str(locationgap))
        
        # when gaps match or when gap is 1 we check location and take out the lowest seed from the iteration
        if(seedgap == locationgap or seedgap == 1):
            if (locationlow < bestlocation):
                bestlocation = locationlow
                print("\nnew lowest location: " + str(locationlow) + "\n")
            # we keep going until gap matches with the highest seed (last seed in the list)
            if(iterseeds[1] == iterseeds[-1]):
                iterdone = True
            iterseeds.pop(0)
            
        # if gaps don't match we get a seed from the middle and try with the gap between lowest seed and the middle seed
        else:
            seedmiddle = iterseeds[0] + int(seedgap/2)
            iterseeds.append(seedmiddle)

print("\nlowest location number in part B: " + str(bestlocation))