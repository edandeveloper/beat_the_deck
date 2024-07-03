class Card:
    """
    Represents a playing card with a name and value.

    Attributes:
        name (str): The name of the card.
        value (int): The value of the card.
    """

    def __init__(self, name: str, value: int):
        """
        Initializes a Card instance with a name and value.

        Args:
            name (str): The name of the card (e.g., "A", "10", "K").
            value (int): The value of the card (e.g., 14 for Ace, 10 for Ten, 13 for King).
        """
        self.name = name
        self.value = value
    
    def get_name(self) -> str:
        """
        Gets the name of the card.

        Returns:
            str: The name of the card.
        """
        return self.name

    def get_value(self) -> int:
        """
        Gets the value of the card.

        Returns:
            int: The value of the card.
        """
        return self.value

    def __eq__(self, other: 'Card') -> bool:
        """
        Checks if the value of this card is equal to the value of another card.

        Args:
            other (Card): The other card to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.value == other.get_value()

    def __ne__(self, other: 'Card') -> bool:
        """
        Checks if the value of this card is not equal to the value of another card.

        Args:
            other (Card): The other card to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.value != other.get_value()

    def __repr__(self) -> str:
        """
        Returns a string representation of the card.

        Returns:
            str: The name of the card.
        """
        return self.name

    def __gt__(self, other: 'Card') -> bool:
        """
        Checks if the value of this card is greater than the value of another card.

        Args:
            other (Card): The other card to compare.

        Returns:
            bool: True if this card's value is greater, False otherwise.
        """
        return self.value > other.get_value()

    def __lt__(self, other: 'Card') -> bool:
        """
        Checks if the value of this card is less than the value of another card.

        Args:
            other (Card): The other card to compare.

        Returns:
            bool: True if this card's value is less, False otherwise.
        """
        return self.value < other.get_value()

    def __ge__(self, other: 'Card') -> bool:
        """
        Checks if the value of this card is greater than or equal to the value of another card.

        Args:
            other (Card): The other card to compare.

        Returns:
            bool: True if this card's value is greater or equal, False otherwise.
        """
        return self.value >= other.get_value()

    def __le__(self, other: 'Card') -> bool:
        """
        Checks if the value of this card is less than or equal to the value of another card.

        Args:
            other (Card): The other card to compare.

        Returns:
            bool: True if this card's value is less or equal, False otherwise.
        """
        return self.value <= other.get_value()
