#!/usr/bin/python3
"""documentation"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self, width, height):
        return (self.__width * self.__height)

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.width}/{self.height}"
