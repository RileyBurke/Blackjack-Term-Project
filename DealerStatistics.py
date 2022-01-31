import sys


def load_dealer_statistics():  # Loads the dealer statistics file to a list to be appended to.
    dealer_stats = []
    try:
        with open("dealer_stats.txt") as file:
            for row in file:
                row = row.replace("\n", "")
                dealer_stats.append(row)
    except FileNotFoundError:
        pass
    except OSError:
        print("File found - error reading the file - closing program")
        sys.exit()
    return dealer_stats


def save_dealer_statistics(dealer_stats):  # Saves the amount the dealer makes to a text file after each game.
    try:
        with open("dealer_stats.txt", "w") as file:
            for stats in dealer_stats:
                file.write(str(stats) + "\n")
    except OSError:
        print("An unexpected exception occurred - closing program")
        sys.exit()
