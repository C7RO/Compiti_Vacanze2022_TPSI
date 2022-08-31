# Score categories.
# Change the values as you see fit.
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def sommaNum(dice, num):
    somma=0
    for n in dice:
        if n == num:
            somma+=n
    return somma

def contFour(dice):
    for i,n in enumerate(dice[:2]):
        cont=1
        for n2 in dice[i+1:]:
            if n== n2:
                cont+=1
        if cont>= 4:
            return n
    return False

def isFullHouse(dice):
    cont=1
    Two=False
    Three=False
    for n in dice[1:]:
        if dice[0]== n:
            cont+=1
    if cont==2:
        Two=True
    if cont==3:
        Three=True
        
    n2= 1
    while dice[n2]== dice[0] and n2< 3:
        n2+=1
    cont=0
    for n in dice[1:]:
        if dice[n2]== n:
            cont+=1
    if cont==2:
        Two=True
    if cont==3:
        Three=True
    return Two and Three
    
def score(dice, category):
    somma=0
    if category==ONES:
        return sommaNum(dice,1)
    if category==TWOS:
        return sommaNum(dice,2)
    if category==THREES:
        return sommaNum(dice,3)
    if category==FOURS:
        return sommaNum(dice,4)
    if category==FIVES:
        return sommaNum(dice,5)
    if category==SIXES:
        return sommaNum(dice,6)
    if category== FULL_HOUSE:
        if isFullHouse(dice):
            for n in dice:
                somma+=n
        return somma
    if category== FOUR_OF_A_KIND:
        if contFour(dice)!= False:
            return contFour(dice)*4
        else:
            return 0
    if category== LITTLE_STRAIGHT:
        if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            return 30
        else:
            return 0
    if category== BIG_STRAIGHT:
        if 6 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            return 30
        else:
            return 0
    if category== CHOICE:
        for n in dice:
            somma+=n
        return somma
    if category== YACHT:
        if dice[0]==dice[1] and dice[0]==dice [2] and dice[0]== dice[3] and dice[0]== dice[4]:
            return 50
        else:
            return 0
