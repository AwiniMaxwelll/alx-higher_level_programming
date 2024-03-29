#!/usr/bin/python3
"""Square class defination"""


class Square:
    """The body of the square class"""

    def __init__(self, size=0):
        """The constructor of Square class
        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of a given size of a square."""
        return (self.__size * self.__size)
