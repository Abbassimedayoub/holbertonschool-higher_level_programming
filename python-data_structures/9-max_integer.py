#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        res = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > res:
                res = my_list[i]
        return rest