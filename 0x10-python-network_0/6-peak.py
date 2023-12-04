""" Find peak in an integer """


def find_peak(list_of_integers):
    """ Takes list of integers and find the highest """

    if len(list_of_integers) == 0:
        return None

    p1 = 0
    p2 = len(list_of_integers) - 1
    max_index = p2

    while p1 != p2:
        if list_of_integers[p1] > list_of_integers[p2]:
            p2 -= 1
        else:
            p1 += 1

        if p1 == p2:
            max_index = p2

    return list_of_integers[max_index]
