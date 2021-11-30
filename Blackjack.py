import random
import csv

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

def bet(): 
    pass #Min 5, max 1000

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
    
def hitMe():
    pass

def play():
    pass

def checkBalance(playerBank):
    print("You have $" + str(playerBank) + " in funds.")
    print()
    
def payout():
    pass

def test():
    pass

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

def addFunds(playerBank):
    pass

def enterCommand(command):
    pass

def main():
    deck = []
    dealerStats = loadDealerStatistics()
    deckOfCards(deck)
    greeting()
    playerBank = int(input("How much money would you like to enter?: $"))
    print()
    mainMenu()
    while True:
        try:
            command = int(input("Choose an option (1-4)"))
            break
        except ValueError:
            print("Invalid option")

                    
    
    print(deck)         #Testing deck
    print(len(deck))
    shuffleDeck(deck)
    print(deck)

if __name__ == "__main__":
    main()
