# Tyler Port
# tport

import random
import sys
import string

# Problem 1.1
# 1. not using triple quotes to specify a multiline string/docstring.
# 2. semicolon instead of colon for the 'for' block.
# 3. inconsistent indentation/spacing for scope.
# 4. not using the equality operator '==', used '=' instead.
# 5. did not specify the tuple with commas between the components.

# Problem 1.2
# 1. (factorial) The while loop continues for ever as n never decrements.
# 2. (sin) "tiny == 1.0e-16" is using the equality operator instead of the "="
#     operator.
# 3. (sin) "while True:" is an infinite loop in this case.
# 4. (sin) The return in the middle of the while loop doesn't return anything.
# 5. (sin) The program prints the result instead of returning it.

# Problem 1.3
# 1. Terrible function naming.
# 2. Docstrings do not describe what the function does,
#    what arguments it takes.
# 3. Variable declaration spacing is inconsistent/bad.
# 4. Useless comments
# 5. else block that does nothing.

# Problem 2.1
def random_walk(n, m):
    """

    Args:
        n (int): The threshold value at which the function records
            the step count when the absolute value of the position
            exceeds this number.
        m (int): The number of times the simulation is run before returning.

    Returns:
        float: The average step count needed to reach the threshold.

    """

    choices = [-1, 1]
    step_counts = []
    for i in range(m):
        position = 0
        step_count = 0
        while abs(position) <= n:
            position += random.choice(choices)
            step_count += 1

        step_counts.append(float(step_count))

    return sum(step_counts) / float(m)


# Problem 2.2
def draw_box(n, p):
    """

    Args:
        n (int): A value representing the size of the interior sides of the
            drawn box.
        p (float): A value between 0.0 and 1.0 that represents the
            probability of a 'O' character at any given location in the drawn box.

    Returns:
        Writes the box to the console.

    """
    assert n > 0,\
        "Argument 'n' is not a positive value: {0}".format(n)
    assert (n % 1) == 0,\
        "Argument 'n' is not an integer: {0}".format(n)
    assert 0.0 <= p <= 1.0,\
        "Argument 'p' is not a valid probability (0.0 < p < 1.0): {0}"\
            .format(p)

    for y in range(0, n+2):
        for x in range(0, n+2):
            if ((y == 0) or (y == n+1)) and ((x == 0) or (x == n+1)):
                sys.stdout.write('+')

            elif ((y == 0) or (y == n+1)) and (0 < x < n+1):
                sys.stdout.write('-')

            elif (0 < y < n+1) and ((x == 0) or (x == n+1)):
                sys.stdout.write('|')

            elif (0 < y < n+1) and (0 < x < n+1):
                if random.random() < p:
                    sys.stdout.write('O')
                else:
                    sys.stdout.write(' ')

        sys.stdout.write('\n')


# Problem 2.3
def initial_value_count(input_list):
    """

    Args:
        input_list (list[int]): A non empty list of python integers

    Returns:
        Tuple[int, int]: Returns the first value of input_list, and
        the number of times it consecutively appears in the list
        from the beginning.

    """
    assert len(input_list) > 0,\
        "Argument 'input_list' is not a non empty list of integers: {0}"\
            .format(input_list)

    count = 1
    while (count < len(input_list)) and (input_list[0] == input_list[count]):
        count += 1

    return input_list[0], count


def run_length_encode(input_list):
    """

    Args:
        input_list (list[int]): A list of integers which may be empty.
            This list will be encoded into run-length format.

    Returns:
        list(Tuple[int, int]): Returns a list of tuples which describes the
            run-length encoded form of the input_list. run-length encoding
            in this case refers to each tuple in the list containing
            the value and number of times it consecutively appears in the list.

    """
    encoded_list = []
    new_list = list(input_list)
    while len(new_list) > 0:
        count = initial_value_count(new_list)
        encoded_list.append(count)
        new_list = new_list[count[1]:]

    return encoded_list


# Problem 3.1
def value_from_char(character):
    """

    Args:
        character (string): Takes an ASCII alphabet character
        and maps it 0-25, a-z.

    Returns:
        int: Numerical representation of the ASCII alphabet character inputted.

    """
    return ord(character.lower()) - ord('a')


def char_from_value(value):
    """

    Args:
        value (int): A number from 0 to 25 that represents an
            ASCII alphabet character.

    Returns:
        string: Returns a python string representing the character
            of value mapped by [a, z] -> [0, 25]
    """
    return chr(value + ord('a'))


