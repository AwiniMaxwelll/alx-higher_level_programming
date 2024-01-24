#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        first_step = my_string.translate({ord('c'): None})
        final_step = first_step.translate({ord('C'): None})
        return (final_step)
