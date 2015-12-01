'''
lab3d.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ----------------------------------------------------------------------

# def apply_rule(character, setup):
#     new_string = ''
#     if character in setup:
#         new_string = setup[character]
#     else:
#         new_string = character
#
#     return new_string


def update(lsys, starting_string):
    """

    :param lsys:
    :param starting_string:
    :return new_string:

    Takes a dict, setup, and a string, lsys, and performs one round of updates on the string per the instructions
    defined within setup.
    """

    new_string = ''
    for value in starting_string:
        right_hand = ''
        if value in lsys:
            right_hand = lsys[value]
        else:
            right_hand = value

        new_string += right_hand

    return new_string


def iterate(lsys, n):
    """

    :param lsys:
    :param n:
    :return start:

    Takes a L-system definition, lsys, and an integer, n, and returns the string that results when that L-system is
    iterated n times
    """
    start = lsys['start']
    for i in range(n):
        start = update(lsys, start)

    return start


def lsystemToDrawingCommands(draw, s):
    """

    :param draw:
    :param s:
    :return commands:

    Takes a dictionary, draw, of character->turtle instuctions, and a L-system string, s.
    Uses draw to map the string to drawing commands, and returns a list, commands, of those commands.
    """
    commands = []
    for character in s:
        if draw.get(character):
            commands.append(draw[character])

    return commands


def bounds(cmds):
    """

    :param cmds:
    :return:

    takes a list of commands to execute and determines the minimum and maximum values of x and y after the commands are
    executed.
    """
    x = 0.0
    y = 0.0
    angle = 0.0

    minX = 0.0
    minY = 0.0

    maxX = 0.0
    maxY = 0.0

    for command in cmds:
        x, y, angle = nextLocation(x, y, angle, command)
        if x > maxX:
            maxX = x

        if x < minX:
            minX = x

        if y > maxY:
            maxY = y

        if y < minY:
            minY = y

    return minX, maxX, minY, maxY


def nextLocation(x, y, angle, cmd):
    """

    :param x:
    :param y:
    :param angle:
    :param cmd:
    :return:

    takes a x and y coordinate, an angle (in degrees,) and a command to execute. returns the resulting x and y
    coordinate and angle.

    """
    action = cmd.split(' ')[0]
    value = float(cmd.split(' ')[1])
    radian_angle = float(angle) * (math.pi / 180.0)

    if action == 'R':
        angle -= value
        while angle < 0.0:
            angle += 360.0

    elif action == 'L':
        angle += value
        if angle > 360.0:
            angle = 360.0 % angle

    elif action == 'F':
        x += value * math.cos(radian_angle)
        y += value * math.sin(radian_angle)

    return x, y, angle


def saveDrawing(filename, bounds_input, cmds):
    """

    :param filename:
    :param bounds:
    :param cmds:
    :return:

    Takes a string, filename, a tuple of bounds, bounds_input, and a list of commands, cmds, and writes them out
    to a text file for use.
    """
    with open(filename, "w") as text_file:
        text_file.write('{0} {1} {2} {3}\n'.format(bounds_input[0], bounds_input[1], bounds_input[2], bounds_input[3]))

        for command in cmds:
            text_file.write(command + '\n')


def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)


def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

