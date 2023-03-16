#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    W_sum = 0
    t_weight = 0

    for tup in my_list:
        w_sum += tup[0] * tup[1]
        t_weight += tup[1]

    return (w_sum / t_weight)
