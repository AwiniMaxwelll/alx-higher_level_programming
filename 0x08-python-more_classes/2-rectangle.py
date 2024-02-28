#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Rectangle class defined by width and height
    """

    def __init__(self, width=0, height=0):
        """Initialize Rectangle instance in constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the width of the rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the Rectangle instance
        Args:
            value: value of the height must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate  the area the Rectangle
        Returns:
            Area of the rectangle self.__height * self.__width
        """
        area_of_rectangle = self.__height * self.__width
        return area_of_rectangle

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            perimeter of the rectangle is 2* self.__height + 2 * self.__width
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter_of_T = (2 * self.__height) + (2 * self.__width)
        return perimeter_of_T
