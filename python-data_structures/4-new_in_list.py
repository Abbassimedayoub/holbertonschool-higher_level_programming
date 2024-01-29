#!/usr/bin/python3i
def replace_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx in range(0, len(new_list)):
        new_list[idx] = element
    return new_list
