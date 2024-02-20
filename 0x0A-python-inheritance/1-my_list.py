#!/usr/bin/python3
"""Inherit from my list module"""


class Mylist(list):
    """class that inherits from my list"""
    def print_sorted(self):
        """pints sorted list"""
        print(sorted(self.copy()))