def make_subst_dicts():
    """

    Returns Tuple[Dict[str, str], Dict[str, str]]: Returns two dicts which
        represent the encoding and decoding keys for a alphabetical
        substitution function.

    """
    encode_dict = {}
    decode_dict = {}
    options = string.ascii_lowercase
    for i in range(26):
        encode_dict[char_from_value(i)] = random.choice(options)
        decode_dict[encode_dict[char_from_value(i)]] = char_from_value(i)
        options = options.replace(encode_dict[char_from_value(i)], '')

    return encode_dict, decode_dict


# Problem 3.2
def encode_subst(coding_dict, input_string):
    """

    Args:
        coding_dict (Dict[str, str]): A dict which maps alphabetical values
            to another alphabetical value.
        input_string (str): A string to be encoded using the substitution
            method and the coding dict.

    Returns:
        str: Returns an encoded form of input_string using the
            substitution method and the coding_dict.

    """
    encoded_string = []
    for character in input_string:
        if character in string.ascii_letters:
            if character.isupper():
                encoded_string.append(coding_dict[character.lower()].upper())
            else:
                encoded_string.append(coding_dict[character])
        else:
            encoded_string.append(character)

    return ''.join(encoded_string)


# Problem 3.3
def encode_seq(direction, input_string):
    """

    Args:
        direction (str): Either 'en' for encoding, or 'de' for decoding.
        input_string (str): The string to be coded sequentially.

    Returns:
        str: The encoded/decoded form of input_string.

    """
    # Holy mother of nested if statements
    coded_string = []
    for index, character in enumerate(input_string):
        if character in string.ascii_letters:
            character_value = value_from_char(character)

            if index == 0:
                if character.isupper():
                    coded_string.append(
                        char_from_value(character_value % 26).upper()
                    )
                else:
                    coded_string.append(
                        char_from_value(character_value % 26)
                    )

            elif index > 0:
                last_coded_index = index - 1
                while coded_string[last_coded_index]\
                        not in string.ascii_letters:
                    if last_coded_index - 1 >= 0:
                        last_coded_index -= 1
                    else:
                        break

                if character.isupper():
                    if direction == 'en':
                        previous_value = value_from_char\
                            (coded_string[last_coded_index])
                        coded_string.append(
                            char_from_value(
                                (character_value + previous_value) % 26
                            ).upper()
                        )

                    elif direction == 'de':
                        previous_value = value_from_char\
                            (input_string[last_coded_index])
                        coded_string.append(
                            char_from_value(
                                (character_value - previous_value) % 26
                            ).upper()
                        )

                else:
                    if direction == 'en':
                        previous_value = value_from_char\
                            (coded_string[last_coded_index])
                        coded_string.append(
                            char_from_value(
                                (character_value + previous_value) % 26
                            )
                        )

                    elif direction == 'de':
                        previous_value = value_from_char\
                            (input_string[last_coded_index])
                        coded_string.append(
                            char_from_value(
                                (character_value - previous_value) % 26
                            )
                        )
        else:
            coded_string.append(character)

    return ''.join(coded_string)


# Problem 3.4
def encode(direction, keys, input_string):
    """

    Args:
        direction (str): Can be 'en' to encode, or 'de' to decode.
        keys (Tuple[Dict[str, str], Dict[str, str]]): A tuple of the
            encoding dict and decoding dict.
        input_string (str): A string to be encoded or decoded.

    Returns:
        str: Returns the coded string.

    """
    coded_string = ''
    if direction == 'en':
        seq_coded_string = encode_seq(direction, input_string)
        coded_string = encode_subst(keys[0], seq_coded_string)
    elif direction == 'de':
        sub_coded_string = encode_subst(keys[1], input_string)
        coded_string = encode_seq(direction, sub_coded_string)

    return coded_string


# Problem 3.5
def encode_file(direction, keys, file_read, file_write):
    """

    Args:
        direction (str): Can be 'en' to encode, or 'de' to decode.
        keys (Tuple[Dict[str, str], Dict[str, str]]): A tuple of the encoding
            dict and decoding dict.
        file_read (str): The name of a text file that contains the text
            you would like to encode/decode.
        file_write (str): The name of the text file that you would like
            to write the encoded/decoded text to.

    Returns:
        None: Writes file to disk.
    """

    with open(file_write, "w") as output_file:
        with open(file_read, "r") as input_file:
            for line in input_file:
                output_file.write(encode(direction, keys, line))

# if __name__ == '__main__':
#     sd = make_subst_dicts()
#     encode_file('en', sd, 'romeo.txt', 'romeo_en.txt')
#     encode_file('de', sd, 'romeo_en.txt', 'romeo_de.txt')
