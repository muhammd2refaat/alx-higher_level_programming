#!/usr/bin/python3
def no_c(my_string):
    # Create a copy of my_string
    new_string = my_string[:]
    # Loop through the copy of my_string
    for i in new_string:
        # Check if i is 'c' or 'C'
        if i == 'c' or i == 'C':
            # Remove 'c' or 'C' from the copy of my_string
            new_string.remove(i)
    # Return the copy of my_string
    return new_string
