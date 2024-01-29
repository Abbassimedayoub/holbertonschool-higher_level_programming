#!/usr/bin/python3
def max_integer(my_list=None):
    if my_list is None:
        return None

    if len(my_list):
        res = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > res:
                res = my_list[i]
        return res
    else:
        return None
