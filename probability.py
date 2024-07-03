from typing import List, Tuple
from deck import DECK  # Assuming DECK is imported correctly from deck module
from card import Card  # Assuming Card class is imported correctly from card module

def calculate_higher(card: Card) -> float:
    """
    Calculate the probability of drawing a card higher than the given card.

    Args:
        card (Card): The Card object to compare against.

    Returns:
        float: The probability of drawing a higher card, calculated as the ratio
               of higher cards to the total cards in the deck.
    """
    higher_cards = [c for c in DECK if c > card]
    return len(higher_cards) / len(DECK)

def calculate_lower(card: Card) -> float:
    """
    Calculate the probability of drawing a card lower than the given card.

    Args:
        card (Card): The Card object to compare against.

    Returns:
        float: The probability of drawing a lower card, calculated as the ratio
               of lower cards to the total cards in the deck.
    """
    lower_cards = [c for c in DECK if c < card]
    return len(lower_cards) / len(DECK)

def best_chance(card: Card) -> Tuple[float, str]:
    """
    Determine the best chance between drawing a higher or lower card compared to
    the given card.

    Args:
        card (Card): The Card object to compare against.

    Returns:
        Tuple[float, str]: A tuple containing the probability and the recommended
                           action ('h' for higher, 'l' for lower).
    """
    higher_prob = calculate_higher(card)
    lower_prob = calculate_lower(card)
    if higher_prob >= lower_prob:
        return higher_prob, "h"
    else:
        return lower_prob, "l"
