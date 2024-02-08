#!/usr/bin/python3
"""Square class defination"""


class Square:
    """The body of the square class"""

    def __init__(self, size=0):
        """The constructor of Square class
        Args:
        size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """returns the size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)
