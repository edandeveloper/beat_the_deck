from BeatTheDeck import *

def calculate_higher(card):
    if len(DECK) == 0:
        return 0
    higher_cards = []
    for c in DECK:
        if c > card:
            higher_cards.append(c)
    pr = len(higher_cards)/len(DECK)
    return pr

def calculate_lower(card):
    if len(DECK) == 0:
        return 0
    lower_cards = []
    for c in DECK:
        if c < card:
            lower_cards.append(c)
    pr = len(lower_cards)/len(DECK)
    return pr

def best_chance(card):
    if calculate_higher(card) >= calculate_lower(card):
        return calculate_higher(card), "h"
    elif calculate_higher(card) < calculate_lower(card):
        return calculate_lower(card), "l"

def find_best_position(board):
    chances = []
    for row in board.get_board():
        chances.append([best_chance(card) if card != Card("", -1) else (0, "h") for card in row])

    max_chance = 0
    max_chance_position = Position(0, 0)
    for r in range(len(chances)):
        for c in range(len(chances[0])):
            if chances[r][c][0] > max_chance:
                max_chance = chances[r][c][0]
                max_chance_position = Position(r, c)
    
    return max_chance_position

def find_best_decision(board):
    return best_chance(board.get_card(find_best_position(board)))[1]


def run_simulation():
    init_deck(DECK)
    board = Board(3)

    position = find_best_position(board)

    while position:
        
        board_card = board.get_card(position)
        decision = find_best_decision(board)
        card = new_card()
    
        if decision == "h":
            if card > board_card:
                board.set_card(card, position)
            else:
                board.set_card(Card(" #", -1), position)

        elif decision == "l":
            if card < board_card:
                board.set_card(card, position)
            else:
                board.set_card(Card(" #", -1), position)

        if len(DECK) == 0:
            return 1

        if not board.valid_board():
            return 0

        position = find_best_position(board)

def many_simulations(runs):
    wins = 0
    for _ in range(runs):
        wins += run_simulation()
    
    print(f"Out of {runs} simulations, {wins} simulations won.")


if __name__ == "__main__":
    many_simulations(100)