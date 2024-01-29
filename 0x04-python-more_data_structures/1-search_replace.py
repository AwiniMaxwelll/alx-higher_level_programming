#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        new_list.append(i)
        if search in new_list:
            index = new_list.index(search)
            new_list[index] = replace

    return new_list
