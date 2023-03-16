#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_sum = 0
    total_weight = 0

    
    for tup in my_list:
        weighted_sum  += tup[0] * tup[1]
        total_weight += tup[1]


    weighted_average = weighted_sum / total_weight
    
    return weighted_average
