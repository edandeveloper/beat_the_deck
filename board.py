import random
from typing import List
from card import Card
from position import Position

class Board:
    """
    Represents the game board for Beat the Deck. 

    Attributes:
        board (List[List[Card]]): A 2D list representing the board with cards.
    """

    board: List[List[Card]] = []

    def __init__(self, dimensions: int, deck: List[Card]):
        """
        Initializes the game board with the given dimensions and a deck of cards.

        Args:
            dimensions (int): The dimensions of the board (e.g., 3 for a 3x3 board).
            deck (List[Card]): The deck of cards to draw from to fill the board.
        """
        self.board = []
        for _ in range(dimensions):
            row = []
            for _ in range(dimensions):
                random_integer = random.randint(0, len(deck) - 1)
                card = deck[random_integer]
                deck.remove(card)
                row.append(card)
            self.board.append(row)

    def get_board(self) -> List[List[Card]]:
        """
        Returns the current state of the board.

        Returns:
            List[List[Card]]: The 2D list representing the board with cards.
        """
        return self.board

    def get_card(self, position: Position) -> Card:
        """
        Gets the card at the specified position on the board.

        Args:
            position (Position): The position of the card on the board.

        Returns:
            Card: The card at the specified position.
        """
        return self.board[position.get_row()][position.get_column()]

    def set_card(self, card: Card, position: Position) -> None:
        """
        Sets the card at the specified position on the board.

        Args:
            card (Card): The card to place on the board.
            position (Position): The position on the board to place the card.
        """
        self.board[position.get_row()][position.get_column()] = card

    def valid_board(self) -> bool:
        """
        Checks if the board has any valid (not flipped) cards left.

        Returns:
            bool: True if there are valid cards, False otherwise.
        """
        for row in self.board:
            for card in row:
                # Checks if the card is not flipped over
                if card != Card("", -1):
                    return True
        return False

    def render_board(self) -> None:
        """
        Renders the board to the console, displaying the current state of all cards.
        """
        print("----------------")
        display = ""
        for row in self.board:
            display += "| "
            for card in row:
                display += f"{str(card)} | "
            display += "\n"

        print(display)
        print("----------------")
