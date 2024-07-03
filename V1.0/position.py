class Position:
    """
    Represents a position on a grid.

    Attributes:
        row (int): The row index of the position.
        column (int): The column index of the position.
    """

    def __init__(self, row: int, column: int):
        """
        Initialize a Position object.

        Args:
            row (int): The row index of the position.
            column (int): The column index of the position.
        """
        self.row = row
        self.column = column
    
    def get_row(self) -> int:
        """
        Get the row index of the position.

        Returns:
            int: The row index.
        """
        return self.row
    
    def get_column(self) -> int:
        """
        Get the column index of the position.

        Returns:
            int: The column index.
        """
        return self.column

    def __repr__(self) -> str:
        """
        Get the string representation of the position.

        Returns:
            str: The string representation in the format "(row, column)".
        """
        return f"({self.row}, {self.column})"
