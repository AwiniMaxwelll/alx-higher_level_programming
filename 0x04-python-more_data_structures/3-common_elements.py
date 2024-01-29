#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_element = []
    for element in set(set_1):
        if element in set(set_2):
            common_element.append(element)
    return common_element
