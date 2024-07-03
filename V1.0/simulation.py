from deck import init_deck, new_card, DECK
from board import Board
from position import Position
from card import Card
from probability import best_chance

def find_best_position(board: Board) -> Position:
    """
    Find the best position on the board based on the highest probability of success.

    Args:
        board (Board): The Board object representing the game board.

    Returns:
        Position: The Position object representing the best position on the board.
    """
    chances = []
    for row in board.get_board():
        # Finds the best chances for each card on the board
        # If face down, the best chance of the card is 0 for calculation purposes
        # The "h" in (0, "h") is irrelevant, it could be any string
        chances.append([best_chance(card) if card != Card("", -1) else (0, "h") for card in row])

    max_chance = 0
    max_chance_position = Position(0, 0)
    for r in range(len(chances)):
        for c in range(len(chances[0])):
            if chances[r][c][0] > max_chance:
                max_chance = chances[r][c][0]
                max_chance_position = Position(r, c)
    
    return max_chance_position

def find_best_decision(board: Board) -> str:
    """
    Determine the best decision ('h' for higher, 'l' for lower) based on the best position on the board.

    Args:
        board (Board): The Board object representing the game board.

    Returns:
        str: The recommended action ('h' for higher, 'l' for lower).
    """
    return best_chance(board.get_card(find_best_position(board)))[1]

def run_simulation() -> int:
    """
    Run a single simulation of the game.

    Returns:
        int: 1 if the simulation wins (all cards drawn successfully), 0 otherwise.
    """

    # The number of decks can be adjusted by inserting an integer in the function
    init_deck()

    # board dimensions can be changed to investigate how it improves win rate
    board = Board(3, DECK)
    
    while True:
        position = find_best_position(board)
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

def many_simulations(runs: int):
    """
    Run multiple simulations of the game and print the number of winning simulations.

    Args:
        runs (int): The number of simulations to run.
    """
    wins = 0
    for _ in range(runs):
        wins += run_simulation()
    
    print(f"Out of {runs} simulations, {wins} simulations won.")
    print(f"That is a win rate of {wins/runs * 100}%")

