#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    key_value = {key: value}
    a_dictionary.update(key_value)
    return a_dictionary
