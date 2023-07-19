#!/usr/bin/python3

"""Rectangle module"""

from rectangle import Rectangle

class Square(Rectangle):
    """Squaer class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of the size property"""
        self.__width = value
        self.__height = value

    def __str__(self):
        """printing the object and class name and it's attributes"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updating the attributes of an object"""
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
        """converting an object to a dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
