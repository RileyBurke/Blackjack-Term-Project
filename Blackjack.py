import random
import csv
import sys

def getCardValue(drawnCard, total): #Untested
    if drawnCard[1] == "2" or card[1] == "3" or card[1] == "4" or card[1] == "5" or card[1] == "6" or card[1] == "7" or card[1] == "8" or card[1] == "9":
        cardValue = int(card[1])
    elif drawnCard[1] == "10" or card[1] == "Jack" or card[1] == "Queen" or card[1] == "King":
        cardValue = 10
    elif drawnCard[1] == "Ace": #1 or 11 based upon current total
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

def bet(): #Nathan
    while True:  #Min 5, max 1000
        try:
            bet = int(input("Enter a bet between $5 and $1000: $"))
        except ValueError:
            print("Invalid integer entered. Please try again")
            continue
        except Exception:
            print("An unexpected exception occured")
            continue
        if bet < 5 or bet > 1000:
            print("Invalid bet entered. Please enter a bet between $5 and $1000")
            continue
        return bet

def deckOfCards(deck):    #Functional
    hearts = [["Hearts", "2"], ["Hearts" , "3"], ["Hearts", "4"], ["Hearts", "5"], ["Hearts", "6"], ["Hearts" , "7"], ["Hearts", "8"], ["Hearts", "9"],
            ["Hearts", "10"], ["Hearts" , "Jack"], ["Hearts", "Queen"], ["Hearts", "King"], ["Hearts", "Ace"]]
    diamonds = [["Diamonds", "2"], ["Diamonds" , "3"], ["Diamonds", "4"], ["Diamonds", "5"], ["Diamonds", "6"], ["Diamonds" , "7"], ["Diamonds", "8"], ["Diamonds", "9"],
            ["Diamonds", "10"], ["Diamonds" , "Jack"], ["Diamonds", "Queen"], ["Diamonds", "King"], ["Diamonds", "Ace"]]
    clubs = [["Clubs", "2"], ["Clubs" , "3"], ["Clubs", "4"], ["Clubs", "5"], ["Clubs", "6"], ["Clubs" , "7"], ["Clubs", "8"], ["Clubs", "9"],
            ["Clubs", "10"], ["Clubs" , "Jack"], ["Clubs", "Queen"], ["Clubs", "King"], ["Clubs", "Ace"]]
    spades = [["Spades", "2"], ["Spades" , "3"], ["Spades", "4"], ["Spades", "5"], ["Spades", "6"], ["Spades" , "7"], ["Spades", "8"], ["Spades", "9"],
            ["Spades", "10"], ["Spades" , "Jack"], ["Spades", "Queen"], ["Spades", "King"], ["Spades", "Ace"]]
    deck += hearts + diamonds + clubs + spades
    
def hit(): #Daniel
    pass

def stand():
    pass

def play():
    pass

def checkBalance(playerBank):
    print("You have $" + str(playerBank) + " in funds.")
    print()
    
def payout(bet, playerBank, total): #3:2 for 21, 1:1 for no blackjack    Riley
    if total == 21:
        payout = round(bet * 2.5, 2)
    else:
        payout = round(bet * 2, 2)
    playerBank += payout
    return playerBank
        
def mainMenu():
    print("Blackjack")
    print()
    print("1. Play")
    print("2. Check balance")
    print("3. Add funds")
    print("4. Exit")
    print()

def greeting():
    print("Welcome to the Eric Stock Casino!")
    print()

def addFunds(playerBank): #Nick
    while True:
        try:
            added_funds = int(input("How much money would you like to add? (1 - 1000): $"))
            if added_funds < 0 or added_funds > 1000:
                print("Invalid amount entered, try again.")
            else:
                print("Added $" + str(added_funds) + " to your bank.")
                playerBank+=added_funds
                break
        except ValueError:
            print("Invalid integer amount entered, try again.")
    print("You now have $ " +str(playerBank) " in funds.")
    return playerBank

def enterCommand(command, playerBank):
    pass

def setNumberOfPlayers():
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

def main():
    deck = []
    dealerStats = loadDealerStatistics()
    deckOfCards(deck)
    greeting()
    numberOfPlayers = setNumberOfPlayers()
    playerBank = int(input("How much money would you like to enter?: $"))
    print()
    #Testing add funds
    playerBank = addFunds(playerBank)
    checkBalance(playerBank)
    
    mainMenu()
    while True:
        try:
            command = int(input("Choose an option (1-4)"))
            break
        except ValueError:
            print("Invalid option")

if __name__ == "__main__":
    main()
