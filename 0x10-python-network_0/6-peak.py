#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    n = len(list_of_integers)
    if n <= 3:
        return max(list_of_integers)
    for i in range(1, n - 1):
        if (
            list_of_integers[i] > list_of_integers[i - 1] and
            list_of_integers[i] > list_of_integers[i + 1]
        ):
            return list_of_integers[i]
    return max(list_of_integers)
