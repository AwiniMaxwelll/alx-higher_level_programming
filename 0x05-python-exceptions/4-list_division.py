#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    t_result = 0
    for i in range(0, list_length):
        try:
            t_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            t_result = 0
            print("wrong type")
        except ZeroDivisionError:
            t_result = 0
            print("division by 0")
        except IndexError:
            t_result = 0
            print("out of range")
        finally:
            pass
        new_list.append_result)
    return new_list
