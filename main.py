'''
Moataz Khallaf A.K.A Hackerman
Life sim
Dec 20, 2018
'''
###imports
from function import *
import csv, time
###vars and lists
fil = 0
names = []
cash = 0
age = 0
name = []
parent1 = []
parent2 = []
relationships = []
death = 0
data = []
ap = 0 #action points
diff = 0 #difficulty

fil = open("data.csv", newline = "") ##this is to get the names list
data = csv.reader(fil)
for line in data:
    names.append(line)

fil = open("bio.txt", "r") ##to pull up bios
text = fil.read()
fil.close()

###Code starts###
while True:
    choice = choicePick(menu())
    try:
        choice = int(choice)
        break
    except ValueError:
        print(choice)
        time.sleep(5)
        clear()

##Your name
first,last = nameGen(names)
name.append(first)
name.append(last)
name = " ".join(name)

##Your parent's names
P1First,P1Last = nameGen(names)
parent1.append(P1First)
parent1.append(last)
parent1 = " ".join(parent1)
relationships.append(parent1)

P2First,P2last = nameGen(names)
parent2.append(P2First)
parent2.append(last)
parent2 = " ".join(parent2)
relationships.append(parent1)


diff = Modifer(choice)
start(diff, name, parent1, parent2)

while death == 0:
    print("age:",age)
    x = mainMenu()
    
    try:
        x = int(x)
    except ValueError:
        x = mainMenu()
    
    if x == 1:
        y = assetMenu()
        y = int(y)
        if y == 1:
            z = carMenu()
            if z == 1:
                car = buyAsset(cars, cash)
            else:
                print(car)
        else:
            z = houseMenu()
            if z == 1:
                house = buyAsset(houses, cash)
            else:
                print(house)
    
    elif x == 2:
        y = relationshipMenu(parent1, parent2)
        print("you hung out with", y, "and had a very fun time")
    
    elif x == 3:
        y = activityMenu()
        print("you enjoyed", y,)
    
    else:
        ageUp()
        age += 1

    death = deathCalc(age)