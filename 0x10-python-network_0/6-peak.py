#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]:
            if mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]:
                return list_of_integers[mid]
            else:
                left = mid + 1
        else:
            right = mid - 1

    return list_of_integers[left]
