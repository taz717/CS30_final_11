'''
Moataz Khallaf
Functions for life sim
dec 20, 2018
'''
            ###imports###
import random, sys, time

            ###Vars and lists###
cars = [
["honda", "civic", 12000],
["honda", "supra", 25000],
["honda", "hondacar", 2000]
]

houses = [
[ "3 Bedrooms","24th St/71st Ave, NW", 30000],
[ "2 Bedrooms","33rd St/53rd Ave, SW", 18000],
[ "studio","31st St/43 Ave, NW", 10000]
]

car = 0
house = 0
            ###inputs###

def menu():
    x = input('''
    Welcome to life sim the only sim where you can actually maybe kinda play the life you wanted
    please follow the following options
    1) start a new game
    2) read the biographies 
    3) exit
    ''')
    x = int(x)
    return x

def jobMenu():
    x = input('''I mean you are old enough to work rn so like pick a job
    (1) garbage man [30k/year]
    (2) Danny Devito [atleast 2/year]
    (3) Janitor [24k/year]
    (4) Priest [jesus is all you need/year]
    (5) fast food place man [a big mac or something]        
    ''')
    return x

def askDifficulty(): ##diff is just going to affect the start until further notice
    x = input('''
    Please pick a number from 1 to 3, 1 being the easiest setting and 3 being the hardest.
    (1) easy Upper middle class probably... maybe 
    (2) medium middle class probably... maybe
    (3) hard blessed be thy father for I have sinned
    ''')
    x = int(x)
    return x

def mainMenu():
    x = input('''
    Please pick an option:
    (1) Assests
    (2) Relationships
    (3) Activites
    (4) Level up (age)
    ''')
    return x

def activityMenu():
    x = input('''
    (1) clubbing
    (2) reddit
    (3) smash 5
    (4) Netflix
    (5) facebook
    (6) instagram
    (7) sports...
    (8) drawing stuff
    ''')
    return x

def relationshipMenu(a, b):
    print(''' Who would you like to hang out with?''')
    print("1", a, "2", b)
    x = input("")
    if x == 1:
        y = a
    else:
        y = b
    return y

def assetMenu():
    x = int(input('''
    Please pick an assets option:
    (1) Cars
    (2) Property
    '''))
    return x

def carMenu():
    x = int(input('''
    (1) buy a car
    (2) View owned cars
    '''))
    return x


def houseMenu():
    x = int(input('''
    (1) buy a new house
    (2) view owned houses
    '''))
    return x


                ###Processing###

def clear():
    time.sleep(5)
    print('\n','\n',"Loading",'\n','\n')

def printBiography():
    fil = open("bio.txt", "r")
    x = fil.read()
    fil.close()
    return x

def choicePick(choice):
    if choice == 1:
        x = askDifficulty()
    elif choice == 2:
        x = printBiography()
    else:
        sys.exit()
    return x

def Modifer(a):
    x = random.randint(1, 2)
    if a == 1:  ##so this is a randomizer for diff mods
        y = x ##it's meant to generate 2 numbers for each diff
    elif a == 2: ##and giving a different value for y depending on a which is the diff modifer
        y = x + 2
    elif a == 3:
        y = x + 4
    return y

def nameGen(a):
    x = random.randint(0, 99)
    for i in range(len(a)):
        if x == i:
            name = []
            first = a[i][0]
            last = a[i][1]
            return first, last

def actionPointsReset(a, b): ##this determines tthe action points depending on your age...
    a = 3
    if (b > 10 and b < 18) or b == 18 :
        a += 5
    elif (b  > 18 and b < 25) or b ==25 :
        a += 15
    elif (b > 25 and b < 40) or b == 40 :
        a += 10
    elif (b > 40 and b < 60) or b == 60 :
        a += 5
    return a

def deathCalc(a):
    x = random.randint(1, 10)
    if (a > 45 and x < 2) or (a  > 75 and x < 5):
            y = 1
            return y
    else:
        y = 0
        return y
'''    
def gamePlay():
    global car, house ##I really don't like how I'm using global vars but I don't have time to come up with a faster solution
    x = mainMenu()
    x = int(x)
    if x == 1:
        y = assetMenu()
        y = int(y)
        if y == 1:
            z = carMenu()
            if z == 1:
                car = buyAsset(cars)
            else:
                print(car)
        else:
            z = houseMenu()
            if z == 1:
                house = buyAsset(houses)
            else:
                print(house)
    
    elif x == 2:
        y = relationshipMenu()
        y = int(y)
    
    elif x == 3:
        y = activityMenu()
        y = int(y)
    
    else:
        ageUp()
'''

def buyAsset(b, a):
    print(b)
    y = input("please pick the Asset name you wish to purchase ")
    for i in range(len(b)):
        if y in b[i][1]:
            if a > b[i][2]:
                a = a - b[i][2]
                x = b[i][1]
                print(x)
                return x
            else:
                print("Sorry I can't hear broke, come back when you got the guap")
        else:
            print("loading")    






                ###outputs###

def actionPointsReduction(a):
    if a == 0:
        print("can't do that please end your year")
        a = 404
    else:
        a -= 1
    return a


