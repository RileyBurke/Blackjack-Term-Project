import sys

def loadDealerStatistics(): #Loads the dealer statistics file to a list to be appended to.
    dealerStats = []
    try:
        with open ("dealerStats.txt") as file:
            for row in file:
                row = row.replace("\n","")
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

def saveDealerStatistics(dealerStats): #Saves the amount the dealer makes to a text file after each game.
    try:
        with open("dealerStats.txt", "w") as file:
            for stats in dealerStats:
                file.write(str(stats) + "\n")
    except Exception:
        print("An unexpected exception occured - closing program")
        sys.exit()
