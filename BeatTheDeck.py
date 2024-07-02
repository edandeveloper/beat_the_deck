import random

DECK = []

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.get_value()

    def __ne__(self, other):
        return self.value != other.get_value()

    def __repr__(self):
        return self.name

    def __gt__(self, other):
        return self.value > other.get_value()

    def __lt__(self, other):
        return self.value < other.get_value()

    def __ge__(self, other):
        return self.value >= other.get_value()

    def __le__(self, other):
        return self.value <= other.get_value()

class Board:
    board = []

    def __init__(self, dimensions):
        self.board = []
        for _ in range(dimensions):
            row = []
            for _ in range(dimensions):
                random_integer = random.randint(0, len(DECK) - 1)
                card = DECK[random_integer]
                DECK.remove(card)
                row.append(card)
            self.board.append(row)

    def get_board(self):
        return self.board

    def get_card(self, position):
        return self.board[position.get_row()][position.get_column()]

    def set_card(self, card, position):
        self.board[position.get_row()][position.get_column()] = card

    def valid_board(self):
        for row in self.board:
            for card in row:
                if card != Card("", -1):
                    return True
        return False

    def render_board(self):
        print("----------------")
        display = ""
        for row in self.board:
            display += "| "
            for card in row:
                display += f"{str(card)} | "
            display += "\n"

        print(display)
        print("----------------")

    

def init_deck(deck):
    deck.clear()
    for i in range(4):
        deck.append(Card(" 2", 2))
        deck.append(Card(" 3", 3))
        deck.append(Card(" 4", 4))
        deck.append(Card(" 5", 5))
        deck.append(Card(" 6", 6))
        deck.append(Card(" 7", 7))
        deck.append(Card(" 8", 8))
        deck.append(Card(" 9", 9))
        deck.append(Card("10", 10))
        deck.append(Card(" J", 11))
        deck.append(Card(" Q", 12))
        deck.append(Card(" K", 13))
        deck.append(Card(" A", 14))

    random.shuffle(deck)

def new_card():
    random_integer = random.randint(0, len(DECK) - 1)
    card = DECK[random_integer]
    DECK.remove(card)
    return card
        
class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column

    def __repr__(self):
        return f"({self.row}, {self.column})"


def game():
    init_deck(DECK)
    board = Board(3)
    grid_positions = {
        'A' : Position(0, 0), 'B' : Position(0, 1), 'C' : Position(0, 2),
        'D' : Position(1, 0), 'E' : Position(1, 1), 'F' : Position(1, 2), 
        'G' : Position(2, 0), 'H' : Position(2, 1), 'I' : Position(2, 2)
        }
    print("The references for each grid position is as follows:")
    print("|  A |  B |  C |")
    print("|  D |  E |  F |")
    print("|  G |  H |  I |")
    print("----------------")
    board.render_board()
 
    position = input("Select a position on the grid: ")

    while position:
        
        current_pos = grid_positions.get(position)
        board_card = board.get_card(current_pos)

        # If card is upside down
        if board_card == Card("", -1):
            print("This position is no longer in play.")
            position = input("Select a position on the grid: ")
            continue

        card = new_card()
        decision = input("Higher (h) or lower (l)? ")
    
        if decision == "h":
            if card > board_card:
                board.set_card(card, current_pos)
            else:
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

        if not board.valid_board():
            print("Game Over")
            break

        position = input("Select a position on the grid: ")

        


if __name__ == "__main__":        
    game()



