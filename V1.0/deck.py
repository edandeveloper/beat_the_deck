import random
from card import Card

DECK: list[Card] = []

def init_deck(number=1) -> None:
    """
    Initializes the deck of cards by creating a numbger of standard 52-card decks
    with 4 suits and shuffles it. Clears the global DECK list before adding new cards.

    Args:
        number (int): The number of decks in the game. Default value of 1. 
    """
    global DECK
    DECK.clear()
    for _ in range(number):
        for _ in range(4):
            DECK.append(Card(" 2", 2))
            DECK.append(Card(" 3", 3))
            DECK.append(Card(" 4", 4))
            DECK.append(Card(" 5", 5))
            DECK.append(Card(" 6", 6))
            DECK.append(Card(" 7", 7))
            DECK.append(Card(" 8", 8))
            DECK.append(Card(" 9", 9))
            DECK.append(Card("10", 10))
            DECK.append(Card(" J", 11))
            DECK.append(Card(" Q", 12))
            DECK.append(Card(" K", 13))
            DECK.append(Card(" A", 14))

    random.shuffle(DECK)

def new_card() -> Card:
    """
    Draws a random card from the DECK and removes it from the deck.

    Returns:
        Card: The drawn card.
    """
    random_integer = random.randint(0, len(DECK) - 1)
    card = DECK[random_integer]
    DECK.remove(card)
    return card
