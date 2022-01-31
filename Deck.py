import random


def shuffle_deck(deck):   # Clears the deck, fills it, and shuffles it for the next game.
    deck.clear()
    deck = deck_of_cards()
    random.shuffle(deck)
    return deck


def deck_of_cards():    # Initializes deck of cards.
    deck = [["Hearts", "2"], ["Hearts", "3"], ["Hearts", "4"], ["Hearts", "5"], ["Hearts", "6"], ["Hearts", "7"],
            ["Hearts", "8"], ["Hearts", "9"], ["Hearts", "10"], ["Hearts", "Jack"], ["Hearts", "Queen"],
            ["Hearts", "King"], ["Hearts", "Ace"], ["Diamonds", "2"], ["Diamonds", "3"], ["Diamonds", "4"],
            ["Diamonds", "5"], ["Diamonds", "6"], ["Diamonds", "7"], ["Diamonds", "8"], ["Diamonds", "9"],
            ["Diamonds", "10"], ["Diamonds", "Jack"], ["Diamonds", "Queen"], ["Diamonds", "King"], ["Diamonds", "Ace"],
            ["Clubs", "2"], ["Clubs", "3"], ["Clubs", "4"], ["Clubs", "5"], ["Clubs", "6"], ["Clubs", "7"],
            ["Clubs", "8"], ["Clubs", "9"], ["Clubs", "10"], ["Clubs", "Jack"], ["Clubs", "Queen"], ["Clubs", "King"],
            ["Clubs", "Ace"], ["Spades", "2"], ["Spades", "3"], ["Spades", "4"], ["Spades", "5"], ["Spades", "6"],
            ["Spades", "7"], ["Spades", "8"], ["Spades", "9"], ["Spades", "10"], ["Spades", "Jack"],
            ["Spades", "Queen"], ["Spades", "King"], ["Spades", "Ace"]]
    return deck
