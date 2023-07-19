#!/usr/bin/python3

"""Defines a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class that inherits from the base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle object.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x coordinate of the Rectangle.

        Args:
            value (int): The x coordinate value to set.

        Raises:
            TypeError: If the x coordinate is not an integer.
            ValueError: If the x coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y coordinate of the Rectangle.

        Args:
            value (int): The y coordinate value to set.

        Raises:
            TypeError: If the y coordinate is not an integer.
            ValueError: If the y coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        Print the Rectangle using the '#' character.

        If the width or height is 0, it will print an empty line.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        else:
            for _ in range(self.y):
                print()
            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """the updating function"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """
        Return the representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle in the format
            "[Rectangle] (id) x/y - width/height".
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
