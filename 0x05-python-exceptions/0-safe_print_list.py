def _len(list_1=[]):
    length = 0
    for _ in list_1:
        length += 1
    return length


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print(my_list[i], end='')
        print('\n', end='')
        return x
    except IndexError:
        print('\n', end='')
        return _len(my_list)
