import random
import sys
import Deck
import DealerStatistics
import Bank

def getCardValue(drawnCard, total): #Returns the number value of a card drawn from the deck.
    if drawnCard[1] == "2" or drawnCard[1] == "3" or drawnCard[1] == "4" or drawnCard[1] == "5" or drawnCard[1] == "6" or drawnCard[1] == "7" or drawnCard[1] == "8" or drawnCard[1] == "9":
        cardValue = int(drawnCard[1])
    elif drawnCard[1] == "10" or drawnCard[1] == "Jack" or drawnCard[1] == "Queen" or drawnCard[1] == "King":
        cardValue = 10
    elif drawnCard[1] == "Ace":
        if total >= 11:       #Returns 11 for an Ace's value unless it would cause you to lose, in that case returns a 1.
            cardValue = 1
        else:
            cardValue = 11
    return cardValue

def getBets(playerBanks, numberOfPlayers): #Accepts bets from each player.
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
                    if playerBanks[counter] >= 5:
                        print("Not enough funds. You have $" + str(playerBanks[counter]))
                        continue
                    else:
                        print("Not enough funds. You have $" + str(playerBanks[counter]))
                        Bank.addFunds(playerBanks, counter+1)
                        continue
                else:
                    playerBanks[counter] -= playerBets[counter]
                    counter += 1
                    break
            except ValueError:
                print("Invalid integer entered. Please try again")
                print()
    print()
    return playerBets

def payout(playerBets, playerBanks, playerTotals, counter): #Pays out winnings to winning players. Rewards 3:2 for blackjack and 1:1 otherwise.
    if playerTotals == 21:
        payout = round(playerBets * 2.5, 2)
    else:
        payout = round(playerBets * 2, 2)
    playerBanks[counter] += payout
    print("Bet: $" + str(playerBets) + "  Winnings: $" + str(payout) + "  New total: $" + str(playerBanks[counter]))
    return payout
    
def hitPlayer(deck, total, counter, turnNumber, flag): #Adds a card to the players hand.
    while True:
        if turnNumber == 1:
            player_card = random.choice(deck)
            print("Player " + str(counter + 1) + " has drawn a " + player_card[1] + " of " + player_card[0] + ".")
            cardValue = getCardValue(player_card, total)
            deck.remove(player_card)
            total += cardValue
            return total
        else:
            player_card = random.choice(deck)
            print("Player " + str(counter + 1) + " has drawn a " + player_card[1] + " of " + player_card[0] + ".")
            cardValue = getCardValue(player_card, total)
            deck.remove(player_card)
            total += cardValue
            if total == 21:
                flag = False
            elif total > 21:
                flag = False
            return total, flag

def hitDealer(deck, dealerTotal, turnNumber, dealerActive): #Adds a card to the dealers hand.
    if turnNumber == 1:
        player_card = random.choice(deck)
        print("The dealer has drawn a " + player_card[1] + " of " + player_card[0] + ".")
        print()
        cardValue = getCardValue(player_card, dealerTotal)
        deck.remove(player_card)
        dealerTotal += cardValue
        return dealerTotal
    else:
        while True:
            if dealerTotal < 17: #Dealer must hit if total is less than 17.
                player_card = random.choice(deck)
                print("The dealer has drawn a " + player_card[1] + " of " + player_card[0] + ".")
                cardValue = getCardValue(player_card, dealerTotal)
                deck.remove(player_card)
                dealerTotal += cardValue
                print("Total is now " + str(dealerTotal) + ".")
                print()
                return dealerTotal, dealerActive
            elif dealerTotal == 21:
                print("Dealer has blackjack.")
                print()
                dealerActive = False
                return dealerTotal, dealerActive
            elif dealerTotal > 21:
                print("Dealer has busted out.")
                print()
                dealerActive = False
                return dealerTotal, dealerActive
            else:
                print("Dealer stands with " + str(dealerTotal) + ".")
                print()
                dealerActive = False
                return dealerTotal, dealerActive

