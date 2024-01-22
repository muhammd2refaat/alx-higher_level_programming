#!/usr/bin/python3
def no_c(my_string):
    # Create a new string
    new_string = ""
    # Iterate over the characters of the string
    for char in my_string:
        # If the character is not 'c' or 'C', append it to the new string
        if char != 'c' and char != 'C':
            new_string += char
    # Return the new string
    return new_string
