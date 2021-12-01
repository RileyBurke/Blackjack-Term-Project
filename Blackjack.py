import random
import csv
import sys

def getCardValue(drawnCard, total): #Functional
    if drawnCard[1] == "2" or drawnCard[1] == "3" or drawnCard[1] == "4" or drawnCard[1] == "5" or drawnCard[1] == "6" or drawnCard[1] == "7" or drawnCard[1] == "8" or drawnCard[1] == "9":
        cardValue = int(drawnCard[1])
    elif drawnCard[1] == "10" or drawnCard[1] == "Jack" or drawnCard[1] == "Queen" or drawnCard[1] == "King":
        cardValue = 10
    elif drawnCard[1] == "Ace":
        if total >= 11:
            cardValue = 1
        else:
            cardValue = 11
    return cardValue

def shuffleDeck(deck):   #Functional
    deck.clear()
    deckOfCards(deck)
    random.shuffle(deck)

def loadDealerStatistics(): #Untested
    dealerStats = []
    try:
        with open ("dealerStats.csv", newline = "") as file:
            for row in file:
                dealerStats.append(row)
    except FileNotFoundError:
        pass
    except OSError:
        print("File found - error reading the file - closing program")
        sys.exit()
    except Exception:
        print("An unexpected exception occured - closing program")
        sys.exit()
    return dealerStats
            
