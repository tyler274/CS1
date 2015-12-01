__author__ = 'Tyler Port'

import logging, random

LOG = logging.getLogger(__name__)

choices = ['R', 'G', 'B', 'Y', 'O', 'W']
code_length = 4

#Ex D.1
def make_random_code():
    '''
    make_random_code() -> list

    Takes no input arguments and returns a psuedorandom list of characters
    of length code_length, and of characters in choices.
    '''
    code = []
    while len(code) < code_length:
        code.append(random.choice(choices))
    return code

#Ex D.2
def count_exact_matches(first_string, second_string):
    '''
    count_exact_matches(first_string, second_string) -> int

    Counts exact string matches in the two inputed lists, and returns the total
    number of matches
    '''
    count = 0
    for index, value in enumerate(first_string):
        if value == second_string[index]:
            count += 1
    return count

#Ex D.3
def count_letter_matches(first_string, second_string):
    '''
    count_letter_matches(first_string, second_string) -> int

    Counts matches number of letters irregardless of position in the string,
    returns the total number of matches.
    '''
    first_list = list(first_string)
    second_list = list(second_string)
    count = 0
    for x in first_list:
        if x in second_list:
            count += 1
            second_list.remove(x)
    return count

#Ex D.4
def compare_codes(code, guess):
    '''
    compare_codes(string1, string2) -> string

    takes the code and the guess and returns a string representing the
    correctness of the guess
    '''
    black_pegs = count_exact_matches(code, guess)
    white_pegs = count_letter_matches(code,guess)
        - count_exact_matches(code, guess)
    blank_pegs = 4 - (black_pegs + white_pegs)
    final_string= ''
    for i in range(black_pegs):
        final_string += 'b'
    for j in range(white_pegs):
        final_string += 'w'
    for k in range(blank_pegs):
        final_string += '-'

    return final_string

#Ex D.5
def run_game():
    '''
    run_game() -> Nothing

    Let's you play mastermind using the code above
    '''
    print('New game.')
    secret_code = make_random_code()
    finished = False
    count = 0
    while finished is not True:
        guess = raw_input(str('Enter your guess: '))
        comparison = compare_codes(secret_code, guess)
        count += 1
        print('Result: {0}'.format(comparison))
        if comparison == 'bbbb':
            finished = True
            print(
                'Congratulations! You cracked the code in {0} moves!'
                    .format(count)
            )
