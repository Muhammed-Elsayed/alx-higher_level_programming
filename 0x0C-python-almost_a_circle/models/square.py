#!/usr/bin/python3

"""Square module.

This module defines the Square class that inherits from Rectangle.
A Square is a special type of rectangle with equal width and height.

"""

from rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Args:
        size (int): The size of the square (equal width and height).
        x (int): The x-coordinate of the square's position (default 0).
        y (int): The y-coordinate of the square's position (default 0).
        id (int): The unique identifier for the square (default None).

    Attributes:
        None

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square object.

        This constructor is used to create a new Square object with the specified size, position,
        and identifier. The width and height of the square are set to the provided size value, as a
        square has equal dimensions.

        Args:
            size (int): The size of the square (equal width and height).
            x (int, optional): The x-coordinate of the square's position (default 0).
            y (int, optional): The y-coordinate of the square's position (default 0).
            id (int, optional): The unique identifier for the square (default None).

        Returns:
            None

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size (equal width and height) of the square.

        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size to set for the square.

        """
        self.__width = value
        self.__height = value

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.

        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: Non-keyword arguments (order: id, size, x, y).
            **kwargs: Keyword arguments (attributes and their new values).

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Convert the square object to a dictionary.

        Returns:
            dict: A dictionary representation of the square object.

        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
