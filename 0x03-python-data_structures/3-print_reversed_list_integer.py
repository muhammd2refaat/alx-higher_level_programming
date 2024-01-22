#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Check if my_list exists
    if my_list:
        # Print the list in reverse
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
