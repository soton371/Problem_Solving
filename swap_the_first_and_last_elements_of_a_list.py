def swap_first_last(list1):
    swapped_list = list1.copy()

    swapped_list[0], swapped_list[-1] = swapped_list[-1], swapped_list[0]

    return swapped_list


