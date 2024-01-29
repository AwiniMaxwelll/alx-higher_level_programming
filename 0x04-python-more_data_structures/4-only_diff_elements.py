#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    all_elements = []
    for element in set_2:
        all_elements.append(element)
    for item in set_1:
        all_elements.append(item)
    return set(all_elements)