def start(num, name, parent1, parent2):
    if num == 1:
        print("Welcome to the world,", name)
        print("You are born to", parent1, "and", parent2)
        print(parent1, "is a world renowned computing scientist, his lack of a highschool diploma was supposed to hinder him down")
        print('''through determination and willpower alone he started a company that simulates history
        this off course has brought him millions of dollars. It all started in a simple garage. He now 
        uses his funds to support disease research. Being the richest human on earth he simply can't feel greed
        money means nothing and all he cares about is the legacy he will leave on earth when he departs to the
        afterlife.
        ''')

        print(parent2, "is a nurse")
        print('''
        Simple as that really. They met while doing their required high school volunteer hours. While this isn't has big of an impact as your father, you can sleep soundly at night
        knowing that both wake up every day motivated by the will to help people,
        ''')
        time.sleep(5)

    elif num == 2:
        print("Welcome to the world,", name)
        print("You are born to", parent1, "and", parent2)
        print(parent1, "is a prof at the local universty. He enjoys teaching and doing reserch on human evolution through history.")
        print('''
        He is most fascinated by the recent changes in humans such as weaker grip and sudden merge of the ring and pinky fingures. This area of research while intersting,
        often leads to drastic conclusions on why these changes in evolution are happening.
        ''')

        print(parent2, "is a marine biologist. Off course these two are meant to be right?")
        print('''
        Being a marine biologist simply means that she goes on trips every now and then to pick and count whales or something. She doesn't talk much about
        it. Just how much fun the job is.
        ''')
        time.sleep(5)

    
    elif num == 3:
        print("it's child!!!", name, "is the name and is ready to live life")
        print("You are born to", parent1, "and", parent2)
        print(parent1, "is a police officer ")
        print('''
        It's a tough job but if handled with care, it can raise a community to become closer than ever and create a safe space for kids and adults alike.
        ''')

        print(parent2, "is a stay at home parent")
        print('''
        possibly the hardest job on earth, getting bored is quite easy when all the chores are done
        and their jobs are to make sure that you and the house is clean.
        ''')
        print("Other than the housework,", parent2, "is determined to volunteer every saterday and do kumba or something like that every sunday evening.")
        time.sleep(5)

    elif num == 4:
        print("it's child!!!", name, "is the name and is ready to live life")
        print("You are born to", parent1, "and", parent2)
        print(parent1, "is a neuro surgeon")
        print('''
        While you may be wondering (at the age of 0), how is this medium difficulty? rest assured I'm about to show.
        
        Living an incredibly busy life that cannot be managed due to the tremendus amount of work you have to finish is hard.
        Having kids on top of that is even harder.
        ''')
        print(parent1, "tries to balence this workload however with your birth he realized that it will take way more dedication to raise you right")
        print('''
        handling this much work has proven toll; however, seeing you for the first time has made him realize his true destiny in life.
        Unable to handle all the pressure...
        ''')
        print("four hours after you were born", parent1, "went back to work.")

        print(parent2, "is a student counciler")
        print('''
        A logical thinker with emotional balence to make sure they don't make awkward scenarios. Smart ones indeed.
        Also free summer!!!!
        ''')
        time.sleep(5)
    
    elif num == 5:
        print("wow... it's a ", name )
        print("born to", parent1, "and", parent2)
        print(parent1, "was just hired at the local pharmacy. Years of hard work has lead", parent1, "to this position. From universty to immigrating to this great country.")
        print('''
        abdiding by the country's rules and following testing to configure the level of education of her previous country.
        ''')
        
        print("error 404", parent2, "is not found in the mainframe.")
        time.sleep(5)

    elif num == 6:
        print('''
        error 607: missing database to complete full structural spawn``````````````````````````````````````````````
        ```````````````````````````````````````````````````````````````````````````````````````````````````````````````
        `````````````````````````````````````````````````````````````````````````````````````````````````````````````````
        `````````````````````````````````````````````````````````````````````````````````````````````
        ''')
        time.sleep(1)
        print('''
        rip.exe/////launch/////////
        
        bfunctions*integrated
        *********************
        *********************
        *********************

        54 68 65 72 65 20 77 65 72 65 20
        63 6f 6d 70 6c 69 63 61 74 69 6f
        6e 73 20 69 6e 20 79 6f 75 72 20
        62 69 72 74 68 2e 20 59 6f 75 72
        20 6d 6f 74 68 65 72 20 70 61 73
        73 65 64 20 64 75 72 69 6e 67 20
        62 69 72 74 68 20 61 6e 64 20 79
        6f 75 72 20 66 61 74 68 65 72 20
        63 6f 75 6c 64 6e 27 74 20 68 61
        6e 64 6c 65 20 74 68 65 20 70 61
        69 6e 2e 20 48 65 20 64 69 64 6e 27
        74 20 77 61 6e 74 20 74 6f 20 72 69
        73 6b 20 68 69 6d 73 65 6c 66 20 62
        6c 61 6d 69 6e 67 20 79 6f 75 20 66
        6f 72 20 68 69 73 20 77 69 66 65 27
        73 20 64 65 61 74 68 2e 
        
        
        *********************
        *********************
        *********************
        
        
        ''')
        
        sys.exit()

def ageUp():
    print('''
    congrats... another year living. Made any resolutions? Have you finished the last one you made?
    Did you creat that million dollar thing you wanted or just browsed reddit?
    ''')

def activityResult(a):
    a = int(a)
    if a == 9:
        print("you went to the doctor for a check up")
    else:
        print("That activity was very cool!")