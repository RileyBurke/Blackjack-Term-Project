import random
import Deck
import DealerStatistics
import Bank


def get_card_value(drawn_card, total):  # Returns the number value of a card drawn from the deck.
    if drawn_card[1] == "2" or drawn_card[1] == "3" or drawn_card[1] == "4" or drawn_card[1] == "5" \
            or drawn_card[1] == "6" or drawn_card[1] == "7" or drawn_card[1] == "8" or drawn_card[1] == "9":
        card_value = int(drawn_card[1])
    elif drawn_card[1] == "10" or drawn_card[1] == "Jack" or drawn_card[1] == "Queen" or drawn_card[1] == "King":
        card_value = 10
    else:  # Ace
        if total >= 11:  # Returns 11 for an Ace's value unless it would cause you to lose, in that case returns a 1.
            card_value = 1
        else:
            card_value = 11
    return card_value


def get_bets(player_banks, number_of_players):  # Accept bets from each player.
    player_bets = [0] * number_of_players
    counter = 0
    for _ in player_bets:
        while True:
            try:
                player_bets[counter] = int(input("Player " + str(counter + 1) +
                                                 " - How much money would you like to bet?: $"))
                if player_bets[counter] < 5 or player_bets[counter] > 1000:
                    print("Invalid bet entered. Please enter a bet between $5 and $1000")
                    continue
                elif player_bets[counter] > player_banks[counter]:
                    if player_banks[counter] >= 5:
                        print("Not enough funds. You have $" + str(player_banks[counter]) + ".")
                        continue
                    else:
                        print("Not enough funds. You have $" + str(player_banks[counter]) + ".")
                        Bank.add_funds(player_banks, counter + 1)
                        continue
                else:
                    player_banks[counter] -= player_bets[counter]
                    counter += 1
                    break
            except ValueError:
                print("Invalid integer entered. Please try again")
                print()
    print()
    return player_bets


def payout(player_bets, player_banks, player_totals, counter):
    # Pays out winnings to winning players. Rewards 3:2 for blackjack and 1:1 otherwise.
    if player_totals == 21:
        winnings = round(player_bets * 2.5, 2)
    else:
        winnings = round(player_bets * 2, 2)
    player_banks[counter] += winnings
    print("Bet: $" + str(player_bets) + "  Winnings: $" + str(winnings) + "  New total: $" + str(player_banks[counter]))
    return winnings


def hit_player(deck, total, counter, turn_number, flag, player_hands):  # Adds a card to the players hand.
    while True:
        player_card = random.choice(deck)
        print("Player " + str(counter + 1) + " has drawn a " + player_card[1] + " of " + player_card[0] + ".")
        card_value = get_card_value(player_card, total)
        deck.remove(player_card)
        total += card_value
        player_hands[counter].append(card_value)
        if turn_number == 1:
            return total
        else:
            if total == 21:
                flag = False
            elif total > 21:
                flag = False
                for card in player_hands[counter]:
                    if card == 11:
                        player_hands[counter].remove(11)
                        player_hands[counter].append(1)
                        total -= 10
                        flag = True
                        break
            return total, flag


def hit_dealer(deck, dealer_total, turn_number, dealer_active, dealer_hand):  # Adds a card to the dealers hand.
    if turn_number == 1:
        player_card = random.choice(deck)
        print("The dealer has drawn a " + player_card[1] + " of " + player_card[0] + ".")
        print()
        card_value = get_card_value(player_card, dealer_total)
        deck.remove(player_card)
        dealer_total += card_value
        dealer_hand.append(card_value)
        return dealer_total
    else:
        while True:
            if dealer_total < 17:  # Dealer must hit if total is less than 17.
                dealer_card = random.choice(deck)
                print("The dealer has drawn a " + dealer_card[1] + " of " + dealer_card[0] + ".")
                card_value = get_card_value(dealer_card, dealer_total)
                deck.remove(dealer_card)
                dealer_total += card_value
                dealer_hand.append(card_value)
                if dealer_total < 21:
                    print("Total is now " + str(dealer_total) + ".")
                    print()
                return dealer_total, dealer_active
            elif dealer_total == 21:
                print("Total is now " + str(dealer_total) + ".")
                print("Dealer has blackjack.")
                print()
                dealer_active = False
                return dealer_total, dealer_active
            elif dealer_total > 21:
                dealer_active = False
                for card in dealer_hand:
                    if card == 11:
                        dealer_hand.remove(11)
                        dealer_hand.append(1)
                        dealer_total -= 10
                        print("Total is now " + str(dealer_total) + ".")
                        print()
                        dealer_active = True
                        break
                if dealer_total > 21:  # Checks again in case of Ace changing from 11 to 1.
                    print("Total is now " + str(dealer_total) + ".")
                    print("Dealer has busted out.")
                    print()
                return dealer_total, dealer_active
            else:
                print("Dealer stands with " + str(dealer_total) + ".")
                print()
                dealer_active = False
                return dealer_total, dealer_active


