import random
intwin = 0
intloss = 0
print("Welcome to Monty Hall!")
while True:
    intcardoor = random.randint(0, 2)
    intfirstdoor = -1
    while intfirstdoor < 0 or intfirstdoor > 2:
        intfirstdoor = int(input("Select a door, 0 to 2."))
    listy = [0, 1, 2]
    if intfirstdoor == intcardoor:
        for x in listy:
            if x == intfirstdoor:
                listy.remove(x)
                break
        intopen = random.choice(listy)
        for y in [0, 1]:
            if listy[y] != intopen:
                intsnddoor = listy[y]    
    else:
        for z in listy:
            if z == intcardoor:
                intsnddoor = z
            if z != intcardoor and z != intfirstdoor:
                intopen = z
    strchange = input("Behind door " + str(intopen) + " is a goat. Would you like to change doors to door " + str(intsnddoor) + "? (y/n)")
    if strchange == "y":
        intfinaldoor = intsnddoor
    else:
        intfinaldoor = intfirstdoor
    print("You chose door " + str(intfinaldoor) + ". The car was behind door " + str(intcardoor) + ".")
    if intfinaldoor == intcardoor:
        print("You win!")
        intwin += 1
    else:
        print("You lose.")
        intloss += 1
    print("You have won " + str(round(((intwin/(intwin + intloss))*100), 2)) + "% of the time.")
    strquit = input("Quit? (y/n)")
    if strquit == "y":
        break
    


