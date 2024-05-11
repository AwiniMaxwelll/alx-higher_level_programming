#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    c_list = list_of_integers
    length = len(c_list)
    if length == 0:
        return
    mid = length // 2
    if (mid == length - 1 or c_list[mid] >= c_list[mid + 1]) and (mid == 0 or c_list[mid] >= c_list[mid - 1]):
        return c_list[mid]
    if mid != length - 1 and c_list[mid + 1] > c_list[mid]:
        return find_peak(c_list[mid + 1:])
    return find_peak(c_list[:mid])
