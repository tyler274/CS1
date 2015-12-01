__author__ = 'Tyler Port'

import nose, random

# Ex B.1:
def complement(dna):
    '''
    complement(string) -> string

    Takes a string of DNA bases and returns a string of the complement bases
    '''
    # I assume the assignment doesn't require input validation
    # and exception raising

    pairs = ''
    # because checking for more cases is :effort:
    for base in dna.upper():
        if base == 'A': pairs += 'T'
        elif base == 'C': pairs += 'G'
        elif base == 'G': pairs += 'C'
        elif base == 'T': pairs += 'A'
    return pairs

#Ex B.2:
def list_complement(dna):
    '''
    list_complement(list) -> nothing (changes input)

    Takes a list of dna bases and changes each base into its complement
    '''
    for index, base in enumerate(dna):
        if base.upper() == 'A':
             dna[index] = 'T'
        elif base.upper() == 'C':
             dna[index] = 'G'
        elif base.upper() == 'G':
             dna[index] = 'C'
        elif base.upper() == 'T':
             dna[index] = 'A'
#Ex B.3:
def product(numbers):
    '''
    product(list) -> number (float/int)

    Computes product of entire list, if the list is empty returns 1
    '''
    total = 1
    for number in numbers:
        total *= number
    return total

#Ex B.4:
def factorial(number):
    '''
    factorial(number) -> number (float/int)

    Computes the factorial of a number using the product function
    '''
    if number == 0:
        return 1

    return product(range(1, number+1))

#Ex B.5:
def dice(m, n):
    '''
    dice(number, number) -> number

    Takes the number of sides and the number of rolls and computes the total
    '''
    rolls = []
    for roll in range(n):
        rolls.append(random.choice(range(1, m+1)))

    return sum(rolls)

#Ex B.6:
def remove_all(l, v):
    '''
    remove_all(list, value) -> nothing (changes input)

    Takes a list and a value and removes all of those values from the list
    '''
    while l.count(v) >= 1:
        l.remove(v)

#Ex B.7:
def remove_all2(l, v):
    '''
    remove_all(list, value) -> nothing (changes input)

    Takes a list and a value and removes all of those values from the list
    '''
    for i in range(l.count(v)):
        l.remove(v)

def remove_all3(l, v):
    '''
    remove_all(list, value) -> nothing (changes input)

    Takes a list and a value and removes all of those values from the list
    '''
    while v in l:
        l.remove(v)

#Ex B.8:
def any_in(l1, l2):
    '''
    any_in(list1, list2) -> boolean

    Takes two lists and returns True if any of the values of each list are the
    same, else returns False.
    '''
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False

'''
Ex C.1.a
the '=' operator does not compare values, use '==' or similar

Ex C.1.b
that's not how you define an argument, 's' -> s, it defines a string 's' not
a variable.

Ex C.1.c
using a string 's' instead of the string stored by variable s, use
return s + '-Caltech'

Ex C.1.d
can't add a string to a list, use lst.append('bam')

Ex C.1.e
the append() function doesn't return the resulting list,
lst2.append(0)
return lst2

Ex C.1.f
Current method will embed the list of str into the list, should use a list
unpacking method

for cha in letters:
    list.append(cha)
'''

#Ex C.2
'''
c was declared when a was 10, and a being changed later does not retroactively
affect every time a was used before then
'''

#Ex C.3
'''
The second function doesn't actually return the value, only prints it to console
'''

#Ex C.4
'''
the second function requires the 'user' to enter in the values of x and y on run
and does not allow x and y to be passed to the function as arguments to be used.

The difference is that passing a value to a function allows the function to use
it immediately, raw_input blocks the program until it recieves its input from
the user.
'''

#Ex C.5:
'''
Strings in python are immutable
'''

#Ex C.6
'''
item is a "new" object created for the loop, and is in no way connected to the
object in lst that it is created from. A proper fix would be to enumerate(lst)
and get the index and value, then change the value at lst[index] to the desired

for index, value in enumerate(lst):
    lst[index] *= 2 
'''