def playGame(deck, playerBanks, numberOfPlayers): #Main blackjack function.
    dealerStats = DealerStatistics.loadDealerStatistics()
    print()
    choice = "y"
    while choice.lower() == "y":
        playerTotals = [0] * numberOfPlayers
        playerFlags = [True] * numberOfPlayers
        playersActive = True
        dealerActive = True
        dealerTotal = 0
        turnNumber = 1
        counter = 0
        playerBets = getBets(playerBanks, numberOfPlayers)
        while playersActive == True:
            while counter < len(playerTotals): #Loops through each player for a given turn
                if turnNumber == 2:            #Turn number 2
                    playerTotals[counter], playerFlags[counter] = hitPlayer(deck, playerTotals[counter], counter, turnNumber, playerFlags[counter])
                    print("Total is now " + str(playerTotals[counter]) + ".")
                    if playerTotals[counter] == 21:
                        print("Player " + str(counter + 1) + " has blackjack!")
                    print()
                    counter += 1
                elif turnNumber > 2:           #Turn >2, gives hit/stand options.
                    if playerFlags[counter] == True:
                        gameOptions(deck, playerTotals, counter, turnNumber, playerBanks, playerBets, playerFlags)
                        if playerFlags[counter] == True:
                            print("Total is now " + str(playerTotals[counter]) + ".")
                        else:
                            if playerTotals[counter] == 21:
                                print("Total is now " + str(playerTotals[counter]) + ".")
                                print("Player " + str(counter + 1) + " has blackjack!")
                            elif playerTotals[counter] > 21:
                                print("Total is now " + str(playerTotals[counter]) + ".")
                                print("Player " + str(counter + 1) + " has busted out.")
                            else:
                                print("Standing at " + str(playerTotals[counter]) + ".")
                        print()
                        counter += 1
                    else:
                        counter += 1
                elif counter == len(playerTotals):
                    break
                else:                #Turn number 1
                    playerTotals[counter] = hitPlayer(deck, playerTotals[counter], counter, turnNumber, playerFlags[counter])
                    print()
                    counter += 1
            if turnNumber == 1:
                dealerTotal = hitDealer(deck, dealerTotal, turnNumber, dealerActive)
            turnNumber += 1
            counter = 0
            if not any(playerFlags): #Checks for any True flags, if all flags are false the game will end.
                playersActive = False
                
        while dealerActive == True:
            dealerTotal, dealerActive = hitDealer(deck, dealerTotal, turnNumber, dealerActive)

        payoutCounter = 0
        dealerWinnings = 0
        for total in playerTotals:
            if total == 21 and dealerTotal != 21:                             #Player wins with blackjack
                print("Player " + str(payoutCounter + 1) + " has blackjack!")
                dealerWinnings -= payout(playerBets[payoutCounter], playerBanks, total, payoutCounter)
            elif total == 21 and dealerTotal == 21:                           #Player and dealer tie with blackjack
                print("Player " + str(payoutCounter + 1) + ": Tied dealer, bet returned.")
                playerBanks[payoutCounter] += playerBets[payoutCounter]
            elif total > 21:                                                  #Player busts
                print("Player " + str(payoutCounter + 1) + " has busted out.")
                dealerWinnings += playerBets[payoutCounter]
            elif total < 21:
                if dealerTotal == total:                                      #Player and dealer tie
                    print("Player " + str(payoutCounter + 1) + ": Tied dealer, bet returned.")
                    playerBanks[payoutCounter] += playerBets[payoutCounter]
                elif dealerTotal <= 21 and dealerTotal > total:               #Dealer wins with higher score
                    print("Player " + str(payoutCounter + 1) + ": Dealer wins.")
                    dealerWinnings += playerBets[payoutCounter]
                else:                                                         #Player wins with higher score
                    print("Player " + str(payoutCounter + 1) + " wins.")
                    dealerWinnings -= payout(playerBets[payoutCounter], playerBanks, total, payoutCounter)
            payoutCounter += 1
            print()

        dealerStats.append(dealerWinnings)
        DealerStatistics.saveDealerStatistics(dealerStats)        
        deck = Deck.shuffleDeck(deck)
        choice = input("Play again? (y/n): ")
        print()
    mainMenu()
    return deck

def gameOptions(deck, playerTotals, counter, turnNumber, playerBanks, playerBets, playerFlags): #Gives players the option to hit or stand.
    print("Player " + str(counter + 1) + " - Total: " + str(playerTotals[counter]))
    while True:
        option = input("Hit or Stand: ")
        if option.title() == "Hit":
            playerTotals[counter], playerFlags[counter] = hitPlayer(deck, playerTotals[counter], counter, turnNumber, playerFlags[counter])
            if playerTotals[counter] == 21:
                playerFlags[counter] = False
                break
            elif playerTotals[counter] > 21:
                playerFlags[counter] = False
                break
            else:
                print("Total is now " + str(playerTotals[counter]) + ".")
                print()
                continue
        elif option.title() == "Stand":
            playerFlags[counter] = False
            break
        else:
            print("Invalid option.")
            continue       
        
def mainMenu(): #Prints menu options.
    print("1. Play")
    print("2. Check balance")
    print("3. Add funds")
    print("4. Exit")
    print()

def greeting(): #Prints initial greeting.
    print("Welcome to the Eric Stock Casino!")
    print()
    print("Blackjack")
    print()

def enterCommand(deck, playerBanks, numberOfPlayers): #Accepts commands to navigate through the menu.
    mainMenu()
    while True:
        try:
            command = int(input("Choose an option (1-4): "))
            if command == 1:
                deck = playGame(deck, playerBanks, numberOfPlayers)
            elif command == 2:
                Bank.checkBalance(playerBanks) 
            elif command == 3:
                Bank.addFunds(playerBanks, 0)
            elif command == 4:
                break
            else:
                print("Not a valid command.")
                print()
                continue
        except ValueError:
            print("Invalid option")
            print()

def setNumberOfPlayers(): #Sets the number of players to play the game.
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

def main():
    deck = Deck.deckOfCards()
    greeting()
    numberOfPlayers = setNumberOfPlayers()
    playerBanks = Bank.setPlayerBanks(numberOfPlayers)
    print()
    enterCommand(deck, playerBanks, numberOfPlayers)
    print("Bye!")
    
if __name__ == "__main__":
    main()
