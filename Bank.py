def setPlayerBanks(numberOfPlayers): #Sets the initial values for the bank of each player.
    playerBanks = [0] * numberOfPlayers
    counter = 0
    for player in playerBanks:
        while True:
            try:
                playerBanks[counter] = int(input("How much money would you like to enter for player " + str(counter + 1) + "?: $"))
                if playerBanks[counter] >= 5:
                    counter += 1
                    break
                else:
                    print("Not enough money to place a bet.")
            except ValueError:
                print("Invalid amount, please try again.")
    return playerBanks

def addFunds(playerBanks, playerNumber):
    #Adds funds to player banks. If chosen in menu it gives an option to choose player. If player runs out of money in game it chooses the player for you before you can bet.
    print()
    while True:
        if len(playerBanks) > 1 and playerNumber == 0:
            try:
                playerNumber = int(input("Enter which player to add funds to (1-" + str(len(playerBanks)) + "): "))
            except ValueError:
                print("Invalid player number. Try again.")
                print()
                continue
        elif playerNumber <= len(playerBanks) and playerNumber > 0 or len(playerBanks) == 1:
            if len(playerBanks) == 1:
                playerNumber = 1
            try:
                addedAmount = int(input("How much money would you like to add?: $"))
                if addedAmount < 0:
                    print("Invalid amount entered, try again.")
                else:
                    playerBanks[playerNumber - 1] += addedAmount
                    print("Added $" + str(addedAmount) + " to your bank.")
                    break
            except ValueError:
                print("Invalid integer amount entered.")
                print()
        else:
            print("Invalid player number. Try again.")
            print()
            continue
    print("You now have $" + str(playerBanks[playerNumber - 1]) + " in funds.")
    print()

def checkBalance(playerBanks): #Allows players to check their balance from the main menu.
    print()
    while True:
        if len(playerBanks) > 1:
            try:
                playerNumber = int(input("Enter number of player to check (1-" + str(len(playerBanks)) + "): "))
            except ValueError:
                print("Invalid player number. Try again.")
                print()
                continue
        else:
            playerNumber = 1
        if playerNumber <= len(playerBanks) and playerNumber > 0:
            print("You have $" + str(playerBanks[playerNumber - 1]) + " in funds.")
            print()
            break
        else:
            print("Invalid player number. Try again.")
            print()
            continue 