def saveDealerStatistics(dealerStats): #Untested
    try:
        with open("dealerStats.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(dealerStats)   
    except Exception:
        print("An unexpected exception occured - closing program")
        sys.exit()

def getBets(playerBanks, numberOfPlayers): #untested
    playerBets = []
    counter = 0
    for counter in range(1, numberOfPlayers):
        while True:  
            try:
                bet = int(input("Enter a bet between $5 and $1000: $"))
                if bet < 5 or bet > 1000:
                    print("Invalid bet entered. Please enter a bet between $5 and $1000")
                    continue
                elif bet <= playerBanks[counter]:
                    playerBanks[counter] - bet
                    playerBets.append(bet)
                else:
                    print("Not enough funds. You have $" + str(playerBanks[counter]))
                    print()
            except ValueError:
                print("Invalid integer entered. Please try again")
                print()
                continue
            except Exception:
                print("An unexpected exception occured")
                print()
                continue
    return playerBets

def deckOfCards():    #Functional
    deck = [["Hearts", "2"], ["Hearts" , "3"], ["Hearts", "4"], ["Hearts", "5"], ["Hearts", "6"], ["Hearts" , "7"], ["Hearts", "8"], ["Hearts", "9"],
            ["Hearts", "10"], ["Hearts" , "Jack"], ["Hearts", "Queen"], ["Hearts", "King"], ["Hearts", "Ace"], ["Diamonds", "2"], ["Diamonds" , "3"],
            ["Diamonds", "4"], ["Diamonds", "5"], ["Diamonds", "6"], ["Diamonds" , "7"], ["Diamonds", "8"], ["Diamonds", "9"], ["Diamonds", "10"],
            ["Diamonds" , "Jack"], ["Diamonds", "Queen"], ["Diamonds", "King"], ["Diamonds", "Ace"], ["Clubs", "2"], ["Clubs" , "3"], ["Clubs", "4"],
            ["Clubs", "5"], ["Clubs", "6"], ["Clubs" , "7"], ["Clubs", "8"], ["Clubs", "9"], ["Clubs", "10"], ["Clubs" , "Jack"], ["Clubs", "Queen"],
            ["Clubs", "King"], ["Clubs", "Ace"], ["Spades", "2"], ["Spades" , "3"], ["Spades", "4"], ["Spades", "5"], ["Spades", "6"], ["Spades" , "7"],
            ["Spades", "8"], ["Spades", "9"], ["Spades", "10"], ["Spades" , "Jack"], ["Spades", "Queen"], ["Spades", "King"], ["Spades", "Ace"]]
    return deck
    
def hit(deck, total): #Functional
    player_card = random.choice(deck)
    print("You have drawn a " + player_card[1] + " of " + player_card[0] + ".")
    card = getCardValue(player_card, total)
    deck.remove(player_card)
    return card

def play(deck, playerBanks, numberOfPlayers):
    playerTotals = [0] * numberOfPlayers
    dealerTotal = 0
    playerBets = getBets(playerBanks, numberOfPlayers)
    
    #Remember to subtract bet
    
    for players in playerTotals:
        players += hit(deck)
    dealerTotal += hit(deck)
    for players in playerTotals:
        players += hit(deck)
    dealerTotal += hit(deck)

def dealerLogic(): #Goes for 17 or higher
    pass

def checkBalance(playerBanks): #Functional, change print statement to be based on number of players
    playerNumber = int(input("Enter number of player to check (1-5): "))
    print("You have $" + str(playerBanks[playerNumber - 1]) + " in funds.")
    print()
    
def payout(bet, playerBanks, total): #To be fixed for list banks
    if total == 21:
        payout = round(bet * 2.5, 2)
    else:
        payout = round(bet * 2, 2)
    playerBanks += payout
    return playerBank
        
def mainMenu(): #Functional
    print("Blackjack")
    print()
    print("1. Play")
    print("2. Check balance")
    print("3. Add funds")
    print("4. Exit")
    print()

def greeting(): #Functional
    print("Welcome to the Eric Stock Casino!")
    print()

def addFunds(playerBanks): #Funtional, change print statement to be based on number of players
    playerNumber = int(input("Enter which player to add funds to (1-5): "))
    while True:
        try:
            addedAmount = int(input("How much money would you like to add?: $"))
            if addedAmount < 0:
                print("Invalid amount entered, try again.")
            else:
                print("Added $" + str(addedAmount) + " to your bank.")
                playerBanks[playerNumber - 1] += addedAmount
                break
        except ValueError:
            print("Invalid integer amount entered, try again.")
    print("You now have $" + str(playerBanks[playerNumber - 1]) + " in funds.")

def enterCommand(deck, playerBanks, numberOfPlayers):
    while True:
        try:
            command = int(input("Choose an option (1-4)"))
            if command == 1:
                play(deck, playerBanks, numberOfPlayers)
            elif command == 2:
                checkBalance(playerBanks) #Add number of players for if statements?
            elif command == 3:
                addFunds(playerBanks)
            elif command == 4:
                break
            else:
                print("Not a valid command.")
                continue
        except ValueError:
            print("Invalid option")

def setNumberOfPlayers(): #Functional
    while True:
        try:
            numberOfPlayers = int(input("How many players? (1-5): "))
            if numberOfPlayers > 0 and numberOfPlayers < 6:
                return numberOfPlayers
                break
            else:
                print("Invalid number of players. Must be a number from 1 to 5.")
                continue
        except ValueError:
            print("Invalid number of players. Must be a number from 1 to 5.")

def setPlayerBanks(numberOfPlayers): #1-5 players banks
    playerBanks = []
    if numberOfPlayers == 1:
        while True:
            try:
                playerOneBank = int(input("How much money would you like to enter for player one?: $"))
                playerBanks.append(playerOneBank)
                if playerOneBank > 5:
                    break
                else:
                    print("Not enough money to place a bet.")
            except ValueError:
                print("Invalid amount, please try again.")
    elif numberOfPlayers == 2:
        playerOneBank = int(input("How much money would you like to enter for player one?: $"))
        playerBanks.append(playerOneBank)
        
        playerTwoBank = int(input("How much money would you like to enter for player two?: $"))
        playerBanks.append(playerTwoBank)
    elif numberOfPlayers == 3:
        playerOneBank = int(input("How much money would you like to enter for player one?: $"))
        playerTwoBank = int(input("How much money would you like to enter for player two?: $"))
        playerThreeBank = int(input("How much money would you like to enter for player three?: $"))
        playerBanks.append(playerOneBank)
        playerBanks.append(playerTwoBank)
        playerBanks.append(playerThreeBank)
    elif numberOfPlayers == 4:
        playerOneBank = int(input("How much money would you like to enter for player one?: $"))
        playerTwoBank = int(input("How much money would you like to enter for player two?: $"))
        playerThreeBank = int(input("How much money would you like to enter for player three?: $"))
        playerFourBank = int(input("How much money would you like to enter for player four?: $"))
        playerBanks.append(playerOneBank)
        playerBanks.append(playerTwoBank)
        playerBanks.append(playerThreeBank)
        playerBanks.append(playerFourBank)
    else:
        playerOneBank = int(input("How much money would you like to enter for player one?: $"))
        playerTwoBank = int(input("How much money would you like to enter for player two?: $"))
        playerThreeBank = int(input("How much money would you like to enter for player three?: $"))
        playerFourBank = int(input("How much money would you like to enter for player four?: $"))
        playerFiveBank = int(input("How much money would you like to enter for player five?: $"))
        playerBanks.append(playerOneBank)
        playerBanks.append(playerTwoBank)
        playerBanks.append(playerThreeBank)
        playerBanks.append(playerFourBank)
        playerBanks.append(playerFiveBank)
    return playerBanks

def main():
    dealerStats = loadDealerStatistics()
    deck = deckOfCards()
    greeting()
    numberOfPlayers = setNumberOfPlayers()
    playerBanks = setPlayerBanks(numberOfPlayers)
    print()
    mainMenu()
    enterCommand(deck, playerBanks, numberOfPlayers)
    print("Bye!")
    

if __name__ == "__main__":
    main()
