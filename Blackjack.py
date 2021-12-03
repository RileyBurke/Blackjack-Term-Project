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

def getBets(playerBanks, numberOfPlayers): #Functional
    playerBets = [0] * numberOfPlayers
    counter = 0
    for player in playerBets:
        while True:
            try:
                playerBets[counter] = int(input("Player " + str(counter + 1) + " - How much money would you like to bet?: $"))
                if playerBets[counter] < 5 or playerBets[counter] > 1000:
                    print("Invalid bet entered. Please enter a bet between $5 and $1000")
                    continue
                elif playerBets[counter] > playerBanks[counter]:
                    print("Not enough funds. You have $" + str(playerBanks[counter]))
                    continue
                else:
                    playerBanks[counter] -= playerBets[counter]
                    counter += 1
                    break
            except ValueError:
                print("Invalid integer entered. Please try again")
                print()
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
    
def hitPlayer(deck, total, counter, turnNumber): #Functional
    player_card = random.choice(deck)
    card = getCardValue(player_card, total)
    deck.remove(player_card)
    print("Player " + str(counter + 1) + " has drawn a " + player_card[1] + " of " + player_card[0] + ".")
    return card

def hitDealer(deck, dealerTotal, turnNumber): #Functional
    if turnNumber == 1:
        player_card = random.choice(deck)
        print("The dealer has drawn a " + player_card[1] + " of " + player_card[0] + ".")
        card = getCardValue(player_card, dealerTotal)
        deck.remove(player_card)
        dealerTotal += card
        return dealerTotal
    else:
        if dealerTotal < 17:
            player_card = random.choice(deck)
            print("The dealer has drawn a " + player_card[1] + " of " + player_card[0] + ".")
            card = getCardValue(player_card, dealerTotal)
            deck.remove(player_card)
            dealerTotal += card
            print("Total is now " + str(dealerTotal) + ".")
            return dealerTotal
        else:
            print("Dealer stands with " + str(dealerTotal))
            return dealerTotal

def playGame(deck, playerBanks, numberOfPlayers):
    playerTotals = [0] * numberOfPlayers
    dealerTotal = 0
    turnNumber = 1
    counter = 0
    playerBets = getBets(playerBanks, numberOfPlayers)
    print()
    while True:
        turnNumber = turn(deck, playerTotals, turnNumber, counter, playerBanks, playerBets)
        if turnNumber <= 2:
            dealerTotal = hitDealer(deck, dealerTotal, turnNumber)
        print()
        for players in playerTotals:
            if playerTotals[counter] == 21:
                print("Player " + str(counter + 1) + " has blackjack!")
                playerBanks[counter] = payout(playerBets[counter], playerBanks[counter], playerTotals[counter], counter)
            elif playerTotals[counter] > 21:
                print("Player " + str(counter + 1) + " has busted out.")
    while True:
        hitDealer(deck, total, turnNumber)
        if dealerTotal == 21:
            print("Dealer has blackjack.")
            break
        elif dealerTotal > 21:
            print("Dealer has busted out.")
            for player in playerBanks:
                payout(playerBets, playerBanks, playerTotals, counter)
            break
    print()
    shuffleDeck(deck)

def gameOptions(deck, playerTotals, counter, turnNumber, playerBanks, playerBets):
    print("Player " + str(counter + 1))
    while True:
        option = input("Hit or Stand: ")
        if option.title() == "Hit":
            playerTotals[counter] += hitPlayer(deck, playerTotals[counter], counter , turnNumber)
            if playerTotals[counter] == 21:
                print("Player " + str(counter + 1) + " has blackjack!")
                payout(playerBets[counter], playerBanks[counter], playerTotals[counter], counter)
                break
            elif playerTotals[counter] > 21:
                print("Player " + str(counter + 1) + " has busted out.")
                break
            else:
                print("Total is now " + str(playerTotals[counter]) + ".")
        elif option.title() == "Stand":
            print("Standing at " + str(playerTotals[counter]))
            break
        else:
            print("Invalid option.")
            continue

def turn(deck, playerTotals, turnNumber, counter, playerBanks, playerBets):
    while counter < len(playerTotals):
        if turnNumber == 2:
            playerTotals[counter] += hitPlayer(deck, playerTotals[counter], counter , turnNumber)
            print("Total is now " + str(playerTotals[counter]) + ".")
            print()
        elif turnNumber > 2:
            gameOptions(deck, playerTotals, counter, turnNumber, playerBanks, playerBets)
            print("Total is now " + str(playerTotals[counter]) + ".")
            print()
        else:
            playerTotals[counter] += hitPlayer(deck, playerTotals[counter], counter , turnNumber)
            print()
        counter += 1
    turnNumber += 1
    return turnNumber

def checkBalance(playerBanks): #Functional
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
    
def payout(playerBets, playerBanks, playerTotals, counter): #Functional
    if playerTotals == 21:
        payout = round(playerBets[counter] * 2.5, 2)
    else:
        payout = round(playerBets[counter] * 2, 2)
    playerBanks += payout
    print("Bet: $" + str(playerBets[counter]) + "  Winnings: $" + str(payout) + "  New total: $" + str(playerBanks))
        
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

def addFunds(playerBanks): #Functional
    while True:
        if len(playerBanks) > 1:
            try:
                playerNumber = int(input("Enter which player to add funds to (1-" + str(len(playerBanks)) + "): "))
            except ValueError:
                print("Invalid player number. Try again.")
                print()
                continue
        else:
            playerNumber = 1
        if playerNumber <= len(playerBanks) and playerNumber > 0:
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
                break
        else:
            print("Invalid player number. Try again.")
            print()
            continue
    print("You now have $" + str(playerBanks[playerNumber - 1]) + " in funds.")
    print()

def enterCommand(deck, playerBanks, numberOfPlayers): #Functional
    while True:
        try:
            command = int(input("Choose an option (1-4): "))
            print()
            if command == 1:
                playGame(deck, playerBanks, numberOfPlayers)
            elif command == 2:
                checkBalance(playerBanks) 
            elif command == 3:
                addFunds(playerBanks)
            elif command == 4:
                break
            else:
                print("Not a valid command.")
                print()
                continue
        except ValueError:
            print("Invalid option")
            print()

def setNumberOfPlayers(): #Functional
    while True:
        try:
            numberOfPlayers = int(input("How many players? (1-5): "))
            if numberOfPlayers > 0 and numberOfPlayers < 6:
                print()
                return numberOfPlayers
            else:
                print("Invalid number of players. Must be a number from 1 to 5.")
                print()
                continue
        except ValueError:
            print("Invalid number of players. Must be a number from 1 to 5.")

def setPlayerBanks(numberOfPlayers): #Functional
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
