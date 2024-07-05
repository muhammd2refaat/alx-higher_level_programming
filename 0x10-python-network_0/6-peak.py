#!/usr/bin/python3
"""
This module defines a function that finds
a peak in a list of unsorted integers.
"""


def find_peak(num_list):
    """Find the peak in a list of integers.
    Args:
        num_list (list): List of integers.
    Returns:
        int or None: The value of the peak or None if the list is empty.
    """
    lst_len = len(num_list)
    if lst_len == 0:
        return None
    peak_index = binary_search(num_list, 0, lst_len - 1)
    return num_list[peak_index]


def binary_search(nums, low, high):
    """Recursive binary search of the peak.
    Args:
        nums (list): List of integers.
        low (int): Lower bound of the search range.
        high (int): Upper bound of the search range.
    Returns:
        int: Index of the peak.
    """
    if low >= high:
        return low

    mid = (high - low) // 2 + low
    if nums[mid] > nums[mid + 1]:
        return binary_search(nums, low, mid)
    else:
        return binary_search(nums, mid + 1, high)
