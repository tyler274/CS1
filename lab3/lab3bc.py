__author__ = 'Tyler Port'

# Going to declare types after the variable in docstrings. i.e. list1 list, list1 is the variable name, list is the type
import os
from collections import Counter

basedir = os.path.abspath(os.path.dirname(__file__))

# Ex B.1
def list_reverse(list_in):
    """
    :param list_in list:
    :return: list_out list:

    Takes a list a returns a new list that is the reverse of the input
    """
    list_out = list(list_in)
    return list_out.reverse()


# Ex B.2
def list_reverse2(list_in):
    """

    :param list_in list:
    :return list_out list :

    Takes a list a returns a new list that is the reverse of the input
    """
    list_out = []
    length = len(list_in)
    for part in range(length):
        list_out.append(list_in[length - 1 - part])

    return list_out


# Ex B.3
def file_info(file_name):
    """

    :param file_name:
    :return (line_count int, word_count int, character_count int) tuple:

    Takes the name of a text file in the same folder as this python script, and returns info about the file in a tuple
    """

    line_count = 0
    word_count = 0
    character_count = 0

    with open(basedir + '/' + file_name, 'r') as f:
        for line in f:
            line_count += 1
            words = line.split()
            word_count += len(words)
            character_count += len(line)

    return line_count, word_count, character_count


# Ex B.4

def file_info2(file_name):
    """

    :param file_name:
    :return {lines int, words int, characters int} dict:

    Takes the name of a text file in the same folder as this python script, and returns info about the file in a tuple.
    """

    line_count, word_count, character_count = file_info(file_name)

    return {'lines': line_count, 'words': word_count, 'characters': character_count}


# Ex B.5

def longest_line(file_name):
    """

    :param file_name:
    :return (length int, long_line string) tuple:

    Takes the name of a text file in the same directory as this file and returns the length of the longest line
    and the line itself.
    """
    long_line = ''
    length = 0

    with open(basedir + '/' + file_name, 'r') as f:
        for line in f:
            new_length = len(line)
            if new_length > length:
                length = new_length
                long_line = line

    return length, long_line


# Ex B.6

def sort_words(string_in):
    """

    :param string_in:
    :return list_string:

    Takes a string and returns a sorted list of the string's contents

    If the input string is empty it returns an empty list
    """
    if string_in == '':
        return []
    split_string = string_in.split(' ', string_in.count(' '))
    list_string = list(split_string)
    list_string.sort()
    return list_string


# Ex B.7

# Note: Had to look this up as I have never had to do this by hand nor would I trust myself to do so.
# first write down the binary number and list the powers of 2 from right to left, starting at 2^0
# 11011010
#
# 2^7  2^6  2^5  2^4  2^3 2^2 2^1 2^0
# 128,  64,  32,  16,  8,  4,  2,  1
#
# Write the digits of the binary numbers below their corresponding powers of two
#
# 128  64  32  16  8  4  2  1
#  1   1   0   1   1  0  1  0
#
# If the binary digit is a 1, write down the power of two above it, else write 0
#
# 128  64  0  16  8  0  2  0
#
# Add the final values
#
# 128+64+16+8+2 = 218
#
# The largest eight digit binary number would be 128+64+32+16+8+4+2+1 = 255

# Ex B.8

def binaryToDecimal(list_of_digits):
    """

    :param list_of_digits list:
    :return total int:

    Takes a list of 0s and 1s and calculates the decimal value of the binary number the list makes
    """
    # Smartass way of doing this follows
    # smartass_decimal = eval('0b' + ''.join(list_of_digits))

    # Desired way now
    length = len(list_of_digits)
    total = 0
    for index, value in enumerate(list_of_digits):
        power = 2**(length - 1 - index)
        if value == 1:
            total += power

    return total

# Ex C.1
# BLARG

# Ex C.2.1
# 1. Non descriptive/useful function name, doesn't tell the user anything about what it does
# 2. No useful argument/parameter naming, what am I supposed to pass to it?
# 3. Chaining mathematical operations like that is not pythonic and muddies what is going on
def sum_of_three_cubes(first_number, second_number, third_number):
    return (first_number ** 3) + (second_number ** 3) + (third_number ** 3)

# Ex C.2.2
# 1. Comment is filled with grammatical mistakes/typos/spelling mistakes
# 2. Ridiculous chaining of operations strikes again
# 3. Function naming is still bad, should use snake_case or camelCase for to make it easier to read
# 4. Goes over recommended line length
def sum_of_four_cubes(first_number, second_number, third_number, fourth_number):
    # Returns the sum of the cubes of all arguments
    return (first_number ** 3) + (second_number ** 3) + (third_number ** 3) + (fourth_number ** 3)

# Ex C.2.3
# 1. Not making use of the exponentiation operator
# 2. inconsistent spacing/tabbing

def sum_of_squares(x, y):
    return x**2 + y**2
def sum_of_three_cubes2(x, y, z):
    return x**3 + y**3 + z**3


