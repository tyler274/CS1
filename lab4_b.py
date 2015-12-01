import random
import collections
from types import StringType
# https://www.youtube.com/watch?v=wf-BqAjZb8M <- the 80 character limit is
# outdated and no longer considered a hard and fast rule by most python devs,
# myself included.

def random_size(int1, int2):
    """
    :param int1:
    :param int2:
    :return random_number:

    Takes two non negative even integers, checks if they are that, then return
    an even integer between the two integers or equal to one of them. checks if
    the output is somehow not that despite a while loop to make sure.
    """
    # Let's do some weird shit because why not.
    inputs = locals()
    for index, value in inputs.iteritems():
        assert value >= 0,\
            '{0} is not a positive integer: {1}'.format(index, value)
        assert value % 2 == 0,\
            '{0} is not an even integer: {1}'.format(index, value)

    assert int1 < int2,\
        'int1 is not smaller than int2: {}, {}'.format(int1, int2)

    random_number = random.randint(int1, int2)

    while random_number % 2 != 0:
        random_number = random.randint(int1, int2)

    assert random_number % 2 == 0,\
        'The output is not an even number: {}'.format(random_number)
    return random_number


def random_position(max_x, max_y):
    """

    :param max_x:
    :param max_y:
    :return (x, y):

    Takes two positive integers, max_x and max_y, and returns a tuple of two
    random integers from 0 to each maximum value respectively.
    """
    inputs = locals()
    for index, value in inputs.iteritems():
        assert value >= 0,\
            '{0} is not a positive integer: {1}'.format(index, value)

    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    return x, y


def random_color():
    """
    :return:

    Returns a random hexdecimal rgb value.
    """
    # For context; this was a lambda function but PEP8 says not to assign
    # lambda's to variables, so def it is.
    def r(): return random.randint(0, 255)
    return '#{0:02x}{1:02x}{2:02x}'.format(r(), r(), r())


def count_values(input_dict):
    """

    :param input_dict:
    :return:

    Takes a dict and counts the unique values in that dict.
    """
    value_list = []
    for value in input_dict.values():
        value_list.append(value)

    return len(set(value_list))


def remove_value(input_dict, arbitrary_item):
    """

    :param input_dict:
    :param arbitrary_item:
    :return:

    Removes all values of arbitrary_item from input_dict
    """
    keys_to_remove = []
    for key, value in input_dict.iteritems():
        if value == arbitrary_item:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        del input_dict[key]

    return input_dict


def split_dict(input_dict):
    """

    :param input_dict:
    :return first_dict, second_dict:

    Takes a dict and splits the dict into two dicts by the alphabet position of
    the first letter of each value's key.
    """
    first_dict = {}
    second_dict = {}
    for key, value in input_dict.iteritems():
        assert type(key) is StringType,\
            'Dict contains key not of type string: {}'.format(key)
        if key.lower()[:1] <= 'm':
            first_dict[key] = value

        if key.lower()[:1] <= 'z' and key.lower()[:1] >= 'n':
            second_dict[key] = value

    return first_dict, second_dict


def count_duplicates(input_dict):
    """

    :param input_dict:
    :return number:

    Takes a dict and counts the number of duplicates.
    """
    l = list(input_dict.values())
    counter_values = collections.Counter(l).values()
    while 1 in counter_values:
        counter_values.remove(1)

    return len(counter_values)



'reload(lab4_b); from lab4_b import *'
