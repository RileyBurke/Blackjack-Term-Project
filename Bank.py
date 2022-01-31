def set_player_banks(number_of_players):  # Sets the initial values for the bank of each player.
    player_banks = [0] * number_of_players
    counter = 0
    for _ in player_banks:
        while True:
            try:
                player_banks[counter] = int(input("How much money would you like to enter for player " +
                                                  str(counter + 1) + "?: $"))
                if player_banks[counter] >= 5:
                    counter += 1
                    break
                else:
                    print("Not enough money to place a bet.")
            except ValueError:
                print("Invalid amount, please try again.")
    return player_banks


def add_funds(player_banks, player_number):
    # Add funds to player banks. If chosen in menu it gives an option to choose player.
    # If player runs out of money in game it chooses the player for you before you can bet.
    print()
    while True:
        if len(player_banks) > 1 and player_number == 0:
            try:
                player_number = int(input("Enter which player to add funds to (1-" + str(len(player_banks)) + "): "))
            except ValueError:
                print("Invalid player number. Try again.")
                print()
                continue
        elif len(player_banks) >= player_number > 0 or len(player_banks) == 1:
            if len(player_banks) == 1:
                player_number = 1
            try:
                added_amount = int(input("How much money would you like to add?: $"))
                if added_amount < 0:
                    print("Invalid amount entered, try again.")
                else:
                    player_banks[player_number - 1] += added_amount
                    print("Added $" + str(added_amount) + " to your bank.")
                    break
            except ValueError:
                print("Invalid integer amount entered.")
                print()
        else:
            print("Invalid player number. Try again.")
            print()
            continue
    print("You now have $" + str(player_banks[player_number - 1]) + " in funds.")
    print()


def check_balance(player_banks):  # Allows players to check their balance from the main menu.
    print()
    while True:
        if len(player_banks) > 1:
            try:
                player_number = int(input("Enter number of player to check (1-" + str(len(player_banks)) + "): "))
            except ValueError:
                print("Invalid player number. Try again.")
                print()
                continue
        else:
            player_number = 1
        if len(player_banks) >= player_number > 0:
            print("You have $" + str(player_banks[player_number - 1]) + " in funds.")
            print()
            break
        else:
            print("Invalid player number. Try again.")
            print()
            continue
