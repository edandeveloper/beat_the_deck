from deck import init_deck, new_card, DECK
from board import Board
from position import Position
from card import Card

def game() -> None:
    """
    Starts and runs the Beat the Deck game. The player selects a position on the grid
    and guesses whether the next card will be higher or lower than the current card in that position.
    The game continues until the deck is empty or all positions on the grid are out of play.
    """
    init_deck()

    # board can be made bigger for an easier game
    board = Board(3, DECK)
    
    grid_positions: dict[str, Position] = {
        'A': Position(0, 0), 'B': Position(0, 1), 'C': Position(0, 2),
        'D': Position(1, 0), 'E': Position(1, 1), 'F': Position(1, 2), 
        'G': Position(2, 0), 'H': Position(2, 1), 'I': Position(2, 2)
    }
    print("The references for each grid position is as follows:")
    print("|  A |  B |  C |")
    print("|  D |  E |  F |")
    print("|  G |  H |  I |")
    print("----------------")
    board.render_board()

    position: str = input("Select a position on the grid: ")

    while position:
        current_pos: Position = grid_positions.get(position)
        board_card: Card = board.get_card(current_pos)

        # If card is upside down
        if board_card == Card("", -1):
            print("This position is no longer in play.")
            position = input("Select a position on the grid: ")
            continue
        
        decision: str = input("Higher (h) or lower (l)? ")
        card: Card = new_card()
    
        if decision == "h":
            if card > board_card:
                board.set_card(card, current_pos)
            else:
                # Set an upside down card
                board.set_card(Card(" #", -1), current_pos)
        elif decision == "l":
            if card < board_card:
                board.set_card(card, current_pos)
            else:
                board.set_card(Card(" #", -1), current_pos)

        board.render_board()
        print(f"Your card is {str(card).strip()}.")
        print(f"You have {len(DECK)} cards left.")

        if len(DECK) == 0:
            print("You beat the deck!")
            break

        # If all cards are upside down
        if not board.valid_board():
            print("Game Over")
            break

        position = input("Select a position on the grid: ")

if __name__ == "__main__":
    game()
