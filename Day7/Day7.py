# we create a 6-letter code to sort the hands
# first letter tells if the player has 4-of-a-kind, full house, etc.
# rest of the letters are card labels converted to letters for sorting

from site import addusersitepackages


with open("input.txt") as f:
    lines = f.readlines()

# function to determine strength for normal hand
def handstrength(hand):
    # set stores only unique characters so 5-of-a-kind gives a set of 1 character
    dif = ''.join(set(hand))
    if (len(dif) == 1):
        return "A"
    elif (len(dif) == 4):
        return "F"
    elif (len(dif) == 5):
        return "G"
    elif (len(dif) == 2):
        ## 4 of a kind has to have 4 same characters in a row when sorted
        cards = ''.join(sorted(hand))
        set_a = ''.join(set(cards[1:]))
        set_b = ''.join(set(cards[:4]))
        if (len(set_a) == 1 or len(set_b) == 1):
            return "B"
        else:
            return "C"
    else:
        ## 3 of a kind has to have 3 same characters in a row when sorted
        cards = ''.join(sorted(hand))
        set_a = ''.join(set(cards[2:]))
        set_b = ''.join(set(cards[:3]))
        set_c = ''.join(set(cards[1:4]))
        if (len(set_a) == 1 or len(set_b) == 1 or len(set_c) == 1):
            return "D"
        else:
            return "E"

# function to determine strength for hand with joker(s)
def jokerhandstrength(hand):
    others = hand.replace("J","")
    if (len(others) < 2):
        return "A"
    else:
        dif = ''.join(set(others))
        if (len(dif) == 1):
            return "A"
        elif (len(dif) == 4):
            return "F"
        elif (len(dif) == 3):
            return "D"
        elif (len(others) == 4):
            cards = ''.join(sorted(others))
            set_a = ''.join(set(cards[:2]))
            set_b = ''.join(set(cards[2:]))
            if (len(set_a) == 1 and len(set_b) == 1):
                return "C"
            else:
                return "B"
        else:
            return "B"

# function to rank hands based on the code and to count winnings
def sortandwin(codes):
    codes.sort()      
    winnings = 0
    for i in range (len(codes)):
        bid = int(codes[i].split()[2])
        rank = (len(codes) - i)
        win = rank * bid
        print(codes[i] + "  \trank " + str(rank) + "  \twins: " + str(win))
        winnings += win
    return winnings

# part A

codes = []
labels = "AKQJT98765432"
letters = "ABCDEFGHIJKLM"

for line in lines:
    hand = line.split()[0]
    
    code = handstrength(hand)
    
    for card in hand:
        for i in range(13):
            if (labels[i] == card):
                code += letters[i]
                
    code = code + " " + line.split("\n")[0]
    codes.append(code)
    
print("\ntotal winnings: " + str(sortandwin(codes)) + "\n")

# part B

codes = []
labels = "AKQT98765432J"
letters = "ABCDEFGHIJKLM"

for line in lines:
    hand = line.split()[0]
    if (hand.find("J") == -1):
        code = handstrength(hand)
    else:
        code = jokerhandstrength(hand)
    
    for card in hand:
        for i in range(13):
            if (labels[i] == card):
                code += letters[i]
                
    code = code + " " + line.split("\n")[0]
    codes.append(code)

print("\ntotal winnings: " + str(sortandwin(codes)) + "\n")