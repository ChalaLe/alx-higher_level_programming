#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = set(my_list)
    num = 0

    for i in uniq_integers:
        num += i

    return (num)