def play_game(deck, player_banks, number_of_players):  # Main blackjack function.
    dealer_stats = DealerStatistics.load_dealer_statistics()
    print()
    choice = "y"
    while choice.lower() == "y":
        player_totals = [0] * number_of_players
        player_hands = []
        for _ in player_totals:
            player_hands.append([])
        dealer_hand = []
        player_flags = [True] * number_of_players
        players_active = True
        dealer_active = True
        dealer_total = 0
        turn_number = 1
        counter = 0
        player_bets = get_bets(player_banks, number_of_players)
        while players_active:
            while counter < len(player_totals):  # Loops through each player for a given turn
                if turn_number == 2:  # Turn number 2
                    player_totals[counter], player_flags[counter] = \
                        hit_player(deck, player_totals[counter], counter, turn_number, player_flags[counter],
                                   player_hands)
                    print("Total is now " + str(player_totals[counter]) + ".")
                    if player_totals[counter] == 21:
                        print("Player " + str(counter + 1) + " has blackjack!")
                    print()
                    counter += 1
                elif turn_number > 2:  # Turn >2, gives hit/stand options.
                    if player_flags[counter]:
                        game_options(deck, player_totals, counter, turn_number, player_flags, player_hands)
                        if player_flags[counter]:
                            print("Total is now " + str(player_totals[counter]) + ".")
                        else:
                            if player_totals[counter] == 21:
                                print("Total is now " + str(player_totals[counter]) + ".")
                                print("Player " + str(counter + 1) + " has blackjack!")
                            elif player_totals[counter] > 21:
                                print("Total is now " + str(player_totals[counter]) + ".")
                                print("Player " + str(counter + 1) + " has busted out.")
                            else:
                                print("Standing at " + str(player_totals[counter]) + ".")
                        print()
                        counter += 1
                    else:
                        counter += 1
                elif counter == len(player_totals):
                    break
                else:  # Turn number 1
                    player_totals[counter] = hit_player(deck, player_totals[counter], counter, turn_number,
                                                        player_flags[counter], player_hands)
                    print()
                    counter += 1
            if turn_number == 1:
                dealer_total = hit_dealer(deck, dealer_total, turn_number, dealer_active, dealer_hand)
            turn_number += 1
            counter = 0
            if not any(player_flags):  # Checks for any True flags, if all flags are false the game will end.
                players_active = False

        while dealer_active:
            dealer_total, dealer_active = hit_dealer(deck, dealer_total, turn_number, dealer_active, dealer_hand)

        payout_counter = 0
        dealer_winnings = 0
        for total in player_totals:
            if total == 21 and dealer_total != 21:  # Player wins with blackjack
                print("Player " + str(payout_counter + 1) + " has blackjack!")
                dealer_winnings -= payout(player_bets[payout_counter], player_banks, total, payout_counter)
            elif total == 21 and dealer_total == 21:  # Player and dealer tie with blackjack
                print("Player " + str(payout_counter + 1) + ": Tied dealer, bet returned.")
                player_banks[payout_counter] += player_bets[payout_counter]
            elif total > 21:  # Player busts
                print("Player " + str(payout_counter + 1) + " has busted out.")
                dealer_winnings += player_bets[payout_counter]
            elif total < 21:
                if dealer_total == total:  # Player and dealer tie
                    print("Player " + str(payout_counter + 1) + ": Tied dealer, bet returned.")
                    player_banks[payout_counter] += player_bets[payout_counter]
                elif 21 >= dealer_total > total:  # Dealer wins with higher score
                    print("Player " + str(payout_counter + 1) + ": Dealer wins.")
                    dealer_winnings += player_bets[payout_counter]
                else:  # Player wins with higher score
                    print("Player " + str(payout_counter + 1) + " wins.")
                    dealer_winnings -= payout(player_bets[payout_counter], player_banks, total, payout_counter)
            payout_counter += 1
            print()

        dealer_hand.clear()
        player_hands.clear()
        dealer_stats.append(dealer_winnings)
        DealerStatistics.save_dealer_statistics(dealer_stats)
        deck = Deck.shuffle_deck(deck)
        choice = input("Play again? (y/n): ")
        print()
    main_menu()
    return deck


def game_options(deck, player_totals, counter, turn_number, player_flags, player_hands):
    # Gives players the option to hit or stand.
    print("Player " + str(counter + 1) + " - Total: " + str(player_totals[counter]))
    while True:
        option = input("Hit or Stand: ")
        if option.title() == "Hit":
            player_totals[counter], player_flags[counter] = hit_player(deck, player_totals[counter], counter,
                                                                       turn_number, player_flags[counter], player_hands)
            if player_totals[counter] == 21:
                player_flags[counter] = False
                break
            elif player_totals[counter] > 21:
                player_flags[counter] = False
                break
            else:
                print("Total is now " + str(player_totals[counter]) + ".")
                print()
                continue
        elif option.title() == "Stand":
            player_flags[counter] = False
            break
        else:
            print("Invalid option.")
            continue


def main_menu():  # Prints menu options.
    print("1. Play")
    print("2. Check balance")
    print("3. Add funds")
    print("4. Exit")
    print()


def greeting():  # Prints initial greeting.
    print("Welcome to the Eric Stock Casino!")
    print()
    print("Blackjack")
    print()


def enter_command(deck, player_banks, number_of_players):  # Accept commands to navigate through the menu.
    main_menu()
    while True:
        try:
            command = int(input("Choose an option (1-4): "))
            if command == 1:
                deck = play_game(deck, player_banks, number_of_players)
            elif command == 2:
                Bank.check_balance(player_banks)
            elif command == 3:
                Bank.add_funds(player_banks, 0)
            elif command == 4:
                break
            else:
                print("Not a valid command.")
                print()
                continue
        except ValueError:
            print("Invalid option")
            print()


def set_number_of_players():  # Sets the number of players to play the game.
    while True:
        try:
            number_of_players = int(input("How many players? (1-5): "))
            if 0 < number_of_players < 6:
                print()
                return number_of_players
            else:
                print("Invalid number of players. Must be a number from 1 to 5.")
                print()
                continue
        except ValueError:
            print("Invalid number of players. Must be a number from 1 to 5.")


def main():
    deck = Deck.deck_of_cards()
    greeting()
    number_of_players = set_number_of_players()
    player_banks = Bank.set_player_banks(number_of_players)
    print()
    enter_command(deck, player_banks, number_of_players)
    print("Bye!")


if __name__ == "__main__":
    main()
